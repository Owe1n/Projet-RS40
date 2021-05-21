# -*- coding: utf-8 -*-
"""

Created on April 2021
@author: Mr Perronnet

"""

from solution.tools.core import Configuration, generate_private_key, generate_public_key, sign_csr


class CertificateAuthority:

    def __init__(self, config: Configuration, password: str, private_key_filename: str, public_key_filename: str):
        self._config = config
        self._private_key = # A compléter
        self._public_key = # A compléter
        self._private_key_filename = private_key_filename
        self._public_key_filename = public_key_filename
        self._password = password

    def sign(self, csr, certificate_filename: str):
        # A compléter
