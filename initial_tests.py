# -*- coding: utf-8 -*-
# import necessary libraries 
import requests

#this function verifies a correct response from our REST request
def check_response(response):
  #check status code to make sure everything went well (200= went well)
    if(response.status_code != 200):
        print ("Error with request")
        quit()
        
    else: 
        #json_object is the json object we received
        json_object = response.json()
        if(json_object["success"]):
            print ('success' )
        else: 
            #message is whatever the issue was
            print (json_object["message"])
            quit()
    
    #if we get here and everything is good
    return json_object["result"]  #return result in json objet in the response

#this function prints a ticker's info
def print_ticker_info(ticker):
    print ("Bid: ")
    print(ticker["Bid"])
    print ("Ask: ")
    print(ticker["Ask"])
    print ("Last: ")
    print(ticker["Last"])

#define variables for REST request
url = 'https://bittrex.com/api/v1.1/public/getmarkets'
data = ""

start = time.time()
#Do a GET request from our URL
response1 = requests.get(url, data) 
results = check_response(response1)

#lets look at litecoin result
#loop through array (results), do something for each result (element)
for element in results: 
    #if the current element is litecoin
    if(element["MarketCurrency"]=="LTC"):
        #Litecoin refers to the litecoin element
        Litecoin = element 
        
print ("Litecoin info: ")
print(Litecoin)
    
#now lets look at one specfic ticker
    
#new ticker url

ticker_url = "https://bittrex.com/api/v1.1/public/getticker"
ticker_data = ""

#this REST request requires parameters
tickers_params = {"market": "BTC-LTC"}

#must put parameters after defined url
ticker_response = requests.get(ticker_url, ticker_data, data=tickers_params)
  
#check everything the same as above
ticker_result = check_response(ticker_response)
print_ticker_info(ticker_result)



        


    
    

    
 

    
    