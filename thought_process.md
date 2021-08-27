## Thought process

This file lists the reasons and thinking behind the steps and choices made for the project. 

### Data extraction
We already had the data in  `json` format but moving forward we will need to extract data for analysis. 
The thinking here was to treat the dummy data as if this is the data we extracted from a real user. 

### Processing Data
Since for data insertion and plotting the data same functions are needed, I decided to put all the functions at one place under a class. 
These functions can be used even further for future tasks. 

The dummy data that we are dealing with is missing a lot of information which I believe would be available while working the real data. 
For example location, account_owner etc are empty columns. 

### Plotting Data

This script is created for ease of calling the functions we want to use. 
For plotting data, we can call the functions accordingly from the class. 
In a real setting, this script's functions can be called based on user's choice. 

There is a function to plot Word Cloud from merchant names, this was included just to show how we can give multiple features to the user. In this case, we can show them a cloud of merchant names they dealt with. 

### Storing Data 

For data storage, I went with `sqlite3` just for the sake of time. We can definitely choose better options
based on our preference. The data stored in the db for now is set to store the monthly expenses of the user based on categories, so that we can know how much a user is spending each month and on what
but this can be expanded further based.


#### Some questions and things to look into
There were some observations I had, but due to time constraints, I couldn't dig more into. 
For example: . 

- Negative values present in `amount` column in data. First thoughts that came to my mind is: 
    - Is this data wrong? Are the negative values present by mistake.
    - Does this represent the loan or debt taken from the service?
    - Does this represent, the customer filled this in app by mistake and wants to remove it from calculation?
    
For now, the results I computed were under the assumption that the data we have contains only positive values but this is the edge case. 


#### What else can we do? 

There is a lot more we can do here. For example, creating APIs, creating Dashboards with Plotly, more analysis and more data etc are intersting things we can do further. 

