from flask import Flask, render_template, json
import pyodbc
import requests
from datetime import datetime
import time

app = Flask(__name__, template_folder='templates')

# Veritabanı bağlantısı
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=database;'
                      'Database=name;'
                      'UID=hilaldindar;'
                      'PWD=****Hilal;')
cursor = conn.cursor()

# Veri çekme ve veritabanına ekleme işlemini gerçekleştiren fonksiyon
def fetch_and_store_earthquake_data():
    try:
        # API'den veri çekme
        url = "https://api.orhanaydogdu.com.tr/deprem/kandilli/live"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()["result"]
            
            for item in data:
                date = datetime.strptime(item["date"], "%Y.%m.%d %H:%M:%S")
                magnitude = float(item["mag"])
                depth = float(item["depth"]) if item["depth"] else None
                location = item["title"]
                latitude = item["geojson"]["coordinates"][1]  # Enlem
                longitude = item["geojson"]["coordinates"][0]  # Boylam

                cursor.execute("""
                MERGE INTO earthquakeh.CanliDepremler AS target
                USING (VALUES (?, ?, ?, ?, ?, ?)) AS source (Tarih, Buyukluk, Derinlik, Lokasyon, Enlem, Boylam)
                ON target.Tarih = source.Tarih
                WHEN MATCHED THEN
                    UPDATE SET target.Buyukluk = source.Buyukluk, target.Derinlik = source.Derinlik, target.Lokasyon = source.Lokasyon,
                    target.Enlem = source.Enlem, target.Boylam = source.Boylam
                WHEN NOT MATCHED THEN
                    INSERT (Tarih, Buyukluk, Derinlik, Lokasyon, Enlem, Boylam) VALUES 
                    (source.Tarih, source.Buyukluk, source.Derinlik, source.Lokasyon, source.Enlem, source.Boylam);
                """, (date, magnitude, depth, location, latitude, longitude))


                conn.commit()

                print("Veri başarıyla veritabanına eklendi veya güncellendi.")
        else:
            print("API'den veri alınamadı. HTTP Hatası:", response.status_code)
            
    except Exception as e:
        print("Hata:", e)
        conn.rollback()

# Web sayfasını güncellemek için verileri getiren fonksiyon
def get_earthquake_data():
    try:
        cursor.execute("SELECT Tarih, Buyukluk FROM earthquakeh.CanliDepremler ORDER BY Tarih ASC")
        data = [{"tarih": row.Tarih.strftime("%Y-%m-%d %H:%M:%S"), "buyukluk": row.Buyukluk} for row in cursor.fetchall()]
        return json.dumps(data)
    except Exception as e:
        print("Hata:", e)
        return "[]"


# Ana sayfa
@app.route('/')
def index():
    return render_template('index.html')

# Canlı veri endpoint'i
@app.route('/data')
def data():
    return get_earthquake_data()

if __name__ == '__main__':
    while True:
        fetch_and_store_earthquake_data()
        # Her 3 dakikada bir çalışmasını sağlar
        time.sleep(180)  
