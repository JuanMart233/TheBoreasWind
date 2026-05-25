import flet as ft


def BaseView(page: ft.Page, user: dict, auth_ctrl, on_logout, on_switch_account):
    from views.guias import GuiasView
    from views.perfil import PerfilView

    # --- avatar navbar (se pasa a PerfilView para actualizarlo) ---
    avatar_mini_foto = ft.Image(
        src=user.get("foto") or "",
        width=28, height=28, border_radius=14,
        fit="cover",
        visible=bool(user.get("foto")),
    )
    avatar_mini_letra = ft.Text(
        user.get("nombre", "?")[0].upper(),
        size=13, weight=ft.FontWeight.BOLD,
        color="white", text_align=ft.TextAlign.CENTER,
        visible=not bool(user.get("foto")),
    )
    avatar_mini = ft.Container(
        width=28, height=28, border_radius=14,
        bgcolor="#7c3aed",
        alignment=ft.Alignment(0, 0),
        content=ft.Stack(controls=[avatar_mini_foto, avatar_mini_letra]),
    )
    perfil_label = ft.Text("Perfil", size=10, color="#6b7280")

    # --- avatar drawer ---
    drawer_foto = ft.Image(
        src=user.get("foto") or "",
        width=48, height=48, border_radius=24,
        fit="cover",
        visible=bool(user.get("foto")),
    )
    drawer_letra = ft.Text(
        user.get("nombre", "?")[0].upper(),
        size=22, weight=ft.FontWeight.BOLD,
        color="white", text_align=ft.TextAlign.CENTER,
        visible=not bool(user.get("foto")),
    )
    avatar_drawer = ft.Container(
        width=48, height=48, border_radius=24,
        bgcolor="#7c3aed",
        alignment=ft.Alignment(0, 0),
        content=ft.Stack(controls=[drawer_foto, drawer_letra]),
    )

    def on_foto_actualizada(nueva_foto):
        tiene = bool(nueva_foto)
        avatar_mini_foto.src = nueva_foto or ""
        avatar_mini_foto.visible = tiene
        avatar_mini_letra.visible = not tiene
        drawer_foto.src = nueva_foto or ""
        drawer_foto.visible = tiene
        drawer_letra.visible = not tiene
        avatar_mini.update()
        avatar_drawer.update()

    # --- contenidos de cada pantalla ---
    inicio_content = _InicioContent(user, on_logout, on_switch_account, avatar_drawer)
    guias_content  = GuiasView(user)
    perfil_content = PerfilView(page, user, auth_ctrl, on_logout, on_switch_account, avatar_mini, avatar_mini_foto, avatar_mini_letra, on_foto_actualizada)

    pantallas = {
        "inicio": inicio_content,
        "guias":  guias_content,
        "perfil": perfil_content,
    }

    def mostrar(destino):
        for key, ctrl in pantallas.items():
            ctrl.visible = (key == destino)
        _actualizar_navbar(destino)
        page.update()

    # --- navbar ---
    def _btn(icon, label, key):
        col = ft.Column(
            controls=[
                ft.Icon(icon, size=26),
                ft.Text(label, size=10),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=2,
        )
        return ft.Container(
            expand=True,
            content=col,
            alignment=ft.Alignment(0, 0),
            on_click=lambda e, k=key: mostrar(k),
            padding=ft.padding.symmetric(vertical=8),
            data=key,
        )

    perfil_btn = ft.Container(
        expand=True,
        content=ft.Column(
            controls=[avatar_mini, perfil_label],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=2,
        ),
        alignment=ft.Alignment(0, 0),
        on_click=lambda e: mostrar("perfil"),
        padding=ft.padding.symmetric(vertical=8),
        ink=True,
    )

    btn_inicio = _btn(ft.Icons.HOME, "Inicio", "inicio")
    btn_guias  = _btn(ft.Icons.MENU_BOOK, "Guías", "guias")

    def _actualizar_navbar(active):
        for btn in [btn_inicio, btn_guias]:
            key = btn.data
            is_active = key == active
            col = btn.content
            col.controls[0].color = "#a855f7" if is_active else "#6b7280"
            col.controls[1].color = "#a855f7" if is_active else "#6b7280"
        is_perfil = active == "perfil"
        avatar_mini.bgcolor = "#a855f7" if is_perfil else "#7c3aed"
        perfil_label.color  = "#a855f7" if is_perfil else "#6b7280"

    navbar = ft.Container(
        bgcolor="#12002e",
        border=ft.border.only(top=ft.BorderSide(1, "#2d1b4e")),
        content=ft.Row(
            controls=[btn_inicio, btn_guias, perfil_btn],
            spacing=0,
        ),
    )

    # estado inicial
    mostrar("inicio")

    return ft.Column(
        spacing=0,
        expand=True,
        controls=[
            ft.Stack(
                expand=True,
                controls=list(pantallas.values()),
            ),
            navbar,
        ],
    )


def _InicioContent(user, on_logout, on_switch_account, avatar_drawer):

    drawer_panel = ft.Container(
        visible=False,
        width=220,
        bgcolor="#1e0a3c",
        border_radius=ft.BorderRadius(0, 0, 12, 0),
        padding=ft.padding.only(top=16, bottom=16),
        content=ft.Column(
            spacing=0,
            controls=[
                ft.Container(
                    padding=ft.padding.symmetric(horizontal=16, vertical=12),
                    content=ft.Row(
                        spacing=12,
                        controls=[
                            avatar_drawer,
                            ft.Text(user.get("nombre", "Usuario"), size=15,
                                    weight=ft.FontWeight.W_600, color="#e9d5ff"),
                        ],
                    ),
                ),
                ft.Divider(color="#4c1d95", height=1),
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON, color="#c084fc"),
                    title=ft.Text("Perfil", color="#e9d5ff"),
                    on_click=lambda e: None,
                ),
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.SWAP_HORIZ, color="#a78bfa"),
                    title=ft.Text("Cambiar de cuenta", color="#e9d5ff"),
                    on_click=lambda e: on_switch_account(),
                ),
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.LOGOUT, color="#f87171"),
                    title=ft.Text("Cerrar sesión", color="#e9d5ff"),
                    on_click=lambda e: on_logout(),
                ),
            ],
        ),
    )

    def toggle_drawer(e):
        drawer_panel.visible = not drawer_panel.visible
        drawer_panel.page.update()

    topbar = ft.Container(
        bgcolor="#12002e",
        padding=ft.padding.symmetric(horizontal=16, vertical=10),
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.Icons.MENU, icon_color="#c084fc", on_click=toggle_drawer),
                ft.Text("BoreasWind", size=18, weight=ft.FontWeight.BOLD, color="#e9d5ff"),
            ],
        ),
    )

    content_area = ft.Container(
        expand=True,
        bgcolor="#0d001f",
        content=ft.Text(
            f"¡Bienvenido, {user.get('nombre', 'Usuario')}!",
            size=22, color="#c084fc",
        ),
        alignment=ft.Alignment(0, 0),
    )

    return ft.Column(
        spacing=0,
        expand=True,
        controls=[
            topbar,
            ft.Row(
                spacing=0,
                expand=True,
                controls=[drawer_panel, content_area],
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
        ],
    )
