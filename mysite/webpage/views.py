from django.shortcuts import render
from django.http import JsonResponse
from bs4 import BeautifulSoup
import requests
from django.shortcuts import render
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup

def country_info(request, country_name):
    # Extract the desired information from the page
    url = f"https://en.wikipedia.org/wiki/{country_name}"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    # Extract data from page using BeautifulSoup
    flag_link = soup.select_one(".infobox img")["src"]
    capital = soup.select_one("th:contains('Capital') + td").text
    largest_city = soup.select("th:contains('Largest city') + td a")
    largest_city = [city.text for city in largest_city]
    official_languages = soup.select("th:contains('Official languages') + td a")
    #official_languages = [language.text for language in official_languages]
    area_total = soup.select_one("th:contains('Total') + td").text
    population = soup.select_one("th:contains('2022 estimate') + td").text
    GDP_nominal = soup.select_one("th:contains('Per capita') + td").text

    final_link= flag_link.split('svg',1)[0]
    final_link='https:'+str(final_link)+'svg'
    final_link=final_link.split('thumb/')[0] + final_link.split('thumb/')[1]
    # Create a JSON object with the extracted information
    data = {
        'flag_link': final_link,
        'capital': capital,
        'largest_city': largest_city,
        'official_languages': official_languages,
        'area_total': area_total,
        'population': population,
        'gdp_nominal': GDP_nominal,
    }

    # Return the JSON object as the response to the API request
    return JsonResponse(data)