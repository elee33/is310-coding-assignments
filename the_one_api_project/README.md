# IS310 Coding Assignments

## Europeana and Sports Data API Project

This project combines data from the Europeana API and a Sports Data API to retrieve and analyze historical sports information. The `getting_culture.py` script fetches details about notable sports events, such as the Olympics, and cultural heritage items related to sports. 

### Project Features
- Queries Europeana’s collection for historical cultural items related to sports.
- Uses a Sports Data API to retrieve information on notable athletes or events.
- Outputs a structured result, combining data from both sources.

### Setup Instructions

1. **Install Required Packages:**
   ```bash
   pip install requests
   ```

2. **Set Up API Keys:**
   - Get an API key for Europeana from [Europeana's API page](https://pro.europeana.eu/pages/get-api) and insert it into the `getting_culture.py` file where prompted.
   - Insert your Sports Data API key, if needed.

### Running the Script

Run the script with:
```bash
python getting_culture.py
