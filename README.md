# fetch_Backend-Engineer-take-home-assessment

## Link for problem statement https://github.com/fetch-rewards/receipt-processor-challenge

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
   
   CURL Commands syntax
   
   For POST request:  
   
   curl -X POST http://127.0.0.1:5000/receipts/process -H "Content-Type:application/json" -d@test/case1.json
   
   FOR GET request:   
   
   curl http://127.0.0.1:5000/receipts/{id}/points   (Replace the {id} with the receipt id generated after sending POST request)
   
   Open another terminal and inside the project folder 'fetch', type the curl commands to see the output.
   
   ![image](https://user-images.githubusercontent.com/41851792/216145070-cf3dcfdd-198d-44d9-a0c8-4652c129e05b.png)

   ![image](https://user-images.githubusercontent.com/41851792/216145224-4ff56bd3-c7a7-403f-8577-1ff6ed62524b.png)

   ![image](https://user-images.githubusercontent.com/41851792/216145292-ec062fdd-dda7-45dc-a881-a6a63553a73a.png)
   
   
6. Sample output of the entire process

   ![image](https://user-images.githubusercontent.com/41851792/216145484-7749fee0-e240-4a61-9043-ed82fe6a3f15.png)


# Testing

For testing my program, I have considered a few cases for checking logical errors and validation errors.

## Logical Errors

![image](https://user-images.githubusercontent.com/41851792/216145677-0569dfd6-5cd1-46d9-aeec-60713a5029a2.png)

![image](https://user-images.githubusercontent.com/41851792/216145717-d3629c99-b77a-4bb7-a2b7-6ec84448da91.png)

## Validation Errors

The following cases will return an error code 400 with the description that “The receipt is invalid” if any of the following fields are 


1. Retailer field is missing in the payload (uploaded receipt)
2. purchaseDate is missing in the payload (uploaded receipt)
3. purchaseTime is missing in the payload (uploaded receipt)
4. items is missing in the payload (uploaded receipt)
5. total is missing in the payload (uploaded receipt)
6. The value of the attribute “retailer” has datatype other than string and if it doesn’t match the pattern defined in the api documentation
7. The value of the attribute “total” has datatype other than string and if it doesn’t match the pattern defined in the api documentation
8. The value of the attribute “items” has datatype other than list and if its length is less than 1
9. The value of the attribute “purchaseDate” has datatype other than string and if it doesn’t match the format defined in the api documentation
10. The value of the attribute “purchaseTime” has datatype other than string and if it doesn’t match the format defined in the api documentation
11. The short description of the item has datatype other than string and if it doesn’t match the format defined in the api documentation
12. The price of the item has datatype other than string and if it doesn’t match the format defined in the api documentation


# Assumptions

1. I am assuming that the user has CURL installed in their device. For installation guide, I referred the following website https://help.ubidots.com/en/articles/2165289-learn-how-to-install-run-curl-on-windows-macosx-linux

2. In rule 5, I have assumed that we will always ROUND UP the price to the nearest integer after multiplying it by 0.2. I have made this assumption by referring to the sample test cases provided in the assignment

