## Question 1
I chose to have the API filter before returning data, because that way I would have less processing to do with the 
data and I would also not need to add that additional complexity to my solution. 

## How to Use Program
As of now, my solution uses hard coded variables within the program for the API url and keys, but prompts for user input for question 3 when run. 
The file can be run from the terminal using `python broad.py`.

## Solution Limitations
The biggest limitation is that the solution for questions three is incomplete, but does work for any two stops that are separated by one
line change. This works for the majority of MBTA stops as most lines overlap at least once, but for example the Blue
and Red lines do not share a stop, and therefore my solution does not work to find a path between stops on those lines.

Another limitation is the lack of a testing library and unit test file. 
I would have added this functionality, but did not have the time to refactor my solution to work with the testing library, so instead relied on manual checking which is not preferred.

## Future Improvements and Changes
A potential improvement would be to switch from the use of dictionaries to an object-oriented class schedule. 
This would be very beneficial for adding additional functionality in the future, as well as for making the third 
question into a fully working solution.

This class structure could look something like this:
- Class Route: contains name and list of Stops on Route
- Class Stops: contains name and list of Routes that the Stop is a part of

By having this structure, it would be easier to navigate from one stop and find the path to another even over several line changes, thus solving my current solution's issues with the third question. 

## Example expected output: 
Routes: Red Line, Mattapan Trolley, Orange Line, Green Line B, Green Line C, Green Line D, Green Line E, Blue Line


Route with most stops: Green Line B, 24

Route with least stops: Mattapan Trolley, 8


Stops that connect two or more subway routes:

Park Street: Red Line, Green Line B, Green Line C, Green Line D, Green Line E

Downtown Crossing: Red Line, Orange Line

Ashmont: Red Line, Mattapan Trolley

State: Orange Line, Blue Line

Haymarket: Orange Line, Green Line D, Green Line E

North Station: Orange Line, Green Line D, Green Line E

Government Center: Green Line B, Green Line C, Green Line D, Green Line E, Blue Line

Boylston: Green Line B, Green Line C, Green Line D, Green Line E

Arlington: Green Line B, Green Line C, Green Line D, Green Line E

Copley: Green Line B, Green Line C, Green Line D, Green Line E

Hynes Convention Center: Green Line B, Green Line C, Green Line D

Kenmore: Green Line B, Green Line C, Green Line D

Saint Paul Street: Green Line B, Green Line C


Please enter the stop names you wish to find the connection between as prompted, or enter "Stop" to end the program

Enter the first stop: Ashmont

Enter the second stop: Davis

Ashmont -> Davis: Red Line
