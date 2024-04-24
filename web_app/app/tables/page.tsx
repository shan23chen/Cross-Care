// @ts-nocheck
'use client';

import React, { useState, useEffect } from 'react';
import {
  Card,
  Table,
  TableRow,
  TableCell,
  TableHead,
  TableHeaderCell,
  TableBody,
  Tab,
  TabList,
  TabGroup,
  Select,
  SelectItem,
  MultiSelect,
  MultiSelectItem
} from '@tremor/react';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import Joyride, { CallBackProps, STATUS, Step } from 'react-joyride';
import ArrowDownwardIcon from '@mui/icons-material/ArrowDownward';
import ArrowUpwardIcon from '@mui/icons-material/ArrowUpward';
import FileDownloadIcon from '@mui/icons-material/FileDownload';
import {
  faChevronLeft,
  faChevronRight,
  faDownload,
  faArrowUp,
  faArrowDown,
  faInfoCircle
} from '@fortawesome/free-solid-svg-icons';

const DataCategories = {
  TotalCounts: 'total',
  GenderCounts: 'gender',
  RacialCounts: 'racial',
  DrugCounts: 'drug' // need to think about this as many to many
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

const TablePage = () => {
  const [selectedCategory, setSelectedCategory] = useState(
    DataCategories.TotalCounts
  );
  const [sortKey, setSortKey] = useState('disease');
  const [sortOrder, setSortOrder] = useState('asc'); // Default sort order
  const [dataToShow, setDataToShow] = useState([]);
  const [prevalenceData, setPrevalenceData] = useState([]);
  const [selectedWindow, setSelectedWindow] = useState(WindowOptions.Window250);
  const [dataSource, setDataSource] = useState(DataSourceOptions.Arxiv); // State for selected data source
  const [selectedDiseases, setSelectedDiseases] = useState([]);
  const [diseaseNames, setDiseaseNames] = useState([]);
  const [isClient, setIsClient] = useState(false);
  const [dataSize, setDataSize] = useState(0);
  const [runTour, setRunTour] = useState(false); // State to control the visibility of the tour
  const [steps, setSteps] = useState<Step[]>([
    // Define the steps for the tour
    {
      target: 'body',
      content: (
        <div>
          <p style={{ marginBottom: '16px' }}>
            {' '}
            <strong> Welcome to Our Health Data Exploration! </strong>
          </p>
          <p style={{ marginBottom: '16px' }}>
            Explore{' '}
            <span style={{ background: '#D3D3D3' }}>
              disparities in global health
            </span>{' '}
            through our dataset. <strong>COVID-19</strong>, leading with{' '}
            <span style={{ background: '#D3D3D3' }}>141,099 cases</span>,
            showcases the biases in attention and resources compared to other
            diseases.
          </p>
          <p style={{ marginBottom: '16px' }}>
            {' '}
            Diseases like infections, diabetes, and mood disorders highlight the
            story of{' '}
            <span style={{ background: '#D3D3D3' }}>unequal focus</span>.
            Let&apos;s dive into the data together.
          </p>
          <p>
            🔍 <strong>Begin your journey</strong> towards understanding{' '}
            <span style={{ background: '#D3D3D3' }}>global health equity</span>.
          </p>
          <div
            style={{
              display: 'flex',
              justifyContent: 'center',
              marginTop: '10px'
            }}
          >
            <img
              style={{ height: '100px' }}
              src="./corona.png"
              alt="Italian Trulli"
            />
          </div>
        </div>
      ),
      placement: 'center'
    },
    {
      target: '.tab-list > :nth-child(1)',
      content: 'Select one or multiple diseases to filter the data.',
      placement: 'bottom'
    },
    {
      target: '.window-select',
      content:
        'Choose a window option to view data aggregated over different time frames.',
      placement: 'bottom'
    },
    {
      target: '.sort-select',
      content: 'Sort the data based on different criteria.',
      placement: 'bottom'
    },
    {
      target: '.download-button',
      content: 'Download the displayed data as a JSON file.',
      placement: 'bottom'
    }
  ]);

  const sortKeys = {
    [DataCategories.TotalCounts]: ['disease', 'real', '0'],
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
        // Set the first 15 diseases as default selected diseases
        const initialDiseases = [
          'arthritis',
          'asthma',
          'bronchitis',
          'cardiovascular disease',
          'chronic kidney disease',
          'coronary artery disease',
          'covid-19',
          'deafness',
          'diabetes',
          'hypertension',
          'liver failure',
          'mental illness',
          'mi',
          'perforated ulcer',
          'visual anomalies'
        ];
        setSelectedDiseases(initialDiseases);
        console.log(names);
      } else {
        console.error('Server error:', response.status);
      }
    } catch (error) {
      console.error('Network error:', error);
    }
  };

  const fetchPrevalence = async () => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/get-prevalence`);
      if (response.ok) {
        const data = await response.json();
        setPrevalenceData(data);
        console.log(data);
      } else {
        console.error('Server error:', response.status);
      }
    } catch (error) {
      console.error('Network error:', error);
    }
  };

  useEffect(() => {
    fetchPrevalence();
    fetchDiseaseNames();
  }, []); // Empty dependency array to run only on component mount

  // Function to fetch sorted data from the server
  const fetchSortedData = async () => {
    const selectedDiseasesString = selectedDiseases.join(',');
    if (selectedCategory === DataCategories.TotalCounts) {
      try {
        const response = await fetch(
          `http://127.0.0.1:5000/get-sorted-data?category=${selectedCategory}&selectedWindow=${selectedWindow}&sortKey=${sortKey}&sortOrder=${sortOrder}&page=${currentPage}&per_page=${pageSize}&selectedDiseases=${selectedDiseasesString}&dataSource=pile`
        );
        if (response.ok) {
          const data = await response.json();
          setDataSize(data[0]);
          const sortedData = data[1];
          setDataToShow(sortedData);
        } else {
          console.error('Server error:', response.status);
        }
      } catch (error) {
        console.error('Network error:', error);
      }
    } else {
      try {
        const response = await fetch(
          `http://127.0.0.1:5000/get-sorted-data?category=${selectedCategory}&selectedWindow=${selectedWindow}&sortKey=${sortKey}&sortOrder=${sortOrder}&page=${currentPage}&per_page=${pageSize}&selectedDiseases=${selectedDiseasesString}&dataSource=${dataSource}`
        );
        if (response.ok) {
          const data = await response.json();
          setDataSize(data[0]);
          const sortedData = data[1];
          setDataToShow(sortedData);
        } else {
          console.error('Server error:', response.status);
        }
      } catch (error) {
        console.error('Network error:', error);
      }
    }
  };

  const handleSort = (newSortKey) => {
    if (sortKey === newSortKey) {
      // Toggle sort order if the same column header is clicked
      setSortOrder(sortOrder === 'asc' ? 'desc' : 'asc');
    } else {
      // Change the sort key and set order to ascending by default
      setSortKey(newSortKey);
    }
  };

  useEffect(() => {
    fetchSortedData();
  }, [
    selectedCategory,
    selectedWindow,
    dataSource,
    sortKey,
    sortOrder,
    currentPage,
    selectedDiseases
  ]);

  // Determine display names based on selected category
  let displayNames = {};
  if (selectedCategory === DataCategories.TotalCounts) {
    displayNames = totalDisplayNames;
  } else if (selectedCategory === DataCategories.GenderCounts) {
    displayNames = genderDisplayNames;
  } else if (selectedCategory === DataCategories.RacialCounts) {
    displayNames = racialDisplayNames;
  }

  // Render sort key dropdown options based on the current category
  const renderSortKeyOptions = () => {
    return Object.keys(displayNames).map((displayName) => (
      <SelectItem key={displayName} value={displayNames[displayName]}>
        {displayName}
      </SelectItem>
    ));
  };

  useEffect(() => {
    // Only run the tour if the 'tourShown' flag is not set in localStorage
    const tourShown = localStorage.getItem('tourShown');
    if (!tourShown) {
      setRunTour(true);
    }
  }, []); // This useEffect will run only once when the component mounts

  const handleJoyrideCallback = (data) => {
    const { status } = data;
    if ([STATUS.FINISHED, STATUS.SKIPPED].includes(status)) {
      setRunTour(false); // Hide the tour once it's finished or skipped
      localStorage.setItem('tourShown', 'true'); // Set a flag in localStorage
    }
  };

  const downloadJsonData = () => {
    let dataToDownload;

    dataToDownload = dataToShow;

    // Create a JSON string from the selected data
    const jsonData = JSON.stringify(dataToDownload);

    // Create a Blob object containing the JSON data
    const blob = new Blob([jsonData], { type: 'application/json' });

    // Create a download link element
    const a = document.createElement('a');
    a.href = window.URL.createObjectURL(blob);

    // Determine the filename based on the dataSource
    const filename = 'chartData';
    a.download = filename;

    // Trigger a click event to initiate the download
    a.click();
  };

  const renderDownloadButton = (onClickHandler) => {
    return (
      <button
        onClick={onClickHandler}
        style={{
          backgroundColor: 'white',
          color: 'black',
          marginLeft: '10px'
        }}
        className="btn mt-4"
      >
        <FileDownloadIcon/>
      </button>
    );
  };

  useEffect(() => {
    setIsClient(true);
  }, []);

  const findDiseaseWithDemographic = (data, diseaseName, demographic) => {
    return data.find(
      (item) =>
        item.disease.toLowerCase() === diseaseName.toLowerCase() &&
        item.demographic.toLowerCase() === demographic.toLowerCase()
    );
  };

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
            buttonNext: {
              backgroundColor: '#750014', // Example: Change the Next button to blue
              color: '#fff',
              borderBlockColor: 'white',
              borderColor: 'white'
            },
            buttonBack: {
              color: '#750014'
            },
            options: {
              primaryColor: '#000'
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
              <TabList className="mb-4 tab-list" variant="line">
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

            <div
              style={{
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center'
              }}
            >
              {/* Disease Multiselect */}
              <MultiSelect
                value={selectedDiseases}
                onValueChange={setSelectedDiseases}
                placeholder="Select Diseases"
                style={{ flex: '30%', marginRight: '20px' }}
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
                    marginLeft: '40px',
                    opacity: dataSource === DataSourceOptions.Pile ? 0.3 : 1, // Shadowed effect when disabled
                    pointerEvents:
                      dataSource === DataSourceOptions.Pile ? 'none' : 'auto' // Disables interaction
                  }}
                >
                  {Object.entries(WindowOptions).map(([key, value]) => (
                    <SelectItem key={key} value={value}>
                      {key}
                    </SelectItem>
                  ))}
                </Select>
              )}

              {/* Data Source Dropdown */}
              {selectedCategory !== DataCategories.TotalCounts && (
                <Select
                  value={dataSource}
                  onValueChange={(newDataSource) => {
                    setDataSource(newDataSource);
                  }}
                  style={{ flex: '20%', marginLeft: '40px' }}
                >
                  {Object.entries(DataSourceOptions).map(([key, value]) => (
                    <SelectItem key={key} value={value}>
                      {key}
                    </SelectItem>
                  ))}
                </Select>
              )}

              <button
                onClick={() => downloadJsonData()}
                style={{
                  backgroundColor: 'white',
                  color: 'black',
                  marginLeft: '10px'
                }}
                className="btn mt-4"
              >
                <FileDownloadIcon />
              </button>
            </div>
            <div
              style={{
                color: '#3c84f4',
                opacity: 0.7,
                fontSize: '13px',
                padding: '5px',
                margin: '5px',
                borderRadius: '5px'
              }}
            >
              <p>* numbers in blue are related to real world prevalence.</p>
            </div>

            <Table className="mt-4">
              <TableHead>
                <TableRow>
                  <TableHeaderCell onClick={() => handleSort('disease')}>
                    Disease
                    {sortKey === 'disease' && (
                      <span style={{ marginLeft: '8px' }}>
                        {sortOrder === 'asc' ? (
                          <ArrowDownwardIcon />
                        ) : (
                          <ArrowUpwardIcon />
                        )}
                      </span>
                    )}
                  </TableHeaderCell>
                  {selectedCategory === DataCategories.TotalCounts && (
                    <TableHeaderCell
                      className="text-right"
                      onClick={() => handleSort('0')}
                    >
                      Counts
                      {sortKey === '0' && (
                        <span style={{ marginLeft: '8px' }}>
                          {sortOrder === 'asc' ? (
                            <ArrowDownwardIcon />
                          ) : (
                            <ArrowUpwardIcon />
                          )}
                        </span>
                      )}
                    </TableHeaderCell>
                  )}{' '}
                  {selectedCategory === DataCategories.GenderCounts && (
                    <>
                      <TableHeaderCell
                        className="text-right"
                        onClick={() => handleSort('male')}
                      >
                        Male
                        {sortKey === 'male' && (
                          <span style={{ marginLeft: '8px' }}>
                            {sortOrder === 'asc' ? (
                              <ArrowDownwardIcon />
                            ) : (
                              <ArrowUpwardIcon />
                            )}
                          </span>
                        )}
                      </TableHeaderCell>
                      <TableHeaderCell
                        className="text-right"
                        onClick={() => handleSort('female')}
                      >
                        Female
                        {sortKey === 'female' && (
                          <span style={{ marginLeft: '8px' }}>
                            {sortOrder === 'asc' ? (
                              <ArrowDownwardIcon />
                            ) : (
                              <ArrowUpwardIcon />
                            )}
                          </span>
                        )}
                      </TableHeaderCell>
                    </>
                  )}
                  {selectedCategory === DataCategories.RacialCounts && (
                    <>
                      <TableHeaderCell
                        onClick={() => handleSort('white/caucasian')}
                      >
                        White/Caucasian
                        {sortKey === 'white/caucasian' && (
                          <span style={{ marginLeft: '8px' }}>
                            {sortOrder === 'asc' ? (
                              <ArrowDownwardIcon />
                            ) : (
                              <ArrowUpwardIcon />
                            )}
                          </span>
                        )}
                      </TableHeaderCell>
                      <TableHeaderCell
                        onClick={() => handleSort('black/african american')}
                      >
                        Black/African American
                        {sortKey === 'black/african american' && (
                          <span style={{ marginLeft: '8px' }}>
                            {sortOrder === 'asc' ? (
                              <ArrowDownwardIcon />
                            ) : (
                              <ArrowUpwardIcon />
                            )}
                          </span>
                        )}
                      </TableHeaderCell>
                      <TableHeaderCell onClick={() => handleSort('asian')}>
                        Asian
                        {sortKey === 'asian' && (
                          <span style={{ marginLeft: '8px' }}>
                            {sortOrder === 'asc' ? (
                              <ArrowDownwardIcon />
                            ) : (
                              <ArrowUpwardIcon />
                            )}
                          </span>
                        )}
                      </TableHeaderCell>
                      <TableHeaderCell
                        onClick={() => handleSort('hispanic/latino')}
                      >
                        Hispanic/Latino
                        {sortKey === 'hispanic/latino' && (
                          <span style={{ marginLeft: '8px' }}>
                            {sortOrder === 'asc' ? (
                              <ArrowDownwardIcon />
                            ) : (
                              <ArrowUpwardIcon />
                            )}
                          </span>
                        )}
                      </TableHeaderCell>
                      <TableHeaderCell
                        onClick={() => handleSort('pacific islander')}
                      >
                        Pacific Islander
                        {sortKey === 'pacific islander' && (
                          <span style={{ marginLeft: '8px' }}>
                            {sortOrder === 'asc' ? (
                              <ArrowDownwardIcon />
                            ) : (
                              <ArrowUpwardIcon />
                            )}
                          </span>
                        )}
                      </TableHeaderCell>

                      <TableHeaderCell
                        onClick={() => handleSort('native american/indigenous')}
                      >
                        Native American/Indigenous
                        {sortKey === 'native american/indigenous' && (
                          <span style={{ marginLeft: '8px' }}>
                            {sortOrder === 'asc' ? (
                              <ArrowDownwardIcon />
                            ) : (
                              <ArrowUpwardIcon />
                            )}
                          </span>
                        )}
                      </TableHeaderCell>
                    </>
                  )}
                </TableRow>
              </TableHead>
              <TableBody>
                {dataToShow.map((item, index) => (
                  <TableRow key={index}>
                    <TableCell>{item.disease}</TableCell>
                    {selectedCategory === DataCategories.TotalCounts && (
                      <TableCell className="text-right">{item['0']}</TableCell>
                    )}
                    {selectedCategory === DataCategories.GenderCounts && (
                      <>
                        <TableCell className="text-right">
                          <span title="Dataset count">{item.male}</span>
                          {findDiseaseWithDemographic(
                            prevalenceData,
                            item.disease,
                            'male'
                          ) && (
                            <span
                              style={{ color: '#3c84f4', opacity: 0.7 }}
                              title="Real world prevalence"
                            >
                              {' | ' +
                                findDiseaseWithDemographic(
                                  prevalenceData,
                                  item.disease,
                                  'male'
                                ).count}
                            </span>
                          )}
                        </TableCell>

                        <TableCell className="text-right">
                          <span title="Dataset count">{item.female}</span>
                          {findDiseaseWithDemographic(
                            prevalenceData,
                            item.disease,
                            'female'
                          ) && (
                            <span
                              style={{ color: '#3c84f4', opacity: 0.7 }}
                              title="Real world prevalence"
                            >
                              {' | ' +
                                findDiseaseWithDemographic(
                                  prevalenceData,
                                  item.disease,
                                  'female'
                                ).count}
                            </span>
                          )}
                        </TableCell>
                      </>
                    )}
                    {selectedCategory === DataCategories.RacialCounts && (
                      <>
                        <TableCell className="text-right">
                          <span title="Dataset count">
                            {item['white/caucasian']}
                          </span>
                          {findDiseaseWithDemographic(
                            prevalenceData,
                            item.disease,
                            'white/caucasian'
                          ) && (
                            <span
                              style={{ color: '#3c84f4', opacity: 0.7 }}
                              title="Real world prevalence"
                            >
                              {' | ' +
                                findDiseaseWithDemographic(
                                  prevalenceData,
                                  item.disease,
                                  'white/caucasian'
                                ).count}
                            </span>
                          )}
                        </TableCell>
                        <TableCell className="text-right">
                          <span title="Dataset count">
                            {item['black/african american']}
                          </span>
                          {findDiseaseWithDemographic(
                            prevalenceData,
                            item.disease,
                            'black/african american'
                          ) && (
                            <span
                              style={{ color: '#3c84f4', opacity: 0.7 }}
                              title="Real world prevalence"
                            >
                              {' | ' +
                                findDiseaseWithDemographic(
                                  prevalenceData,
                                  item.disease,
                                  'black/african american'
                                ).count}
                            </span>
                          )}
                        </TableCell>
                        <TableCell className="text-right">
                          <span title="Dataset count">{item['asian']}</span>
                          {findDiseaseWithDemographic(
                            prevalenceData,
                            item.disease,
                            'asian'
                          ) && (
                            <span
                              style={{ color: '#3c84f4', opacity: 0.7 }}
                              title="Real world prevalence"
                            >
                              {' | ' +
                                findDiseaseWithDemographic(
                                  prevalenceData,
                                  item.disease,
                                  'asian'
                                ).count}
                            </span>
                          )}
                        </TableCell>
                        <TableCell className="text-right">
                          <span title="Dataset count">
                            {item['hispanic/latino']}
                          </span>
                          {findDiseaseWithDemographic(
                            prevalenceData,
                            item.disease,
                            'hispanic/latino'
                          ) && (
                            <span
                              style={{ color: '#3c84f4', opacity: 0.7 }}
                              title="Real world prevalence"
                            >
                              {' | ' +
                                findDiseaseWithDemographic(
                                  prevalenceData,
                                  item.disease,
                                  'hispanic/latino'
                                ).count}
                            </span>
                          )}
                        </TableCell>
                        <TableCell className="text-right">
                          {item['pacific islander']}
                        </TableCell>
                        <TableCell className="text-right">
                          <span title="Dataset count">
                            {item['native american/indigenous']}
                          </span>
                          {findDiseaseWithDemographic(
                            prevalenceData,
                            item.disease,
                            'native american/indigenous'
                          ) && (
                            <span
                              style={{ color: '#3c84f4', opacity: 0.7 }}
                              title="Real world prevalence"
                            >
                              {' | ' +
                                findDiseaseWithDemographic(
                                  prevalenceData,
                                  item.disease,
                                  'native american/indigenous'
                                ).count}
                            </span>
                          )}
                        </TableCell>
                      </>
                    )}
                  </TableRow>
                ))}
              </TableBody>
            </Table>
            <div
              className="toastContent"
              style={{
                display: 'flex',
                justifyContent: 'center',
                alignContent: 'center'
              }}
            >
              <button
                onClick={() => setCurrentPage(currentPage - 1)}
                className={`btn mt-4 ${currentPage <= 1 ? 'invisible' : ''}`}
                disabled={currentPage <= 1}
                style={{
                  pointerEvents: currentPage <= 1 ? 'none' : 'auto',
                  border: 'none',
                  background: 'transparent',
                  margin: '0px',
                  alignSelf: 'center'
                }}
              >
                <FontAwesomeIcon
                  icon={faChevronLeft}
                  size="lg"
                  style={{ color: 'black' }}
                />
              </button>

              <span style={{ alignSelf: 'center' }}>Page {currentPage}</span>

              <button
                onClick={() => setCurrentPage(currentPage + 1)}
                className={`btn mt-4 ${
                  dataSize <= currentPage * pageSize ? 'invisible' : ''
                }`}
                disabled={dataSize <= currentPage * pageSize}
                style={{
                  pointerEvents:
                    dataSize <= currentPage * pageSize ? 'none' : 'auto',
                  border: 'none',
                  background: 'transparent',
                  margin: '0px',
                  alignSelf: 'center'
                }}
              >
                <FontAwesomeIcon
                  icon={faChevronRight}
                  size="lg"
                  style={{ color: 'black' }}
                />
              </button>
            </div>
          </Card>
        </div>
      </section>
    </>
  );
};

export default TablePage;
