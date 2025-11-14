BACKEND — saving_goals_api

Python + Flask + PostgreSQL (Railway)
REST API untuk aplikasi Tabungan / Saving Goals.

🚀 Fitur

CRUD Tabungan (Create, Read, Update, Delete)

Database PostgreSQL (Railway)

ORM menggunakan SQLAlchemy

CORS diaktifkan agar Flutter Web dapat mengakses API

Struktur backend jelas & mudah dikembangkan

📁 Struktur Folder
saving_goals_api/
│── app.py
│── requirements.txt
│── config/
│     └── database.py
│── models/
│     └── tabungan_model.py
│── routes/
│     └── web.py
└── controllers/
      └── tabungan_controller.py

🗄 Database (PostgreSQL Railway)

Nama tabel: tabungan

Kolom	Tipe	Keterangan
id_tabungan	SERIAL (PK)	Primary key
nama_tabungan	VARCHAR(100)	Nama tabungan
deskripsi	VARCHAR(255)	Deskripsi tabungan
target	FLOAT	Target tabungan
saldo	FLOAT	Saldo tabungan
created_at	TIMESTAMP	Otomatis
updated_at	TIMESTAMP	Otomatis
⚙️ Cara Menjalankan Backend di Local
1. Clone repo
git clone https://github.com/USERNAME/saving_goals_api.git
cd saving_goals_api

2. Install library Python
pip install -r requirements.txt

3. Jalankan API
python app.py


Default berjalan di:

http://localhost:5000

🌐 Endpoint API
➤ GET Semua Tabungan

GET /api/tabungan

➤ GET Tabungan by ID

GET /api/tabungan/{id}

➤ POST Tambah Tabungan

POST /api/tabungan

Body:

{
  "nama_tabungan": "Liburan Jepang",
  "deskripsi": "Target liburan",
  "target": 5000000,
  "saldo": 1000000
}

➤ PUT Update Tabungan

PUT /api/tabungan/{id}

➤ DELETE Hapus Tabungan

DELETE /api/tabungan/{id}

🚀 Deployment Railway

Upload project ke GitHub

Buka Railway → New Project → Deploy from GitHub

Tambahkan Environment Variable:

DATABASE_URL=postgresql://USER:PASSWORD@HOST:PORT/railway


Deploy

API siap diakses:

https://saving-goals-api-production.up.railway.app/api/tabungan