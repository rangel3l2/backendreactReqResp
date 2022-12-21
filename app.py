from flask import Flask,request, redirect
import base64
import datetime
from json import *


app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    # your processing here
    return {'route': request.url, 
            'detail':'not found, be sure its exist'}

@app.route('/')

def home():
    
    return '<h2>Olá mundo<h2/>'

@app.route('/message', methods = ['GET', 'POST'])
def messageHandler(listaFile = []):
    if request.method == 'GET':
        return '<h1>olá mundo<h1>'
    
        
    if request.method =='POST': 
        
            
            image_string = request.json  
                     
            
                
            listaFile.append(image_string)  
             
            #print(listaFile)       
            return {"data" : listaFile} 
        
        
if __name__ == "__main__" :    
   app.run(debug= True) 
#flask run --host= 0.0.0.0.
       
