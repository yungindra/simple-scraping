import requests
from bs4 import BeautifulSoup
import csv

response = requests.get("https://www.example.com/countries")
soup = BeautifulSoup(response.text, "html.parser")

result = []

country_blocks = soup.find_all("div", class_="col-md-4 country")

for block in country_blocks:
    name_element = block.find("h3", class_="country-name")
    country_name = name_element.get_text(strip=True)

    capital_element = block.find("span", class_="country-capital")
    capital_name = capital_element.get_text(strip=True)

    population_element = block.find("span", class_="country-population")
    population_name = population_element.get_text(strip=True)

    result.append({
        "name": country_name,
        "capital": capital_name,
        "population": population_name
    })

for item in result:
    print(f"Country: {item['name']} - Capital: {item['capital']} - Population: {item['population']}")

#Save to CSV
with open("Countries.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["name", "capital", "population"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for item in result:
        writer.writerow(item)

print("✅ Data has been saved to Countries.csv")