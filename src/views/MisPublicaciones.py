import flet as ft
from models.PublicacionModel import PublicacionModel

def MisPublicacionesView(page: ft.Page, user: dict, on_back):
    pub_model = PublicacionModel()
    
    lista_publicaciones = ft.Column(spacing=12, scroll=ft.ScrollMode.AUTO, expand=True)
    
    # Dialog para editar publicación
    caja_editar_contenido = ft.TextField(
        hint_text="Contenido de la publicación",
        multiline=True,
        min_lines=3,
        max_lines=6,
        border_color="#7c3aed",
        focused_border_color="#a855f7",
        color="white",
        bgcolor="#2d1b4e",
    )
    
    imagen_editar = {"url": None, "id": None}
    preview_editar = ft.Image(
        src="https://via.placeholder.com/200",
        visible=False, 
        border_radius=8, 
        height=200, 
        fit="contain"
    )
    
    caja_url_editar = ft.TextField(
        hint_text="URL de la imagen",
        border_color="#7c3aed",
        focused_border_color="#a855f7",
        color="white",
        bgcolor="#2d1b4e",
    )
    
    def previsualizar_editar(e):
        url = caja_url_editar.value.strip()
        if url:
            imagen_editar["url"] = url
            preview_editar.src = url
            preview_editar.visible = True
        else:
            imagen_editar["url"] = None
            preview_editar.visible = False
        preview_editar.update()
    
    mensaje_editar = ft.Text("", size=12, text_align=ft.TextAlign.CENTER)
    
    dialog_editar = ft.AlertDialog(
        modal=True,
        title=ft.Text("Editar publicación", color="#e9d5ff"),
        bgcolor="#1e0a3c",
        content=ft.Container(
            width=400,
            content=ft.Column(
                controls=[
                    caja_editar_contenido,
                    caja_url_editar,
                    ft.ElevatedButton(
                        "👁 Previsualizar",
                        bgcolor="#2d1b4e",
                        color="#c084fc",
                        on_click=previsualizar_editar,
                    ),
                    preview_editar,
                    mensaje_editar,
                ],
                spacing=12,
                tight=True,
            )
        ),
        actions=[
            ft.TextButton("Cancelar", on_click=lambda e: cerrar_dialog_editar()),
            ft.ElevatedButton(
                "Guardar",
                bgcolor="#7c3aed",
                color="white",
                on_click=lambda e: guardar_edicion(),
            ),
        ],
    )
    
    # Dialog para confirmar eliminación
    dialog_confirmar = ft.AlertDialog(
        modal=True,
        title=ft.Text("¿Eliminar publicación?", color="#e9d5ff"),
        bgcolor="#1e0a3c",
        content=ft.Text(
            "Esta acción no se puede deshacer. Se eliminarán todos los comentarios.",
            color="#c084fc",
        ),
        actions=[
            ft.TextButton("Cancelar", on_click=lambda e: cerrar_dialog_confirmar()),
            ft.ElevatedButton(
                "Eliminar",
                bgcolor="#dc2626",
                color="white",
                on_click=lambda e: confirmar_eliminacion(),
            ),
        ],
    )
    
    pub_a_eliminar = {"id": None}
    
    def abrir_dialog_editar(pub):
        imagen_editar["id"] = pub["id"]
        imagen_editar["url"] = pub.get("imagen_url")
        caja_editar_contenido.value = pub["contenido"]
        caja_url_editar.value = pub.get("imagen_url") or ""
        
        if pub.get("imagen_url"):
            preview_editar.src = pub["imagen_url"]
            preview_editar.visible = True
        else:
            preview_editar.visible = False
        
        mensaje_editar.value = ""
        dialog_editar.open = True
        page.dialog = dialog_editar
        page.update()
    
    def cerrar_dialog_editar():
        dialog_editar.open = False
        page.update()
    
    def guardar_edicion():
        contenido = caja_editar_contenido.value.strip()
        if not contenido:
            mensaje_editar.value = "El contenido no puede estar vacío"
            mensaje_editar.color = "#f87171"
            mensaje_editar.update()
            return
        
        if pub_model.actualizar_publicacion(imagen_editar["id"], contenido, imagen_editar["url"]):
            cerrar_dialog_editar()
            cargar_publicaciones()
        else:
            mensaje_editar.value = "Error al actualizar"
            mensaje_editar.color = "#f87171"
            mensaje_editar.update()
    
    def abrir_dialog_confirmar(pub_id):
        pub_a_eliminar["id"] = pub_id
        dialog_confirmar.open = True
        page.dialog = dialog_confirmar
        page.update()
    
    def cerrar_dialog_confirmar():
        dialog_confirmar.open = False
        page.update()
    
    def confirmar_eliminacion():
        if pub_model.eliminar_publicacion(pub_a_eliminar["id"]):
            cerrar_dialog_confirmar()
            cargar_publicaciones()
    
    def cargar_publicaciones():
        lista_publicaciones.controls.clear()
        try:
            publicaciones = pub_model.obtener_publicaciones_usuario(user["email"])
        except:
            publicaciones = []
        
        if not publicaciones:
            lista_publicaciones.controls.append(
                ft.Container(
                    expand=True,
                    content=ft.Text("No tienes publicaciones aún", size=16, color="#a78bfa"),
                    alignment=ft.Alignment(0, 0),
                )
            )
        else:
            for pub in publicaciones:
                if pub.get("foto"):
                    avatar_content = ft.Image(src=pub["foto"], width=40, height=40, border_radius=20, fit="cover")
                else:
                    avatar_content = ft.Text(pub["nombre"][0].upper(), size=18, color="white")
                
                avatar = ft.Container(
                    width=40, height=40, border_radius=20,
                    bgcolor="#7c3aed",
                    content=avatar_content,
                    alignment=ft.Alignment(0, 0),
                )
                
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
                                expand=True,
                            ),
                            ft.Row(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.icons.EDIT,
                                        icon_color="#a855f7",
                                        tooltip="Editar",
                                        on_click=lambda e, p=pub: abrir_dialog_editar(p),
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.DELETE,
                                        icon_color="#ef4444",
                                        tooltip="Eliminar",
                                        on_click=lambda e, pid=pub["id"]: abrir_dialog_confirmar(pid),
                                    ),
                                ],
                                spacing=0,
                            )
                        ],
                        spacing=10,
                    ),
                    ft.Text(pub["contenido"], size=14, color="#e9d5ff"),
                ]
                
                if pub.get("imagen_url"):
                    card_controls.append(ft.Image(src=pub["imagen_url"], border_radius=8, fit="contain", height=200))
                
                card_pub = ft.Container(
                    bgcolor="#1e0a3c",
                    border_radius=12,
                    padding=16,
                    content=ft.Column(spacing=12, controls=card_controls),
                )
                lista_publicaciones.controls.append(card_pub)
    
    cargar_publicaciones()
    
    topbar = ft.Container(
        bgcolor="#12002e",
        padding=ft.padding.symmetric(horizontal=16, vertical=10),
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.Icons.ARROW_BACK, icon_color="#c084fc", on_click=lambda e: on_back()),
                ft.Text("Mis Publicaciones", size=18, weight=ft.FontWeight.BOLD, color="#e9d5ff"),
            ],
        ),
    )
    
    # Cargar publicaciones
    try:
        cargar_publicaciones()
    except:
        pass
    
    return ft.Column(
        spacing=0,
        expand=True,
        controls=[
            topbar,
            ft.Container(
                expand=True,
                bgcolor="#0d001f",
                padding=16,
                content=lista_publicaciones,
            )
        ],
    )
