import json
import requests
import pandas as pd



# create json body for updating user
# initial body only includes required values
def BodyCreatorUpdate(data, i, url, token):  	

	# set authorization settings
	headersForUpdate = {
		"Content-Type": "application/scim+json",
		"Authorization": "Basic "+token,
		}

	bodyForUpdate = {
		"id": str(data.iloc[i]["id"]),
		"userName": str(data.iloc[i]["userName"]),
		"name": {				
		},
		"emails": [
			{
				"value": data.iloc[i]["mailValue"]
			}
		],
		"urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {	
			"manager": {
			}	

		},
		"urn:sap:cloud:scim:schemas:extension:custom:2.0:User": {
			"attributes": [
				{
					"name" : "customAttribute1",
					"value": ("" if data.iloc[i]["customAttribute1"] == "NONE" else data.iloc[i]["customAttribute1"])
				},
				
				{
					"name" : "customAttribute2",
					"value": ("" if data.iloc[i]["customAttribute2"] == "NONE" else data.iloc[i]["customAttribute2"])
				},
				
				{
					"name" : "customAttribute3",
					"value": ("" if data.iloc[i]["customAttribute3"] == "NONE" else data.iloc[i]["customAttribute3"])
				},
				
				{
					"name" : "customAttribute4",
					"value": ("" if data.iloc[i]["customAttribute4"] == "NONE" else data.iloc[i]["customAttribute4"])
				},
				
				{
					"name" : "customAttribute5",
					"value": ("" if data.iloc[i]["customAttribute5"] == "NONE" else data.iloc[i]["customAttribute5"])
				}

			]
			
			}
		}
           

    # adding new values to body to update, according to csv input file columns 

	if "givenName" in data.columns:
	    	bodyForUpdate["name"].update({"givenName": ""} if data.iloc[i]["givenName"] == "NONE" else {"givenName": data.iloc[i]["givenName"]})
	if "familyName" in data.columns:
	    	bodyForUpdate["name"].update({"familyName": ""} if data.iloc[i]["familyName"] == "NONE" else {"familyName": data.iloc[i]["familyName"]})
	if "honorificPrefix" in data.columns:
	        bodyForUpdate["name"].update({"honorificPrefix": ""} if data.iloc[i]["honorificPrefix"] == "NONE" else {"honorificPrefix": data.iloc[i]["honorificPrefix"]})
	if "middleName" in data.columns:
	    	bodyForUpdate["name"].update({"middleName": ""} if data.iloc[i]["middleName"] == "NONE" else {"middleName": data.iloc[i]["middleName"]})
	if "locale" in data.columns:
	    	bodyForUpdate.update({"locale": ""} if data.iloc[i]["locale"] == "NONE" else {"locale": data.iloc[i]["locale"]})
	if "displayName" in data.columns:
	    	bodyForUpdate.update({"displayName": ""} if data.iloc[i]["displayName"] == "NONE" else {"displayName": data.iloc[i]["displayName"]})
	if "companyRelationship" in data.columns:
	    	bodyForUpdate.update({"companyRelationship": ""} if data.iloc[i]["companyRelationship"] == "NONE" else {"companyRelationship": data.iloc[i]["companyRelationship"]})
	if "company" in data.columns:
	    	bodyForUpdate.update({"company": ""} if data.iloc[i]["company"] == "NONE" else {"company": data.iloc[i]["company"]})
	if "department" in data.columns:
	    	bodyForUpdate.update({"department": ""} if data.iloc[i]["department"] == "NONE" else {"department": data.iloc[i]["department"]})
	if "userType" in data.columns:
	    	bodyForUpdate.update({"userType": ""} if data.iloc[i]["userType"] == "NONE" else {"userType": data.iloc[i]["userType"]})			
	if "status" in data.columns:
	    	bodyForUpdate.update({"status": ""} if data.iloc[i]["status"] == "NONE" else {"status": str(data.iloc[i]["status"])})
	if "sendMail" in data.columns:
	    	bodyForUpdate.update({"sendMail": ""} if data.iloc[i]["sendMail"] == "NONE" else {"sendMail": str(data.iloc[i]["sendMail"])})
	if "mailVerified" in data.columns:
	    	bodyForUpdate.update({"mailVerified": ""} if data.iloc[i]["mailVerified"] == "NONE" else {"mailVerified": str(data.iloc[i]["mailVerified"])})
	if "employeeNumber" in data.columns:
	    	bodyForUpdate["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"].update({"employeeNumber": data.iloc[i]["employeeNumber"]})
	if "costCenter" in data.columns:
	    	bodyForUpdate["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"].update({"costCenter": data.iloc[i]["costCenter"]})
	if "organization" in data.columns:
	    	bodyForUpdate["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"].update({"organization": data.iloc[i]["organization"]})
	if "division" in data.columns:
	    	bodyForUpdate["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"].update({"division": data.iloc[i]["division"]})
	if "department" in data.columns:
	    	bodyForUpdate["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"].update({"department": data.iloc[i]["department"]})
	if "managerValue" in data.columns:
			bodyForUpdate["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"]["manager"].update({"value": data.iloc[i]["managerValue"]})
	if "managerRef" in data.columns:
			bodyForUpdate["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"]["manager"].update({"$ref": str(data.iloc[i]["managerRef"])})
	
	

	# parse body object to json
	BodyForUpdate = json.dumps(bodyForUpdate)

	print(BodyForUpdate)
	
	# send request for updating user
	response = requests.request("PUT", url, headers=headersForUpdate, data=BodyForUpdate)
	if(response.status_code==200):
    		print(data.iloc[i]["mailValue"]+"mailine sahip kullanici guncellendi")
	elif(response.status_code==409):
    		print(data.iloc[i]["mailValue"]+"icin csv dosyasindaki bilgilerin tutarliligini kontrol ediniz")



# create json body for creating new user
# initial body only includes required values
def BodyCreatorCreate(data, i, url, token):

	# set authorization settings
	headersForCreate = {
		"Content-Type": "application/scim+json",
		"Authorization": "Basic "+token,
	}

	bodyForCreate = {
		"userName": str(data.iloc[i]["userName"]),
		"name": {				
		},
		"emails": [
			{
				"value": data.iloc[i]["mailValue"]
			}
		],
		"urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {	
			"manager": {
			}	

		},
		"urn:sap:cloud:scim:schemas:extension:custom:2.0:User": {
			"attributes": [
				{
					"name" : "customAttribute1",
					"value": ("" if data.iloc[i]["customAttribute1"] == "NONE" else data.iloc[i]["customAttribute1"])
				},
				
				{
					"name" : "customAttribute2",
					"value": ("" if data.iloc[i]["customAttribute2"] == "NONE" else data.iloc[i]["customAttribute2"])
				},
				
				{
					"name" : "customAttribute3",
					"value": ("" if data.iloc[i]["customAttribute3"] == "NONE" else data.iloc[i]["customAttribute3"])
				},
				
				{
					"name" : "customAttribute4",
					"value": ("" if data.iloc[i]["customAttribute4"] == "NONE" else data.iloc[i]["customAttribute4"])
				},
				
				{
					"name" : "customAttribute5",
					"value": ("" if data.iloc[i]["customAttribute5"] == "NONE" else data.iloc[i]["customAttribute5"])
				}

			]
			
			}
		}

	# adding new values to body to update, according to csv input file columns
	if "givenName" in data.columns:
	    	bodyForCreate["name"].update({"givenName": ""} if data.iloc[i]["givenName"] == "NONE" else {"givenName": data.iloc[i]["givenName"]})
	if "familyName" in data.columns:
	    	bodyForCreate["name"].update({"familyName": ""} if data.iloc[i]["familyName"] == "NONE" else {"familyName": data.iloc[i]["familyName"]})
	if "honorificPrefix" in data.columns:
	        bodyForCreate["name"].update({"honorificPrefix": ""} if data.iloc[i]["honorificPrefix"] == "NONE" else {"honorificPrefix": data.iloc[i]["honorificPrefix"]})
	if "middleName" in data.columns:
	    	bodyForCreate["name"].update({"middleName": ""} if data.iloc[i]["middleName"] == "NONE" else {"middleName": data.iloc[i]["middleName"]})
	if "locale" in data.columns:
	    	bodyForCreate.update({"locale": ""} if data.iloc[i]["locale"] == "NONE" else {"locale": data.iloc[i]["locale"]})
	if "displayName" in data.columns:
	    	bodyForCreate.update({"displayName": ""} if data.iloc[i]["displayName"] == "NONE" else {"displayName": data.iloc[i]["displayName"]})
	if "companyRelationship" in data.columns:
	    	bodyForCreate.update({"companyRelationship": ""} if data.iloc[i]["companyRelationship"] == "NONE" else {"companyRelationship": data.iloc[i]["companyRelationship"]})
	if "company" in data.columns:
	    	bodyForCreate.update({"company": ""} if data.iloc[i]["company"] == "NONE" else {"company": data.iloc[i]["company"]})
	if "department" in data.columns:
	    	bodyForCreate.update({"department": ""} if data.iloc[i]["department"] == "NONE" else {"department": data.iloc[i]["department"]})
	if "userType" in data.columns:
	    	bodyForCreate.update({"userType": ""} if data.iloc[i]["userType"] == "NONE" else {"userType": data.iloc[i]["userType"]})			
	if "status" in data.columns:
	    	bodyForCreate.update({"status": ""} if data.iloc[i]["status"] == "NONE" else {"status": str(data.iloc[i]["status"])})
	if "sendMail" in data.columns:
	    	bodyForCreate.update({"sendMail": ""} if data.iloc[i]["sendMail"] == "NONE" else {"sendMail": str(data.iloc[i]["sendMail"])})
	if "mailVerified" in data.columns:
	    	bodyForCreate.update({"mailVerified": ""} if data.iloc[i]["mailVerified"] == "NONE" else {"mailVerified": str(data.iloc[i]["mailVerified"])})
	if "employeeNumber" in data.columns:
	    	bodyForCreate["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"].update({"employeeNumber": data.iloc[i]["employeeNumber"]})
	if "costCenter" in data.columns:
	    	bodyForCreate["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"].update({"costCenter": data.iloc[i]["costCenter"]})
	if "organization" in data.columns:
	    	bodyForCreate["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"].update({"organization": data.iloc[i]["organization"]})
	if "division" in data.columns:
	    	bodyForCreate["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"].update({"division": data.iloc[i]["division"]})
	if "department" in data.columns:
	    	bodyForCreate["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"].update({"department": data.iloc[i]["department"]})
	if "managerValue" in data.columns:
			bodyForCreate["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"]["manager"].update({"value": data.iloc[i]["managerValue"]})
	if "managerRef" in data.columns:
			bodyForCreate["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"]["manager"].update({"$ref": str(data.iloc[i]["managerRef"])})
	

	# parse body object to json
	BodyForCreate = json.dumps(bodyForCreate)
	
	# send request for creating user
	response = requests.request("POST", url, headers=headersForCreate, data=BodyForCreate)
	if(response.status_code==201):
		print(data.iloc[i]["mailValue"]+" mailine sahip kullanici olusturuldu")
	elif(response.status_code==409):
		print(data.iloc[i]["mailValue"]+" mailline sahip kullanici sistemde mevcut")