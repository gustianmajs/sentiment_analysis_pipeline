# sentiment_analysis_pipeline

## SIB6_Final Project
1.  Login to Finnhub
2.  Login to MongoDB Atlas
3.  Docker Compose Airflow

## Steps :
1.  Jalankan Airflow menggunakan docker-compose up
2.  Buat Plugins:
a.  Finnhub loader
b.  MongoDB loader
c.  entiment Analysis
d.  Postgres loader
3.  Buat kode Python untuk mengekstrak data dari Finnhub dan memuatnya ke MongoDB
4.  Buat kode Python untuk mengambil data dari MongoDB, melakukan analisis sentimen, dan memuat hasilnya ke Postgres
5.  Buat Environment Python menggunakan python -m venv env
6.  Aktifkan environment menggunakan env/Scripts/activate
7.  Jalankan pip install -r requirements.txt
8.  Jalankan python finhub_mongodb_loader.py
9.  Jalankan pip install psycopg2-binary
10.  Jalankan python sentiment_analysis_loader.py
11.  Buat Database menggunakan salah satu dari dua metode berikut:
A.  Masuk ke Docker Desktop -> postgres image -> terminal -> psql -Uairflow -> create database data_warehouse; -> \du -> \l
B.  Atau docker exec -it <postgres image id> bash -> psql -Uairflow -> create database data_warehouse; -> \du -> \l
12.  Periksa database yang baru dibuat menggunakan:
\c data_warehouse -> \d -> select * from sentiment_news_analysis limit 20;
 
