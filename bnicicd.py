import requests

print ("hello world")
print ("Add new print : cicd")
print ("ok")

response = requests.get("https://www.google.com")

print (response.text)