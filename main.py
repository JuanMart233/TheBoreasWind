import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

import flet as ft
from controllers.UserController import AuthController
from views.LoginView import LoginView
from views.Nivel import NivelView

def start(page: ft.Page):
    page.padding = 0

    def on_resize(e):
        page.update()
    page.on_resized = on_resize
    try:
        auth_ctrl = AuthController()
    except Exception as e:
        page.add(ft.Text(f"Error BD: {e}", color=ft.Colors.RED))
        return

    def show_nivel(user, nivel):
        auth_ctrl.guardar_nivel(user["email"], nivel)
        page.controls.clear()
        page.add(ft.Text(f"¡Bienvenido, {user['nombre']}! Nivel: {nivel}", color="#e8d5a3", size=22))
        page.update()

    def on_login(user):
        page.controls.clear()
        if not user.get("nivel"):
            page.add(NivelView(page, user, on_nivel=show_nivel))
        else:
            page.add(ft.Text(f"Bienvenido de nuevo, {user['nombre']}", color="#e8d5a3", size=22))
        page.update()

    def show_login():
        page.controls.clear()
        page.add(LoginView(page, auth_ctrl, on_login=on_login))

    show_login()

ft.run(start, assets_dir="base/assest")
