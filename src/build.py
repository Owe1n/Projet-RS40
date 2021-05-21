# -*- coding: utf-8 -*-
"""

Created on April 2021
@author: Mr Perronnet

"""

from tools.core import Configuration
from ca.core import CertificateAuthority
from server.core import Server

RESOURCES_DIR = "resources/"
CA_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "ca-private-key.pem"
CA_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "ca-public-key.pem"
SERVER_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "server-private-key.pem"
SERVER_CSR_FILENAME = RESOURCES_DIR + "server-csr.pem"
SERVER_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "server-public-key.pem"
CA_PASSWORD = # A compléter
SERVER_PASSWORD = # A compléter

CA_CONFIGURATION = Configuration( # A compléter
SERVER_CONFIGURATION = Configuration( # A compléter

# Création de l'autorité de certification
certificate_authority = CertificateAuthority(
    # A compléter
)

# Création du server
server = Server(
    # A compléter
)

# Signature du certificat par l'autorité de certification
signed_certificate = # A compléter

print("finished ...")
