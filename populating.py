import requests, os, subprocess, multiprocessing
from time import sleep

BASE_URL = 'http://10.109.71.6:8056/api/v1/'

user_create_url = os.path.join(BASE_URL, 'auth/users/')
jwt_create_url = os.path.join(BASE_URL, 'auth/jwt/create/')
natural_person_url = os.path.join(BASE_URL, 'natural-people/')
legal_person_url = os.path.join(BASE_URL, 'legal-people/')
address_url = os.path.join(BASE_URL, 'addresses/')
email_url = os.path.join(BASE_URL, 'emails/')
phone_url = os.path.join(BASE_URL, 'phones/')
account_url = os.path.join(BASE_URL, 'accounts/')
investment_url = os.path.join(BASE_URL, 'investments/')
account_investment_url = os.path.join(BASE_URL, 'investments/account/new/')
card_new_url = os.path.join(BASE_URL, 'cards/')
create_loan_url = os.path.join(BASE_URL, 'loans/')
card_transaction_url = os.path.join(BASE_URL, 'card-transactions/')
pix_url = os.path.join(BASE_URL, 'pix/')


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
		subprocess.run(['py', 'manage.py', 'runserver', '10.109.71.6:8056'], check=True)
	except subprocess.CalledProcessError as e:
		print(e)
	except Exception as e:
		print(e)


def superuser_creation():
	try:
		subprocess.run(['py', 'manage.py', 'create_superuser'], check=True)
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


def create_account(headers, type):
    response = requests.post(account_url, headers=headers, json={
        'type': type
    })
    return response.json()


def create_investment(headers, type, contribution, admin_fee, period, risc_rate, profitability, is_active=True):
	response = requests.post(investment_url, headers=headers, json={
		'type':type,
		'contribution':contribution,
		'admin_fee': admin_fee,
		'period': period, 
		'risc_rate': risc_rate,
		'profitability': profitability,
		'is_active': is_active
	})
	return response.json()


def create_account_investment(headers, id_account, id_investment):
	response = requests.post(account_investment_url, headers=headers, json={
		'id_account':id_account,
		'id_investment':id_investment
	})
	return response.json()


def create_loan(headers, id_account, amount, installment_amount, observation):
	response = requests.post(create_loan_url, headers=headers, json={
		'id_account': id_account,
		'amount_request': amount,
		'installment_amount': installment_amount,
		'observation': observation
	})
	return response.json()


def create_card(headers, id_account):
	response = requests.post(card_new_url, headers=headers, json={
		'id_account': id_account
	})
	return response.json()


def create_card_transaction(headers, id_account, id_card, operation, amount):
	response = requests.post(card_transaction_url, headers=headers, json={
		'id_account': id_account,
		'id_card': id_card,
		'operation': operation,
		'amount': amount
	})
	return response.json()


def create_pix(headers, payer_account, receiver_account, amount):
	response = requests.post(pix_url, headers=headers, json={
		'id_account': payer_account,
		'id_receiver_account': receiver_account,
		'amount': amount
	})
	return response.json()


def main():
	#CREATING DATABSE
	data_base_creation()
	server_process = multiprocessing.Process(target=run_server)
	server_process.start()
	sleep(1)

	# SUPER USER HEADER
	superuser_creation()
	super_user_header = create_headers(123,'123')

	# NATURAL PERSON REGISTRASTION
	print(user_create(123456, "test@test"))
	headers_1 = create_headers(123456, "test@test")
	print(headers_1)
	print(create_natural_person(headers_1, 123456, 'Luís', '2004-06-19', '222222', 'Beck'))
 
	print(user_create(1234567, "test@test"))
	headers_2 = create_headers(1234567, "test@test")
	print(create_natural_person(headers_2, 1234567, 'Luís', '2004-06-19', '222222', 'Beck'))

	# LEGAL PERSON REGISTRASTION
	print(user_create(654321, "test@test"))
	headers_3 = create_headers(654321, "test@test")
	print(create_legal_person(headers_3, 654321, 'Fantasy', '2023-06-19', '1234', '4321', 'Cars'))
 
	print(user_create(7654321, "test@test"))
	headers_4 = create_headers(7654321, "test@test")
	print(create_legal_person(headers_4, 7654321, 'Fantasy', '2023-06-19', '1234', '4321', 'Cars'))
 
	# ADDRESS REGISTRASTION
	print(create_address(headers_1, 123456, 'Rua Jones', '69', 'LeWhite Green', 'Varsóvia', 'Polônia', '12564789'))
 
	# EMAIL REGISTRASTION
	print(create_email(headers_1, 123456, 'test@gmail.com'))
 
	# PHONE REGISTRASTION
	print(create_phone(headers_1, 123456, '+55', '11', '1111-1111'))
 
	# ACCOUNT REGISTRASTION
	print(create_account(headers_1, 'Savings'))
	print(create_account(headers_3, 'Current'))	

	# INVESTMENT REGISTRATION
	print(create_investment(super_user_header, 'LCA', 135.25, 1.5, '2030-12-11', 2.3, 15.6))
	print(create_investment(super_user_header, 'BCT', 192.25, 3.5, '2030-12-11', 5.2, 29.6))

	print(create_account_investment(headers_1, 1111,1))
	print(create_account_investment(headers_1, 1111,2))
	print(create_account_investment(headers_1, 1112,1))
	print(create_account_investment(headers_1, 1112,2))

	print(create_loan(headers_1, 1111, 1459.25, 4, "personal use"))
	print(create_loan(headers_1, 1111, 1325, 3, "personal use"))
	print(create_loan(headers_2, 1112, 150.25, 2, "personal use"))

	print(create_card(headers_1, 1111))

	print(create_card_transaction(headers_1, 1111, 1, "Debit", 500))

	print(create_pix(headers_1, 1111,1112,125))

	# server_process.join()

if __name__ == '__main__':
	main()