from urllib import response

import requests

url = 'https://detik.com'
try:
    response = requests.get( url )
    print(f'success ! {response}')
    print(f'content! {response.text}')
except Exception as e:
    print(f'there is an error {e}!')
print('success!!!')

