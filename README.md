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
```

# 📘 Input, Output & Workflow Details

This document provides a more detailed explanation of the input format, expected output, and the internal workings of the Concert Scraper script.

---

## 📥 Input Format

The scraper requires an Excel file named `artist_names.xlsx` to be present in the same directory as the script.

### File Structure

The Excel file must contain a column labeled `artist_name`. Each row should contain the name of a musical artist or band you wish to scrape upcoming concert data for.

**Example content of `artist_names.xlsx`:**

| artist_name     |
|-----------------|
| Taylor Swift    |
| Coldplay        |
| Foo Fighters    |
| Arctic Monkeys  |
| Metallica       |

---

## 📤 Output

After running the script, a CSV file named `Output.csv` is generated in the current directory. It contains scraped concert information for each artist in the input file.

### Columns in `Output.csv`:

- `Name`: The artist's name
- `Date`: Date of the concert
- `Concert`: Concert event title
- `ConcertLink`: Direct link to the concert details on ConcertArchives
- `Venue`: Name of the venue
- `City`: City where the event is held
- `State`: State/region of the venue
- `Country`: Country of the event

**Example Output:**

| Name          | Date       | Concert         | ConcertLink                        | Venue         | City     | State | Country |
|---------------|------------|------------------|-------------------------------------|---------------|----------|-------|---------|
| Coldplay      | May 25, 2025 | Music of the Spheres | https://.../concerts/...       | Wembley Arena | London   | England | UK      |

---

## ⚙️ How It Works

1. **Slugify Artist Name**
   - The artist name is converted into a URL-friendly "slug" (e.g., `"Foo Fighters"` → `"foo-fighters"`).

2. **Open Browser and Load Page**
   - Selenium opens Chrome and navigates to the band’s ConcertArchives page using the slug.

3. **Locate Upcoming Concerts**
   - The page is parsed for a table of upcoming concerts using XPath selectors.

4. **Extract Data**
   - For each concert, the script extracts:
     - Date
     - Event name and link
     - Venue
     - City, state, and country (parsed from a comma-separated string)

5. **Store and Save**
   - Data is collected into a list of dictionaries.
   - Once all artists are processed, the data is saved to `Output.csv`.

6. **Clean Exit**
   - The browser is closed automatically after data extraction is complete for each artist.

---

## 🛠 Troubleshooting Tips

- Make sure your `chromedriver` version matches your Chrome browser.
- If data isn't being fetched:
  - Check for changes in the website layout.
  - Ensure artist names are spelled correctly.
  - Try increasing the `sleep()` duration if the page loads slowly.

---

Feel free to contribute improvements or report issues in the [Issues](../../issues) tab.

