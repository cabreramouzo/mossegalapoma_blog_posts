import requests
import json
import base64

#read credentials from file
cred_file = open("./credentials.txt", 'r')
user = cred_file.readline()
psw = cred_file.readline()
cred_file.close()

credentials = user + ':' + psw

token = base64.b64encode(credentials.encode())

url_srcdest = "http://localhost/wp-json/wp/v2/posts"

headers = {'Content-Type': 'application/json', 
         'Authorization': 'Basic ' + token.decode('utf-8')
         }
html_file = open("/Users/MAC/Library/Mobile Documents/com~apple~CloudDocs/Porno Mossegalapoma/programa_tipic_nomes_body.html",'r')
contents = html_file.read()
author_id_tomas = '1'
post = \
    {
        "title":"Testing via API via Python3",
        "content":contents,
        "status": "publish",
        "comment_status" : "open" ,
        "password" : "1234",

    }

response = requests.post(url_srcdest, json=post, headers=headers)

print(response)