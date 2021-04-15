import requests
import json
import pandas as pd
from http.client import HTTPSConnection
from base64 import b64encode
import BodyCreator

EmailsFromCSV = []
EmailsFromRequest = []
Config = pd.read_csv("config.csv")
tenantID = Config.iloc[0]["tenantID"]
userName = Config.iloc[0]["UserName"]
password = Config.iloc[0]["Password"]


# create dynamic token with username and password that is going (to be entered from console by the user)
token = b64encode(bytes((f"{userName}:{password}"), encoding="utf-8")).decode("ascii")


# get json file for users in SAP system, with dynamic tenantID (to be entered from console by the user)
requestURL = "https://{0}.accounts.ondemand.com/service/scim/Users".format(tenantID) 
payload	= {}
headers = {
  "Content-Type": "application/scim+json",
  "Authorization": "Basic "+token
}
response = requests.request("GET", requestURL, headers=headers, data=payload)

# parse json response to text
CSVdata = json.loads(response.text) 

# get email property from parsed text
for person in CSVdata["Resources"]: 
  CSVEmail = person["emails"]
  CSVEmailValue = CSVEmail[0]
  EmailsFromRequest.append(CSVEmailValue["value"])
       
# read input csv data and replace nan fields with "NONE" for later operations
data = pd.read_csv("import.csv").fillna("NONE")

# creating json bodies: 
# if mail from input csv file matches with any mail from get users request list, then update. If no match, then create new user. 
for i in range(len(data.axes[0])):
		if(data.iloc[i]["mailValue"] in EmailsFromRequest): #update user
			url = "https://"+tenantID+".accounts.ondemand.com/service/scim/Users/"+data.iloc[i]["id"]
			BodyCreator.BodyCreatorUpdate(data,i,url,token)
		else: #create user 
			url = "https://"+tenantID+".accounts.ondemand.com/service/scim/Users"			
			BodyCreator.BodyCreatorCreate(data,i,url,token)