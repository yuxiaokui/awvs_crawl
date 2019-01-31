from wvs import wvs

from flask_cors import CORS
from flask import Flask,request
app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/scan", methods=['GET','POST'])
def scan():
    if request.method == 'POST':
        a = wvs(request.form['website'])
        a.scan()
        return 'Scanning...'
    else:
        return 'Please use the POST!'

@app.route("/view",methods=['GET'])
def view():
    a = wvs('test')
    filename = a.view()
    return str(filename)

@app.route("/del",methods=['GET','POST'])
def delete():
    a = wvs('test')
    filepath = a.delete(request.form['filename'])
    return 'OK'

@app.route("/listurl",methods=['GET','POST'])
def listurl():
    a = wvs('test')
    result = a.listurl(request.form['filename'])
    return str(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
