import requests

# API keys
europeana_api_key = "scallawlani"  
sports_api_key = "3"  


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
    sports_url = f"https://thesportsdb.com/api/v1/json/{sports_api_key}/searchplayers.php"
    params = {'p': query}
    response = requests.get(sports_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("player", [])
    else:
        print(f"Sports API error: {response.status_code}")
        return []

# Run queries
def main():
    sport_query = "Olympics"
    europeana_results = search_europeana(sport_query)
    sports_results = search_sports(sport_query)

    print("Europeana Results:")
    for item in europeana_results:
        title = item.get('title', ['No title'])[0]
        data_provider = item.get('dataProvider', 'Unknown provider')
        print(f"Title: {title}, Provider: {data_provider}")

    print("\nSports API Results:")
    for player in sports_results:
        player_name = player.get('strPlayer', 'No name')
        player_team = player.get('strTeam', 'No team')
        player_sport = player.get('strSport', 'No sport')
        print(f"Name: {player_name}, Team: {player_team}, Sport: {player_sport}")

if __name__ == "__main__":
    main()
