# -*- coding: utf-8 -*-
"""

Created on Wed May  6 12:46:22 2020
@author: Mr ABBAS-TURKI

Modified on April 2021
@author: Mr Perronnet

"""

from flask import Flask,  render_template, redirect, session
from flask import request

import sys
import logging
from logging.config import dictConfig
import datetime
from database import DBAccess



# définir le message secret
SECRET_MESSAGE = "nouveauMdp" # A modifier


RESOURCES_DIR = "resources/"
CA_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "ca-private-key.pem"
CA_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "ca-public-key.pem"
SERVER_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "server-private-key.pem"
SERVER_CSR_FILENAME = RESOURCES_DIR + "server-csr.pem"
SERVER_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "server-public-key.pem"


app = Flask(__name__)


fileLogger = logging.getLogger('file')
fileHandler = logging.FileHandler("./logs/connexions.log")
fileLogger.addHandler(fileHandler)


app.secret_key = 'A_SECRET_KEY'



db = DBAccess()

@app.route("/")
def home():

    return redirect("/login")


@app.route("/secret")
def get_secret_message():
    if "isConnected" in session:
        if session["isConnected"] != True:
            return redirect("/login")
        ip_address = request.remote_addr
        fileLogger.warning(f'{ip_address} had access to secret at {datetime.datetime.now()} ')
        session.pop("isConnected",None)
    else :
         return redirect("/login")
    return SECRET_MESSAGE

@app.route("/login" , methods=("GET","POST"))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if db.sign_in(username,password) == 0:
            session['isConnected'] = True
            if username == "admin" :
                session['isAdmin'] = True
                return redirect("/addUser")
            return redirect("/secret")
        
    ip_address = request.remote_addr
    fileLogger.warning(f'{ip_address} had access to login at {datetime.datetime.now()} ')
    return render_template("index.html")
@app.route("/addUser" , methods=("GET","POST"))
def addUser():
    if "isAdmin" in session:
        if request.method == 'POST':
                username = request.form['username']
                password = request.form['password']
                db.sign_up(username,password)
    else : 
        return redirect("/login")
    return render_template("addUser.html")

@app.route("/logout" , methods=("GET","POST"))
def logout():
    session.pop("isAdmin",None)
    return redirect("/login")

if __name__ == "__main__":
    

    # HTTP version
    #app.run(debug=True, host="0.0.0.0", port=8081)
    # HTTPS version
    app.run(ssl_context=(SERVER_PUBLIC_KEY_FILENAME, SERVER_PRIVATE_KEY_FILENAME) , host="localhost" ,port=5000)
    
    
    