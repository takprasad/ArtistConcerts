# 🎵 Concert Scraper with Selenium

This Python project uses Selenium to scrape upcoming concert data for music artists from [ConcertArchives.org](https://www.concertarchives.org). Given a list of artist names in an Excel file, it fetches concert details like date, venue, city, and country, and saves them to a CSV file.

## 🚀 Features

- Converts artist names into slug URLs using Unicode normalization.
- Automatically opens each artist’s concert page on ConcertArchives.org.
- Scrapes upcoming concert data including:
  - Date
  - Concert Name & Link
  - Venue
  - City, State, Country
- Saves the collected data into a `Output.csv` file.
- Supports batch processing for multiple artists (first 200 by default).

## 🧰 Requirements

- Python 3.7+
- Google Chrome browser
- ChromeDriver (must match your Chrome version)
- The following Python packages:
  - `selenium`
  - `pandas`
  - `openpyxl` (for reading Excel files)

Install the dependencies using:

```bash
pip install selenium pandas openpyxl
