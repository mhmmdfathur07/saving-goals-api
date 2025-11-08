from flask import Blueprint
from controllers.TabunganController import (
    get_all_tabungan,
    get_tabungan_by_id,
    add_tabungan,
    update_tabungan,
    delete_tabungan
)

web = Blueprint("web", __name__)

# Endpoint API
web.route("/api/tabungan", methods=["GET"])(get_all_tabungan)
web.route("/api/tabungan/<int:id_tabungan>", methods=["GET"])(get_tabungan_by_id)
web.route("/api/tabungan", methods=["POST"])(add_tabungan)
web.route("/api/tabungan/<int:id_tabungan>", methods=["PUT"])(update_tabungan)
web.route("/api/tabungan/<int:id_tabungan>", methods=["DELETE"])(delete_tabungan)
