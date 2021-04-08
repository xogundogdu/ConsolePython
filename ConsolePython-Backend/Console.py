from types import BuiltinMethodType
import requests
import json
import csv
import pandas as pd
import numpy as np

EmailsFromCSV=[]
EmailsFromRequest=[]
UserIsExist=False

requestURL = "https://aik7cgkgf.accounts.ondemand.com/service/scim/Users" #get json file 
payload={}
headers1 = {
  'Content-Type': 'application/scim+json',
  'Authorization': 'Basic YTE3MzkwOTItODcxMC00NjVhLWI1MjktMWIxMjA2MzRmMWM5OllpbGRpejIwMjA='
}
response = requests.request("GET", requestURL, headers=headers1, data=payload)
       
CSVdata=json.loads(response.text) #parse response to json

for person in CSVdata["Resources"]: #get and print email property from json
  CSVEmail=person["emails"]
  CSVEmailValue=CSVEmail[0]
  EmailsFromRequest.append(CSVEmailValue["value"])
      
# with open('test.csv', 'r') as Data:
#     SR = csv.DictReader(Data, delimiter=',')
# 	df=pd.DataFrame(data=SR.data.)
# 	print(df)
   
data=pd.read_csv("test.csv")
print(data.head())


#print(*EmailsFromCSV,sep = "\n")
print("----------------------------------------------------------------------------")
#print(*EmailsFromRequest,sep = "\n")

for i in range(len(data.axes[0])):   #will be updated users
	for j  in range(len(data.axes[1])):
		if(data.iloc[i][j] in EmailsFromRequest):
			print("mail eşleşti")
			BodyForUpdate ={
			"userName": data.iloc[i]["loginName"],
			"name": {
				"givenName": data.iloc[i]["firstName"],
				"familyName": data.iloc[i]["familyName"],
				"middleName": data.iloc[i]["middleName"],
				"honorificPrefix": data.iloc[i]["honorificPrefix"]
			},
			"emails": [
				{
					"value": data.iloc[i]["mail"]
				}
			],
			"locale": data.iloc[i]["locale"],
			"displayName": data.iloc[i]["displayName"],
			"companyRelationship": data.iloc[i]["companyRelationship"],
			"company": data.iloc[i]["company"],
			"department": data.iloc[i]["department"],
			"userType": data.iloc[i]["userType"],
			"active": data.iloc[i]["status"],
			"sendMail": data.iloc[i]["sendMail"],
			"mailVerified": data.iloc[i]["mailVerified"],
			"urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
				"employeeNumber": data.iloc[i]["employeeNumber"],
				"costCenter": data.iloc[i]["costCenter"],
				"organization": data.iloc[i]["organization"],
				"division": data.iloc[i]["division"],
				"department": data.iloc[i]["department"],
				"manager": {
					"value": data.iloc[i]["managerValue"],
					"$ref": data.iloc[i]["managerRef"]
				}
			},
			"urn:sap:cloud:scim:schemas:extension:custom:2.0:User": {
				"attributes": [
					{
						"name": "customAttribute01",
						"value": data.iloc[i]["spCustomAttribute01"]
					},
					{
						"name": "customAttribute02",
						"value": data.iloc[i]["spCustomAttribute02"]
					}
				]
			}
			}		

			
			requestURLForUpdate = "https://aik7cgkgf.accounts.ondemand.com/service/scim/Users" 
			payloadForUpdate={}
			headersForUpdate = {
  			'Content-Type': 'application/scim+json',
  			'Authorization': 'Basic YTE3MzkwOTItODcxMC00NjVhLWI1MjktMWIxMjA2MzRmMWM5OllpbGRpejIwMjA='
			}
			responseForUpdate = requests.request("POST", requestURLForUpdate, headers=headersForUpdate, data=BodyForUpdate)

			
			print(responseForUpdate.status_code)

			data.drop(data.index[i])
			
			print(data)

			

		


	
			
	