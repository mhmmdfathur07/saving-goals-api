from flask import Flask
from flask_cors import CORS
from config.database import engine, Base
from routes.web import web
import models.tabungan_model  # Registrasi model agar SQLAlchemy mengenali

# =========================================================
# Inisialisasi aplikasi Flask
# =========================================================
app = Flask(__name__)

# =========================================================
# Aktifkan CORS (izin akses dari Flutter / domain lain)
# =========================================================
# Mengizinkan semua domain untuk mengakses endpoint /api/*
CORS(app, resources={r"/api/*": {"origins": "*"}})

# =========================================================
# Inisialisasi database dan buat tabel otomatis
# =========================================================
Base.metadata.create_all(bind=engine)

# =========================================================
# Registrasi blueprint route utama
# =========================================================
app.register_blueprint(web)

# =========================================================
# Route utama untuk tes API
# =========================================================
@app.route("/")
def home():
    return {"message": "✅ Saving Goals API is running on Railway!"}

# =========================================================
# Jalankan server lokal
# =========================================================
if __name__ == "__main__":
    # host=0.0.0.0 → agar bisa diakses dari luar container Railway
    app.run(debug=True, host="0.0.0.0", port=5000)
