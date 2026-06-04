import flet as ft

def NivelExperimentadoView(page: ft.Page, user, on_continuar):
    def continuar(e):
        on_continuar(user, "Experimentado")

    w = page.window.width or 800
    h = page.window.height or 600
    bg = ft.Image(src="fondito.jpeg", fit="cover", width=w, height=h)
    overlay = ft.Container(bgcolor=ft.Colors.with_opacity(0.72, "#1a0a2e"), width=w, height=h)

    def on_resize(e):
        nw = page.window.width or 800
        nh = page.window.height or 600
        bg.width, bg.height = nw, nh
        overlay.width, overlay.height = nw, nh
        page.update()
    page.on_resized = on_resize

    return ft.Container(
        expand=True,
        bgcolor="#0a0a1a",
        content=ft.Stack(
            controls=[
                bg,
                overlay,
                ft.Container(
                    expand=True,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text("✦ Experimentado de Teyvat ✦", size=11, color="#ce93d8",
                                            text_align=ft.TextAlign.CENTER,
                                            weight=ft.FontWeight.W_500),
                                    ft.Text("¡Bienvenido, viajero/a de Teyvat!", size=30,
                                            weight=ft.FontWeight.BOLD, color="#e8d5a3",
                                            text_align=ft.TextAlign.CENTER),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=4,
                            ),
                            padding=ft.Padding.only(top=10),
                        ),
                        ft.Container(
                            content=ft.Image(src="lynea.gif", width=180, height=180),
                            border_radius=90,
                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                            shadow=ft.BoxShadow(blur_radius=30, color="#ab47bc", spread_radius=2),
                        ),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text(
                                        "Has elegido el camino del Experimentado.",
                                        size=15, color="#b0bec5",
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                    ft.Text(
                                        "Ya conoces el mundo de Teyvat, pero aún hay secretos\n"
                                        "por descubrir. Realizarás un rápido test para confirmar\n"
                                        "tu rango entre los aventureros. ⚔️",
                                        size=13, color=ft.Colors.WHITE54,
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=8,
                            ),
                            bgcolor=ft.Colors.with_opacity(0.25, "#4a148c"),
                            border_radius=16,
                            padding=ft.Padding.symmetric(horizontal=30, vertical=18),
                            border=ft.Border.all(1, "#7b1fa2"),
                            width=420,
                        ),
                        ft.ElevatedButton(
                            content=ft.Row(
                                controls=[
                                    ft.Icon(ft.Icons.SHIELD, color="#e8d5a3", size=18),
                                    ft.Text("¡Demostrar mi valía!", size=16, color="#e8d5a3",
                                            weight=ft.FontWeight.BOLD),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=8,
                            ),
                            width=280, height=55,
                            bgcolor="#4a148c",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=12),
                                shadow_color="#ab47bc",
                                elevation=8,
                            ),
                            on_click=continuar,
                        ),
                        ft.Text("— El Consejo de los Archons te observa —",
                                size=11, color=ft.Colors.WHITE24,
                                text_align=ft.TextAlign.CENTER),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=22,
                    tight=True,
                ),
                ),
            ],
            expand=True,
        ),
    )
