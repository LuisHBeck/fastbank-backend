import requests, os, subprocess, multiprocessing, dotenv, base64
from time import sleep

dotenv.load_dotenv()

IP = os.getenv('IP')
PORT = os.getenv('PORT')
VERSION = 'v1'
BASE_URL = f'http://localhost:{PORT}/api/{VERSION}/'

user_create_url = os.path.join(BASE_URL, 'auth/users/')
jwt_create_url = os.path.join(BASE_URL, 'auth/jwt/create/')
natural_person_url = os.path.join(BASE_URL, 'natural-people/')
legal_person_url = os.path.join(BASE_URL, 'legal-people/')
address_url = os.path.join(BASE_URL, 'addresses/')
email_url = os.path.join(BASE_URL, 'emails/')
phone_url = os.path.join(BASE_URL, 'phones/')
account_url = os.path.join(BASE_URL, 'accounts/')
investment_url = os.path.join(BASE_URL, 'investments/')
account_investment_url = os.path.join(BASE_URL, 'account-investments/')
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
		subprocess.run(['py', 'manage.py', 'runserver', f'{IP}:{PORT}'], check=True)
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


def user_create(register_number, password, picture):
	with open(picture, 'rb') as image:
		files = {
			'picture': (image.name, image, 'image/jpeg')
		}
		response = requests.post(user_create_url, 
			data={
				"register_number": register_number,
				"password": password
			},
			files=files)
	print(response.json())
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
	print(response.json())
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
	print(response.json())
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
	print(response.json())
	return response.json()


def create_email(headers, user, email):
    response = requests.post(email_url, headers=headers, json={
        'user': user,
        'email': email
    })
    print(response.json())
    return response.json()


def create_phone(headers, user, area_code, prefix_number, phone_number):
    response = requests.post(phone_url, headers=headers, json={
        'user': user,
        'area_code': area_code,
        'prefix_number': prefix_number,
        'phone_number': phone_number
    })
    print(response.json())
    return response.json()


def create_account(headers, type):
    response = requests.post(account_url, headers=headers, json={
        'type': type
    })
    print(response.json())
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
	print(response.json()) 
	return response.json()


def create_account_investment(headers, id_account, id_investment):
	response = requests.post(account_investment_url, headers=headers, json={
		'id_account':id_account,
		'id_investment':id_investment
	})
	print(response.json())
	return response.json()


def create_loan(headers, id_account, amount, installment_amount, observation):
	response = requests.post(create_loan_url, headers=headers, json={
		'id_account': id_account,
		'amount_request': amount,
		'installment_amount': installment_amount,
		'observation': observation
	})
	print(response.json())
	return response.json()


def create_card(headers, id_account):
	response = requests.post(card_new_url, headers=headers, json={
		'id_account': id_account
	})
	print(response.json())
	return response.json()


def create_card_transaction(headers, id_account, id_card, operation, amount):
	response = requests.post(card_transaction_url, headers=headers, json={
		'id_account': id_account,
		'id_card': id_card,
		'operation': operation,
		'amount': amount
	})
	print(response.json())
	return response.json()


def create_pix(headers, payer_account, receiver_account, amount):
	response = requests.post(pix_url, headers=headers, json={
		'id_account': payer_account,
		'id_receiver_account': receiver_account,
		'amount': amount
	})
	print(response.json())
	return response.json()


def main():
	#CREATING DATABSE
	# data_base_creation()
	# server_process = multiprocessing.Process(target=run_server)
	# server_process.start()
	# sleep(1)

	# superuser_creation()
	super_user_header = create_headers(11111111111,'123')

	user1 = user_create(register_number="45505681000", password="test@test", picture='users\\photo\\alemao.jpg')
	headers_1 = create_headers(user1['register_number'], "test@test")
	natural1 = create_natural_person(headers_1, user1['register_number'], 'Luís', '2004-06-19', '394541716', 'Beck')
 
	user2 = user_create(28142572001, "test@test", 'users\\photo\\alemao.jpg')
	headers_2 = create_headers(user2['register_number'], "test@test")
	natural2 = create_natural_person(headers_2, user2['register_number'], 'Luís', '2004-06-19', '378889205', 'Beck')

	user3 = user_create(52205116000160, "test@test", 'users\\photo\\alemao.jpg')
	headers_3 = create_headers(user3['register_number'], "test@test")
	legal1 = create_legal_person(headers_3, user3['register_number'], 'Fantasy', '2023-06-19', '86420975183', '159716446', 'Cars')
 
	user4 = user_create(67040725000184, "test@test", 'users\\photo\\alemao.jpg')
	headers_4 = create_headers(user4['register_number'], "test@test")
	legal2 = create_legal_person(headers_4, user4['register_number'], 'Fantasy', '2023-06-19', '93721845601', '050175645', 'Cars')
 
	address1 = create_address(headers_1, user1['register_number'], 'Rua Jones', '69', 'LeWhite Green', 'Varsóvia', 'Polônia', '132760190')
 
	email1 = create_email(headers_1, user1['register_number'], 'test@gmail.com')
 
	phone1 = create_phone(headers_1, 45505681000, '+55', '19', '267777141')
 
	account1 = create_account(headers_1, 'Savings')
	account2 = create_account(headers_3, 'Current')	

	invest1 = create_investment(super_user_header, 'LCA', 135.25, 1.5, '2030-12-11', 2.3, 15.6)
	invest2 = create_investment(super_user_header, 'BCT', 192.25, 3.5, '2030-12-11', 5.2, 29.6)

	acc_invest1 = create_account_investment(headers_1, 1111, invest1['id'])
	acc_invest2 =create_account_investment(headers_1, 1111, invest2['id'])
	acc_invest3 =create_account_investment(headers_1, 1112, invest1['id'])
	acc_invest4 =create_account_investment(headers_1, 1112, invest2['id'])

	loan1 = create_loan(headers_1, 1111, 1459.25, 4, "personal use")
	loan1 = create_loan(headers_1, 1111, 1325, 3, "personal use")
	loan1 = create_loan(headers_2, 1112, 150.25, 2, "personal use")

	card1 = create_card(headers_1, 1111)

	card_t1 = create_card_transaction(headers_1, 1111, 1, "Debit", 500)

	pix1 = create_pix(headers_1, 1111,1112,125)

if __name__ == '__main__':
	main()