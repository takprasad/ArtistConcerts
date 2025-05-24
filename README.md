🎵 Concert Scraper with Selenium
This Python project uses Selenium to scrape upcoming concert data for music artists from ConcertArchives.org. Given a list of artist names in an Excel file, it fetches concert details like date, venue, city, and country, and saves them to a CSV file.

🚀 Features
Converts artist names into slug URLs using Unicode normalization.

Automatically opens each artist’s concert page on ConcertArchives.org.

Scrapes upcoming concert data including:

Date

Concert Name & Link

Venue

City, State, Country

Saves the collected data into a Output.csv file.

Supports batch processing for multiple artists (first 200 by default).

🧰 Requirements
Python 3.7+

Google Chrome browser

ChromeDriver (must match your Chrome version)

The following Python packages:

selenium

pandas

openpyxl (for reading Excel files)

Install the dependencies using:

bash
Copy
Edit
pip install selenium pandas openpyxl
Also, ensure chromedriver is installed and accessible via PATH.

📁 Input
The script expects an Excel file named artist_names.xlsx in the same directory with a column named artist_name.

Example:

plaintext
Copy
Edit
| artist_name     |
|-----------------|
| Taylor Swift    |
| Coldplay        |
| Foo Fighters    |
📤 Output
A CSV file named Output.csv will be created containing scraped data with the following columns:

Name

Date

Concert

ConcertLink

Venue

City

State

Country

⚙️ How It Works
Slugifies each artist's name to construct a URL.

Uses Selenium to open the concert listings.

Extracts concert info via XPath selectors.

Stores the data in a pandas DataFrame.

Exports the data to a CSV file.

🏃‍♂️ Running the Script
Make sure your input Excel file is ready, then run:

bash
Copy
Edit
python concert_scraper.py
⚠️ Notes
Some rows may be skipped due to inconsistent HTML or missing data.

Ensure your internet connection is stable during scraping.

Sites may change their structure over time—XPath selectors may need updates.
