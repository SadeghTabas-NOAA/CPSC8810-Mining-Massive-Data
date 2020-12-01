## CPSC8810 - Mining Massive Data

### Timeline:
|Num| Todo List | Deadline | Status |
| --- | --- | --- | --- |
|01| Download the Datasets from GRDC website | Sep 14 | Done! |
|02| Extract the Stations with less than 10% missing values | Sep 21 | Done! |
|03| Implement an Automatic ARIMA model to fill the missing values | Sep 28 | Done! |
|04| Submit the first report (Checkpoint 1) | Sep 30 | Done! |
|05| Implement a Machine Learning Method to Forecast Streamflow | Oct 28 | Done |
|06| Submit Checkpoint 2 | Oct 31 | Done |
|07| Submit Checkpoint 3 and final report| Nov 30 | Done |
|05| Presentation | Dec 8| Working! |

### Folder description

Datasets: Each input station data comprises information from both GRDC and NCDC stations
Documents: Empty
Reports: Contains checkpoint reports
Models:
    1. Two ipython notebooks fill the missing values using two different deep neural networks
    2. ARIMA.py replaces missing values with Autoregressive integrated moving average method
    3. GRDC_visualization.py performs analytics, given a world meterological union subregion, parse the grdc stations data and find geographically closest stations
       that are active the same time period
    4. folium.py visualizes station information and corresponding streamflow time series in a global map using folium package
    5. LSTM_Singlelayer, LSTM_CNN, MLP are three data driven models used in our project
    6. Streamflow prediction app with keras,django is an app to run inference on streamflow prediction model for one station
    7. 




