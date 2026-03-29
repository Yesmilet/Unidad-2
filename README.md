# Unidad 2: Componentes y Librerías

## Descripción General

En el desarrollo de software moderno, la organización, reutilización y mantenibilidad del código son aspectos fundamentales. En este contexto, los **componentes** y las **librerías** juegan un papel clave, ya que permiten estructurar aplicaciones de manera modular, facilitando su comprensión, escalabilidad y evolución.

La presente unidad aborda el estudio conceptual y práctico de estos elementos, analizando su importancia dentro de la ingeniería de software, así como su aplicación en el desarrollo de sistemas. Se exploran tanto las librerías proporcionadas por los lenguajes de programación como la creación de componentes y paquetes definidos por el usuario.

---

## Contenido de la Unidad

# 2.1 Definición conceptual de componentes y librerías

Un **componente** es una unidad modular de software que encapsula una funcionalidad específica, la cual puede ser utilizada de manera independiente o integrada dentro de un sistema más grande. Su principal objetivo es promover la reutilización y reducir la duplicidad de código.

Los componentes se caracterizan por tener:
- Una funcionalidad bien definida
- Bajo acoplamiento con otros componentes
- Alta cohesión interna
- Capacidad de reutilización

#### Tipos de componentes

-  **Componentes visuales**: Son aquellos que forman parte de la interfaz gráfica del usuario. Permiten la interacción directa con el sistema, como botones, menús, formularios y ventanas.
  
-  **Componentes no visuales**: Se encargan de la lógica interna del sistema, como el procesamiento de datos, validaciones, cálculos o comunicación con servicios externos.

Por otro lado, una **librería (o paquete)** es un conjunto organizado de funciones, clases y/o componentes que permiten ampliar las capacidades de un lenguaje de programación. Estas librerías pueden ser desarrolladas por los propios creadores del lenguaje o por terceros.

#### Importancia de los componentes y librerías

- Permiten dividir sistemas complejos en partes más simples
- Facilitan el mantenimiento y la actualización del software
- Promueven la reutilización del código
- Reducen tiempos de desarrollo
- Mejoran la calidad del software

---


Un **componente** es una unidad modular de software que encapsula tanto datos como comportamiento, permitiendo su reutilización dentro de un sistema. Estos elementos son fundamentales para estructurar aplicaciones complejas en partes más simples y organizadas.

Por otro lado, una **librería** es un conjunto de componentes y funcionalidades agrupadas que extienden las capacidades de un lenguaje de programación, facilitando el desarrollo de aplicaciones.

---

#### Relación entre teoría y práctica

El siguiente ejemplo muestra cómo se aplican estos conceptos mediante el uso de:

- Una **librería externa** (Flet)
- Un **modelo de datos** (`Usuario`)
- Un **componente visual** (`TarjetaPerfil`)

---

#### Código aplicado

```python
import flet as ft
from dataclasses import dataclass

@dataclass
class Usuario:
    nombre: str
    rol: str
    color_borde: str = ft.Colors.BLUE

class TarjetaPerfil(ft.Container):
    def __init__(self, data: Usuario):
        super().__init__()
        self.data = data
        
        self.padding = 10
        self.border_radius = 10
        self.border = ft.Border.all(2, self.data.color_borde)
        self.width = 250  
        
        self.content = ft.Column(
            controls=[
                ft.Text(self.data.nombre, weight=ft.FontWeight.BOLD, size=20),
                ft.Text(self.data.rol, italic=True),
                ft.Button("Ver Perfil", on_click=self.saludar)
            ],
            tight=True,
            horizontal_alignment=ft.CrossAxisAlignment.START
        )

    def saludar(self, e):
        print(f"Interactuando con: {self.data.nombre}")

def main(page: ft.Page):
    page.title = "Unidad 2: Data Class corregido"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    u1 = Usuario("Ana García", "Desarrolladora Senior", ft.Colors.GREEN)
    u2 = Usuario("Carlos Ruiz", "Arquitecto de Software", ft.Colors.BLUE)

    tarjetas = [TarjetaPerfil(u1), TarjetaPerfil(u2)]

    page.add(
        ft.Text("Lista de Usuarios (Data Class)", size=30, weight="bold"),
        ft.Row(
            tarjetas, 
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )

if __name__ == "__main__":
    
    try:
        ft.run(main)
    except AttributeError:
        ft.app(main)
```

---

#### Análisis conceptual del ejemplo

Este código permite identificar claramente los elementos teóricos del subtema:

##### Uso de librerías

- Se utiliza la librería **Flet** (`flet`) para la construcción de la interfaz gráfica.
- Se utiliza `dataclasses`, una librería estándar de Python, para definir estructuras de datos de forma sencilla.

Esto demuestra cómo las librerías proporcionan herramientas que facilitan el desarrollo.

---

##### Definición de componentes

- La clase `TarjetaPerfil` representa un **componente visual reutilizable**.
- Encapsula:
  - Datos (objeto `Usuario`)
  - Diseño (estructura visual)
  - Comportamiento (evento `saludar`)

Esto cumple con el principio de **encapsulación**, ya que todo está contenido en una sola unidad.

---

##### Modelo de datos (estructura lógica)

- La clase `Usuario` representa un **componente no visual**.
- Define atributos como nombre, rol y color.
- Permite separar la lógica de datos de la interfaz.

Esto refleja una buena práctica en ingeniería de software: separar datos y presentación.

---

##### Reutilización

- Se crean múltiples instancias (`u1`, `u2`) del mismo modelo.
- Se reutiliza el componente `TarjetaPerfil` para mostrar diferentes usuarios.

Esto demuestra cómo los componentes permiten evitar duplicación de código.

---

##### Modularidad

El programa está dividido en partes independientes:

- Datos → `Usuario`
- Interfaz → `TarjetaPerfil`
- Control → `main()`

Esto facilita:
- Mantenimiento
- Escalabilidad
- Comprensión del sistema

---

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/0de4b644-6ef0-43a2-867e-e4fbcb493e42" />


#### Conclusión del subtema

Este ejemplo demuestra que los componentes y librerías no solo son conceptos teóricos, sino herramientas prácticas que permiten construir sistemas organizados, reutilizables y eficientes. La correcta aplicación de estos principios mejora significativamente la calidad del software desarrollado.

### 2.2 Uso de librerías proporcionadas por el lenguaje

Los lenguajes de programación modernos incluyen librerías estándar que proporcionan soluciones a problemas comunes, evitando que el desarrollador tenga que implementar desde cero funcionalidades básicas.

Estas librerías suelen incluir herramientas para:
- Manejo de archivos
- Operaciones matemáticas
- Manipulación de texto
- Conexión a bases de datos
- Desarrollo de interfaces gráficas

El uso adecuado de estas librerías permite optimizar el proceso de desarrollo, ya que han sido previamente diseñadas, probadas y optimizadas por expertos.

#### Ventajas del uso de librerías estándar

- Incremento en la productividad
- Reducción de errores
- Código más claro y estructurado
- Mayor confiabilidad en las soluciones implementadas
- Estándares comunes entre desarrolladores

Además, el conocimiento de las librerías disponibles en un lenguaje es una habilidad esencial para cualquier programador, ya que permite aprovechar al máximo sus capacidades.

---

Los lenguajes de programación modernos incluyen una gran variedad de **librerías estándar y externas** que permiten resolver problemas comunes sin necesidad de implementar todo desde cero. Estas librerías proporcionan funciones, clases y herramientas que optimizan el desarrollo de aplicaciones.

El uso adecuado de estas librerías es fundamental, ya que permite a los desarrolladores enfocarse en la lógica del problema en lugar de reinventar soluciones ya existentes.

---

#### Aplicación práctica

El siguiente ejemplo muestra el uso de librerías en Python para desarrollar una aplicación web sencilla. En este caso, se emplea la librería **Flask**, que permite crear aplicaciones web de forma rápida y estructurada.

---

#### Código aplicado

```python
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
```

---

#### Análisis conceptual

##### Uso de librerías externas

- Se utiliza **Flask**, una librería externa que permite construir aplicaciones web.
- Flask proporciona herramientas como:
  - Creación de rutas (`@app.route`)
  - Manejo de solicitudes (`request`)
  - Renderizado de vistas (`render_template`)

Esto demuestra cómo una librería puede abstraer procesos complejos como la comunicación entre cliente y servidor.

---

##### Uso de librerías estándar

- Se utiliza la librería `random`, incluida en Python.
- Permite generar valores aleatorios, en este caso para simular la elección de la computadora.

Esto muestra cómo las librerías estándar complementan el desarrollo sin necesidad de dependencias externas.

---

##### Automatización de procesos

Gracias a Flask, el programa puede:

- Recibir datos desde un formulario web
- Procesar información del usuario
- Generar respuestas dinámicas
- Mostrar resultados en una interfaz

Todo esto sin necesidad de implementar manualmente protocolos de comunicación web.

---

##### Separación de responsabilidades

El sistema está dividido en diferentes niveles:

- **Entrada** → datos del usuario (`request`)
- **Procesamiento** → lógica del juego (`determinar_ganador`)
- **Salida** → interfaz (`render_template`)

Esta estructura es fundamental en el desarrollo de aplicaciones web.

---

##### Interacción cliente-servidor

El uso de Flask permite simular un entorno cliente-servidor donde:

- El usuario interactúa desde el navegador
- El servidor procesa la información
- Se devuelve una respuesta dinámica

Esto representa un modelo básico de aplicaciones web modernas.

---
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/6cabb914-5dda-497b-b378-a58e849b6d88" />

---
<img width="500" height="1500" alt="image" src="https://github.com/user-attachments/assets/64b55445-3883-4cc3-90ad-d2684c27a6bf" />

#### Conclusión del subtema

El uso de librerías proporcionadas por el lenguaje, tanto estándar como externas, es esencial para el desarrollo eficiente de software. Estas herramientas permiten simplificar tareas complejas, mejorar la organización del código y acelerar el proceso de desarrollo, siendo una base fundamental en la creación de aplicaciones modernas.

# 2.3 Creación de componentes definidos por el usuario

En muchos casos, las librerías existentes no cubren completamente las necesidades de un proyecto, por lo que es necesario desarrollar **componentes personalizados**.

La creación de componentes propios permite:
- Adaptar soluciones a problemas específicos
- Reutilizar lógica dentro del mismo proyecto
- Mantener una estructura ordenada del código
- Facilitar el trabajo colaborativo

#### Componentes no visuales

Estos componentes encapsulan lógica de negocio o funcionalidad específica, como operaciones matemáticas, validaciones o procesamiento de datos.

#### Componentes visuales

Son elementos gráficos diseñados por el usuario que pueden integrarse en interfaces. Su creación depende del lenguaje o framework utilizado, pero en todos los casos buscan mejorar la experiencia del usuario y la organización de la interfaz.

#### Buenas prácticas al crear componentes

- Definir claramente su funcionalidad
- Evitar dependencias innecesarias
- Documentar su uso
- Diseñar interfaces simples y claras
- Promover la reutilización

---
En este apartado se desarrolla la creación de componentes personalizados mediante el uso de un framework de interfaz gráfica. En este caso, se utiliza la librería **Flet**, la cual permite construir aplicaciones visuales de forma sencilla mediante componentes reutilizables.

#### Explicación del código

El código presentado tiene como objetivo definir e implementar un **componente visual personalizado**, demostrando cómo encapsular funcionalidad y diseño en una sola estructura reutilizable.

---

#### Importación de la librería

```python
import flet as ft
```

Se importa la librería **Flet**, que proporciona los elementos necesarios para crear interfaces gráficas. Se utiliza el alias `ft` para simplificar su uso a lo largo del código.

---

#### Definición del componente personalizado

```python
class TarjetaPerfil(ft.Container):
```

Se define una clase llamada `TarjetaPerfil`, la cual hereda de `ft.Container`.  
Esto indica que el componente creado será un contenedor visual que puede incluir otros elementos en su interior.

---

#### Constructor del componente

```python
def __init__(self, nombre, rol, color_borde=ft.Colors.BLUE):
```

El constructor permite inicializar el componente con ciertos parámetros:

- `nombre`: Nombre del usuario
- `rol`: Rol o profesión
- `color_borde`: Color del borde (opcional)

Esto permite que el componente sea **dinámico y reutilizable**, ya que puede adaptarse a diferentes datos.

---

#### Estructura interna del componente

```python
self.content = ft.Column(
    controls=[
        ft.Text(nombre, weight=ft.FontWeight.BOLD, size=20),
        ft.Text(rol, italic=True),
        ft.ElevatedButton("Ver Perfil", on_click=self.saludar)
    ],
    tight=True
)
```

Se define el contenido del componente utilizando una columna (`Column`) que organiza los elementos verticalmente:

- Un texto con el nombre (resaltado en negritas)
- Un texto con el rol (en cursiva)
- Un botón interactivo

El botón está vinculado al método `self.saludar`, lo que permite ejecutar una acción cuando el usuario interactúa.

---

#### Estilo del componente

```python
self.border = ft.Border.all(2, color_borde)
self.padding = 10
self.border_radius = 10
self.width = 200
```

Se aplican estilos visuales al componente:

- Borde con grosor y color configurable
- Espaciado interno (padding)
- Bordes redondeados
- Ancho fijo

Esto demuestra cómo un componente no solo encapsula lógica, sino también su apariencia.

---

####  Método de interacción

```python
def saludar(self, e):
    print(f"Interactuando con el componente de {self.content.controls[0].value}")
```

Este método se ejecuta cuando el usuario hace clic en el botón.  
Su función es mostrar un mensaje en consola indicando con qué componente se está interactuando.

Esto representa el **comportamiento interno del componente**, reforzando el concepto de encapsulación.

---

#### Función principal

```python
def main(page: ft.Page):
```

Define la interfaz principal de la aplicación, donde se integran los componentes creados.

---

#### Instanciación de componentes

```python
usuario1 = TarjetaPerfil("Ana García", "Desarrolladora Senior", ft.Colors.GREEN)
usuario2 = TarjetaPerfil("Carlos Ruiz", "Arquitecto de Software")
```

Se crean dos instancias del componente `TarjetaPerfil`, cada una con diferentes datos.  
Esto demuestra la reutilización del componente en distintos contextos.

---

#### Renderizado en pantalla

```python
page.add(
    ft.Text("Lista de Usuarios", size=30, weight="bold"),
    ft.Row([usuario1, usuario2], alignment=ft.MainAxisAlignment.CENTER)
)
```

Se agregan los componentes a la página:

- Un título
- Una fila (`Row`) que contiene las tarjetas de usuario

---

#### Ejecución de la aplicación

```python
if __name__ == "__main__":
    ft.app(target=main)
```

Este bloque inicia la aplicación, indicando que la función `main` será el punto de entrada.

---

#### Análisis conceptual

Este ejemplo demuestra claramente los principios de:

- **Encapsulación**: El componente agrupa datos, diseño y comportamiento.
- **Reutilización**: Puede instanciarse múltiples veces con diferentes valores.
- **Modularidad**: Permite dividir la interfaz en partes independientes.
- **Interactividad**: Responde a eventos del usuario (clics).

---

```python
import flet as ft

# Definición del componente personalizado (Subtema 2.3)

class TarjetaPerfil(ft.Container):
    def __init__(self, nombre, rol, color_borde=ft.Colors.BLUE):
        super().__init__()
        self.content = ft.Column(
            controls=[
                ft.Text(nombre, weight=ft.FontWeight.BOLD, size=20),
                ft.Text(rol, italic=True),
                # El botón busca la instrucción en self.saludar
                ft.ElevatedButton("Ver Perfil", on_click=self.saludar)
            ],
            tight=True
        )
        # Usamos ft.Border.all para evitar las advertencias que viste en consola
        ```python
        self.border = ft.Border.all(2, color_borde)
        self.padding = 10
        self.border_radius = 10
        self.width = 200

    # El flujo del programa salta a esta función al hacer clic
    def saludar(self, e):
        # Se ejecuta el print con los datos del componente
        print(f"Interactuando con el componente de {self.content.controls[0].value}")

def main(page: ft.Page):
    page.title = "Unidad 2: Componentes Definidos por el Usuario"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Instanciando nuestros componentes personalizados
    usuario1 = TarjetaPerfil("Ana García", "Desarrolladora Senior", ft.Colors.GREEN)
    usuario2 = TarjetaPerfil("Carlos Ruiz", "Arquitecto de Software")

    page.add(
        ft.Text("Lista de Usuarios", size=30, weight="bold"),
        ft.Row([usuario1, usuario2], alignment=ft.MainAxisAlignment.CENTER)
    )

if __name__ == "__main__":
    ft.app(target=main)
```
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/f065d6a1-6797-47d4-a3fc-693b55794ce5" />


# 2.4 Creación y uso de librerías definidas por el usuario

Una **librería definida por el usuario** es un conjunto de componentes creados con el propósito de ser reutilizados en uno o varios proyectos. Estas permiten organizar el código de manera más eficiente y facilitar su distribución.

#### Características de una librería propia

- Agrupa funcionalidades relacionadas
- Puede ser reutilizada en diferentes aplicaciones
- Facilita el mantenimiento del código
- Permite escalar proyectos de manera ordenada

#### Proceso general de creación

1. Identificar funcionalidades comunes
2. Agruparlas en módulos o archivos
3. Definir una estructura clara
4. Documentar su uso
5. Integrarla en distintos proyectos

#### Beneficios

- Reducción del tiempo de desarrollo
- Mayor consistencia en el código
- Facilidad para corregir errores en un solo lugar
- Mejor organización del proyecto


En el desarrollo de software, una práctica fundamental es la creación de **librerías propias**, las cuales permiten organizar el código en módulos reutilizables. Estas librerías agrupan componentes relacionados, facilitando su mantenimiento, escalabilidad y reutilización en distintos proyectos.

A diferencia de las librerías estándar, las librerías definidas por el usuario responden a necesidades específicas del sistema que se está desarrollando.

---

#### Aplicación práctica

El siguiente ejemplo muestra cómo se utiliza una **librería personalizada**, en este caso representada por el componente `ProductCard`, el cual es importado desde un archivo externo.

---

#### Código aplicado

```python
import flet as ft 
from product_card import ProductCard

productos = [
    {"id": 1, "nombre": "Laptop Gamer", "descripcion": "Ryzen 7 16GB RAM", "precio": 25000, "ruta_imagen": "laptopgamer.jpg"},
    {"id": 2, "nombre": "Mouse Gamer", "descripcion": "Mouse RGB", "precio": 350, "ruta_imagen": "mouse.jpg"},
    {"id": 3, "nombre": "Teclado Mecánico", "descripcion": "Switch blue RGB", "precio": 1200, "ruta_imagen": "teclado.jpg"},
    {"id": 4, "nombre": "Audifonos Gamer", "descripcion": "Sonido envolvente", "precio": 900, "ruta_imagen": "audifonosg.jpg"},
    {"id": 5, "nombre": "Televisión 32", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "televisor.jpg"},
    {"id": 6, "nombre": "Audifonos", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "audifonos.jpg"},
    {"id": 7, "nombre": "Cargador", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "cargador.jpg"},
    {"id": 8, "nombre": "Impresora", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "impresora.jpg"},
    {"id": 9, "nombre": "Tablet", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "tablet.jpg"},
    {"id": 10, "nombre": "Smartwatch", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "smartwatch.jpg"},
    {"id": 11, "nombre": "Laptop", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "laptop.jpg"},
    {"id": 12, "nombre": "Bocina", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "bocina.jpg"},
    {"id": 13, "nombre": "Multicontactos", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "multicontacto.jpg"},
    {"id": 14, "nombre": "Microfono", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "microfono.jpg"},
    {"id": 15, "nombre": "Router", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "router.jpg"},
]

def main(page: ft.Page):
    page.title = "TechStore"
    page.scroll = "auto"
    page.bgcolor = "#BFC8ED"
    page.padding = 30
    page.assets_dir = "assets"

    carrito = []
    favoritos = []
    
    carrito_text = ft.Text("0", size=16, weight="bold", color="#3742FA")
    favoritos_text = ft.Text("0", size=16, weight="bold", color="#FF6B81")
    
    def mostrar_mensaje(msg):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(msg, color="white"),
            bgcolor="#3742FA"
        )
        page.snack_bar.open = True
        page.update()
    
    def agregar_carrito(producto):
        carrito.append(producto)
        carrito_text.value = str(len(carrito))
        mostrar_mensaje(f"✓ {producto['nombre']} agregado al carrito")
        page.update()
    
    def agregar_favorito(producto):
        if producto not in favoritos:
            favoritos.append(producto)
        else:
            favoritos.remove(producto)
        favoritos_text.value = str(len(favoritos))
        page.update()

    header = ft.Container(
        content=ft.Row([
            ft.Column([
                ft.Text("TechStore", size=50, weight="bold"),
                ft.Text("Catálogo de productos tecnológicos", size=16)
            ]),
            ft.Row([
                ft.Container(
                    content=ft.Row([ft.Text("❤️"), favoritos_text])
                ),
                ft.Container(
                    content=ft.Row([ft.Text("🛒"), carrito_text])
                )
            ])
        ])
    )

    tarjetas = []
    for p in productos:
        card = ProductCard(
            p["nombre"],
            p["descripcion"],
            p["precio"],
            p["ruta_imagen"]
        )
        card.agregar = lambda e, prod=p: agregar_carrito(prod)
        tarjetas.append(card)

    grid = ft.Row(
        controls=tarjetas,
        wrap=True
    )

    page.add(header, grid)

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
```

---

#### Análisis conceptual

##### Uso de librerías definidas por el usuario

- Se importa `ProductCard` desde un archivo externo (`product_card.py`).
- Esto representa una **librería o módulo personalizado**, creado para encapsular la lógica y diseño de un producto.

Esto demuestra cómo un desarrollador puede crear sus propias herramientas reutilizables.

---

##### Modularidad del sistema

El sistema se divide en diferentes partes:

- **Datos** → lista `productos`
- **Componente externo** → `ProductCard`
- **Lógica de negocio** → funciones como `agregar_carrito` y `agregar_favorito`
- **Interfaz** → construcción de la página con Flet

Esta separación permite una mejor organización del código.

---

##### Reutilización de componentes

El componente `ProductCard` se reutiliza múltiples veces para mostrar distintos productos.  
Esto evita repetir código y facilita la expansión del sistema (por ejemplo, agregar más productos).

---

##### Manejo del estado

El programa implementa estructuras como:

- `carrito` → almacena productos agregados
- `favoritos` → controla productos marcados

Esto refleja el manejo de **estado de la aplicación**, fundamental en sistemas interactivos.

---

##### Interacción con el usuario

El sistema permite:

- Agregar productos al carrito
- Marcar favoritos
- Mostrar mensajes dinámicos

Esto evidencia el uso de eventos y lógica interactiva dentro de la aplicación.

---

#### Conclusión del subtema

La creación y uso de librerías definidas por el usuario permite construir sistemas más organizados, reutilizables y escalables. Este enfoque facilita la separación de responsabilidades dentro del software, mejorando su mantenimiento y permitiendo el desarrollo de aplicaciones más complejas de manera eficiente.

### Componente Reutilizable: `product_card.py`

##  Definición de clase

```python
class ProductCard(ft.Container):
```

Se crea un componente personalizado heredando de `Container`.

 Esto cumple el requisito de **herencia**.

---

##  Diseño del contenedor

```python
self.width = 260
self.padding = 15
self.border_radius = 12
self.bgcolor = "white"
```

* Tamaño fijo
* Bordes redondeados
* Fondo blanco

---

##  Sombra

```python
self.shadow = ft.BoxShadow(
    blur_radius=10,
    color="#dddddd",
    offset=ft.Offset(2, 4)
)
```

Da efecto moderno tipo tarjeta.

---

##  Imagen

```python
ft.Image(
    src=f"/{imagen}",
    width=230,
    height=150,
    fit="cover"
)
```

Carga imágenes desde `/assets`.

---

##  Textos

```python
ft.Text(nombre, size=18, weight="bold")
ft.Text(descripcion, size=13)
ft.Text(f"$ {precio}", color="#2ED573")
```

* Nombre en negritas
* Descripción pequeña
* Precio resaltado en verde

---

##  Botones

```python
ft.Row(
    controls=[
        ft.Text("❤️"),
        ft.Container(
            content=ft.Text("Agregar")
        )
    ]
)
```

* ❤️ Favorito (visual)
* 🛒 Botón agregar

---

##  Animación (Hover)

```python
self.on_hover = self.hover
```

```python
def hover(self, e):
    if e.data == "true":
        self.bgcolor = "#EEF1F5"
```

 Cambia color al pasar el mouse.

---

#  Estructura del Proyecto

```bash
PIntegrador/
│
├── main.py
├── product_card.py
├── assets/
│   ├── laptopgamer.jpg
│   ├── mouse.jpg
│   └── ...
```

---

#  Cómo ejecutar (Git Bash)

##  1. Ir al proyecto

```bash
cd C:\Users\lunaz\Downloads\TAP\PIntegrador
```

##  2. Ejecutar

```bash
python main.py
```

O en web:

```bash
flet run main.py --web
```
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/2bab4557-5018-469b-bf17-35726b8a5e5b" />

---

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/8492a4af-3606-4f6a-aece-8cfa42faff14" />


#  Build para Web

```bash
flet build web
```

<img width="1904" height="1012" alt="image" src="https://github.com/user-attachments/assets/bdad6bf8-28d0-415b-bf70-51600e547393" />


---


<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/d73b8d50-debe-473f-8835-3961dd9c5e24" />


graceful-crepe-82e897
# LINK DESPLIEGUE WEB
## https://graceful-crepe-82e897.netlify.app

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/806c8653-26d3-4e68-b5b6-21f70df50db9" />


---

#  Subir a GitHub

```bash
git init
git add .
git commit -m "Proyecto TechStore"
git branch -M main
git remote add origin https://github.com/tu-usuario/techstore.git
git push -u origin main
```

---

#  Conclusión

Este proyecto permitió:

* Aplicar herencia en componentes
* Crear interfaces reutilizables
* Manejar recursos (assets)
* Preparar una app escalable a futuro

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/bc84ac01-9a5a-4bf3-924e-eb9e46df83bc" />
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/e3381066-1efa-4bef-95a4-bfe69bb7ae27" />

---

## Ejecución del Proyecto

Para ejecutar los ejemplos incluidos en este repositorio, es necesario contar con un entorno de desarrollo configurado con el lenguaje correspondiente. Posteriormente, se pueden ejecutar los archivos desde la terminal o un entorno de desarrollo integrado (IDE).

---


## Conclusión

El uso de componentes y librerías representa una de las bases fundamentales del desarrollo de software moderno. Estos permiten construir aplicaciones más organizadas, eficientes y escalables, además de facilitar el mantenimiento y la reutilización del código.

Asimismo, la capacidad de crear componentes y librerías propias otorga al desarrollador un mayor control sobre sus proyectos, permitiendo adaptar soluciones a necesidades específicas y mejorar la calidad del software desarrollado.

---

## Autor

- Nombre: Hidalgo Flores Yesenia Milet
- Unidad: 2 - Componentes y Librerías
- Materia: Topicos Avanzados de Programación

---

## Bibliografías
UNIDAD 2 COMPONENTES y LIBRERIAS. (2019, 23 mayo). https://componentesylibreriasunit2.blogspot.com/2019/05/

Client challenge. (s. f.-h). https://es.slideshare.net/slideshow/componentes-y-libreras-tpicos-avanzados-de-programacin/35825047

Jk, J. (2016). Unidad III: Componentes y librerías Definición conceptual de componentes, paquetes/librerías. www.academia.edu. 

https://www.academia.edu/23849067/Unidad_III_Componentes_y_librer%C3%ADas_Definici%C3%B3n_conceptual_de_componentes_paquetes_librer%C3%ADas
