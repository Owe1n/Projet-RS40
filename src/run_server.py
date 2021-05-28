# -*- coding: utf-8 -*-
"""

Created on Wed May  6 12:46:22 2020
@author: Mr ABBAS-TURKI

Modified on April 2021
@author: Mr Perronnet

"""

from flask import Flask
from flask import request
import sys
import logging
from logging.config import dictConfig
import datetime


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




# logging.basicConfig(filename='./logs/connexions.log',  level=logging.WARNING)


@app.route("/")
def get_secret_message():
    ip_address = request.remote_addr
    fileLogger.warning(f'{ip_address} was connected at {datetime.datetime.now()} ')
    
    return SECRET_MESSAGE


if __name__ == "__main__":


    # HTTP version
    #app.run(debug=True, host="0.0.0.0", port=8081)
    # HTTPS version
    app.run(ssl_context=(SERVER_PUBLIC_KEY_FILENAME, SERVER_PRIVATE_KEY_FILENAME) , host="localhost" ,port=5000)
    
    
    