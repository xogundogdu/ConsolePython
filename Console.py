from json.decoder import JSONDecoder
from types import BuiltinMethodType
from numpy.core.numeric import True_
import requests
import json
import pandas as pd
from lowercase_booleans import true, false
from requests.api import put

EmailsFromCSV=[]
EmailsFromRequest=[]
UserIsExist=False

requestURL = "https://aik7cgkgf.accounts.ondemand.com/service/scim/Users" #get json file 
payload={}
headers1 = {
  "Content-Type": "application/scim+json",
  "Authorization": "Basic YTE3MzkwOTItODcxMC00NjVhLWI1MjktMWIxMjA2MzRmMWM5OllpbGRpejIwMjA="
}
response = requests.request("GET", requestURL, headers=headers1, data=payload)
       
CSVdata=json.loads(response.text) #parse response to json

for person in CSVdata["Resources"]: #get and print email property from json
  CSVEmail=person["emails"]
  CSVEmailValue=CSVEmail[0]
  EmailsFromRequest.append(CSVEmailValue["value"])
       
data=pd.read_csv("test1.csv")
print(data)
print(data.iloc[0]["mailValue"]+"+++++++++++")

print("----------------------------------------------------------------------------")
for i in range(len(data.axes[0])):
	#for j  in range(len(data.axes[1])):
		if(data.iloc[i]["mailValue"] in EmailsFromRequest): #update user
			print("mail eslesti ve guncelleme baslatildi")			
			BodyForUpdate =json.dumps({
			"id":str(data.iloc[i]["id"]),
			"userName":str(data.iloc[i]["userName"]),
			"name": {
				"givenName":data.iloc[i]["givenName"],
				"familyName":data.iloc[i]["familyName"],
				"middleName":data.iloc[i]["middleName"],
				"honorificPrefix":data.iloc[i]["honorificPrefix"]
			},
			"emails": [
				{
					"value":data.iloc[i]["mailValue"]
				}
			],
			"locale":data.iloc[i]["locale"],
			"displayName":data.iloc[i]["displayName"],
			"companyRelationship":data.iloc[i]["companyRelationship"],
			"company":data.iloc[i]["company"],
			"department":data.iloc[i]["department"],
			"userType":data.iloc[i]["userType"],
			"active": True,
			"sendMail": str(data.iloc[i]["sendMail"]),
			"mailVerified": str(data.iloc[i]["mailVerified"]),
			"urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
				"employeeNumber":data.iloc[i]["employeeNumber"],
				"costCenter":data.iloc[i]["costCenter"],
				"organization":data.iloc[i]["organization"],
				"division":data.iloc[i]["division"],
				"department":data.iloc[i]["department"],
				"manager": {
					"value":data.iloc[i]["managerValue"],
					"$ref":str(data.iloc[i]["managerRef"])
				}
			},
			"urn:sap:cloud:scim:schemas:extension:custom:2.0:User": {
				"attributes": [
					{
						"name":data.iloc[i]["CustomAttribute1name"],
						"value":data.iloc[i]["CustomAttribute1value"]
					},
					{
						"name":data.iloc[i]["CustomAttribute2name"],
						"value":data.iloc[i]["CustomAttribute2value"]
					}
				]
			}
			})
			requestURLForUpdate = "https://aik7cgkgf.accounts.ondemand.com/service/scim/Users/"+data.iloc[i]["id"]
			headersForUpdate = {
  			"Content-Type": "application/scim+json",
  			"Authorization": "Basic YTE3MzkwOTItODcxMC00NjVhLWI1MjktMWIxMjA2MzRmMWM5OllpbGRpejIwMjA=",
			}			
			#responseForUpdate = requests.put(requestURLForUpdate, headers=headersForUpdate, data=BodyForUpdate)	
			responseForUpdate= requests.request("PUT",requestURLForUpdate,headers=headersForUpdate,data=BodyForUpdate)				
			print(type(BodyForUpdate))
			print(BodyForUpdate)			
			print(responseForUpdate.status_code)
			print("----------------------------------------------------------------------------")
		else:#create user 			
			BodyForCreate =json.dumps({
			"userName":str(data.iloc[i]["userName"]),
			"name": {
				"givenName":data.iloc[i]["givenName"],
				"familyName":data.iloc[i]["familyName"],
				"middleName":data.iloc[i]["middleName"],
				"honorificPrefix":data.iloc[i]["honorificPrefix"]
			},
			"emails": [
				{
					"value":data.iloc[i]["mailValue"]
				}
			],
			"locale":data.iloc[i]["locale"],
			"displayName":data.iloc[i]["displayName"],
			"companyRelationship":data.iloc[i]["companyRelationship"],
			"company":data.iloc[i]["company"],
			"department":data.iloc[i]["department"],
			"userType":data.iloc[i]["userType"],
			"active": True,
			"sendMail": str(data.iloc[i]["sendMail"]),
			"mailVerified": str(data.iloc[i]["mailVerified"]),
			"urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
				"employeeNumber":data.iloc[i]["employeeNumber"],
				"costCenter":data.iloc[i]["costCenter"],
				"organization":data.iloc[i]["organization"],
				"division":data.iloc[i]["division"],
				"department":data.iloc[i]["department"],
				"manager": {
					"value":data.iloc[i]["managerValue"],
					"$ref":str(data.iloc[i]["managerRef"])
				}
			},
			"urn:sap:cloud:scim:schemas:extension:custom:2.0:User": {
				"attributes": [
					{
						"name":data.iloc[i]["CustomAttribute1name"],
						"value":data.iloc[i]["CustomAttribute1value"]
					},
					{
						"name":data.iloc[i]["CustomAttribute2name"],
						"value":data.iloc[i]["CustomAttribute2value"]
					}
				]
			}
			})
			requestURLForCreate = "https://aik7cgkgf.accounts.ondemand.com/service/scim/Users" 
			headersForCreate = {
  			"Content-Type": "application/scim+json",
  			"Authorization": "Basic YTE3MzkwOTItODcxMC00NjVhLWI1MjktMWIxMjA2MzRmMWM5OllpbGRpejIwMjA=",
			}			
			responseForCreate = requests.request("POST",requestURLForCreate, headers=headersForCreate, data=BodyForCreate)			
			print(BodyForCreate)
			print(responseForCreate.status_code)
			print("----------------------------------------------------------------------------")