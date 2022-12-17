# flast is folder Flask is function

from flask import Flask 
import json

app = Flask("server")

@app.get("/")
def home():
   return "hello from flask"

@app.get("/test")
def test():
   return "This is another endpoint in new folder called 'test'."

@app.get("/about")
def about():
   return "About me: Kenneth Chung"

#############  catalogue API ##########
@app.get("/api/version")
def version():
   version = {
      "V":"V.1.0.1.",
      "name":"Candy Firewall",
   }
   return json.dumps(version)




app.run(debug=True)