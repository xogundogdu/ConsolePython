import json
import requests
def BodyCreatorUpdate(data,i,tenantID,url,token):
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
    headersForUpdate = {
"Content-Type": "application/scim+json",
"Authorization": "Basic "+token,
}			
    requests.request("PUT",url,headers=headersForUpdate,data=BodyForUpdate)				

def BodyCreatorCreate(data,i,tenantID,url,token):
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
    url = "https://"+tenantID+".accounts.ondemand.com/service/scim/Users" 
    headersForCreate = {
"Content-Type": "application/scim+json",
"Authorization": "Basic "+token,
}			
    requests.request("POST",url, headers=headersForCreate, data=BodyForCreate)			
