import os
import requests
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
DB_URL = os.getenv("DB_URL")

# extract data from World Bank API

def extract():
    url = "https://api.worldbank.org/v2/country/KE/indicator/DT.DOD.DECT.CD"
    params = {
        'date': '2010:2024',
        'format': 'json'
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        rel_data = []
        data = response.json()
        for item in data[1]:
            rel_data.append({
                'countryName': item['country']['id'],
                'year': item['date'],
                'debtValue': item['value'],
                'indicator': item['indicator']['value']
            })
        return rel_data
    else:
        print(f"Error fetching data: {response.status_code}, {response.text}")

# Transform and load data into db
def transform_load(data, url):
    df = pd.DataFrame(data)
    df.dropna(inplace=True)

    try:
        engine = create_engine(url)
        df.to_sql('external_data', con=engine, index=False, if_exists='replace')
        print('Data loaded successfully!')
    except Exception as e:
        print(f"Error loading into db: {e}")

if __name__ == '__main__':
    print("Data extraction is starting...")

    data = extract()

    print("Data extraction complete, transforming and loading starting...")

    transform_load(data, url=DB_URL)


