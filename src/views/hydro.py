import flet as ft


def HydroView(page: ft.Page, user: dict, on_volver=None):
    def volver(e):
        if on_volver:
            on_volver()

    return ft.Column(
        spacing=0,
        expand=True,
        controls=[
            ft.Container(
                bgcolor="#12002e",
                padding=ft.padding.symmetric(horizontal=16, vertical=10),
                content=ft.Row(controls=[
                    ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#c084fc", on_click=volver),
                    ft.Text("Hydro", size=18, weight=ft.FontWeight.BOLD, color="#38bdf8"),
                ], spacing=8),
            ),
            ft.Container(
                expand=True,
                bgcolor="#0d001f",
                alignment=ft.Alignment(0, 0),
                content=ft.Text("💧 Guía de Hydro — Próximamente", size=18, color="#38bdf8"),
            ),
        ],
    )
