# Books Scraper Python

This project demonstrates a web scraping pipeline built using Python.

The scraper collects data from [Books to Scrape](http://books.toscrape.com), a sample online bookstore, and saves the data into a CSV file.

## Features

- Fetch HTML pages using `requests`
- Parse and extract data using `BeautifulSoup`
- Collect book titles and prices
- Save extracted data as `books_data.csv`
- Easy to extend with pagination to scrape all books

## Tools Used

- Python 3
- Requests
- BeautifulSoup
- Pandas

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/nehajainpython/books-scraper-python.git
