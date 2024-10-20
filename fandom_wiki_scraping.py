import requests
from bs4 import BeautifulSoup
import csv

# URL of the Lord of the Rings fandom wiki page
url = "https://lotr.fandom.com/wiki/Category:Canon_characters_in_The_Rings_of_Power"

# Make the HTTP request to get the page content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all the character links on the page
    characters = soup.find_all('a', class_='category-page__member-link')

    # Open a CSV file to write the scraped data
    with open('lotr_canon_characters.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Character Name', 'Link'])

        # Loop through all the character links and write to CSV
        for character in characters:
            character_name = character.get_text()
            character_link = "https://lotr.fandom.com" + character.get('href')
            writer.writerow([character_name, character_link])

    print("Scraping complete! Data saved to lotr_canon_characters.csv")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

