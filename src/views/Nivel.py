import flet as ft
from views.nivelprincipiante import NivelPrincipianteView
from views.nivelexperimentado import NivelExperimentadoView
from views.nivelexperto import NivelExpertoView
from views.TestView import TestView

def NivelView(page: ft.Page, user, on_nivel):
    COLORES = {
        "Aprendiz":      {"bg": "#1a237e", "glow": "#4fc3f7", "emoji": "🌱"},
        "Experimentado": {"bg": "#4a148c", "glow": "#ab47bc", "emoji": "⚔️"},
        "Experto":       {"bg": "#7f0000", "glow": "#e53935", "emoji": "🔥"},
    }

    def ir_a_vista(nivel):
        page.controls.clear()
        if nivel == "Aprendiz":
            page.add(NivelPrincipianteView(page, user, on_continuar=lambda u, n: ir_al_test(u)))
        elif nivel == "Experimentado":
            page.add(NivelExperimentadoView(page, user, on_continuar=lambda u, n: ir_al_test(u)))
        elif nivel == "Experto":
            page.add(NivelExpertoView(page, user, on_continuar=lambda u, n: ir_al_test(u)))
        page.update()

    def ir_al_test(u):
        page.controls.clear()
        page.add(TestView(page, u, on_resultado=on_nivel))
        page.update()

    def mostrar_dialogo(nivel):
        c = COLORES[nivel]
        dlg = ft.AlertDialog(
            modal=True,
            bgcolor="#0d0d1f",
            shape=ft.RoundedRectangleBorder(radius=16),
            title=ft.Row(
                controls=[
                    ft.Text(c["emoji"], size=22),
                    ft.Text(f"Confirmar nivel", size=18, weight=ft.FontWeight.BOLD,
                            color="#e8d5a3"),
                ],
                spacing=8,
            ),
            content=ft.Column(
                controls=[
                    ft.Divider(color=c["glow"], height=1),
                    ft.Text(
                        f"¿Estás seguro de que deseas continuar como\n"
                        f"{c['emoji']} {nivel}?",
                        size=14, color=ft.Colors.WHITE70,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Text(
                        "Esta elección definirá tu camino en Teyvat.",
                        size=12, color=ft.Colors.WHITE38,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ],
                spacing=10,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
            ),
            actions=[
                ft.TextButton(
                    "Cancelar",
                    style=ft.ButtonStyle(color=ft.Colors.WHITE54),
                    on_click=lambda e: cerrar_dialogo(dlg),
                ),
                ft.ElevatedButton(
                    "¡Confirmar!",
                    bgcolor=c["bg"],
                    color="#e8d5a3",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                        shadow_color=c["glow"],
                        elevation=6,
                    ),
                    on_click=lambda e, n=nivel: confirmar(dlg, n),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.overlay.append(dlg)
        dlg.open = True
        page.update()

    def cerrar_dialogo(dlg):
        dlg.open = False
        page.update()

    def confirmar(dlg, nivel):
        dlg.open = False
        page.update()
        ir_a_vista(nivel)

    def mostrar_confirmacion(nivel):
        mostrar_dialogo(nivel)

    return ft.Container(
        expand=True,
        content=ft.Stack(
            controls=[
                ft.Image(src="fondito.jpeg", fit="cover", expand=True),
                ft.Container(expand=True, bgcolor=ft.Colors.with_opacity(0.75, "#0a0a1a")),
                ft.Container(
                    expand=True,
                    alignment=ft.Alignment(0, 0),
                    content=ft.Column(
                    controls=[
                        ft.Text("✦ Elige tu Rango de Aventurero ✦", size=11, color="#a0c4ff",
                                text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.W_500),
                        ft.Text("¿Cuál es tu nivel de experiencia?", size=28,
                                weight=ft.FontWeight.BOLD, color="#e8d5a3",
                                text_align=ft.TextAlign.CENTER),
                        ft.Text("El camino que elijas definirá tu aventura en Teyvat",
                                size=14, color=ft.Colors.WHITE54,
                                text_align=ft.TextAlign.CENTER),
                        ft.Container(
                            content=ft.Image(src="lynea.gif", width=260, height=260),
                            border_radius=130,
                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                            shadow=ft.BoxShadow(blur_radius=25, color="#4fc3f7", spread_radius=1),
                        ),
                        ft.ElevatedButton(
                            content=ft.Row(
                                controls=[
                                    ft.Text("🌱", size=20),
                                    ft.Column(
                                        controls=[
                                            ft.Text("Rango de aventura 1-25", size=17, color="#e8d5a3",
                                                    weight=ft.FontWeight.BOLD),
                                            ft.Text("Nuevo en el mundo de Teyvat", size=11,
                                                    color="#90caf9"),
                                        ],
                                        spacing=2,
                                        horizontal_alignment=ft.CrossAxisAlignment.START,
                                    ),
                                ],
                                spacing=12,
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            width=300, height=65,
                            bgcolor="#1a237e",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=12),
                                shadow_color="#4fc3f7",
                                elevation=6,
                            ),
                            on_click=lambda e: mostrar_confirmacion("Aprendiz"),
                        ),
                        ft.ElevatedButton(
                            content=ft.Row(
                                controls=[
                                    ft.Text("⚔️", size=20),
                                    ft.Column(
                                        controls=[
                                            ft.Text("Rango de aventura 26-50", size=17, color="#e8d5a3",
                                                    weight=ft.FontWeight.BOLD),
                                            ft.Text("Conoces los fundamentos de Teyvat", size=11,
                                                    color="#ce93d8"),
                                        ],
                                        spacing=2,
                                        horizontal_alignment=ft.CrossAxisAlignment.START,
                                    ),
                                ],
                                spacing=12,
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            width=300, height=65,
                            bgcolor="#4a148c",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=12),
                                shadow_color="#ab47bc",
                                elevation=6,
                            ),
                            on_click=lambda e: mostrar_confirmacion("Experimentado"),
                        ),
                        ft.ElevatedButton(
                            content=ft.Row(
                                controls=[
                                    ft.Text("🔥", size=20),
                                    ft.Column(
                                        controls=[
                                            ft.Text("Rango de aventura 51-60", size=17, color="#e8d5a3",
                                                    weight=ft.FontWeight.BOLD),
                                            ft.Text("Eres un experto de Teyvat", size=11,
                                                    color="#ef9a9a"),
                                        ],
                                        spacing=2,
                                        horizontal_alignment=ft.CrossAxisAlignment.START,
                                    ),
                                ],
                                spacing=12,
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            width=300, height=65,
                            bgcolor="#7f0000",
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=12),
                                shadow_color="#e53935",
                                elevation=6,
                            ),
                            on_click=lambda e: mostrar_confirmacion("Experto"),
                        ),
                        ft.Text("— La Guía del Viento te acompaña —",
                                size=11, color=ft.Colors.WHITE24,
                                text_align=ft.TextAlign.CENTER),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=18,
                    tight=True,
                ),
                ),
            ],
            expand=True,
        ),
    )
