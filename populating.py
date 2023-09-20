import requests, os, subprocess, multiprocessing
from time import sleep

BASE_URL = 'http://127.0.0.1:8056/api/v1/'

user_create_url = os.path.join(BASE_URL, 'auth/users/')
jwt_create_url = os.path.join(BASE_URL, 'auth/jwt/create/')
natural_person_url = os.path.join(BASE_URL, 'natural-person/')
legal_person_url = os.path.join(BASE_URL, 'legal-person/')
address_url = os.path.join(BASE_URL, 'addresses/')
email_url = os.path.join(BASE_URL, 'emails/')
phone_url = os.path.join(BASE_URL, 'phones/')
account_url = os.path.join(BASE_URL, 'accounts/')


def data_base_creation():
	try: 
		subprocess.run(['py', 'manage.py', 'makemigrations'], check=True)
		subprocess.run(['py', 'manage.py', 'migrate'], check=True)
		print('Success')
	except subprocess.CalledProcessError as e:
		print(e)
	except Exception as e:
		print(e)	


def run_server():
	try:
		subprocess.run(['py', 'manage.py', 'runserver', '8056'], check=True)
	except subprocess.CalledProcessError as e:
		print(e)
	except Exception as e:
		print(e)	


def user_create(register_number, password, picture='a'):
	response = requests.post(user_create_url, 
		json={
			"register_number": register_number,
			"picture": picture,
			"password": password,
		})
	return response.json()
	

def create_headers(register_number, password):
	response = requests.post(jwt_create_url, 
		json={
			'register_number': register_number, 
			'password': password
		})
	access_token = response.json()['access']
	headers = {'Authorization': f'Bearer {access_token}'}
	return headers


def create_natural_person(headers, register_number, name, birth_date, rg, social_name):
	response = requests.post(natural_person_url, headers=headers,
		json={
			'user': register_number,
			'name': name,
			'birth_date': birth_date,
			'cpf': str(register_number),
			'rg': rg,
			'social_name': social_name
		})
	return response.json()


def create_legal_person(headers, register_number, fantasy_name, establishment_date, municipal_registration, state_registration, legal_nature):
	response = requests.post(legal_person_url, headers=headers,
		json={
			'user': register_number,
			'fantasy_name': fantasy_name,
			'establishment_date': establishment_date,
			'cnpj': str(register_number),
			'municipal_registration': municipal_registration,
			'state_registration': state_registration,
			'legal_nature': legal_nature
		})
	return response.json()


def create_address(headers, user, street, number, neighborhood, city, state, cep):
	response = requests.post(address_url, headers=headers, json={
		'user': user,
        'street': street,
        'number': number,
        'neighborhood': neighborhood,
        'city': city,
        'state': state,
        'cep': cep
	})
	return response.json()


def create_email(headers, user, email):
    response = requests.post(email_url, headers=headers, json={
        'user': user,
        'email': email
    })
    return response.json()


def create_phone(headers, user, area_code, prefix_number, phone_number):
    response = requests.post(phone_url, headers=headers, json={
        'user': user,
        'area_code': area_code,
        'prefix_number': prefix_number,
        'phone_number': phone_number
    })
    return response.json()


def create_account(headers, user, agency, number, type_a, balance, credit_limit, is_active=True):
    response = requests.post(account_url, headers=headers, json={
        'user': user,
        'agency': agency,
        'number': number,
        'type': type_a,
        'balance': balance,
        'credit_limit': credit_limit,
        'is_active': is_active
    })
    return response.json()


def main():
	#CREATING DATABSE
	data_base_creation()
	server_process = multiprocessing.Process(target=run_server)
	server_process.start()
	sleep(1)

	# NATURAL PERSON REGISTRASTION
	print(user_create(123456, "test@test"))
	headers = create_headers(123456, "test@test")
	print(headers)
	print(create_natural_person(headers, 123456, 'Luís', '2004-06-19', '222222', 'Beck'))
 
	print(user_create(1234567, "test@test"))
	headers = create_headers(1234567, "test@test")
	print(create_natural_person(headers, 1234567, 'Luís', '2004-06-19', '222222', 'Beck'))

	# LEGAL PERSON REGISTRASTION
	print(user_create(654321, "test@test"))
	headers = create_headers(654321, "test@test")
	print(create_legal_person(headers, 654321, 'Fantasy', '2023-06-19', '1234', '4321', 'Cars'))
 
	print(user_create(7654321, "test@test"))
	headers = create_headers(7654321, "test@test")
	print(create_legal_person(headers, 7654321, 'Fantasy', '2023-06-19', '1234', '4321', 'Cars'))
 
	# ADDRESS REGISTRASTION
	print(create_address(headers, 123456, 'Rua Jones', '69', 'LeWhite Green', 'Varsóvia', 'Polônia', '12564789'))
 
	# EMAIL REGISTRASTION
	print(create_email(headers, 123456, 'test@gmail.com'))
 
	# PHONE REGISTRASTION
	print(create_phone(headers, 123456, '+55', '11', '1111-1111'))
 
	# ACCOUNT REGISTRASTION
	print(create_account(headers, [123456], 1, 1, 'Current', 10000.00, 1000.00))
	print(create_account(headers, [7654321], 1, 2, 'Savings', 20175.00, 3268.56))	

	# server_process.join()

if __name__ == '__main__':
	main()