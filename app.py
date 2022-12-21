from flask import Flask,request, redirect
from json import *


app = Flask(__name__)



@app.route('/')
def home():
    
    return '<h2>Olá mundo<h2/>'

@app.route('/message', methods = ['POST'])
def messageHandler(listaFile = []):   
    if request.method =='POST': 
        
            
            image_string = request.json  
                     
            
                
            listaFile.append(image_string)  
             
            #print(listaFile)       
            return {"data" : listaFile} 
        
        
if __name__ == "__main__" :    
   app.run(debug= True) 
#flask run --host= 0.0.0.0.
       
