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


token = b64encode(bytes((f"{userName}:{password}"), encoding="utf-8")).decode("ascii")

requestURL = "https://{0}.accounts.ondemand.com/service/scim/Users".format(tenantID) #get json file 
payload	= {}
headers = {
  "Content-Type": "application/scim+json",
  "Authorization": "Basic "+token
}
response = requests.request("GET", requestURL, headers=headers, data=payload)
       
CSVdata = json.loads(response.text) #parse response to json


for person in CSVdata["Resources"]: #get email property from json
  CSVEmail = person["emails"]
  CSVEmailValue = CSVEmail[0]
  EmailsFromRequest.append(CSVEmailValue["value"])
       
data = pd.read_csv("example.csv").fillna("NONE")

for i in range(len(data.axes[0])):
		if(data.iloc[i]["mailValue"] in EmailsFromRequest): #update user
			url = "https://"+tenantID+".accounts.ondemand.com/service/scim/Users/"+data.iloc[i]["id"]
			BodyCreator.BodyCreatorUpdate(data,i,url,token)
		else:#create user 
			url = "https://"+tenantID+".accounts.ondemand.com/service/scim/Users"			
			BodyCreator.BodyCreatorCreate(data,i,url,token)