from types import BuiltinMethodType
import requests
import json
import csv
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
      
with open('test.csv', 'r') as Data:
    SR = csv.DictReader(Data, delimiter=',')
    print(SR.line_num)
    print(SR.fieldnames)
    print(SR.dialect)
    print(SR.reader)
    print(SR.restkey)
    print(SR.restval)
    for row in SR:
        print (row['mail'])


print(*EmailsFromCSV,sep = "\n")
print("----------------------------------------------------------------------------")
print(*EmailsFromRequest,sep = "\n")

for mail in EmailsFromCSV:
  if(mail in EmailsFromRequest):
    print(mail+" Email eşleşti")
    print(mail+"'e sahip kullanıcıyı güncelle")
  else:
    print(mail+" böyle bir kullanıcı yok")
    print("csvden kullanıcı oluştur request")

body ={
	"userName": "123123",
	"name": {
		"givenName": "Gokhan",
		"familyName": "Yilmazturk",
		"middleName": "Ahmet",
		"honorificPrefix": "Mr."
	},
	"emails": [
		{
			"value": "gokhan.yilmazturk@nttdata.com"
		}
	],
	"locale": "TR",
	"displayName": "Gokhan Yilmazturk NTT",
	"companyRelationship": "Partner",
	"company": "SFSF",
	"department": "Administration",
	"userType": "partner",
	"active": "true",
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
}