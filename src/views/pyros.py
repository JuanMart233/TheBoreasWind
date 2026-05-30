import flet as ft
from views.PersonajeDetalle import PersonajeDetalle

PERSONAJES = [
    {"nombre": "Arlecchino",  "imagen": "arlee.jpg", "region": "Fontaine", "rol": "", "elemento": "Pyro", "reacciones": "Derretidos y sobrecarga", "talentos": "Basicos > ulti > elemental", "estadisticas": "2k de ataque, 80% probabilidad critica, 200 daño critico", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 2",  "imagen": "", "region": "text", "rol": "", "elemento": "Pyro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 3",  "imagen": "", "region": "text", "rol": "", "elemento": "Pyro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 4",  "imagen": "", "region": "text", "rol": "", "elemento": "Pyro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 5",  "imagen": "", "region": "text", "rol": "", "elemento": "Pyro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 6",  "imagen": "", "region": "text", "rol": "", "elemento": "Pyro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 7",  "imagen": "", "region": "text", "rol": "", "elemento": "Pyro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 8",  "imagen": "", "region": "text", "rol": "", "elemento": "Pyro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 9",  "imagen": "", "region": "text", "rol": "", "elemento": "Pyro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 10", "imagen": "", "region": "text", "rol": "", "elemento": "Pyro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 11", "imagen": "", "region": "text", "rol": "", "elemento": "Pyro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 12", "imagen": "", "region": "text", "rol": "", "elemento": "Pyro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 13", "imagen": "", "region": "text", "rol": "", "elemento": "Pyro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 14", "imagen": "", "region": "text", "rol": "", "elemento": "Pyro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 15", "imagen": "", "region": "text", "rol": "", "elemento": "Pyro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 16", "imagen": "", "region": "text", "rol": "", "elemento": "Pyro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 17", "imagen": "", "region": "text", "rol": "", "elemento": "Pyro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 18", "imagen": "", "region": "text", "rol": "", "elemento": "Pyro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
]


def PyroView(page: ft.Page, user: dict, on_volver=None):
    return _ElementoView(page, user, on_volver, "Pyro", "#ef4444", PERSONAJES)


def _ElementoView(page, user, on_volver, titulo, color, personajes):
    detalle = ft.Container(expand=True, visible=False)

    def abrir(p):
        detalle.content = PersonajeDetalle(page, p, on_volver=volver_grid)
        detalle.visible = True
        grid_view.visible = False
        page.update()

    def volver_grid():
        detalle.visible = False
        detalle.content = None
        grid_view.visible = True
        page.update()

    def cubito(p):
        return ft.Container(
            width=100, height=120,
            border_radius=14,
            bgcolor="#1e0a3c",
            border=ft.border.all(1, "#4c1d95"),
            ink=True,
            on_click=lambda e, per=p: abrir(per),
            content=ft.Column(
                spacing=6,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Image(src=p.get("imagen") or "placeholder.png", width=56, height=56, fit="contain",
                             error_content=ft.Container(width=56, height=56, bgcolor="#2a1a4e", border_radius=8)),
                    ft.Text(p["nombre"], size=11, color="#e9d5ff", weight=ft.FontWeight.W_600,
                            text_align=ft.TextAlign.CENTER),
                ],
            ),
        )

    cubitos = [cubito(p) for p in personajes]
    filas = []
    for i in range(0, len(cubitos) - 1, 2):
        filas.append(ft.Row(controls=[cubitos[i], cubitos[i + 1]], spacing=14,
                            alignment=ft.MainAxisAlignment.CENTER))
    if len(cubitos) % 2 != 0:
        filas.append(ft.Row(controls=[cubitos[-1]], alignment=ft.MainAxisAlignment.CENTER))

    grid_view = ft.Container(
        expand=True,
        bgcolor="#0d001f",
        padding=20,
        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=14,
            controls=[
                ft.Text(f"Personajes {titulo}", size=16, color=color, weight=ft.FontWeight.BOLD),
                *filas,
            ],
        ),
    )

    topbar = ft.Container(
        bgcolor="#12002e",
        padding=ft.padding.symmetric(horizontal=16, vertical=10),
        content=ft.Row(controls=[
            ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#c084fc",
                          on_click=lambda e: on_volver() if on_volver else None),
            ft.Text(titulo, size=18, weight=ft.FontWeight.BOLD, color=color),
        ], spacing=8),
    )

    return ft.Column(
        spacing=0, expand=True,
        controls=[topbar, ft.Stack(expand=True, controls=[grid_view, detalle])],
    )
