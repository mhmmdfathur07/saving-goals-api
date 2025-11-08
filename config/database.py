from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

# ============================================================
# KONFIGURASI DATABASE RAILWAY
# ============================================================
# Ganti URL ini sesuai database Railway kamu (gunakan PUBLIC URL)
DATABASE_URL = "postgresql://postgres:jernqksJptfFDenntwFLVvmYXkCxtnkW@ballast.proxy.rlwy.net:10405/railway"

# ============================================================
# SETUP ENGINE & SESSION
# ============================================================
# Engine: penghubung antara SQLAlchemy dan PostgreSQL
engine = create_engine(DATABASE_URL, echo=True)

# Session: objek untuk melakukan query
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base: class dasar untuk semua model ORM
Base = declarative_base()

# ============================================================
# FUNGSI DEPENDENCY UNTUK SESSION
# ============================================================
def get_db():
    """Dependency untuk membuat sesi database per request Flask."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ============================================================
# OPSIONAL: CEK KONEKSI OTOMATIS SAAT STARTUP
# ============================================================
try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT NOW();"))
        print("✅ Database connected successfully at:", result.scalar())
except SQLAlchemyError as e:
    print("❌ Database connection failed:", str(e))
