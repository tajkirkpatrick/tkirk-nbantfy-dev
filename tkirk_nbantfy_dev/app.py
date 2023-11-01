import urllib3
from bs4 import BeautifulSoup

def main():
    # Creating a PoolManager instance for sending requests.
    http = urllib3.PoolManager()

    # Sending a GET request and getting back response as HTTPResponse object.
    resp = http.request("GET", "https://www.basketball-reference.com/teams/HOU/2024_games.html")

    soup = BeautifulSoup(resp.data, 'html.parser')

    print(soup.prettify())

if __name__ == "__main__":
    main()