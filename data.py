import requests
from bs4 import BeautifulSoup
import csv


def fetch_table_data():
    table_data = []
    try:
        response = requests.get("https://www.delhisldc.org/Redirect.aspx?Loc=0804")
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', id='ContentPlaceHolder3_dgrid')

        for row in table.find_all('tr'):
            row_data = []
            for cell in row.find_all('td'):
                row_data.append(cell.get_text(strip=True))

            table_data.append(row_data)
        return table_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    
table_data = fetch_table_data()

with open("data.csv", 'w') as csvfile:
    writer = csv.writer(csvfile)

    for i in table_data:
        writer.writerow(i)
