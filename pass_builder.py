import hashlib

import os, base64

class PassBuilder:

	def get_hash(self, plain):
		return hashlib.sha512(plain).hexdigest()

	def salter(self):
		return base64.b64encode(os.urandom(20))

	def check_pass(self, plain, salt, expected):
		return self.get_hash(plain + salt) == expected

		

