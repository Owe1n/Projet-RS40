# -*- coding: utf-8 -*-
"""

Created on Wed May  6 12:46:22 2020
@author: Mr ABBAS-TURKI

Modified on April 2021
@author: Mr Perronnet

"""

from flask import Flask

# définir le message secret
SECRET_MESSAGE = "nouveauMdp" # A modifier
app = Flask(__name__)


@app.route("/")
def get_secret_message():
    return SECRET_MESSAGE


if __name__ == "__main__":
    # HTTP version
    app.run(debug=True, host="0.0.0.0", port=8081)
    # HTTPS version
    # A compléter