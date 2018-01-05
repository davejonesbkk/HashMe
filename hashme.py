import hashlib, argparse, uuid, os



from pass_builder import PasswordHelper

PH = PasswordHelper()


def pass_input(plain, h):


	while len(plain) <=7:
		plain = input('Enter your password. It must be at least 8 characters long: ')

	print('Your plain text password is ', plain)

	plain = h.digest()

	salt = PH.get_salt()

	hashed = plain+salt

	print('Plain is ',plain)
	print('The salt is ',salt)
	print('The hash ',hashed)


	validated = PH.validate_password(plain, salt, hashed)

	if validated == True:
		print('Validated')
	else:
		print('False')

	




def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('hash_choice', choices=hashlib.algorithms_available, help='Which has would you like to use?')

	args = parser.parse_args()	

	h = hashlib.new(args.hash_choice)

	plain = ''


	pass_input(plain, h)

if __name__ == '__main__':
	main()
