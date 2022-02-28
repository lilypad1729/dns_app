from flask import Flask, request, Response
from time import gmtime, strftime
import json
import os
import requests

app = Flask(__name__)

    
@app.route('/', methods = ['GET', 'POST'])
def AS():


    file = 'address_map.json'
    if not os.path.exists(file):
        os.system(r'touch address_map.json')
        file = 'address_map.json'
    
    
    ## US ask ip address of a hostname
    if request.method == 'GET':
        key = request.args.get('name')
        with open(file, 'r') as json_file:
            data = json.load(json_file)
            address = data.get(key)
            return Response(address, status = 200)
            
    ## FS register information in AS
    else:
        data_get = request.form
        host_name = data_get['name']
        ip_address = data_get['address']
        dict = {}
        dict[host_name] = ip_address
        with open(file, 'w') as json_file:
            json.dump(dict, json_file)
        return Response("hostname is successfully registered", status = 200)


app.run(host='0.0.0.0',
        port=53533,
        debug=True)
