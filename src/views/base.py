import flet as ft
from models.PublicacionModel import PublicacionModel
from views.PublicacionDetalle import PublicacionDetalleView
from views.CrearPublicacion import CrearPublicacionView


def BaseView(page: ft.Page, user: dict, auth_ctrl, on_logout, on_switch_account):
    from views.guias import GuiasView
    from views.perfil import PerfilView

    #avatar navbar (se pasa a PerfilView para actualizarlo)
    avatar_mini_foto = ft.Image(
        src=user.get("foto") if user.get("foto") else "https://via.placeholder.com/28",
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

    #avatar drawer (se pasa a drawer para actualizarlo)
    drawer_foto = ft.Image(
        src=user.get("foto") if user.get("foto") else "https://via.placeholder.com/48",
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
        avatar_mini_foto.src = nueva_foto if nueva_foto else "https://via.placeholder.com/28"
        avatar_mini_foto.visible = tiene
        avatar_mini_letra.visible = not tiene
        drawer_foto.src = nueva_foto if nueva_foto else "https://via.placeholder.com/48"
        drawer_foto.visible = tiene
        drawer_letra.visible = not tiene
        avatar_mini.update()
        avatar_drawer.update()

    #pantalla de detalle de publicación
    detalle_publicacion_container = ft.Container(visible=False, expand=True)
    crear_publicacion_container = ft.Container(visible=False, expand=True)

    def ir_a_publicacion(pub_id):
        detalle_publicacion_container.content = PublicacionDetalleView(
            page, user, pub_id, lambda: mostrar("inicio")
        )
        detalle_publicacion_container.visible = True
        crear_publicacion_container.visible = False
        inicio_content.visible = False
        guias_content.visible = False
        perfil_content.visible = False
        page.update()

    def volver_inicio_y_actualizar():
        print("volver_inicio_y_actualizar called")
        # Primero ocultar la pantalla de crear
        crear_publicacion_container.visible = False
        # Luego cargar las publicaciones (antes de hacer visible)
        inicio_content.cargar_publicaciones()
        # Ahora hacer visible el contenido
        detalle_publicacion_container.visible = False
        inicio_content.visible = True
        # Actualizar la página
        page.update()

    def abrir_crear_publicacion(e):
        try:
            print("abrir_crear_publicacion called")
            crear_publicacion_container.content = CrearPublicacionView(
                page,
                user,
                lambda: mostrar("inicio"),
                volver_inicio_y_actualizar
            )
            crear_publicacion_container.visible = True
            detalle_publicacion_container.visible = False
            inicio_content.visible = False
            guias_content.visible = False
            perfil_content.visible = False
            page.update()
        except Exception as ex:
            print(f"Error al abrir crear publicacion: {ex}")
            page.update()

    #contenidos de cada pantalla
    inicio_content = _InicioContent(page, user, on_logout, on_switch_account, avatar_drawer, lambda dest: mostrar(dest), ir_a_publicacion, abrir_crear_publicacion)
    guias_content  = GuiasView(page, user)
    perfil_content = PerfilView(page, user, auth_ctrl, on_logout, on_switch_account, avatar_mini, avatar_mini_foto, avatar_mini_letra, on_foto_actualizada)

    pantallas = {
        "inicio": inicio_content,
        "guias":  guias_content,
        "perfil": perfil_content,
    }

    def mostrar(destino):
        detalle_publicacion_container.visible = False
        crear_publicacion_container.visible = False
        for key, ctrl in pantallas.items():
            ctrl.visible = (key == destino)
        _actualizar_navbar(destino)
        page.update()

    #navbar y botones
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
                controls=list(pantallas.values()) + [detalle_publicacion_container, crear_publicacion_container],
            ),
            navbar,
        ],
    )


def _InicioContent(page, user, on_logout, on_switch_account, avatar_drawer, mostrar_pantalla, ir_a_publicacion, on_crear_publicacion):
    pub_model = PublicacionModel()
    
    feed_publicaciones = ft.Column(spacing=12, scroll=ft.ScrollMode.AUTO, expand=True)
    
    # dialog para crear publicación
    caja_contenido = ft.TextField(
        hint_text="¿Qué estás pensando?",
        multiline=True,
        min_lines=3,
        max_lines=6,
        border_color="#7c3aed",
        focused_border_color="#a855f7",
        color="white",
        bgcolor="#2d1b4e",
    )
    
    imagen_seleccionada = {"url": None}
    preview_imagen = ft.Image(
        src="https://via.placeholder.com/200",
        visible=False, 
        border_radius=8, 
        height=200, 
        fit="contain"
    )
    
    caja_url_imagen = ft.TextField(
        hint_text="URL de la imagen (opcional)",
        border_color="#7c3aed",
        focused_border_color="#a855f7",
        color="white",
        bgcolor="#2d1b4e",
    )
    
    def previsualizar_imagen(e):
        url = caja_url_imagen.value.strip()
        if url:
            imagen_seleccionada["url"] = url
            preview_imagen.src = url
            preview_imagen.visible = True
        else:
            imagen_seleccionada["url"] = None
            preview_imagen.visible = False
        preview_imagen.update()
    
    mensaje_publicar = ft.Text("", size=12, text_align=ft.TextAlign.CENTER)
    
    dialog_publicar = ft.AlertDialog(
        modal=True,
        title=ft.Text("Crear publicación", color="#e9d5ff"),
        bgcolor="#1e0a3c",
        content=ft.Container(
            width=400,
            content=ft.Column(
                controls=[
                    caja_contenido,
                    caja_url_imagen,
                    ft.ElevatedButton(
                        "👁 Previsualizar",
                        bgcolor="#2d1b4e",
                        color="#c084fc",
                        on_click=previsualizar_imagen,
                    ),
                    preview_imagen,
                    mensaje_publicar,
                ],
                spacing=12,
                tight=True,
            )
        ),
        actions=[
            ft.TextButton("Descartar", on_click=lambda e: cerrar_dialog()),
            ft.ElevatedButton(
                "Publicar",
                bgcolor="#7c3aed",
                color="white",
                on_click=lambda e: publicar_post(),
            ),
        ],
    )
    
    def abrir_dialog_publicar(e):
        try:
            print("abrir_dialog_publicar called")

            # show a quick snack to confirm click (will be replaced by dialog)
            try:
                page.snack_bar = ft.SnackBar(ft.Text("Abrir diálogo..."))
                page.snack_bar.open = True
            except Exception:
                pass

            # Reset inputs (don't call .update() on dialog controls before they're added to the page)
            caja_contenido.value = ""
            caja_url_imagen.value = ""
            imagen_seleccionada["url"] = None
            preview_imagen.visible = False
            mensaje_publicar.value = ""

            # Attach and open the dialog first, then update the page so controls are present
            page.dialog = dialog_publicar
            dialog_publicar.open = True
            page.update()
        except Exception as ex:
            print(f"Error al abrir dialog: {ex}")
            # Try to set an error message (safe assignment without calling .update() on the control)
            try:
                mensaje_publicar.value = f"Error al abrir: {ex}"
            except:
                pass
            page.update()
    
    def cerrar_dialog():
        dialog_publicar.open = False
        page.update()
    
    def cargar_publicaciones():
        print(f"cargar_publicaciones() called, obtener_publicaciones...")
        feed_publicaciones.controls.clear()
        try:
            publicaciones = pub_model.obtener_publicaciones()
            print(f"cargar_publicaciones() got {len(publicaciones) if publicaciones else 0} publications")
        except Exception as e:
            print(f"Error al obtener publicaciones: {e}")
            publicaciones = []
        
        if not publicaciones:
            feed_publicaciones.controls.append(
                ft.Text("No hay publicaciones aún", color="#a78bfa", size=14)
            )
        else:
            for pub in publicaciones:
                # Avatar
                if pub.get("foto"):
                    avatar_content = ft.Image(
                        src=pub["foto"], 
                        width=40, 
                        height=40, 
                        border_radius=20, 
                        fit="cover"
                    )
                else:
                    avatar_content = ft.Text(
                        pub["nombre"][0].upper(), 
                        size=18, 
                        color="white"
                    )
                
                avatar = ft.Container(
                    width=40, height=40, border_radius=20,
                    bgcolor="#7c3aed",
                    content=avatar_content,
                    alignment=ft.Alignment(0, 0),
                )
                
                # Controles
                card_controls = [
                    ft.Row(
                        controls=[
                            avatar,
                            ft.Column(
                                controls=[
                                    ft.Text(pub["nombre"], size=14, weight=ft.FontWeight.BOLD, color="#e9d5ff"),
                                    ft.Text(str(pub["fecha_creacion"]), size=10, color="#a78bfa"),
                                ],
                                spacing=2,
                            )
                        ],
                        spacing=10,
                    ),
                    ft.Text(pub["contenido"], size=14, color="#e9d5ff"),
                ]
                
                if pub.get("imagen_url"):
                    card_controls.append(
                        ft.Image(
                            src=pub["imagen_url"], 
                            border_radius=8, 
                            fit="contain"
                        )
                    )
                
                card_pub = ft.Container(
                    bgcolor="#1e0a3c",
                    border_radius=12,
                    padding=16,
                    on_click=lambda e, pid=pub["id"]: ir_a_publicacion(pid),
                    content=ft.Column(spacing=12, controls=card_controls),
                )
                feed_publicaciones.controls.append(card_pub)
        print(f"cargar_publicaciones() finished, feed_publicaciones has {len(feed_publicaciones.controls)} controls")
    
    def publicar_post():
        contenido = caja_contenido.value.strip()
        if not contenido:
            mensaje_publicar.value = "Escribe algo para publicar"
            mensaje_publicar.color = "#f87171"
            mensaje_publicar.update()
            return
        
        try:
            exito, pub_id = pub_model.crear_publicacion(
                user["email"],
                contenido,
                imagen_seleccionada["url"]
            )
            print(f"_InicioContent publicar_post: exito={exito}, pub_id={pub_id}")
            
            if exito:
                cerrar_dialog()
                cargar_publicaciones()
                page.update()
            else:
                mensaje_publicar.value = "Error al publicar"
                mensaje_publicar.color = "#f87171"
                mensaje_publicar.update()
        except Exception as ex:
            print(f"Error en publicar_post: {ex}")
            mensaje_publicar.value = f"Error: {str(ex)}"
            mensaje_publicar.color = "#f87171"
            mensaje_publicar.update()
    
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
                    on_click=lambda e: (setattr(drawer_panel, 'visible', False), mostrar_pantalla("perfil")),
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
        page.update()

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
        padding=16,
        content=ft.Column(
            spacing=16,
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(f"¡Bienvenido, {user.get('nombre', 'Usuario')}!", size=18, color="#c084fc", expand=True),
                        ft.ElevatedButton(
                            "📝 Publicar",
                            bgcolor="#7c3aed",
                            color="white",
                            on_click=on_crear_publicacion,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Divider(color="#2d1b4e", height=1),
                feed_publicaciones,
            ]
        ),
    )

    # Cargar publicaciones después de crear la vista
    try:
        cargar_publicaciones()
    except:
        pass
    
    inicio_col = ft.Column(
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
    inicio_col.cargar_publicaciones = cargar_publicaciones
    return inicio_col
