# -*- coding: utf-8 -*-
"""Servidor Flask mínimo del sistema de la Guía 5: sirve el tablero HTML y el JSON del pronóstico.
Uso: pip install flask; python 26.11.12.06_Servidor_Flask_Tablero.py
(en la misma carpeta que el HTML y el JSON) y abrir http://127.0.0.1:5000"""
import json
import os
from flask import Flask, jsonify, send_file

AQUI = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)


@app.route("/")
def tablero():
    return send_file(os.path.join(AQUI, "08_Tablero_Pronostico_SPY_30_sesiones.html"))


@app.route("/api/dashboard")
def api_dashboard():
    with open(os.path.join(AQUI, "dashboard_regresion_spy.json"), encoding="utf-8") as f:
        return jsonify(json.load(f))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
