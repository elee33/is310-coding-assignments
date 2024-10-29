
<<<<<<< HEAD
## Europeana and Sports Data API Project

This project combines data from the Europeana API and a Sports Data API to retrieve and analyze historical sports information. The `getting_culture.py` script fetches details about notable sports events, such as the Olympics, and cultural heritage items related to sports. 
=======
Project Overview

This project uses The One API to get data on characters from J.R.R. Tolkien's world. It then cross-references this information with Europeana to find related historical and cultural items. The goal is to bring together pop culture data with European heritage artifacts.

Script Summary

The script getting_culture.py does the following:

Fetches character data from The One API (like name, race, and realm).
Searches Europeana for items that might be connected to these characters.
Displays the combined information.
Setup

echo "# API Getting Data Assignment

## Project Overview

This project uses **The One API** to get data on characters from J.R.R. Tolkien's world. It then cross-references this information with **Europeana** to find related historical and cultural items. The goal is to bring together pop culture data with European heritage artifacts.

## Script Summary

The script \`getting_culture.py\` does the following:
- Fetches character data from **The One API** (like name, race, and realm).
- Searches **Europeana** for items that might be connected to these characters.
- Displays the combined information.

## Setup

1. **Requirements**:
   - Install Python and the \`requests\` package.
   \`\`\`bash
   pip install requests
   \`\`\`

2. **Get API Keys**:
   - Register at [The One API](https://the-one-api.dev) and [Europeana API](https://pro.europeana.eu/pages/get-api).
   - Store these keys securely.

3. **Running the Script**:
   - Run the script by entering:
   \`\`\`bash
   python getting_culture.py
   \`\`\`
" > README.md
>>>>>>> 2208d07 (Final project update with README and getting_culture script)

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
