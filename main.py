<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Piedra Papel Tijeras PRO</title>

<style>
body {
    background: #0f172a;
    color: white;
    font-family: Arial;
    text-align: center;
    margin-top: 40px;
}

h1 {
    font-size: 28px;
}

input {
    padding: 10px;
    border-radius: 8px;
    border: none;
    margin: 10px;
}

button {
    padding: 15px;
    margin: 10px;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    font-size: 16px;
}

.btn {
    width: 100px;
    height: 100px;
}

.piedra { background: #3b82f6; }
.papel { background: #22c55e; }
.tijera { background: #ef4444; }

#resultado {
    font-size: 24px;
    margin-top: 20px;
    font-weight: bold;
}

#marcador {
    margin-top: 20px;
    font-size: 18px;
}
</style>

</head>
<body>

<h1>🪨 Piedra, Papel o Tijeras</h1>

<input type="text" id="nombre" placeholder="Ingresa tu nombre">
<br>
<button onclick="iniciar()">Iniciar</button>

<p id="jugador"></p>

<h3>Elige tu opción:</h3>

<button class="btn piedra" onclick="jugar('Piedra')">✊<br>Piedra</button>
<button class="btn papel" onclick="jugar('Papel')">✋<br>Papel</button>
<button class="btn tijera" onclick="jugar('Tijeras')">✌️<br>Tijeras</button>

<p id="eleccion"></p>
<p id="cpu"></p>
<p id="resultado"></p>
<p id="marcador">Tu: 0 | CPU: 0</p>

<script>
let puntosJugador = 0;
let puntosCPU = 0;

const opciones = ["Piedra", "Papel", "Tijeras"];

function iniciar() {
    let nombre = document.getElementById("nombre").value;
    if (nombre === "") {
        document.getElementById("jugador").innerText = "⚠️ Escribe tu nombre";
    } else {
        document.getElementById("jugador").innerText = "Jugador: " + nombre;
    }
}

function jugar(eleccion) {
    let cpu = opciones[Math.floor(Math.random() * 3)];

    document.getElementById("eleccion").innerText = 
        "Tú: " + eleccion;

    document.getElementById("cpu").innerText = 
        "CPU: " + cpu;

    let resultado = "";

    if (eleccion === cpu) {
        resultado = "Empate";
    } else if (
        (eleccion === "Piedra" && cpu === "Tijeras") ||
        (eleccion === "Papel" && cpu === "Piedra") ||
        (eleccion === "Tijeras" && cpu === "Papel")
    ) {
        resultado = "Ganaste";
        puntosJugador++;
    } else {
        resultado = "Perdiste";
        puntosCPU++;
    }

    document.getElementById("resultado").innerText = resultado;

    document.getElementById("marcador").innerText =
        "Tu: " + puntosJugador + " | CPU: " + puntosCPU;
}
</script>

</body>
</html>