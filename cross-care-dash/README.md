# Dashboard for Cross Care

## To install and run

**Change directory to cross-care-dash**
```bash
cd cross-care-dash
```

**Then run the following commands to install dependencies**
```bash
pip install flask
npm install
```

**To run react server**
```bash
npm run dev
```

**To run flask server**
```bash
python app/tables/data_sort.py
```


## TODO
- Think about disease-drugs table as many to many

- dash processing temporal data
  - See here https://www.tremor.so/docs/visualizations/line-chart
  - need to add date key 
  - need to create different lines for each group + disease as can only have one category in the line chart i think 
  - rename for category_time_counts e.g. total_monthly_counts.json
  - add slider for years in temporal data
- Flask
  - allow time selection for temporal data

## Interesting Co-occurences

