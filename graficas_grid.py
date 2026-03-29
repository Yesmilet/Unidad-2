import matplotlib.pyplot as plt
import flet as ft
import flet_charts as fch
import random # Para simular datos de sensores

# --- FUNCIONES DE GRÁFICAS ---

def generar_grafica_barras():
    productos = ["A", "B", "C", "D"]
    ventas = [15, 30, 45, 10]
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.bar(productos, ventas, color="skyblue")
    ax.set_title("Ventas por Producto", fontsize=10, weight='bold')
    plt.tight_layout()
    return fig

def generar_grafica_lineas():
    meses = ["Ene", "Feb", "Mar", "Abr", "May"]
    rendimiento = [10, 25, 18, 40, 35]
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.plot(meses, rendimiento, color="orange", marker='o', linewidth=2)
    ax.set_title("Tendencia de Rendimiento", fontsize=10, weight='bold')
    ax.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    return fig

def generar_grafica_dispersion():
    # Simulando 20 lecturas de un sensor (Unidad 4.3: Manipulación)
    x = [i for i in range(20)]
    y = [random.randint(10, 50) for _ in range(20)]

    fig, ax = plt.subplots(figsize=(4, 3))
    # Dibujamos los puntos (Scatter)
    ax.scatter(x, y, color="purple", alpha=0.6, edgecolors="white")
    ax.set_title("Muestreo de Sensores", fontsize=10, weight='bold')

    plt.tight_layout()
    return fig

def main(page: ft.Page):
    page.title = "Dashboard TAP - Gráfica 3"
    page.theme_mode = "light"
    page.vertical_alignment = "start"
    page.horizontal_alignment = "center"

    header = ft.Text("Dashboard de Visualización - Paso 3: Dispersión", size=24, weight="bold")

    tablero = ft.GridView(
        expand=True,
        runs_count=2,
        spacing=20,
        run_spacing=20,
        child_aspect_ratio=1.5,
    )

    # --- ESPACIO 1: BARRAS ---
    fig_1 = generar_grafica_barras()
    contenedor_1 = ft.Container(content=fch.MatplotlibChart(figure=fig_1), border=ft.border.all(1, "black12"), border_radius=10, padding=5)
    plt.close(fig_1)

    # --- ESPACIO 2: LÍNEAS ---
    fig_2 = generar_grafica_lineas()
    contenedor_2 = ft.Container(content=fch.MatplotlibChart(figure=fig_2), border=ft.border.all(1, "black12"), border_radius=10, padding=5)
    plt.close(fig_2)

    # --- ESPACIO 3: DISPERSIÓN (NUEVA) ---
    fig_3 = generar_grafica_dispersion()
    contenedor_3 = ft.Container(
        content=fch.MatplotlibChart(figure=fig_3),
        border=ft.border.all(1, "black12"),
        border_radius=10,
        padding=5
    )
    plt.close(fig_3)

    # --- ESPACIO 4: SIGUE VACÍO ---
    espacio_4 = ft.Container(
        content=ft.Text("Próximamente: Gráfica 4", color="grey"),
        bgcolor="#f9f9f9",
        border=ft.border.all(1, "black12"),
        border_radius=10,
        alignment=None
    )

    # Cargamos los controles al tablero
    tablero.controls.append(contenedor_1)
    tablero.controls.append(contenedor_2)
    tablero.controls.append(contenedor_3)
    tablero.controls.append(espacio_4)

    page.add(header, ft.Divider(), tablero)

if __name__ == "__main__":
    ft.app(target=main)