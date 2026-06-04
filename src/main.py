import os
import sys

# Aseguramos que el directorio src y la raíz del proyecto estén en sys.path.
sys.path.insert(0, os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

import flet as ft
from controllers.UserController import AuthController
from views.LoginView import LoginView
from views.Nivel import NivelView
from views.base import BaseView

ASSETS_DIR = os.path.join(ROOT_DIR, "base", "assest")


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

    def show_base(user):
        page.controls.clear()
        page.add(BaseView(page, user, auth_ctrl, on_logout=show_login, on_switch_account=show_login))
        page.update()

    def show_nivel(user, nivel):
        auth_ctrl.guardar_nivel(user["email"], nivel)
        user["nivel"] = nivel
        show_base(user)

    def on_login(user):
        page.controls.clear()
        if not user.get("nivel"):
            page.add(NivelView(page, user, on_nivel=show_nivel))
        else:
            show_base(user)
        page.update()

    def show_login():
        page.controls.clear()
        page.add(LoginView(page, auth_ctrl, on_login=on_login))

    show_login()


def main():
    ft.run(start, assets_dir=ASSETS_DIR)


if __name__ == "__main__":
    main()
