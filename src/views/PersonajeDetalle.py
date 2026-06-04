import flet as ft


def img(src, w=60, h=60):
    return ft.Image(src=src or "placeholder.png", width=w, height=h, fit="contain",
                    error_content=ft.Container(width=w, height=h, bgcolor="#2a1a4e", border_radius=8))


def img_label(src, label, w=70, h=70):
    return ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=4,
        controls=[
            ft.Text(label, size=11, color="#c084fc"),
            img(src, w, h),
        ],
    )


def seccion(titulo, contenido):
    return ft.Container(
        width=420,
        bgcolor="#1a0a3c",
        border_radius=12,
        border=ft.Border.all(1, "#4c1d95"),
        padding=ft.Padding.symmetric(horizontal=14, vertical=10),
        content=ft.Column(
            spacing=8,
            controls=[
                ft.Text(titulo, size=13, color="#c084fc", weight=ft.FontWeight.BOLD),
                contenido,
            ],
        ),
    )


def fila_imgs(srcs, labels=None):
    controls = []
    for i, src in enumerate(srcs):
        lbl = labels[i] if labels else None
        if lbl:
            controls.append(img_label(src, lbl))
        else:
            controls.append(img(src))
    return ft.Row(controls=controls, spacing=10, alignment=ft.MainAxisAlignment.CENTER)


def PersonajeDetalle(page: ft.Page, personaje: dict, on_volver):
    """
    personaje = {
        "nombre": str,
        "imagen": str,
        "region": str,
        "elemento": str,
        "reacciones": str,
        "talentos": str,
        "estadisticas": str,
        "artefactos": ["img1", "img2", "img3"],
        "equipos": [  # 3 columnas x 4 imágenes
            ["img","img","img","img"],
            ["img","img","img","img"],
            ["img","img","img","img"],
        ],
        "armas5": ["img","img","img"],
        "armas4": ["img","img","img"],
        "extra3": [("img","text"),("img","text"),("img","text")],
        "extra2": [("img","text"),("img","text")],
    }
    """
    p = personaje

    # --- Cabecera: imagen + nombre ---
    cabecera = ft.Row(
        controls=[
            img(p.get("imagen"), 80, 80),
            ft.Column(
                spacing=4,
                controls=[
                    ft.Text(p.get("nombre", ""), size=22, weight=ft.FontWeight.BOLD, color="#e9d5ff"),
                    ft.Row(spacing=8, controls=[
                        ft.Text(f"🗺 {p.get('region', 'text')}  rol: {p.get('rol', '')}", size=12, color="#a0c4ff"),
                        ft.Text(f"✦ {p.get('elemento', 'text')}", size=12, color="#c084fc"),
                    ]),
                ],
            ),
        ],
        spacing=16,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # --- Reacciones ---
    reacciones = ft.Text(p.get("reacciones", "text"), size=12, color="#e0e0e0")

    # --- Talentos y estadísticas ---
    talentos = ft.Text(p.get("talentos", "text") + "\n" + p.get("estadisticas", "text"),
                       size=12, color="#e0e0e0")

    # --- Artefactos: 3 imágenes en fila ---
    artefactos_imgs = fila_imgs(p.get("artefactos", ["", "", ""]))

    # --- Mejores equipos: 3 filas x 4 imágenes, scrolleable ---
    cols_equipos = p.get("equipos", [[""] * 4, [""] * 4, [""] * 4])
    filas_equipos = [
        ft.Row(
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[img(s, 55, 55) for s in fila],
        )
        for fila in cols_equipos
    ]
    equipos_scroll = ft.Container(
        width=420,
        height=260,
        bgcolor="#120030",
        border_radius=10,
        border=ft.Border.all(1, "#4c1d95"),
        padding=10,
        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,
            spacing=8,
            controls=filas_equipos,
        ),
    )

    # --- Armas 5★ ---
    armas5_imgs = fila_imgs(p.get("armas5", ["", "", ""]))

    # --- Armas 4★ ---
    armas4_imgs = fila_imgs(p.get("armas4", ["", "", ""]))

    # --- Extra 3 imágenes con texto ---
    extra3 = p.get("extra3", [])
    if extra3:
        extra3_row = ft.Row(
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[img_label(s, t) for s, t in extra3],
        )

    # --- Extra 2 imágenes con texto ---
    extra2 = p.get("extra2", [])
    if extra2:
        extra2_row = ft.Row(
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[img_label(s, t) for s, t in extra2],
        )

    contenido = ft.Column(
        scroll=ft.ScrollMode.AUTO,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=12,
        controls=[
            cabecera,
            ft.Divider(color="#4c1d95", height=1),
            seccion("Reacciones principales", reacciones),
            seccion("Talentos y estadísticas", talentos),
            seccion("Artefactos", artefactos_imgs),
            ft.Container(
                width=420,
                content=ft.Column(spacing=6, controls=[
                    ft.Text("Mejores equipos", size=13, color="#c084fc", weight=ft.FontWeight.BOLD),
                    equipos_scroll,
                ]),
            ),
            seccion("Armas 5 estrellas ⭐", armas5_imgs),
            seccion("Armas 4 estrellas ⭐", armas4_imgs),
            *([seccion("text", extra3_row)] if extra3 else []),
            *([seccion("text", extra2_row)] if extra2 else []),
            ft.Container(height=20),
        ],
    )

    return ft.Column(
        spacing=0,
        expand=True,
        controls=[
            ft.Container(
                bgcolor="#12002e",
                padding=ft.Padding.symmetric(horizontal=16, vertical=10),
                content=ft.Row(controls=[
                    ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#c084fc",
                                  on_click=lambda e: on_volver()),
                    ft.Text(p.get("nombre", ""), size=18,
                            weight=ft.FontWeight.BOLD, color="#e9d5ff"),
                ], spacing=8),
            ),
            ft.Container(
                expand=True,
                bgcolor="#0d001f",
                padding=ft.Padding.symmetric(horizontal=16, vertical=12),
                content=contenido,
            ),
        ],
    )
