import requests
from datetime import datetime

print ("hello world")
print ("Add new print : cicd")
print ("ok")

response = requests.get("https://www.google.com")

waktu = datetime.now()

with open("tempResponse/"+str(waktu)+".txt","w") as f:
    f.write(response.text)
