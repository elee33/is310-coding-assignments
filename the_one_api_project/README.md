# Europeana and Sports Data API Project

This project uses data from the **Europeana API** and **TheSportsDB API** to retrieve and analyze sports-related historical and cultural information. The `getting_culture.py` script fetches details about specific teams (e.g., "Arsenal") and cross-references these details with historical items from Europeana’s collections.

## Project Overview

The objective is to combine sports data and historical cultural artifacts to illustrate the intersection between sports history and European cultural heritage.

## Features

- **Europeana Search**: Retrieves historical and cultural items from Europeana related to the query (e.g., team names).
- **Sports Data Retrieval**: Uses TheSportsDB API to get team information, including stadium details and description.
- **Structured Output**: Combines and displays information from both sources in a readable format.

## Script Summary

The script `getting_culture.py` performs the following:

1. **Fetches team data from TheSportsDB API**: Retrieves information on specific teams, including stadium names and a description.
2. **Searches Europeana**: Finds items from Europeana’s database that are culturally related to the sports query.
3. **Displays Results**: Outputs the combined data, showing both sports and historical results.

## Example Output

```plaintext
Sports API Results:
Team: Arsenal, Stadium: Emirates Stadium

Europeana Results:
Title: Arsenal, Provider: Slovak National Gallery
Title: Arsenal, Provider: National Library of France
Title: Arsenal, Provider: Deutsche Fotothek
Title: Arsenal, Provider: German Documentation Center for Art History - Marburg Picture Index

