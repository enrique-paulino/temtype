# TemType 

## Description

This project is a web application built with Flask that provides information about Temtem creatures, including their types, weaknesses, and matchups. The main functionalities include searching for a specific Temtem, displaying its types, and showing the matchups with other types. This works by scraping data from the Temtem Fandom Wiki. It uses the `fandom` Python module along with `requests` and `BeautifulSoup` for web scraping.

## Functions:

- `FindTem(temtem)`: Checks if a Temtem exists on the Fandom Wiki.
- `ScrapeSummary(temtem)`: Scrapes the summary of a Temtem.
- `ScrapePicture(temtem)`: Scrapes images of a Temtem.
- `ScrapeType(temtem)`: Scrapes the types of a Temtem.
- `ScrapeMatchup(temtem)`: Scrapes the type matchups of a Temtem.

## Demo in Action

Include a gif here that demonstrates the usage of the Temtype web application. This will provide users with a visual representation of how the application works.

![Demo](https://i.imgur.com/YJtkB5I.gif)

## Usage

To run the web application:

1. Install Python (3.8).
2. Download the files as zip, and extract into a new folder.
3. Open the terminal in said folder and run the following command:
`pip install -r requirements.txt`
4. Open the file: `run_temtype.py` 
    - The cmd window will immediately close, this is normal.
5. Access the application in your web browser at `http://localhost:5000`.

## Note

This project is designed to illustrate the use of Flask and web scraping for displaying Temtem information.
