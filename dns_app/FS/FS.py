from flask import Flask, request, Response
import requests
import json

app = Flask(__name__)


@app.route('/register')
def register():
    host_name = request.args.get('hostname')
    ip_address = '0.0.0.0'
    dict = {}
    dict['name'] = host_name
    dict['address'] = ip_address
    r = requests.post('http://0.0.0.0:53533', data = dict)
    return r.text

@app.route('/fabonacci')
def fabonacci():
    x = request.args.get('number')
    sum = Fibonacci(int(x))
    return Response("the fibonacci munber for "+str(x)+" is: "+str(sum), status = 200)
    
    
def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n < 0:
        return('Invalid input')
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
        
app.run(host='0.0.0.0',
        port=9090,
        debug=True)
