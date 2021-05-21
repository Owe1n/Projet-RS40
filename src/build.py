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
CA_PASSWORD = "UnSuperMDPdeCa"
SERVER_PASSWORD = "UnSuperMDPdeServer"

CA_CONFIGURATION = Configuration("PE","Ancash","Chimbote","Gaggle","www.gaggle.com")
SERVER_CONFIGURATION = Configuration("FR","France","Paris","UtMb","www.utmb.com",["127.0.0.1"])

# Création de l'autorité de certification
certificate_authority = CertificateAuthority(CA_CONFIGURATION,CA_PASSWORD,CA_PRIVATE_KEY_FILENAME,CA_PUBLIC_KEY_FILENAME)

# Création du server
server = Server(SERVER_CONFIGURATION,SERVER_PASSWORD,SERVER_PRIVATE_KEY_FILENAME,SERVER_CSR_FILENAME)

# Signature du certificat par l'autorité de certification
signed_certificate = certificate_authority.sign(server.get_csr(),SERVER_PUBLIC_KEY_FILENAME)

print("finished ...")
