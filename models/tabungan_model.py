from sqlalchemy import Column, Integer, String, DateTime, func
from config.database import Base

class Tabungan(Base):
    __tablename__ = "tabungan"

    id_tabungan = Column(Integer, primary_key=True, index=True)
    nama_tabungan = Column(String(100), nullable=False)
    deskripsi = Column(String(255), nullable=True)

    # Railway kadang tidak mendukung NUMERIC/DECIMAL, jadi kita pakai INTEGER
    # untuk menyimpan nilai uang dalam satuan rupiah (tanpa desimal)
    target = Column(Integer, nullable=False, default=0)
    saldo = Column(Integer, nullable=False, default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
