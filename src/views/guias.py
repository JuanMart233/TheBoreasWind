import flet as ft


def GuiasView(page: ft.Page, user: dict, on_volver_guias=None):
    elementos = [
        {"nombre": "Pyro",    "imagen": "pyro.webp",    "modulo": "views.pyros",   "vista": "PyroView"},
        {"nombre": "Cryo",    "imagen": "cryo.webp",    "modulo": "views.cryos",   "vista": "CryoView"},
        {"nombre": "Dendro",  "imagen": "dendro.webp",  "modulo": "views.dendros", "vista": "DendroView"},
        {"nombre": "Anemo",   "imagen": "anemo.webp",   "modulo": "views.anemos",  "vista": "AnemoView"},
        {"nombre": "Electro", "imagen": "electro.webp", "modulo": "views.electro", "vista": "ElectroView"},
        {"nombre": "Geo",     "imagen": "geo.webp",     "modulo": "views.geos",    "vista": "GeoView"},
        {"nombre": "Hydro",   "imagen": "hydro.webp",   "modulo": "views.hydro",   "vista": "HydroView"},
    ]

    # Contenedor donde se inyecta la pantalla del elemento
    detalle = ft.Container(expand=True, visible=False)

    def abrir_elemento(modulo_str, vista_str):
        import importlib
        mod = importlib.import_module(modulo_str)
        vista_fn = getattr(mod, vista_str)
        detalle.content = vista_fn(page, user, on_volver=volver_a_grid)
        detalle.visible = True
        grid_view.visible = False
        page.update()

    def volver_a_grid():
        detalle.visible = False
        detalle.content = None
        grid_view.visible = True
        page.update()

    def cubito(el):
        return ft.Container(
            width=100,
            height=120,
            border_radius=14,
            bgcolor="#1e0a3c",
            border=ft.Border.all(1, "#4c1d95"),
            ink=True,
            on_click=lambda e, m=el["modulo"], v=el["vista"]: abrir_elemento(m, v),
            content=ft.Column(
                spacing=6,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Image(src=el["imagen"], width=56, height=56, fit="contain"),
                    ft.Text(el["nombre"], size=13, color="#e9d5ff", weight=ft.FontWeight.W_600),
                ],
            ),
        )

    topbar = ft.Container(
        bgcolor="#12002e",
        padding=ft.Padding.symmetric(horizontal=16, vertical=10),
        content=ft.Row(
            controls=[
                ft.Icon(ft.Icons.MENU_BOOK, color="#c084fc"),
                ft.Text("Guías", size=18, weight=ft.FontWeight.BOLD, color="#e9d5ff"),
            ],
            spacing=10,
        ),
    )

    cubitos = [cubito(el) for el in elementos]
    filas = []
    for i in range(0, len(cubitos) - 1, 2):
        filas.append(ft.Row(
            controls=[cubitos[i], cubitos[i + 1]],
            spacing=14,
            alignment=ft.MainAxisAlignment.CENTER,
        ))
    if len(cubitos) % 2 != 0:
        filas.append(ft.Row(
            controls=[cubitos[-1]],
            alignment=ft.MainAxisAlignment.CENTER,
        ))

    grid_view = ft.Container(
        expand=True,
        bgcolor="#0d001f",
        padding=20,
        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Elementos", size=16, color="#c084fc", weight=ft.FontWeight.BOLD),
                *filas,
            ],
            spacing=14,
        ),
    )

    return ft.Column(
        spacing=0,
        expand=True,
        controls=[
            topbar,
            ft.Stack(expand=True, controls=[grid_view, detalle]),
        ],
    )
