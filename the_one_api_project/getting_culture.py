import requests

# API keys
europeana_api_key = "scallawlani"  
sports_api_key = "3"  # TheSportsDB API key

# Europeana API setup
def search_europeana(query):
    europeana_url = "https://api.europeana.eu/record/v2/search.json"
    params = {
        'wskey': europeana_api_key,
        'query': query,
        'media': 'true',
        'profile': 'rich',
        'rows': 5  
    }
    response = requests.get(europeana_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("items", [])
    else:
        print(f"Europeana API error: {response.status_code}")
        return []

# Sports API setup
def search_sports(query):
    sports_url = f"https://www.thesportsdb.com/api/v1/json/{sports_api_key}/searchteams.php"
    params = {'t': query}
    response = requests.get(sports_url, params=params)
    if response.status_code == 200:
        data = response.json()
        print("Sports API raw response:", data)  # For debugging
        return data.get("teams", [])
    else:
        print(f"Sports API error: {response.status_code}")
        return None

# Main function to run queries and print results
def main():
    sport_query = "Arsenal"  # Change this query as needed
    europeana_results = search_europeana(sport_query)
    sports_results = search_sports(sport_query)

    print("Europeana Results:")
    for item in europeana_results:
        title = item.get('title', ['No title'])[0]
        data_provider = item.get('dataProvider', 'Unknown provider')
        print(f"Title: {title}, Provider: {data_provider}")

    print("\nSports API Results:")
    if sports_results:  # Only print if sports_results is not None
        for team in sports_results:
            team_name = team.get('strTeam', 'No team name')
            team_stadium = team.get('strStadium', 'No stadium info')
            print(f"Team: {team_name}, Stadium: {team_stadium}")
    else:
        print("No teams found for the given query.")

# Run the main function
if __name__ == "__main__":
    main()

