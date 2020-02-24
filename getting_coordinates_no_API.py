from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # for locating elements
import pandas as pd
import time

bar = '==========================================================='
msg = 'Please, DO NOT minimize the browser window during execution'

def export_data_frame():
    print('exporting data frame\n ...')
    export_excel = dfloc.to_excel(r'outputAddLatLon.xlsx', index=None, header=True)

# First, declare an approximate latitude and longitude where you want gmaps to make the search of addresses
LAT = '39.4674796'
LON = '-0.3721032'

names_cols = ['name']
dfread = pd.read_excel(r'inputAddresses.xlsx', header=0, names=names_cols,
                   index_col=None)  # Don't forget to add '.xlsx' at the end of the path
df = dfread

numrows = df.shape[0]
numcols = df.shape[1]

latitude = []
longitude = []

driver = webdriver.Chrome()
driver.implicitly_wait(10)

linkofpage="https://www.google.com/maps/@"+LAT+","+LON+",17.00z"
driver.get(linkofpage)

# dataframe that will contain coordinates
dfloc = df

id_search_bar = "searchboxinput"
id_search_button = 'searchbox-searchbutton'
for i in range(numrows):
    driver.find_element_by_id(id_search_bar).clear()
    driver.find_element_by_id(id_search_bar).send_keys(df.iloc[i, 0])
    driver.find_element_by_id(id_search_button).click()
    # we leave the website some time to think
    time.sleep(4)
    address = driver.current_url
    dummy = address.split("@")
    dummy = dummy[-1].split(",")
    print(bar)
    print(msg)
    print(bar)
    print('Address: ', df.iloc[i, 0])
    print(i, dummy[0], dummy[1])
    latitude.append(float(dummy[0]))
    longitude.append(float(dummy[1]))
    dfloc = df.loc[0:i, :]
    print('filas en dataframe: ', dfloc.shape[0])
    print('tamaño de listas: ', len(latitude), len(longitude))
    dfloc['latitude'] = latitude
    dfloc['longitude'] = longitude
    # Since it is a slow process, we export line by line the output file
    export_data_frame()
    dfloc = dfloc.drop(columns=["latitude", "longitude"])

print('let us print a few lines of the data frame\n ...')
print(dfloc.head())
