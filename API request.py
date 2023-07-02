import json

import requests
import pandas as pd



test_input = {'text':'Macaroni and Cheese macaroni, cheese, small red onion diced ounce package small past','mode':'free_text','no_of_recipes':3} # free_text mode

test_input = {'name':'Macaroni and Cheese','category':'main-dish','summary':'This is a recipe for macaroni and cheese.',
              'ingredients':'macaroni, cheese, butter, milk','diet_type':'Vegetarian',
              'mode':'full_model','no_of_recipes':5} # full_model mode


response = requests.post('http://127.0.0.1:5000/get-recipe', json=test_input)
# response = requests.post('https://foodrecommendation.azurewebsites.net/get-recipe', json=test_input)

print(response.status_code)
print(response.json())

# convert server response into dataframe
data1 = json.loads(response.json())

df = pd.DataFrame(data1)

df.head()