import flet as ft
from views.MisPublicaciones import MisPublicacionesView


def _censurar_email(email):
    partes = email.split("@")
    if len(partes) != 2:
        return email
    usuario, dominio = partes
    if len(usuario) <= 2:
        return f"{'*' * len(usuario)}@{dominio}"
    return f"{usuario[0]}{'*' * (len(usuario) - 2)}{usuario[-1]}@{dominio}"


def PerfilView(page: ft.Page, user: dict, auth_ctrl, on_logout, on_switch_account, avatar_mini, avatar_mini_foto, avatar_mini_letra, on_foto_actualizada):

    rutaFoto = {"value": user.get("foto") or ""}
    codigoMandado = {"value": False}
    
    # Container para la vista de mis publicaciones
    mis_publicaciones_container = ft.Container(visible=False, expand=True)

    # --- avatar ---
    fotoImg = ft.Image(
        src=rutaFoto["value"] if rutaFoto["value"] else None,
        width=90, height=90, border_radius=45,
        fit="cover",
        visible=bool(rutaFoto["value"]),
    )
    letraInicial = ft.Text(
        user.get("nombre", "?")[0].upper(),
        size=38, weight=ft.FontWeight.BOLD,
        color="white", text_align=ft.TextAlign.CENTER,
        visible=not bool(rutaFoto["value"]),
    )
    circuloAvatar = ft.Container(
        width=90, height=90, border_radius=45,
        bgcolor="#7c3aed",
        alignment=ft.Alignment(0, 0),
        content=ft.Stack(controls=[fotoImg, letraInicial]),
    )
    nombreTexto = ft.Text(
        user.get("nombre", "Usuario"),
        size=20, weight=ft.FontWeight.BOLD, color="#e9d5ff",
    )

    # ===================== PANEL INICIO =====================
    panelInicio = ft.Column(
        visible=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=16,
        controls=[
            ft.Container(height=10),
            circuloAvatar,
            nombreTexto,
            ft.Text(_censurar_email(user.get("email", "")), size=13, color="#a78bfa"),
            ft.Container(
                bgcolor="#1e0a3c",
                border_radius=10,
                padding=ft.padding.symmetric(horizontal=20, vertical=10),
                border=ft.border.all(1, "#4c1d95"),
                content=ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.STAR, color="#a855f7", size=16),
                        ft.Text(f"Nivel: {user.get('nivel', 'Sin nivel')}", size=14, color="#e9d5ff"),
                    ],
                    spacing=8,
                ),
            ),
            ft.Container(height=4),
            ft.ElevatedButton(
                "Mis Publicaciones",
                icon=ft.Icons.ARTICLE,
                bgcolor="#3b0764", color="#e9d5ff", width=280,
                on_click=lambda e: mostrar_mis_publicaciones(),
            ),
            ft.ElevatedButton(
                "Editar perfil",
                icon=ft.Icons.EDIT,
                bgcolor="#3b0764", color="#e9d5ff", width=280,
                on_click=lambda e: mostrarPanel("editar"),
            ),
            ft.ElevatedButton(
                "Cambiar contraseña",
                icon=ft.Icons.LOCK_RESET,
                bgcolor="#3b0764", color="#e9d5ff", width=280,
                on_click=lambda e: mostrarPanel("contra"),
            ),
            ft.Divider(color="#2d1b4e"),
            ft.ElevatedButton(
                "Cerrar sesión",
                icon=ft.Icons.LOGOUT,
                bgcolor="#1e0a3c", color="#f87171", width=280,
                on_click=lambda e: on_logout(),
            ),
            ft.ElevatedButton(
                "Cambiar de cuenta",
                icon=ft.Icons.SWAP_HORIZ,
                bgcolor="#1e0a3c", color="#a78bfa", width=280,
                on_click=lambda e: on_switch_account(),
            ),
        ],
    )

    # ===================== PANEL EDITAR =====================
    cajaNombre = ft.TextField(
        value=user.get("nombre", ""),
        label="Nombre",
        prefix_icon=ft.Icons.PERSON,
        width=300, border_radius=10,
        border_color="#7c3aed", focused_border_color="#a855f7",
        label_style=ft.TextStyle(color="#c084fc"),
        color="white", bgcolor="#2d1b4e",
    )
    cajaUrlFoto = ft.TextField(
        value=rutaFoto["value"],
        label="URL de foto de perfil",
        hint_text="https://...",
        prefix_icon=ft.Icons.IMAGE,
        width=300, border_radius=10,
        border_color="#7c3aed", focused_border_color="#a855f7",
        label_style=ft.TextStyle(color="#c084fc"),
        hint_style=ft.TextStyle(color="#4b3a6b"),
        color="white", bgcolor="#2d1b4e",
    )
    avisoGuardado = ft.Text("", size=13, text_align=ft.TextAlign.CENTER)

    def previsualizarFoto(e):
        url = cajaUrlFoto.value.strip()
        if url:
            rutaFoto["value"] = url
            fotoImg.src = url
            fotoImg.visible = True
            letraInicial.visible = False
        else:
            rutaFoto["value"] = ""
            fotoImg.visible = False
            letraInicial.visible = True
        fotoImg.update()
        letraInicial.update()

    def guardarCambios(e):
        previsualizarFoto(e)
        ok, txt = auth_ctrl.actualizar_perfil(
            user["email"], cajaNombre.value, rutaFoto["value"]
        )
        if ok:
            user["nombre"] = cajaNombre.value
            user["foto"] = rutaFoto["value"]
            nombreTexto.value = cajaNombre.value
            nombreTexto.update()
            on_foto_actualizada(rutaFoto["value"])
        avisoGuardado.value = txt
        avisoGuardado.color = "#86efac" if ok else "#f87171"
        avisoGuardado.update()

    panelEditar = ft.Column(
        visible=False,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=16,
        controls=[
            ft.Container(height=4),
            ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.ARROW_BACK, icon_color="#c084fc",
                        on_click=lambda e: mostrarPanel("inicio"),
                    ),
                    ft.Text("Editar perfil", size=17, weight=ft.FontWeight.BOLD, color="#e9d5ff"),
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            circuloAvatar,
            cajaNombre,
            cajaUrlFoto,
            ft.ElevatedButton(
                "Previsualizar foto",
                icon=ft.Icons.VISIBILITY,
                bgcolor="#2d1b4e", color="#c084fc", width=300,
                on_click=previsualizarFoto,
            ),
            avisoGuardado,
            ft.ElevatedButton(
                "Guardar cambios",
                icon=ft.Icons.SAVE,
                bgcolor="#7c3aed", color="white", width=300,
                on_click=guardarCambios,
            ),
        ],
    )

    # ===================== PANEL CONTRASEÑA =====================
    cajaCodigoEmail = ft.TextField(
        label="Código de 6 dígitos",
        prefix_icon=ft.Icons.KEY,
        width=300, border_radius=10,
        border_color="#7c3aed", focused_border_color="#a855f7",
        label_style=ft.TextStyle(color="#c084fc"),
        color="white", bgcolor="#2d1b4e",
        visible=False,
    )
    cajaContraNueva = ft.TextField(
        label="Nueva contraseña",
        prefix_icon=ft.Icons.LOCK,
        password=True, width=300, border_radius=10,
        border_color="#7c3aed", focused_border_color="#a855f7",
        label_style=ft.TextStyle(color="#c084fc"),
        color="white", bgcolor="#2d1b4e",
        visible=False,
    )
    avisoContra = ft.Text("", size=13, text_align=ft.TextAlign.CENTER)
    btnMandarCodigo = ft.ElevatedButton(
        "Enviar código al correo",
        icon=ft.Icons.EMAIL,
        bgcolor="#3b0764", color="#e9d5ff", width=300,
    )
    btnActualizarContra = ft.ElevatedButton(
        "Cambiar contraseña",
        icon=ft.Icons.LOCK_RESET,
        bgcolor="#7c3aed", color="white", width=300,
        visible=False,
    )

    def mandarCodigo(e):
        ok, txt = auth_ctrl.enviar_codigo(user["email"])
        avisoContra.value = txt
        avisoContra.color = "#86efac" if ok else "#f87171"
        if ok:
            codigoMandado["value"] = True
            cajaCodigoEmail.visible = True
            cajaContraNueva.visible = True
            btnActualizarContra.visible = True
            btnMandarCodigo.text = "Reenviar código"
        avisoContra.update()
        cajaCodigoEmail.update()
        cajaContraNueva.update()
        btnActualizarContra.update()
        btnMandarCodigo.update()

    def actualizarContra(e):
        ok_v, _ = auth_ctrl.verificar_codigo(user["email"], cajaCodigoEmail.value.strip())
        if not ok_v:
            avisoContra.value = "Código incorrecto."
            avisoContra.color = "#f87171"
            avisoContra.update()
            return
        ok, txt = auth_ctrl.cambiar_password(user["email"], cajaContraNueva.value.strip())
        avisoContra.value = txt
        avisoContra.color = "#86efac" if ok else "#f87171"
        if ok:
            cajaCodigoEmail.visible = False
            cajaContraNueva.visible = False
            btnActualizarContra.visible = False
            codigoMandado["value"] = False
            cajaCodigoEmail.value = ""
            cajaContraNueva.value = ""
            btnMandarCodigo.text = "Enviar código al correo"
        avisoContra.update()
        cajaCodigoEmail.update()
        cajaContraNueva.update()
        btnActualizarContra.update()
        btnMandarCodigo.update()

    btnMandarCodigo.on_click = mandarCodigo
    btnActualizarContra.on_click = actualizarContra

    panelContra = ft.Column(
        visible=False,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=16,
        controls=[
            ft.Container(height=4),
            ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.ARROW_BACK, icon_color="#c084fc",
                        on_click=lambda e: mostrarPanel("inicio"),
                    ),
                    ft.Text("Cambiar contraseña", size=17, weight=ft.FontWeight.BOLD, color="#e9d5ff"),
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            ft.Text(
                "Te mandaremos un código a tu correo\npara confirmar el cambio.",
                size=13, color="#a78bfa", text_align=ft.TextAlign.CENTER,
            ),
            btnMandarCodigo,
            cajaCodigoEmail,
            cajaContraNueva,
            btnActualizarContra,
            avisoContra,
        ],
    )

    # ===================== NAVEGACIÓN =====================
    def mostrar_mis_publicaciones():
        mis_publicaciones_container.content = MisPublicacionesView(
            page, user, lambda: volver_a_perfil()
        )
        mis_publicaciones_container.visible = True
        panelInicio.visible = False
        panelEditar.visible = False
        panelContra.visible = False
        mis_publicaciones_container.update()
        panelInicio.update()
        panelEditar.update()
        panelContra.update()
    
    def volver_a_perfil():
        mis_publicaciones_container.visible = False
        panelInicio.visible = True
        mis_publicaciones_container.update()
        panelInicio.update()
    
    def mostrarPanel(cual):
        mis_publicaciones_container.visible = False
        panelInicio.visible = cual == "inicio"
        panelEditar.visible = cual == "editar"
        panelContra.visible = cual == "contra"
        mis_publicaciones_container.update()
        panelInicio.update()
        panelEditar.update()
        panelContra.update()

    topbar = ft.Container(
        bgcolor="#12002e",
        padding=ft.padding.symmetric(horizontal=16, vertical=10),
        content=ft.Row(
            controls=[
                ft.Icon(ft.Icons.PERSON, color="#c084fc"),
                ft.Text("Perfil", size=18, weight=ft.FontWeight.BOLD, color="#e9d5ff"),
            ],
            spacing=10,
        ),
    )

    areaContenido = ft.Container(
        expand=True,
        bgcolor="#0d001f",
        content=ft.Stack(
            expand=True,
            controls=[
                ft.Column(
                    scroll=ft.ScrollMode.AUTO,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=0,
                    controls=[panelInicio, panelEditar, panelContra],
                ),
                mis_publicaciones_container,
            ]
        ),
    )

    return ft.Column(
        spacing=0,
        expand=True,
        controls=[topbar, areaContenido],
    )
