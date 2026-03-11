import requests
import pandas as pd
from bs4 import BeautifulSoup


def get_data():
    url = "http://books.toscrape.com"
    response = requests.get(url)
    return response


def parse_data(response):

    if response.status_code == 200:
        print("Fetch data successful")
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    elif response.status_code == 404:
        print("Page not found")

    elif response.status_code == 500:
        print("Server error")

    else:
        print("Fetch unsuccessful")


def extract_data(soup):

    books = soup.find_all("h3")
    prices = soup.find_all("p", class_="price_color")

    title_list = []
    price_list = []

    for book, price in zip(books, prices):
        title_list.append(book.a["title"])
        price_list.append(price.text)

    return title_list, price_list


def main():

    try:
        response = get_data()
        soup = parse_data(response)

        title_list, price_list = extract_data(soup)

        # Create DataFrame
        df = pd.DataFrame({
            "title": title_list,
            "price": price_list
        })

        print(df.head())

        # Save CSV
        df.to_csv("books_data.csv", index=False)

        print("Data saved successfully")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()