# SeleniumCoordinates
An alternative method to obtain coordinates for a set of addresses
## Purpose
Use Python in combination with Selenium webdriver and pandas in order to perform a series of resquests consisting on street addresses and obtain the corresponding (approximate) latitude and longitude.
## Inputs and outputs
<ul>
  <li> <b>Inputs</b> (<i>InputAddresses</i>): a file containing a list with addresses requests. </li>
  <li> <b>Outputs</b> (<i>outputAddLatLon</i>): a file containing a list with addresses requests and two more columns with the corresponding latitudes and longitudes. </li>		
</ul>

## Important remarks
<ul>
<li> In order to properly work it is necessary to NOT minimize the browser window. If it gets minimized, the output coordinates will not be updated for subsequent addresses. <li>
<li> Please modify the path to your chromedriver in the script. In Windows, add the location chromedriver.exe to the path. <li>  
</ul>


