import requests
from bs4 import BeautifulSoup
import urllib.parse

def get_all_subpages(url):
    try:
        # Fetch the webpage
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the links on the page
        links = soup.find_all('a')

        # Extract the URLs of the subpages
        subpages = set()
        base_url = urllib.parse.urlparse(url).scheme + "://" + urllib.parse.urlparse(url).netloc
        for link in links:
            href = link.get('href')
            if href and href.startswith('/'):
                subpage_url = base_url + href
                subpages.add(subpage_url)
            elif href and href.startswith(base_url):
                subpages.add(href)

        return subpages
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Get the website URL from the user
website_url = input("Enter the website URL: ")

# Get all the subpages of the website
subpages = get_all_subpages(website_url)

# Print the subpages
if subpages:
    print("Subpages:")
    for subpage in subpages:
        print(subpage)
else:
    print("No subpages found.")
