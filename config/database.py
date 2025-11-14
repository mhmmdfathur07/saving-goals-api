from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError, OperationalError
import time

# ============================================================
# KONFIGURASI DATABASE RAILWAY
# ============================================================
DATABASE_URL = "postgresql://postgres:jernqksJptfFDenntwFLVvmYXkCxtnkW@ballast.proxy.rlwy.net:10405/railway"

# ============================================================
# SETUP ENGINE & SESSION
# ============================================================
# Opsi penting:
# - pool_pre_ping=True  → auto cek koneksi sebelum query (hindari broken pipe)
# - pool_recycle=1800   → ganti koneksi setiap 30 menit (hindari idle timeout)
# - pool_size=5 & max_overflow=10 → atur pool kecil tapi fleksibel
engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
    pool_recycle=1800,
    pool_size=5,
    max_overflow=10,
)

# Session & Base setup
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
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
# CEK KONEKSI OTOMATIS DENGAN RETRY (ANTISLEEP MODE)
# ============================================================
def test_connection(retries=5, delay=5):
    """Coba koneksi ke database dengan retry jika gagal."""
    for attempt in range(1, retries + 1):
        try:
            with engine.connect() as conn:
                result = conn.execute(text("SELECT NOW();"))
                print(f"✅ Database connected successfully at: {result.scalar()}")
                return
        except OperationalError as e:
            print(f"⚠️ Attempt {attempt} failed: {e}")
            if attempt < retries:
                print(f"🔁 Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print("❌ Database connection failed after multiple attempts.")
                

        # ============================================================
# CONTEXT MANAGER UNTUK SESSION AMAN
# ============================================================
from contextlib import contextmanager

@contextmanager
def with_session():
    """Context manager untuk aman membuka & menutup sesi database."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Jalankan saat startup
test_connection()

