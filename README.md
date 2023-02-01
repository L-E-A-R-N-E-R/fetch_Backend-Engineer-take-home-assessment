# fetch_Backend-Engineer-take-home-assessment

# Follow the step by step instructions below to execute the program

1. Download the project zip file and then extract it

2. Open your terminal and access the project folder with cd command

   cd fetch (change directory to the project folder)
   
3. Build the docker image

   Inside fetch, build the docker image using the command

   
   docker build --tag fetch-python-docker .
   
   EXPECTED OUTPUT
   
   ![image](https://user-images.githubusercontent.com/41851792/216139849-fd04459c-237d-47ea-81e7-104283cb909d.png)

4. Launch the app

   Inside the container, there is the flask app. Running the container will launch the app. In order to run the container, use the following command
   
   docker run --publish 5000:5000 fetch-python-docker

   EXPECTED OUTPUT
   
   ![image](https://user-images.githubusercontent.com/41851792/216140072-b3b0869b-6711-4e59-98a1-a9d3b3494aeb.png)

   The local server will start on port 5000
   
5. Sending http requests to the server

   POST REQUEST  (/receipts/process)
   
   Here, we will use CURL to send POST and GET requests to the server. There are 5 test cases inside the test folder, they are all json files and we will use one        test case at a time. In each test case, I have considered a hybrid of scenarios described in the 'Description' column of the table. The Payload column describes      the json file and the 'Input command and Output' column shows output for the respective http request to the server. 
   
   Sending the POST requests will generate the receipt id.
   Sending a GET request will display the points for a receipt id.
   
   Open another terminal and inside the project folder 'fetch', type the curl commands to see the output.
   
   


