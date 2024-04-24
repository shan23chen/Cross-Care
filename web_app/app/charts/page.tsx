// @ts-nocheck
'use client';

import React, { useState, useEffect, use } from 'react';
import {
  Card,
  Tab,
  TabList,
  TabGroup,
  Select,
  SelectItem,
  BarChart,
  Title,
  Subtitle,
  Button,
  MultiSelect,
  MultiSelectItem,
  Switch,
  LineChart
} from '@tremor/react';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import FileDownloadIcon from '@mui/icons-material/FileDownload';
import { faDownload, faInfoCircle } from '@fortawesome/free-solid-svg-icons';
import Joyride, { CallBackProps, STATUS, Step } from 'react-joyride';

const DataCategories = {
  TotalCounts: 'total',
  GenderCounts: 'gender',
  RacialCounts: 'racial',
  DrugCounts: 'drug', // need to think about this as many to many
  TimeCounts: 'time'
};

const WindowOptions = {
  // Total: 'total',
  Window10: 'window_10',
  Window50: 'window_50',
  Window100: 'window_100',
  Window250: 'window_250'
};

const DataSourceOptions = {
  Arxiv: 'arxiv',
  Github: 'github',
  Wikipedia: 'wikipedia', // Change the URL to your custom data source endpoint
  StackExchange: 'stackexchange',
  Pile: 'pile'
};

const ChartPage = () => {
  const [selectedCategory, setSelectedCategory] = useState(
    DataCategories.GenderCounts
  );
  const [sortKey, setSortKey] = useState('disease');
  const [sortOrder, setSortOrder] = useState('asc');
  const [dataToShow, setDataToShow] = useState([]);
  const [selectedWindow, setSelectedWindow] = useState(WindowOptions.Window250);
  const [dataSource, setDataSource] = useState(DataSourceOptions.Arxiv); // State for selected data source
  const [selectedDiseases, setSelectedDiseases] = useState([]);
  const [diseaseNames, setDiseaseNames] = useState([]);
  const [isClient, setIsClient] = useState(false);
  const [runTour, setRunTour] = useState(false); // State to control the visibility of the tour
  const [steps, setSteps] = useState<Step[]>([
    {
      target: 'body',
      content: 'Use these tabs to switch between different data categories.',
      placement: 'center'
    },
    {
      target: '.multi-select',
      content: 'Select one or more diseases to filter the chart data.',
      placement: 'bottom'
    },
    {
      target: '.bar-chart',
      content: 'View the distribution of data across selected diseases.',
      placement: 'top'
    }
    // Add more steps as needed
  ]);

  const sortKeys = {
    [DataCategories.TotalCounts]: ['disease', '0'],
    [DataCategories.GenderCounts]: ['disease', 'male', 'female'],
    [DataCategories.RacialCounts]: [
      'disease',
      'white/caucasian',
      'black/african american',
      'asian',
      'hispanic/latino',
      'pacific islander',
      'native american/indigenous'
    ]
  };

  const totalDisplayNames = {
    Disease: 'disease',
    Count: '0'
  };
  const genderDisplayNames = {
    Male: 'male',
    Female: 'female'
  };

  const racialDisplayNames = {
    'White/Caucasian': 'white/caucasian',
    'Black/African American': 'black/african american',
    Asian: 'asian',
    'Hispanic/Latino': 'hispanic/latino',
    'Pacific Islander': 'pacific islander',
    'Native American/Indigenous': 'native american/indigenous'
  };

  const initialDiseaseList = [
    "arthritis", "asthma", "bronchitis", "cardiovascular disease", "chronic kidney disease", "coronary artery disease", "covid-19", "deafness", "diabetes", "hypertension", "liver failure", "mental illness", "mi", "perforated ulcer", "visual anomalies"
  ];

  const [currentPage, setCurrentPage] = useState(1);
  const pageSize = 10; // or any other number

  const fetchDiseaseNames = async () => {
    try {
      const response = await fetch(
        `http://127.0.0.1:5000/get-disease-names?dataSource=${dataSource}`
      );
      if (response.ok) {
        const names = await response.json();
        setDiseaseNames(names);

        // Set initialDiseases to the diseases from initialDiseaseList that are present in the fetched names
        const initialDiseases = initialDiseaseList.filter((disease) =>
          names.includes(disease)
        );
        setSelectedDiseases(initialDiseases);
      } else {
        console.error('Server error:', response.status);
      }
    } catch (error) {
      console.error('Network error:', error);
    }
  };
  useEffect(() => {
    fetchDiseaseNames();
  }, []); // Empty dependency array to run only on component mount

  // Function to fetch sorted data from the server
  const fetchChartData = async () => {
    console.log(dataSource);
    console.log(dataSource);
    const selectedDiseasesString = selectedDiseases.join(',');
    try {
      const response = await fetch(
        `http://127.0.0.1:5000/get-chart-data?category=${selectedCategory}&selectedWindow=${selectedWindow}&sortKey=${sortKey}&sortOrder=${sortOrder}&page=${currentPage}&per_page=${pageSize}&selectedDiseases=${selectedDiseasesString}&dataSource=${dataSource}`
      );
      if (response.ok) {
        const fetchedData = await response.json();
        console.log("Data to show: ", fetchedData);
        setDataToShow(fetchedData); // Set transformed data
      } else {
        console.error('Server error:', response.status);
      }
    } catch (error) {
      console.error('Network error:', error);
    }
  };

  // Fetch data when sortKey, sortOrder, selectedCategory, or selectedWindow changes
  useEffect(() => {
    fetchChartData();
  }, [
    selectedCategory,
    selectedWindow,
    dataSource,
    sortKey,
    sortOrder,
    currentPage,
    selectedDiseases
  ]);

  const [additionalChartData, setAdditionalChartData] = useState([]);

  const transformData = (data) => {
    const groupedByDisease = {};
  
    data.forEach(item => {
      const { count, demographic, disease } = item;
  
      if (!groupedByDisease[disease]) {
        groupedByDisease[disease] = { disease: disease };  
      }
  
      // Initialize the demographic count if it does not exist
      if (!groupedByDisease[disease][demographic]) {
        groupedByDisease[disease][demographic] = 0;
      }
  
      // Sum the counts for each demographic
      groupedByDisease[disease][demographic] = count;
    });
  
    // Convert the groupedByDisease object into an array of objects
    return Object.values(groupedByDisease);
  };
  
  
  
  const fetchAdditionalChartData = async () => {
    const selectedDiseasesString = selectedDiseases.join(',');
    try {
      const response = await fetch(
        `http://127.0.0.1:5000/get-prevalence?category=${selectedCategory}&selectedDiseases=${selectedDiseasesString}`
      );
      if (response.ok) {
        const fetchedData = await response.json();
        console.log('Additional Chart Data:', fetchedData);
        const transformedData = transformData(fetchedData);
        console.log('Transformed Data:', transformedData);
        setAdditionalChartData(transformedData);

      } else {
        console.error('Server error:', response.status);
      }
    } catch (error) {
      console.error('Network error:', error);
    }
  };
  useEffect(() => {
    fetchAdditionalChartData();
  }, [selectedCategory, sortKey, sortOrder, currentPage, selectedDiseases]);

  // Determine display names based on selected category
  let displayNames = {};
  if (selectedCategory === DataCategories.TotalCounts) {
    displayNames = totalDisplayNames;
  } else if (selectedCategory === DataCategories.GenderCounts) {
    displayNames = genderDisplayNames;
  } else if (selectedCategory === DataCategories.RacialCounts) {
    displayNames = racialDisplayNames;
  }

  const downloadJsonData = (dataSource) => {
    let dataToDownload;

    if (dataSource === 'chartData') {
      dataToDownload = dataToShow;
    } else if (dataSource === 'additionalChartData') {
      dataToDownload = additionalChartData;
    } else {
      console.error('Invalid dataSource:', dataSource);
      return;
    }

    // Create a JSON string from the selected data
    const jsonData = JSON.stringify(dataToDownload);

    // Create a Blob object containing the JSON data
    const blob = new Blob([jsonData], { type: 'application/json' });

    // Create a download link element
    const a = document.createElement('a');
    a.href = window.URL.createObjectURL(blob);

    // Determine the filename based on the dataSource
    const filename =
      dataSource === 'chartData'
        ? 'chart_data.json'
        : 'additional_chart_data.json';
    a.download = filename;

    // Trigger a click event to initiate the download
    a.click();
  };

  useEffect(() => {
    // Only run the tour if the 'tourShown' flag is not set in localStorage
    const tourShown = localStorage.getItem('tourShown');
    if (!tourShown) {
      setRunTour(true);
    }
  }, []);

  const handleJoyrideCallback = (data: CallBackProps) => {
    const { status } = data;
    if ([STATUS.FINISHED, STATUS.SKIPPED].includes(status)) {
      setRunTour(false); // Hide the tour once it's finished or skipped
      localStorage.setItem('tourShown', 'true'); // Set a flag in localStorage
    }
  };

  // Render sort key dropdown options based on the current category
  const renderSortKeyOptions = () => {
    return Object.keys(displayNames).map((displayName) => (
      <SelectItem key={displayName} value={displayNames[displayName]}>
        {displayName}
      </SelectItem>
    ));
  };
  // Determine the categories for the BarChart based on the selected category
  let chartCategories = [];
  if (selectedCategory === DataCategories.TotalCounts) {
    chartCategories = ['0'];
  } else if (selectedCategory === DataCategories.GenderCounts) {
    chartCategories = ['male', 'female'];
  } else if (selectedCategory === DataCategories.RacialCounts) {
    chartCategories = [
      'white/caucasian',
      'black/african american',
      'asian',
      'hispanic/latino',
      'pacific islander',
      'native american/indigenous'
    ];
  }

  const chartColors = [
    'blue',
    'red',
    'orange',
    'amber',
    'purple',
    'lime',
    'green',
    'pink',
    'emerald',
    'cyan',
    'teal',
    'yellow',
    'zinc',
    'stone',
    'sky',
    'indigo',
    'neutral',
    'violet',
    'slate',
    'fuchsia',
    'rose',
    'gray'
  ];

  useEffect(() => {
    setIsClient(true);
  }, []);

  return (
    <>
      {isClient && (
        <Joyride
          continuous
          run={runTour}
          scrollToFirstStep
          showProgress
          showSkipButton
          steps={steps}
          callback={handleJoyrideCallback}
          styles={{
            options: {
              zIndex: 10000 // Ensure Joyride tooltip is above other elements
            }
          }}
        />
      )}
      <section className="flex-col justify-center items-center space-y-6 pb-8 pt-5 md:pb-12 md:pt-5 lg:pb-32 lg:pt-5">
        <div className="flex flex-col items-center px-40">
          <Card>
            <TabGroup
              index={Object.values(DataCategories).indexOf(selectedCategory)}
              onIndexChange={(index) =>
                setSelectedCategory(Object.values(DataCategories)[index])
              }
            >
              <TabList className="mb-4" variant="line">
                <Tab>Total Counts</Tab>
                <Tab>Gender Counts</Tab>
                <Tab>Racial Counts</Tab>
                <button
                  onClick={() =>
                    (window.location.href = 'http://localhost:3000/docs')
                  } // Replace this with your actual documentation page URL
                  style={{
                    backgroundColor: 'transparent',
                    border: 'none',
                    cursor: 'pointer',
                    color: 'inherit' // Adjust color to fit your design
                  }}
                  title="Documentation"
                >
                  <FontAwesomeIcon icon={faInfoCircle} size="lg" />{' '}
                  {/* You can adjust the size (lg, 2x, etc.) */}
                </button>
              </TabList>
            </TabGroup>
            <Title>Dynamic Disease Data Visualization</Title>
            <Subtitle>
              Counts per disease overall and for each subgroup.
            </Subtitle>

            <div
              style={{
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center',
                flex: '70%'
              }}
            >
              {/* Disease Multiselect */}
              <MultiSelect
                value={selectedDiseases}
                onValueChange={setSelectedDiseases}
                placeholder="Select Diseases"
                style={{ flex: '30%', marginRight: '20px'}}
              >
                {diseaseNames.map((disease) => (
                  <MultiSelectItem key={disease} value={disease}>
                    {disease}
                  </MultiSelectItem>
                ))}
              </MultiSelect>

              {/* Window Dropdown */}
              {selectedCategory !== DataCategories.TotalCounts && (
                  <Select
                    value={selectedWindow}
                    onValueChange={setSelectedWindow}
                    style={{
                      flex: '20%',
                      marginLeft: '20px',
                      marginRight: '20px',
                      opacity: dataSource === DataSourceOptions.Pile ? 0.3 : 1,  // Shadowed effect when disabled
                      pointerEvents: dataSource === DataSourceOptions.Pile ? 'none' : 'auto',  // Disables interaction
                    }}
                  >
                    {Object.entries(WindowOptions).map(([key, value]) => (
                      <SelectItem key={key} value={value}>
                        {key}
                      </SelectItem>
                    ))}
                  </Select>
              )}

              {/* Sort Key Dropdown */}
              <Select
                value={sortKey}
                onValueChange={setSortKey}
                style={{ flex: '20%' }}
              >
                {renderSortKeyOptions()}
              </Select>

              {/* Data Source Dropdown */}
              <Select
                value={dataSource}
                onValueChange={setDataSource}
                style={{ flex: '20%', marginLeft: '20px' }}
              >
                {Object.entries(DataSourceOptions).map(([key, value]) => (
                  <SelectItem key={key} value={value}>
                    {key}
                  </SelectItem>
                ))}
              </Select>

              {/* Sort Order Button */}
              <button
                onClick={() =>
                  setSortOrder(sortOrder === 'asc' ? 'desc' : 'asc')
                }
                className="btn mt4"
                style={{
                  marginTop: '0px',
                  flex: '20%',
                  marginLeft: '20px',
                  alignSelf: 'center'
                }}
              >
                {sortOrder === 'asc' ? 'Ascending' : 'Descending'}
              </button>

              {/* Download Button with Icon */}
              <button
                onClick={() => downloadJsonData('chartData')}
                style={{
                  backgroundColor: 'white',
                  color: 'black',
                  flex: '20px',
                  marginLeft: '10px'
                }}
                className="btn mt-4"
              >
                <FileDownloadIcon />
              </button>
            </div>
            <BarChart
              className="mt-4 h-80"
              data={dataToShow}
              index="disease"
              categories={chartCategories}
              colors={chartColors}
              stack={false} // Set to true for stacked bar chart
              yAxisWidth={60}
            />
          </Card>
        </div>
        {selectedCategory !== DataCategories.TotalCounts && (
          <div className="flex flex-col items-center px-40">
            <Card>
              <TabGroup
                index={Object.values(DataCategories).indexOf(selectedCategory)}
                onIndexChange={(index) =>
                  setSelectedCategory(Object.values(DataCategories)[index])
                }
              >
                <TabList className="mb-4" variant="line">
                  <Tab>Total Counts</Tab>
                  <Tab>Gender Counts</Tab>
                  <Tab>Racial Counts</Tab>
                </TabList>
              </TabGroup>
              <Title>Real World Representativeness</Title>
              <Subtitle>
                The actual occurrence rate of a condition or characteristic within a specific population, observed in everyday, non-experimental settings.
              </Subtitle>

              <div
                style={{
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  flex: '70%'
                }}
              >
                {/* Disease Multiselect */}
                <MultiSelect
                  value={selectedDiseases}
                  onValueChange={setSelectedDiseases}
                  placeholder="Select Diseases"
                  style={{ flex: '30%' }}
                >
                  {diseaseNames.map((disease) => (
                    <MultiSelectItem key={disease} value={disease}>
                      {disease}
                    </MultiSelectItem>
                  ))}
                </MultiSelect>

                {/* Download Button with Icon */}
                <button
                  onClick={() => downloadJsonData('additionalChartData')}
                  style={{
                    backgroundColor: 'white',
                    color: 'black',
                    flex: '20px',
                    marginLeft: '10px'
                  }}
                  className="btn mt-4"
                >
                  <FileDownloadIcon />
                </button>
              </div>
              <BarChart
                className="mt-4 h-80"
                data={additionalChartData}
                index="disease"
                categories={chartCategories}
                colors={chartColors}
                stack={false} // Set to true for stacked bar chart
                yAxisWidth={60}
              />
            </Card>
          </div>
        )}
      </section>
    </>
  );
};

export default ChartPage;
