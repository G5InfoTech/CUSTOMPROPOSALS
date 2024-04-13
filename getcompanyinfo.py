import requests
from bs4 import BeautifulSoup
import os

def scrape_company_info(url):
    try:
        # Fetch the webpage
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the "About Us" section
        about_us_section = soup.find('div', {'class': 'about-us'})
        if about_us_section:
            about_us_text = about_us_section.get_text(strip=True)
        else:
            about_us_text = "About Us section not found on the website."

        # Find the "Leadership Team" section
        leadership_team_section = soup.find('div', {'class': 'leadership-team'})
        if leadership_team_section:
            leadership_team_text = leadership_team_section.get_text(strip=True)
        else:
            leadership_team_text = "Leadership Team section not found on the website."

        # Save the information to a text file
        company_name = url.replace('https://', '').replace('www.', '').split('/')[0]
        file_name = f"{company_name}_company_info.txt"
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(f"About Us:\n{about_us_text}\n\nLeadership Team:\n{leadership_team_text}")

        print(f"Company information saved to '{file_name}'.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Get the company website URL from the user
company_url = input("Enter the company website URL: ")

# Scrape the company information and save it to a text file
scrape_company_info(company_url)
