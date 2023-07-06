# Your Forecast - Emoji Weather
#### Video Demo:  <URL https://youtu.be/pyW8nz62-xU>
#### Description:
My objective was to implement a weather web application using emojis in order to convey some of the information that would normally just be text or numbers. I opted to create the web app using Python and Flask, along with Jinja and Javascript to render the HTML files.

In order to get facts about the weather, I used a free API service that provides weather in .json format when a GET call is made to the API's url address. The .json file is long so I created a function in a helpers file in order to parse the key elements from the .json object returned by the API request. There were some issues different names in the json files for the differnt timesteps (daily or hourly) so I had to specify what these were in each instance. The lookup function returns a dictionary of dictionaries that can be used to populate a table with the weather. Also included in a helpers file are are functions that return emojis when they get temperature, precipitation, and wind speed as inputs. 

When a user lands on the weather app on the / route, they are shown a text box to search for a location and an option of hourly or daily as radio buttons. I used radio buttons as they instantly show the two options and are mutually exclusive so the user can easily gather what they do.

If the user searches for a valid location, the api call will be made for their timestep (daily is default) and a POST is made to /weather. Within this app route, the lookup function is called on the location and the output will be assigned to a dictionary object called weather. The /weather route will use a function to return the current date and time and will create a list with those dates and times with appropriate formats depending on if it is an hourly or daily forecast. By design the hourly forecast is limited to 25 of the available 160 hours in the weather dictionary object in order to be able to show the weather at an appropriate scale on the web page.

If the user enters an invalid location and the API call raises an exception as a result, the site flashes a message using flask asking them to try again. 

The /weather route will also call the different functions for the different emojis on the temperature, precipitation, and wind keys in the dictionaries with the outputs being stored in a list. The list, date ranges, weather are all used to render a weather.html template, which displays the weather in a table along with the emojis and some javascript that changes the background color of the temperature cells in the table once the page has fully loaded.

The table is created with a for loop using Jinja. The advantage of this approach is that the same lines of HTML can be used to output both the daily and hourly weather report tables.

An evolution to the web application might be:
- using AJAX to autopopulate the location search bar
- allowing users to switch between daily and hourly without reentering location on the /weather.html page
- allowing users to switch between imperial and metric units

A key learning and takeaway from this final project is to think about all potential use cases and user needs up front. This is because some of the design choices I made limited the opportunity to easily add on the additional functionalities I called out in the list above. 

For example, the coloring for the temperature cells currently uses javascript to change the background color of each table data tag in that row based on the value of the temperature in celsius. Extra work would be needed to implement a version of the website that allows users to switch to farenheit. The issue is not as significant for the emoji functions that currently use metric units to determine the correct emoji because the API request could stay the same and conversion could take place after the emoji functions are called on the weather dictionary in metric units.