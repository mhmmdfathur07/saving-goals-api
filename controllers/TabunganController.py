from flask import jsonify, request
from config.database import get_db
from models.tabungan_model import Tabungan
from sqlalchemy.orm import Session

# ===============================================================
# GET SEMUA DATA TABUNGAN
# ===============================================================
def get_all_tabungan():
    db: Session = next(get_db())
    data = db.query(Tabungan).all()
    result = []
    for t in data:
        result.append({
            "id_tabungan": t.id_tabungan,
            "nama_tabungan": t.nama_tabungan,
            "deskripsi": t.deskripsi,
            "target": int(t.target) if t.target is not None else 0,
            "saldo": int(t.saldo) if t.saldo is not None else 0,
            "created_at": t.created_at.strftime("%Y-%m-%d %H:%M:%S") if t.created_at else None,
            "updated_at": t.updated_at.strftime("%Y-%m-%d %H:%M:%S") if t.updated_at else None
        })
    return jsonify(result)

# ===============================================================
# GET DATA TABUNGAN BY ID
# ===============================================================
def get_tabungan_by_id(id_tabungan):
    db: Session = next(get_db())
    data = db.query(Tabungan).filter(Tabungan.id_tabungan == id_tabungan).first()
    if not data:
        return jsonify({"message": "Data tidak ditemukan"}), 404
    return jsonify({
        "id_tabungan": data.id_tabungan,
        "nama_tabungan": data.nama_tabungan,
        "deskripsi": data.deskripsi,
        "target": int(data.target) if data.target is not None else 0,
        "saldo": int(data.saldo) if data.saldo is not None else 0,
        "created_at": data.created_at.strftime("%Y-%m-%d %H:%M:%S") if data.created_at else None,
        "updated_at": data.updated_at.strftime("%Y-%m-%d %H:%M:%S") if data.updated_at else None
    })

# ===============================================================
# POST (TAMBAH DATA TABUNGAN)
# ===============================================================
def add_tabungan():
    db: Session = next(get_db())
    body = request.json or {}

    # Validasi sederhana
    if "nama_tabungan" not in body:
        return jsonify({"message": "Field 'nama_tabungan' wajib diisi"}), 400

    new_data = Tabungan(
        nama_tabungan=body["nama_tabungan"],
        deskripsi=body.get("deskripsi", ""),
        target=int(body.get("target", 0)),
        saldo=int(body.get("saldo", 0))
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return jsonify({
        "message": "Data berhasil ditambahkan",
        "id_tabungan": new_data.id_tabungan
    }), 201

# ===============================================================
# PUT (UPDATE DATA TABUNGAN)
# ===============================================================
def update_tabungan(id_tabungan):
    db: Session = next(get_db())
    body = request.json or {}

    data = db.query(Tabungan).filter(Tabungan.id_tabungan == id_tabungan).first()
    if not data:
        return jsonify({"message": "Data tidak ditemukan"}), 404

    # Update hanya field yang dikirim oleh client
    if "nama_tabungan" in body:
        data.nama_tabungan = body["nama_tabungan"]
    if "deskripsi" in body:
        data.deskripsi = body["deskripsi"]
    if "target" in body:
        data.target = int(body["target"])
    if "saldo" in body:
        data.saldo = int(body["saldo"])

    db.commit()
    db.refresh(data)

    return jsonify({"message": "Data berhasil diperbarui"})

# ===============================================================
# DELETE DATA TABUNGAN
# ===============================================================
def delete_tabungan(id_tabungan):
    db: Session = next(get_db())
    data = db.query(Tabungan).filter(Tabungan.id_tabungan == id_tabungan).first()
    if not data:
        return jsonify({"message": "Data tidak ditemukan"}), 404
    db.delete(data)
    db.commit()
    return jsonify({"message": "Data berhasil dihapus"})
