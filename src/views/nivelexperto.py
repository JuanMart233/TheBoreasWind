import flet as ft

def NivelExpertoView(page: ft.Page, user, on_continuar):
    def continuar(e):
        on_continuar(user, "Experto")

    w = page.window.width or 800
    h = page.window.height or 600
    bg = ft.Image(src="fondito.jpeg", fit="cover", width=w, height=h)
    overlay = ft.Container(bgcolor=ft.Colors.with_opacity(0.72, "#1a0000"), width=w, height=h)

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
                                    ft.Text("✦ Tryhard de Teyvat ✦", size=11, color="#ef9a9a",
                                            text_align=ft.TextAlign.CENTER,
                                            weight=ft.FontWeight.W_500),
                                    ft.Text("¡Bienvenido, aventurero de Teyvat!", size=30,
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
                            shadow=ft.BoxShadow(blur_radius=30, color="#e53935", spread_radius=2),
                        ),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text(
                                        "Has elegido el camino del Experto.",
                                        size=15, color="#b0bec5",
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                    ft.Text(
                                        "Eres un Tryhard del meta?. Tu dominio podra ser bueno\n"
                                        "Pero siempre podras mejorar mas\n"
                                        "El abismos, el teatro y la confragacion esperan por ti. 🔥"
                                        "Realizarás un rápido test para confirmar \n"
                                        "tu rango entre los aventureros. ⚔️",
                                        size=13, color=ft.Colors.WHITE54,
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=8,
                            ),
                            bgcolor=ft.Colors.with_opacity(0.25, "#7f0000"),
                            border_radius=16,
                            padding=ft.Padding.symmetric(horizontal=30, vertical=18),
                            border=ft.Border.all(1, "#c62828"),
                            width=420,
                        ),
                        ft.ElevatedButton(
                            content=ft.Row(
                                controls=[
                                    ft.Icon(ft.Icons.WHATSHOT, color="#e8d5a3", size=18),
                                    ft.Text("¡Enfrentar el Abismo!", size=16, color="#e8d5a3",
                                            weight=ft.FontWeight.BOLD),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=8,
                            ),
                            width=280, height=55,
                            bgcolor="#7f0000",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=12),
                                shadow_color="#e53935",
                                elevation=8,
                            ),
                            on_click=continuar,
                        ),
                        ft.Text("— El poder de los Arcontes fluye en ti —",
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
