# KenyanExternalDebtAnalysis

## Project Overview
This is the analysis of external debt owed by Kenya between 2010 and 2024. This project contains:

- A Python script for extracting from the World Bank Indicators API, transforming and loading data into a PostgreSQL database hosted on Aiven.
- A Jupyter notebook for testing purposes
- A SQL script which contains SQL queries used for generating dashboards on Grafana
- The Grafana dashboard which contains a line chart indicating Kenya’s external debt over time and a bar graph showing Year-over-Year debt change.

## Project Requirements

- Python 3.x
- `pandas==2.1.4` 
> NOTE: The newer version of pandas i.e. pandas==2.2.1 has a compatability issue with SQLAlchemy that raises an error when loading data into a database using the `df.to_sql` method from pandas. Use pandas==2.1.4 for this project, unless the issue has been sorted.
- SQLAlchemy
- `psycopg2-binary`
- `requests`
- `dotenv`

## Setup instructions

### 1. Clone this project
To clone this project, head over to your terminal and run the following command:

```bash
git clone https://github.com/dkkinyua/KenyanExternalDebtAnalysis
cd KenyanExternalDebtAnalysis
```
### 2. Install and setup your virtual environment

```bash
python3 -m venv your_env
your_env\Scripts\activate # Windows
your_env/bin/activate # Linux/MacOS
```

### 3. Install required dependencies

Run the following commands to install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Configure your environment variables.

For this project, a PostgreSQL database hosted on Aiven was used as the data target. To set up your own free PostgreSQL database on Aiven, click [here](https://console.aiven.io/signup). Get your database URI and create your `.env` file.

```ini
DB_URL="postgresql://user:pwd@host:port/database
```

Get this environment variable using `dotenv`'s `load_dotenv` method as so

```python
import os
from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv("DB_URL")
```

### 5. Run your script

```bash
python script.py
```

## Insights Discovered

There's been steady growth of external debt between 2010 and 2023, which reflects a **383% increase** in external debt over a period of 13 years, showing an overreliance on external borrowing to finance development

From the bar chart in the dashboard, **2014-2015** and **2017-2018** stand out as periods of high borrowing. The **2017** spike being the highest of them all, which coincides with the 2017 election period.

There's been slow debt growth between **2021 and 2023** which shows efforts to slow down external borrowing or external pressure from debt servicing.

## Technical or logical challenges you encountered

Some of the technical or logical challenges encountered include:

- Inconsistent time formats
- Dealing with missing/NaN values
- The API returns nested JSON or XML, not always straightforward for Pandas ingestion

