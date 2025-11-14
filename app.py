from flask import Flask
from flask_cors import CORS
from config.database import engine, Base
from routes.web import web
import models.tabungan_model

app = Flask(__name__)

# ✅ Aktifkan CORS untuk semua route dan semua origin
CORS(app, resources={r"/*": {"origins": "*"}})

# ✅ Buat tabel jika belum ada
Base.metadata.create_all(bind=engine)

# ✅ Daftarkan blueprint
app.register_blueprint(web)

@app.route("/")
def home():
    return {"message": "Saving Goals API is running"}

if __name__ == "__main__":
    # Gunakan host 0.0.0.0 agar bisa diakses dari luar (misalnya Railway)
    app.run(debug=True, host="0.0.0.0", port=5000)
