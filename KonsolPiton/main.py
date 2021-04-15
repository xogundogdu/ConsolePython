import numpy
import pandas as pd
import requests
import numpy as np
import json

data = pd.read_csv("example.csv")

print(data)

url = "https://aik7cgkgf.accounts.ondemand.com/service/scim/Users"

for i in range(len(data.axes[0])):
    body = {"id": str(data.iloc[i]["id"]),
            "userName": str(data.iloc[i]["userName"]),
            "name": {
                "givenName": data.iloc[i]["givenName"],
                "familyName": data.iloc[i]["familyName"],
                "middleName": data.iloc[i]["middleName"],
                "honorificPrefix": data.iloc[i]["honorificPrefix"]
            },
            "emails": [
                {
                    "value": data.iloc[i]["mailValue"]
                }
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
                        "name": data.iloc[i]["CustomAttribute1name"],
                        "value": data.iloc[i]["CustomAttribute1value"]
                    },
                    {
                        "name": data.iloc[i]["CustomAttribute2name"],
                        "value": data.iloc[i]["CustomAttribute2value"]
                    }
                ]
            }}

body = {k: v for k, v in body.items() if numpy.isnan(v)}

print(body)

payload = json.dumps(body)
headers = {
    'Content-Type': 'application/scim+json',
    'Authorization': 'Basic YTE3MzkwOTItODcxMC00NjVhLWI1MjktMWIxMjA2MzRmMWM5OllpbGRpejIwMjA='
}

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)
