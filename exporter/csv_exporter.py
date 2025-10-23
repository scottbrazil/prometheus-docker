from prometheus_client import Gauge, start_http_server
import csv
import time
import os

CSV_FILE = os.getenv("CSV_FILE", "/data/data.csv")
UPDATE_INTERVAL = int(os.getenv("UPDATE_INTERVAL", "30"))

temperature_gauge = Gauge('temperature_celsius', 'Temperature readings', ['city'])

def load_csv():
    try:
        with open(CSV_FILE) as f:
            reader = csv.DictReader(f)
            for row in reader:
                city = row['city']
                temp = float(row['temperature'])
                temperature_gauge.labels(city=city).set(temp)
        print(f"Loaded CSV: {CSV_FILE}")
    except Exception as e:
        print(f"Error reading CSV: {e}")

if __name__ == '__main__':
    start_http_server(8000)  # Metrics available at http://localhost:8000/metrics
    while True:
        load_csv()
        time.sleep(UPDATE_INTERVAL)
