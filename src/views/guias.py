import flet as ft


def GuiasView(user: dict):
    topbar = ft.Container(
        bgcolor="#12002e",
        padding=ft.padding.symmetric(horizontal=16, vertical=10),
        content=ft.Row(
            controls=[
                ft.Icon(ft.Icons.MENU_BOOK, color="#c084fc"),
                ft.Text("Guías", size=18, weight=ft.FontWeight.BOLD, color="#e9d5ff"),
            ],
            spacing=10,
        ),
    )

    Textito = ft.Container(
        expand=True,
        bgcolor="#0d001f",
        content=ft.Text("📖 Próximamente: guías de Teyvat", size=18, color="#c084fc"),
        alignment=ft.Alignment(0, 0),
    )

    return ft.Column(
        spacing=0,
        expand=True,
        controls=[topbar, Textito],
    )
