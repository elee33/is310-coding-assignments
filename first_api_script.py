import requests
import apikey

# Retrieve your API key
api_key = apikey.load('THE_ONE_API_KEY')

# Set up the headers with the token
url = 'https://the-one-api.dev/v2/character'
headers = {
    'Authorization': f'Bearer {api_key}'
}

# Make the request
response = requests.get(url, headers=headers)

# Check if the response was successful
if response.status_code == 200:
    characters = response.json().get('docs', [])
    
    # Loop through each character and print specific details
    for character in characters:
        name = character.get('name', 'N/A')
        race = character.get('race', 'N/A')
        gender = character.get('gender', 'N/A')
        realm = character.get('realm', 'N/A')
        
        print(f"Name: {name}, Race: {race}, Gender: {gender}, Realm: {realm}")
else:
    print(f"Failed to retrieve data: {response.status_code}")

