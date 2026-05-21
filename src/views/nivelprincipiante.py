import flet as ft

def NivelPrincipianteView(page: ft.Page, user, on_continuar):
    def continuar(e):
        on_continuar(user, "Aprendiz")

    return ft.Container(
        expand=True,
        bgcolor="#0a0a1a",
        content=ft.Stack(
            controls=[
                ft.Image(src="fondito.jpeg", fit="cover", expand=True),
                ft.Container(expand=True, bgcolor=ft.Colors.with_opacity(0.72, "#0a0a1a")),
                ft.Container(
                    expand=True,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text("✦ Viajero Recién Llegado ✦", size=11, color="#a0c4ff",
                                            text_align=ft.TextAlign.CENTER,
                                            weight=ft.FontWeight.W_500),
                                    ft.Text("¡Bienvenido a Teyvat!", size=30,
                                            weight=ft.FontWeight.BOLD, color="#e8d5a3",
                                            text_align=ft.TextAlign.CENTER),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=4,
                            ),
                            padding=ft.padding.only(top=10),
                        ),
                        ft.Container(
                            content=ft.Image(src="lynea.gif", width=180, height=180),
                            border_radius=90,
                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                            shadow=ft.BoxShadow(blur_radius=30, color="#4fc3f7", spread_radius=2),
                        ),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text(
                                        "Has elegido el camino del principiante.",
                                        size=15, color="#b0bec5",
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                    ft.Text(
                                        "Como todo gran viajero, comenzarás desde el principio.\n"
                                        "Aprenderás los fundamentos de Python paso a paso,\n"
                                        "guiado por los Arcontes de Teyvat. 🌿"
                                        "Realizarás un rápido test para confirmar \n"
                                        "tu rango entre los aventureros. ⚔️",
                                        size=13, color=ft.Colors.WHITE54,
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=8,
                            ),
                            bgcolor=ft.Colors.with_opacity(0.25, "#1a237e"),
                            border_radius=16,
                            padding=ft.padding.symmetric(horizontal=30, vertical=18),
                            border=ft.border.all(1, "#3949ab"),
                            width=420,
                        ),
                        ft.ElevatedButton(
                            content=ft.Row(
                                controls=[
                                    ft.Icon(ft.Icons.AUTO_AWESOME, color="#e8d5a3", size=18),
                                    ft.Text("¡Comenzar mi aventura!", size=16, color="#e8d5a3",
                                            weight=ft.FontWeight.BOLD),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=8,
                            ),
                            width=280, height=55,
                            bgcolor="#1a237e",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=12),
                                shadow_color="#4fc3f7",
                                elevation=8,
                            ),
                            on_click=continuar,
                        ),
                        ft.Text("— Primogems del conocimiento te esperan —",
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
