from dotenv import load_dotenv
import requests
import os

load_dotenv()

class Quote:
    def __init__(self):
        self.URL = os.getenv('url')
        self.list_of_quotes = self.get_quotes()

    def get_quotes(self):
        response = requests.get(self.URL)
        return response.json()

if __name__ == '__main__':
    quotes = Quote().list_of_quotes[1]
    print(quotes)
