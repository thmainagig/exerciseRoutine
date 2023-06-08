import requests
import os
from datetime import datetime

exercise = input('What exercise did you do? ').title()
GENDER = input('What is your gender?Male/Female ').title()
WEIGHT_KG = float(input('What is your weight in kg? '))
HEIGHT_CM = float(input('What is your height in cm? '))
AGE = int(input('What is your age? '))

APP_ID = os.environ.get('APP_ID')
NUTRI_API_KEY = os.environ.get('APP_KEY')

Nutri_Endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
saa = datetime.today().time().strftime('%H:%M:%S')
leo = datetime.today().date().strftime('%d/%m/%Y')

nutri_config = {
    'query': exercise,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

headers = {
    'x-app-id': APP_ID,
    'x-app-key': NUTRI_API_KEY
}

response = requests.post(url=Nutri_Endpoint, json=nutri_config, headers=headers)
output = response.json()
print(output)

KEY = os.environ.get('SHEET_KEY')
for _ in output['exercises']:
    sheets_Endpoint = f'https://api.sheety.co/{KEY}/myWorkouts/sheet1'

    sheets_config = {
        'sheet1': {
         'Date': leo,
         'Time': saa,
         'Exercise': _['name'],
         'Duration': _['duration_min'],
         'Calories': _['nf_calories']
                   }
    }

    headers = {
        'Authorization': 'Bearer miamiYinyang',
        'Content-Type': 'application/json'
    }

    res = requests.post(url=sheets_Endpoint, json=sheets_config, headers=headers)
    print(res.json())