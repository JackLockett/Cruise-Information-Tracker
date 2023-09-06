import requests
from bs4 import BeautifulSoup

cruise_dict = {
    "Marella Discovery": "https://www.cruisemapper.com/ships/Marella-Discovery-712",
    "Marella Discovery 2": "https://www.cruisemapper.com/ships/Marella-Discovery-2-651",
    "Marella Explorer": "https://www.cruisemapper.com/ships/Marella-Explorer-1814",
    "Marella Explorer 2": "https://www.cruisemapper.com/ships/Marella-Explorer-2-1620",
    "Marella Voyager": "https://www.cruisemapper.com/ships/Marella-Voyager-682"
}

print("\nAvailable cruises to track:\n")
for index, cruise_name in enumerate(cruise_dict.keys(), start=1):
    print(f"{index}. {cruise_name}")

while True:
    try:
        user_choice = int(input("\nEnter the number corresponding to the cruise you want to track (1-5): "))
        if 1 <= user_choice <= 5:
            selected_cruise_name = list(cruise_dict.keys())[user_choice - 1]
            selected_cruise_url = cruise_dict[selected_cruise_name]
            break
        else:
            print("\nInvalid input. Please enter a number between 1 and 5.")
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

response = requests.get(selected_cruise_url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    current_cruise_heading = soup.find("h3", class_="contentTitle", id="current_cruise")

    if current_cruise_heading:
        current_cruise_info = current_cruise_heading.find_next("p").text.strip()
        print(f"\nCurrent Cruise Info for {selected_cruise_name}:\n\n", current_cruise_info)
    else:
        print("\nCurrent cruise information not found on the page.")
else:
    print("\nFailed to retrieve the web page. Status code:", response.status_code)
