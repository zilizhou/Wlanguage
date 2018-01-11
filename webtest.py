# -*- coding:utf-8 -*-
from flask import Flask
from flask import request
import  json
app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Hello World!</h1>'
@app.route('/test',methods=['GET', 'POST'])
def test():
    if request.method =='POST':
        return (request.form['para'])
    else:
        return ('ok')
@app.route('/reccodes',methods=['GET', 'POST'])
def reccodes():
    if request.method =='POST':
        return (request.form['codes'])
    else:
        return (request.form['codes'])


@app.route('/doubleClickNode')
def doubleClickNode():
    # print(request.args['data'])
    return "successCallback" + "(" + json.dumps(request.args)+ ")"
@app.route('/dataFront')
def dataFront():
    ontodata={'nodes':[{'id': 0, 'label': "node0",'color':'red'},
{'id': 1,'label': "node1"},

{'id': 2,'label': "node2"},

{'id': 3,'label': "node3"},

{'id': 4,'label': "node4"},

{'id': 5,'label': "node5"},

{'id': 6,'label': "node6"},

{'id': 7,'label': "node7"},

{'id': 8,'label': "node8"},

{'id': 9,'label': "node9"}],'edges':[{'from': 1, 'to': 0, 'id': "a16f4906-1275-418f-a1f3-c23dff88b164"},

{'from': 2, 'to': 0, 'label': "2af0", 'id': "018ef3fb-dff2-4f08-806c-cbdcb126b348"},

{'from': 3, 'to': 1, 'label': "3af1", 'id': "c3cf6e34-1bb5-4dce-9b37-619001c38261"},

{'from': 4, 'to': 2, 'label': "4af2", 'id': "da9003d6-c873-4129-aba9-e97d2324a7fa"},

{'from': 5, 'to': 1, 'label': "5af1", 'id': "1fd292c0-6973-41f9-b426-8e2bdf5177f5"},

{'from': 6, 'to': 5, 'label': "6af5", 'id': "7cb9a101-5d7b-4eb9-ba1a-fbff2eda4e39"},

{'from': 7, 'to': 5, 'label': "7af5", 'id': "02c14b68-0fdd-45bb-b05b-1334ee468e1e"},

{'from': 8, 'to': 3, 'label': "8af3", 'id': "bcdbe71c-59de-4443-8c4c-5644056f40db"},

{'from': 9, 'to': 5, 'label': "9af5", 'id': "2d2a09a0-3d6c-4ea8-ba91-b328e7e93022"}]}

    return "successCallback" + "(" + json.dumps(ontodata) + ")"


if __name__ == '__main__':
    app.run( host = '0.0.0.0',  port = 5000,   debug = True)