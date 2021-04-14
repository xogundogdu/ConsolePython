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

	sJson = {
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
			"attributes": {

			}
			
			}
		}
           

    # adding new values to body to update, according to csv input file columns 

	if "givenName" in data.columns:
	    	sJson["name"].update({"givenName": ""} if data.iloc[i]["givenName"] == "NONE" else {"givenName": data.iloc[i]["givenName"]})
	if "familyName" in data.columns:
	    	sJson["name"].update({"familyName": ""} if data.iloc[i]["familyName"] == "NONE" else {"familyName": data.iloc[i]["familyName"]})
	if "honorificPrefix" in data.columns:
	        sJson["name"].update({"honorificPrefix": ""} if data.iloc[i]["honorificPrefix"] == "NONE" else {"honorificPrefix": data.iloc[i]["honorificPrefix"]})
	if "middleName" in data.columns:
	    	sJson["name"].update({"middleName": ""} if data.iloc[i]["middleName"] == "NONE" else {"middleName": data.iloc[i]["middleName"]})
	if "locale" in data.columns:
	    	sJson.update({"locale": ""} if data.iloc[i]["locale"] == "NONE" else {"locale": data.iloc[i]["locale"]})
	if "displayName" in data.columns:
	    	sJson.update({"displayName": ""} if data.iloc[i]["displayName"] == "NONE" else {"displayName": data.iloc[i]["displayName"]})
	if "companyRelationship" in data.columns:
	    	sJson.update({"companyRelationship": ""} if data.iloc[i]["companyRelationship"] == "NONE" else {"companyRelationship": data.iloc[i]["companyRelationship"]})
	if "company" in data.columns:
	    	sJson.update({"company": ""} if data.iloc[i]["company"] == "NONE" else {"company": data.iloc[i]["company"]})
	if "department" in data.columns:
	    	sJson.update({"department": ""} if data.iloc[i]["department"] == "NONE" else {"department": data.iloc[i]["department"]})
	if "userType" in data.columns:
	    	sJson.update({"userType": ""} if data.iloc[i]["userType"] == "NONE" else {"userType": data.iloc[i]["userType"]})			
	if "status" in data.columns:
	    	sJson.update({"status": ""} if data.iloc[i]["status"] == "NONE" else {"status": str(data.iloc[i]["status"])})
	if "sendMail" in data.columns:
	    	sJson.update({"sendMail": ""} if data.iloc[i]["sendMail"] == "NONE" else {"sendMail": str(data.iloc[i]["sendMail"])})
	if "mailVerified" in data.columns:
	    	sJson.update({"mailVerified": ""} if data.iloc[i]["mailVerified"] == "NONE" else {"mailVerified": str(data.iloc[i]["mailVerified"])})
	if "employeeNumber" in data.columns:
	    	sJson["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"].update({"employeeNumber": data.iloc[i]["employeeNumber"]})
	if "costCenter" in data.columns:
	    	sJson["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"].update({"costCenter": data.iloc[i]["costCenter"]})
	if "organization" in data.columns:
	    	sJson["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"].update({"organization": data.iloc[i]["organization"]})
	if "division" in data.columns:
	    	sJson["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"].update({"division": data.iloc[i]["division"]})
	if "department" in data.columns:
	    	sJson["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"].update({"department": data.iloc[i]["department"]})
	if "managerValue" in data.columns:
			sJson["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"]["manager"][0].update({"value": data.iloc[i]["managerValue"]})
	if "managerRef" in data.columns:
			sJson["urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"]["manager"][0].update({"$ref": str(data.iloc[i]["managerRef"])})
	
	#custom attributes (max 10 fields can be utilized):
	if "CustomAttribute1name" in data.columns:
			sJson["urn:sap:cloud:scim:schemas:extension:custom:2.0:User"]["attributes"][0].update({"name": data.iloc[0]["CustomAttribute1name"]})
	if "CustomAttribute1value" in data.columns:
			sJson["urn:sap:cloud:scim:schemas:extension:custom:2.0:User"]["attributes"][0].update({"value": data.iloc[0]["CustomAttribute1value"]})
	if "CustomAttribute2name" in data.columns:
			sJson["urn:sap:cloud:scim:schemas:extension:custom:2.0:User"]["attributes"][1].update({"name": data.iloc[1]["CustomAttribute2name"]})
	if "CustomAttribute2value" in data.columns:
			sJson["urn:sap:cloud:scim:schemas:extension:custom:2.0:User"]["attributes"][1].update({"value": data.iloc[1]["CustomAttribute2value"]})
	if "CustomAttribute3name" in data.columns:
			sJson["urn:sap:cloud:scim:schemas:extension:custom:2.0:User"]["attributes"][2].update({"name": data.iloc[2]["CustomAttribute3name"]})
	if "CustomAttribute3value" in data.columns:
			sJson["urn:sap:cloud:scim:schemas:extension:custom:2.0:User"]["attributes"][2].update({"value": data.iloc[2]["CustomAttribute3value"]})
	if "CustomAttribute4name" in data.columns:
			sJson["urn:sap:cloud:scim:schemas:extension:custom:2.0:User"]["attributes"][3].update({"name": data.iloc[3]["CustomAttribute4name"]})
	if "CustomAttribute4value" in data.columns:
			sJson["urn:sap:cloud:scim:schemas:extension:custom:2.0:User"]["attributes"][3].update({"value": data.iloc[3]["CustomAttribute4value"]})
	if "CustomAttribute5name" in data.columns:
			sJson["urn:sap:cloud:scim:schemas:extension:custom:2.0:User"]["attributes"][4].update({"name": data.iloc[4]["CustomAttribute5name"]})
	if "CustomAttribute5value" in data.columns:
			sJson["urn:sap:cloud:scim:schemas:extension:custom:2.0:User"]["attributes"][4].update({"value": data.iloc[4]["CustomAttribute5value"]})
	if "CustomAttribute6name" in data.columns:
			sJson["urn:sap:cloud:scim:schemas:extension:custom:2.0:User"]["attributes"][5].update({"name": data.iloc[5]["CustomAttribute6name"]})
	if "CustomAttribute6value" in data.columns:
			sJson["urn:sap:cloud:scim:schemas:extension:custom:2.0:User"]["attributes"][5].update({"value": data.iloc[5]["CustomAttribute6value"]})
	if "CustomAttribute7name" in data.columns:
			sJson["urn:sap:cloud:scim:schemas:extension:custom:2.0:User"]["attributes"][6].update({"name": data.iloc[6]["CustomAttribute7name"]})
	if "CustomAttribute7value" in data.columns:
			sJson["urn:sap:cloud:scim:schemas:extension:custom:2.0:User"]["attributes"][6].update({"value": data.iloc[6]["CustomAttribute7value"]})
	if "CustomAttribute8name" in data.columns:
			sJson["urn:sap:cloud:scim:schemas:extension:custom:2.0:User"]["attributes"][7].update({"name": data.iloc[7]["CustomAttribute8name"]})
	if "CustomAttribute8value" in data.columns:
			sJson["urn:sap:cloud:scim:schemas:extension:custom:2.0:User"]["attributes"][7].update({"value": data.iloc[7]["CustomAttribute8value"]})
	if "CustomAttribute9name" in data.columns:
			sJson["urn:sap:cloud:scim:schemas:extension:custom:2.0:User"]["attributes"][8].update({"name": data.iloc[8]["CustomAttribute9name"]})
	if "CustomAttribute9value" in data.columns:
			sJson["urn:sap:cloud:scim:schemas:extension:custom:2.0:User"]["attributes"][8].update({"value": data.iloc[8]["CustomAttribute9value"]})
	if "CustomAttribute10name" in data.columns:
			sJson["urn:sap:cloud:scim:schemas:extension:custom:2.0:User"]["attributes"][9].update({"name": data.iloc[9]["CustomAttribute10name"]})
	if "CustomAttribute10value" in data.columns:
			sJson["urn:sap:cloud:scim:schemas:extension:custom:2.0:User"]["attributes"][9].update({"value": data.iloc[9]["CustomAttribute10value"]})


	# parse body object to json
	BodyForUpdate = json.dumps(sJson)

	print(BodyForUpdate)
	
	# send request for updating user
	response = requests.request("PUT", url, headers=headersForUpdate, data=BodyForUpdate)

	print(response.status_code)
	print(response.text)



# create json body for creating new user
def BodyCreatorCreate(data, i, url, token):
	headersForCreate = {
		"Content-Type": "application/scim+json",
		"Authorization": "Basic "+token,
	}
	BodyForCreate = json.dumps({
		"userName": str(data.iloc[i]["userName"]),
		"name": {
			"givenName": data.iloc[i]["givenName"],
			"familyName": data.iloc[i]["familyName"],
			"middleName": data.iloc[i]["middleName"],
			"honorificPrefix": data.iloc[i]["honorificPrefix"]
		},
		"emails": [
			{"value": data.iloc[i]["mailValue"]}
		],
		"locale": data.iloc[i]["locale"],
		"displayName": data.iloc[i]["displayName"],
		"companyRelationship": data.iloc[i]["companyRelationship"],
		"company": data.iloc[i]["company"],
		"department": data.iloc[i]["department"],
		"userType": data.iloc[i]["userType"],
		"active": True,
		"sendMail": str(data.iloc[i]["sendMail"]),
		"mailVerified": str(data.iloc[i]["mailVerified"]),
		"urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
			"employeeNumber": data.iloc[i]["employeeNumber"],
			"costCenter": data.iloc[i]["costCenter"],
			"organization": data.iloc[i]["organization"],
			"division": data.iloc[i]["division"],
			"department": data.iloc[i]["department"],
			"manager": {
				"value": data.iloc[i]["managerValue"],
				"$ref": str(data.iloc[i]["managerRef"])
			}
		},
		"urn:sap:cloud:scim:schemas:extension:custom:2.0:User": {
			"attributes": [
				{
					"name": ("" if data.iloc[0]["CustomAttribute1name"] == "NONE" else data.iloc[0]["CustomAttribute1name"]),
					"value":("" if data.iloc[0]["CustomAttribute1value"] == "NONE" else data.iloc[0]["CustomAttribute1value"])
				},
				{
					"name": ("" if data.iloc[0]["CustomAttribute2name"] == "NONE" else data.iloc[0]["CustomAttribute2name"]),
					"value":("" if data.iloc[0]["CustomAttribute2value"] == "NONE" else data.iloc[0]["CustomAttribute2value"])
				}
			]
		}
		})
	# send request for creating user
	response = requests.request("POST", url, headers=headersForCreate, data=BodyForCreate)

	print(response.status_code)
	print(response.text)
