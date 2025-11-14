from flask import jsonify, request
from config.database import with_session
from models.tabungan_model import Tabungan

# ===============================================================
# GET SEMUA DATA TABUNGAN
# ===============================================================
def get_all_tabungan():
    with with_session() as db:
        data = db.query(Tabungan).all()
        result = [
            {
                "id_tabungan": t.id_tabungan,
                "nama_tabungan": t.nama_tabungan,
                "deskripsi": t.deskripsi,
                "target": int(t.target or 0),
                "saldo": int(t.saldo or 0),
                "created_at": t.created_at.strftime("%Y-%m-%d %H:%M:%S") if t.created_at else None,
                "updated_at": t.updated_at.strftime("%Y-%m-%d %H:%M:%S") if t.updated_at else None,
            }
            for t in data
        ]
        return jsonify(result)

# ===============================================================
# GET BY ID
# ===============================================================
def get_tabungan_by_id(id_tabungan):
    with with_session() as db:
        data = db.query(Tabungan).filter(Tabungan.id_tabungan == id_tabungan).first()
        if not data:
            return jsonify({"message": "Data tidak ditemukan"}), 404
        return jsonify({
            "id_tabungan": data.id_tabungan,
            "nama_tabungan": data.nama_tabungan,
            "deskripsi": data.deskripsi,
            "target": int(data.target or 0),
            "saldo": int(data.saldo or 0),
            "created_at": data.created_at.strftime("%Y-%m-%d %H:%M:%S") if data.created_at else None,
            "updated_at": data.updated_at.strftime("%Y-%m-%d %H:%M:%S") if data.updated_at else None,
        })

# ===============================================================
# POST
# ===============================================================
def add_tabungan():
    body = request.json or {}
    if "nama_tabungan" not in body:
        return jsonify({"message": "Field 'nama_tabungan' wajib diisi"}), 400

    with with_session() as db:
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
# PUT
# ===============================================================
def update_tabungan(id_tabungan):
    body = request.json or {}
    with with_session() as db:
        data = db.query(Tabungan).filter(Tabungan.id_tabungan == id_tabungan).first()
        if not data:
            return jsonify({"message": "Data tidak ditemukan"}), 404

        for field in ["nama_tabungan", "deskripsi", "target", "saldo"]:
            if field in body:
                setattr(data, field, body[field])

        db.commit()
        return jsonify({"message": "Data berhasil diperbarui"})

# ===============================================================
# DELETE
# ===============================================================
def delete_tabungan(id_tabungan):
    with with_session() as db:
        data = db.query(Tabungan).filter(Tabungan.id_tabungan == id_tabungan).first()
        if not data:
            return jsonify({"message": "Data tidak ditemukan"}), 404
        db.delete(data)
        db.commit()
        return jsonify({"message": "Data berhasil dihapus"})
