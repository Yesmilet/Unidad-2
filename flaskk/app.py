from flask import Flask, render_template, request
import random

app = Flask(__name__)

opciones = ["Piedra", "Papel", "Tijeras"]

iconos = {
    "Piedra": "✊",
    "Papel": "✋",
    "Tijeras": "✌️"
}

puntos = {"jugador": 0, "cpu": 0}

def determinar_ganador(jugador, cpu):
    if jugador == cpu:
        return "Empate"
    elif (
        (jugador == "Piedra" and cpu == "Tijeras") or
        (jugador == "Papel" and cpu == "Piedra") or
        (jugador == "Tijeras" and cpu == "Papel")
    ):
        return "Ganaste"
    else:
        return "Perdiste"

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    cpu = ""
    jugador = ""
    nombre = ""

    global puntos

    if request.method == "POST":
        nombre = request.form.get("nombre")
        jugador = request.form.get("opcion")

        if jugador:
            cpu = random.choice(opciones)
            resultado = determinar_ganador(jugador, cpu)

            if resultado == "Ganaste":
                puntos["jugador"] += 1
            elif resultado == "Perdiste":
                puntos["cpu"] += 1

    return render_template(
        "index.html",
        resultado=resultado,
        cpu=cpu,
        jugador=jugador,
        iconos=iconos,
        puntos=puntos,
        nombre=nombre
    )

if __name__ == "__main__":
    app.run(debug=True)