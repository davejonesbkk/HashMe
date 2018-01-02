import hashlib

import argparse 

import sys





def pass_input(pass_choice, h):

	while len(pass_choice) <=7:
		pass_choice = raw_input('Enter your password. It must be at least 8 characters long: ')

	print('Your plain text password is ', pass_choice)

	h.update(pass_choice.encode('utf-8'))

	print('Your hashed password is ', h.digest())



	


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('hash_choice', choices=hashlib.algorithms_available, help='Which has would you like to use?')

	args = parser.parse_args()	

	h = hashlib.new(args.hash_choice)

	pass_choice = ''


	pass_input(pass_choice, h)

if __name__ == '__main__':
	main()
