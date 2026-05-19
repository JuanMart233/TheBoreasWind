import flet as ft

def NivelView(page: ft.Page, user, on_nivel):
    def seleccionar(nivel):
        on_nivel(user, nivel)

    return ft.Container(
        expand=True,
        bgcolor="#0a0a1a",
        content=ft.Column(
            controls=[
                ft.Text("¿Cuál es tu nivel de experiencia?", size=28, weight=ft.FontWeight.BOLD, color="white", text_align=ft.TextAlign.CENTER),
                ft.Text("Elige una opción para continuar", size=16, color=ft.Colors.WHITE54, text_align=ft.TextAlign.CENTER),
                ft.Container(height=20),
                ft.Image(src="lynea.gif", width=200, height=200),
                ft.ElevatedButton(
                    "🌱 Aprendiz",
                    width=280,
                    height=60,
                    bgcolor="#1565C0",
                    color="white",
                    style=ft.ButtonStyle(text_style=ft.TextStyle(size=18)),
                    on_click=lambda e: seleccionar("Aprendiz"),
                ),
                ft.ElevatedButton(
                    "⚔️ Experimentado",
                    width=280,
                    height=60,
                    bgcolor="#6A1B9A",
                    color="white",
                    style=ft.ButtonStyle(text_style=ft.TextStyle(size=18)),
                    on_click=lambda e: seleccionar("Experimentado"),
                ),
                ft.ElevatedButton(
                    "🔥 Experto",
                    width=280,
                    height=60,
                    bgcolor="#B71C1C",
                    color="white",
                    style=ft.ButtonStyle(text_style=ft.TextStyle(size=18)),
                    on_click=lambda e: seleccionar("Experto"),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            expand=True,
        ),
    )
