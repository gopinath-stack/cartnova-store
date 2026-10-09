import os
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_NAME = os.environ.get("DB_NAME", "shopflow")
DB_USER = os.environ.get("DB_USER", "shopflow")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")


def get_connection():
    return psycopg2.connect(
        host=DB_HOST, port=DB_PORT, dbname=DB_NAME,
        user=DB_USER, password=DB_PASSWORD,
    )


@app.after_request
def allow_frontend(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/api/products")
def products():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name, price FROM products ORDER BY id")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify([{"id": r[0], "name": r[1], "price": float(r[2])} for r in rows])
    except Exception as e:
        return jsonify(error=str(e)), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
