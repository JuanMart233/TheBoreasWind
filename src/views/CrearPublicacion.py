import flet as ft
from models.PublicacionModel import PublicacionModel

def CrearPublicacionView(page: ft.Page, user: dict, on_back, on_publish):
    pub_model = PublicacionModel()

    caja_contenido = ft.TextField(
        hint_text="¿Qué estás pensando?",
        multiline=True,
        min_lines=3,
        max_lines=6,
        border_color="#7c3aed",
        focused_border_color="#a855f7",
        color="white",
        bgcolor="#2d1b4e",
        expand=True,
    )

    caja_url_imagen = ft.TextField(
        hint_text="URL de la imagen (opcional)",
        border_color="#7c3aed",
        focused_border_color="#a855f7",
        color="white",
        bgcolor="#2d1b4e",
    )

    preview_imagen = ft.Image(src="https://via.placeholder.com/200", visible=False, border_radius=8, height=200, fit="contain")

    mensaje = ft.Text("", size=12, text_align=ft.TextAlign.CENTER)

    def previsualizar(e=None):
        url = caja_url_imagen.value.strip()
        if url:
            preview_imagen.src = url
            preview_imagen.visible = True
        else:
            preview_imagen.visible = False
        page.update()

    def publicar(e=None):
        contenido = caja_contenido.value.strip()
        if not contenido:
            mensaje.value = "Escribe algo para publicar"
            mensaje.color = "#f87171"
            page.update()
            return
        try:
            exito, pub_id = pub_model.crear_publicacion(user["email"], contenido, caja_url_imagen.value.strip() or None)
            print(f"CrearPublicacionView publicar: exito={exito}, pub_id={pub_id}")
            if exito:
                page.snack_bar = ft.SnackBar(ft.Text("Publicación creada"))
                page.snack_bar.open = True
                on_publish()
                page.update()
            else:
                mensaje.value = "Error al publicar"
                mensaje.color = "#f87171"
                page.update()
        except Exception as ex:
            mensaje.value = f"Error: {ex}"
            mensaje.color = "#f87171"
            page.update()

    def descartar(e=None):
        on_back()

    topbar = ft.Container(
        bgcolor="#12002e",
        padding=ft.Padding.symmetric(horizontal=16, vertical=10),
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.Icons.ARROW_BACK, icon_color="#c084fc", on_click=lambda e: on_back()),
                ft.Text("Crear publicación", size=18, weight=ft.FontWeight.BOLD, color="#e9d5ff"),
            ],
        ),
    )

    content = ft.Column(
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
                        caja_contenido,
                        caja_url_imagen,
                        ft.Row(controls=[
                            ft.ElevatedButton("👁 Previsualizar", bgcolor="#2d1b4e", color="#c084fc", on_click=previsualizar),
                            ft.Row(controls=[], expand=True),
                        ], spacing=8),
                        preview_imagen,
                        mensaje,
                        ft.Row(
                            controls=[
                                ft.ElevatedButton("Publicar", bgcolor="#7c3aed", color="white", on_click=publicar),
                                ft.TextButton("Descartar", on_click=descartar),
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                )
            )
        ]
    )

    return content
