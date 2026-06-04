import flet as ft
from models.PublicacionModel import PublicacionModel

def PublicacionDetalleView(page: ft.Page, user: dict, pub_id: int, on_back):
    pub_model = PublicacionModel()
    
    try:
        publicacion = pub_model.obtener_publicacion_por_id(pub_id)
    except:
        publicacion = None
    
    if not publicacion:
        return ft.Container(
            content=ft.Text("Publicación no encontrada", color="red"),
            expand=True,
        )

    comentarios_list = ft.Column(spacing=8, scroll=ft.ScrollMode.AUTO)
    
    def cargar_comentarios():
        comentarios_list.controls.clear()
        try:
            comentarios = pub_model.obtener_comentarios(pub_id)
        except:
            comentarios = []
            
        for c in comentarios:
            if c.get("foto"):
                avatar_content = ft.Image(src=c["foto"], width=32, height=32, border_radius=16, fit="cover")
            else:
                avatar_content = ft.Text(c["nombre"][0].upper(), size=14, color="white")
            
            avatar = ft.Container(
                width=32, height=32, border_radius=16,
                bgcolor="#7c3aed",
                content=avatar_content,
                alignment=ft.Alignment(0, 0),
            )
            
            comentarios_list.controls.append(
                ft.Container(
                    bgcolor="#1e0a3c",
                    border_radius=8,
                    padding=10,
                    content=ft.Row(
                        controls=[
                            avatar,
                            ft.Column(
                                controls=[
                                    ft.Text(c["nombre"], size=12, weight=ft.FontWeight.BOLD, color="#e9d5ff"),
                                    ft.Text(c["comentario"], size=12, color="#c084fc"),
                                ],
                                spacing=2,
                                expand=True,
                            )
                        ],
                        spacing=8,
                    )
                )
            )

    # Avatar
    if publicacion.get("foto"):
        avatar_pub_content = ft.Image(src=publicacion["foto"], width=40, height=40, border_radius=20, fit="cover")
    else:
        avatar_pub_content = ft.Text(publicacion["nombre"][0].upper(), size=18, color="white")
    
    avatar_pub = ft.Container(
        width=40, height=40, border_radius=20,
        bgcolor="#7c3aed",
        content=avatar_pub_content,
        alignment=ft.Alignment(0, 0),
    )
    
    pub_controls = [
        ft.Row(
            controls=[
                avatar_pub,
                ft.Column(
                    controls=[
                        ft.Text(publicacion["nombre"], size=14, weight=ft.FontWeight.BOLD, color="#e9d5ff"),
                        ft.Text(str(publicacion["fecha_creacion"]), size=10, color="#a78bfa"),
                    ],
                    spacing=2,
                )
            ],
            spacing=10,
        ),
        ft.Text(publicacion["contenido"], size=14, color="#e9d5ff"),
    ]
    
    if publicacion.get("imagen_url"):
        pub_controls.append(ft.Image(src=publicacion["imagen_url"], border_radius=8))

    caja_comentario = ft.TextField(
        hint_text="Escribe un comentario...",
        border_color="#7c3aed",
        focused_border_color="#a855f7",
        color="white",
        bgcolor="#2d1b4e",
        multiline=True,
        min_lines=1,
        max_lines=3,
        expand=True,
    )

    def enviar_comentario(e):
        texto = caja_comentario.value.strip()
        if texto:
            if pub_model.agregar_comentario(pub_id, user["email"], texto):
                caja_comentario.value = ""
                page.update()
                cargar_comentarios()
                page.update()

    topbar = ft.Container(
        bgcolor="#12002e",
        padding=ft.Padding.symmetric(horizontal=16, vertical=10),
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.Icons.ARROW_BACK, icon_color="#c084fc", on_click=lambda e: on_back()),
                ft.Text("Publicación", size=18, weight=ft.FontWeight.BOLD, color="#e9d5ff"),
            ],
        ),
    )
    
    # Cargar comentarios
    try:
        cargar_comentarios()
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
                content=ft.Column(
                    scroll=ft.ScrollMode.AUTO,
                    spacing=12,
                    controls=[
                        ft.Container(
                            bgcolor="#1e0a3c",
                            border_radius=12,
                            padding=16,
                            content=ft.Column(spacing=12, controls=pub_controls)
                        ),
                        ft.Divider(color="#2d1b4e"),
                        ft.Text("Comentarios", size=16, weight=ft.FontWeight.BOLD, color="#e9d5ff"),
                        comentarios_list,
                        ft.Row(
                            controls=[
                                caja_comentario,
                                ft.IconButton(icon=ft.Icons.SEND, icon_color="#a855f7", on_click=enviar_comentario),
                            ],
                            spacing=8,
                        )
                    ]
                )
            )
        ],
    )
