import requests
from bs4 import BeautifulSoup

def get_filmography(actor_name):
    # Construct the Wikipedia URL for the actor's page
    url = f"https://en.wikipedia.org/wiki/{actor_name.replace(' ', '_')}_filmography"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find the filmography table on the page
        filmography_table = soup.find("table", class_="wikitable")
        if filmography_table:
            films = []
            # Extract film titles from the table rows and headers
            for row in filmography_table.find_all(["th", "td"]):
                title = row.get_text(strip=True)
                films.append(title)
            return films
        else:
            print("No filmography table found on the Wikipedia page.")
    else:
        print("Error fetching Wikipedia page:", response.status_code)
    return None

# Example usage
actor_name = input("Enter the name of the actor: ").strip()
filmography = get_filmography(actor_name)
if filmography:
    print(f"Filmography of {actor_name} in descending order:")
    for film in filmography:
        print(film)
else:
    print("No filmography found for the given actor name.")
