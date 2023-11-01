import urllib3
from bs4 import BeautifulSoup


def main():
    # Creating a PoolManager instance for sending requests.
    http = urllib3.PoolManager()

    # Sending a GET request and getting back response as HTTPResponse object.
    resp = http.request(
        "GET", "https://www.basketball-reference.com/teams/HOU/2024_games.html#games"
    )

    soup = BeautifulSoup(resp.data, "html.parser")

    schedule_table = soup.find_all("table", id="games")[0]
    table_body = schedule_table.find("tbody")

    print(table_body)


if __name__ == "__main__":
    main()
