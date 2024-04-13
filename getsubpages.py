import requests
from bs4 import BeautifulSoup
import urllib.parse
import re

def get_all_subpages(url):
    """
    Retrieves a list of subpages from the given URL that contain specified terms.

    Args:
        url (str): The URL of the website to search for subpages.

    Returns:
        list: A list of URLs of subpages that contain specified terms (e.g., "about us", "leadership", "team", "executive").
              If no subpages are found or an error occurs, an empty list is returned.

    Example:
        >>> subpages = get_all_subpages("https://www.example.com")
        >>> if subpages:
        ...     print("Subpages:")
        ...     for subpage in subpages:
        ...         print(subpage)
        ... else:
        ...     print("No subpages found.")
    """
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

        # Filter subpages containing specified terms
        filtered_subpages = []
        for subpage in subpages:
            if re.search(r'about\s*us|about-us|aboutus|about|leadership|team|executive', subpage, re.IGNORECASE):
                filtered_subpages.append(subpage)

        return filtered_subpages

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return []

# Get the website URL from the user
website_url = input("Enter the website URL: ")

# Get all the subpages of the website containing specified terms
subpages = get_all_subpages(website_url)

# Print the subpages
if subpages:
    print("Subpages:")
    for subpage in subpages:
        print(subpage)
else:
    print("No subpages found.")