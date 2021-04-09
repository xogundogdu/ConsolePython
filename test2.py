import requests
import json

url = "https://aik7cgkgf.accounts.ondemand.com/service/scim/Users/P000000"

payload = json.dumps({
  "id": "P000000",
  "userName": "7890",
  "name": {
    "givenName": "mehmet",
    "familyName": "mehmet",
    "middleName": "mehmet",
    "honorificPrefix": "Mr."
  },
  "emails": [
    {
      "value": "bulgur@itelligence.com.tr"
    }
  ],
  "locale": "TR",
  "displayName": "Gokhan Yilmazturk NTT",
  "companyRelationship": "Partner",
  "company": "SFSF",
  "department": "Administration",
  "userType": "partner",
  "active": True,
  "sendMail": "true",
  "mailVerified": "false",
  "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
    "employeeNumber": "JohnS",
    "costCenter": "costCenter",
    "organization": "SFSF",
    "division": "Finance",
    "department": "Administration",
    "manager": {
      "value": "P000002",
      "$ref": "https://aik7cgkgf.accounts.ondemand.com/service/scim/Users/P000002"
    }
  },
  "urn:sap:cloud:scim:schemas:extension:custom:2.0:User": {
    "attributes": [
      {
        "name": "customAttribute1",
        "value": "Home Address2"
      },
      {
        "name": "customAttribute2",
        "value": "Telephone2"
      }
    ]
  }
})
headers = {
  'Content-Type': 'application/scim+json',
  'Authorization': 'Basic YTE3MzkwOTItODcxMC00NjVhLWI1MjktMWIxMjA2MzRmMWM5OllpbGRpejIwMjA='
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
