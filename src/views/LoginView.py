import flet as ft
from views.RecuperarView import RecuperarView

def LoginView(page: ft.Page, auth_controller, on_login):
    error_text = ft.Text("", color=ft.Colors.RED_400, size=13)
    show_password = ft.Ref[ft.TextField]()

    def toggle_password(e):
        show_password.current.password = not show_password.current.password
        page.update()
    
    AdoDeidad = ft.Image(
        src="arledotore.gif",
        height=150,
        border_radius=120,
    )
    email_input = ft.TextField(
        label="Correo electrónico",
        width=350,
        prefix_icon=ft.Icons.EMAIL,
        border_radius=10,
    )
    password_input = ft.TextField(
        ref=show_password,
        label="Contraseña",
        width=350,
        password=True,
        prefix_icon=ft.Icons.LOCK,
        suffix=ft.IconButton(icon=ft.Icons.REMOVE_RED_EYE, on_click=toggle_password),
        border_radius=10,
    )

    def login_click(e):
        error_text.value = ""
        user, msg = auth_controller.login(email_input.value.strip(), password_input.value.strip())
        if user:
            on_login(user)
        else:
            error_text.value = msg
            page.update()

    reg_nombre = ft.TextField(label="Nombre", width=350, prefix_icon=ft.Icons.PERSON, border_radius=10)
    reg_email = ft.TextField(label="Correo electrónico", width=350, prefix_icon=ft.Icons.EMAIL, border_radius=10)
    reg_password = ft.TextField(label="Contraseña", width=350, password=True, prefix_icon=ft.Icons.LOCK, border_radius=10)
    reg_error = ft.Text("", color=ft.Colors.RED_400, size=13)
    reg_success = ft.Text("", color=ft.Colors.GREEN_400, size=13)
    register_form = ft.Column(
        controls=[
            ft.Text("Crear cuenta", size=22, weight=ft.FontWeight.BOLD),
            reg_nombre,
            reg_email,
            reg_password,
            reg_error,
            reg_success,
            ft.ElevatedButton(
                "Registrarse",
                width=200,
                bgcolor=ft.Colors.GREEN_400,
                color="white",
                on_click=lambda e: register_click(e),
            ),
            ft.TextButton("Ya tengo cuenta", on_click=lambda e: toggle_form(e)),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15,
        visible=False,
    )

    def register_click(e):
        reg_error.value = ""
        reg_success.value = ""
        ok, msg = auth_controller.registrar(
            reg_nombre.value.strip(),
            reg_email.value.strip(),
            reg_password.value.strip(),
        )
        if ok:
            reg_success.value = msg
            reg_nombre.value = ""
            reg_email.value = ""
            reg_password.value = ""
        else:
            reg_error.value = msg
        page.update()

    login_form = ft.Column(
        controls=[
            ft.Icon(ft.Icons.LOCK_PERSON, size=80, color=ft.Colors.RED_400),
            ft.Text("Bienvenido a BoreasWind", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_400),
            AdoDeidad,
            email_input,
            password_input,
            error_text,
            ft.ElevatedButton(
                "Iniciar Sesión",
                on_click=login_click,
                width=200,
                bgcolor=ft.Colors.RED_400,
                color="black",
            ),
            ft.TextButton( "¿No tienes cuenta? Crea una",
                on_click=lambda e: toggle_form(e),
                style=ft.ButtonStyle(color="#003366", bgcolor=ft.Colors.RED_400)),
            ft.TextButton("¿Olvidaste tu contraseña?",
                on_click=lambda e: ir_recuperar(e),
                style=ft.ButtonStyle(color="#003366", bgcolor=ft.Colors.RED_400)),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )

    def toggle_form(e):
        login_form.visible = not login_form.visible
        register_form.visible = not register_form.visible
        page.update()

    def ir_recuperar(e):
        def volver():
            page.controls.clear()
            page.add(LoginView(page, auth_controller, on_login))
            page.update()
        page.controls.clear()
        page.add(RecuperarView(page, auth_controller, on_volver=volver))
        page.update()

    w = page.width or page.window.width or 800
    h = page.height or page.window.height or 600

    bg_image = ft.Image(src="mavuikita.webp", width=w, height=h, fit="cover")
    bg_overlay = ft.Container(width=w, height=h, bgcolor=ft.Colors.with_opacity(0.5, "#000000"))
    fg_container = ft.Container(
        content=ft.Column(
            controls=[login_form, register_form],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        alignment=ft.Alignment(0, 0),
        width=w,
        height=h,
    )
    stack = ft.Stack(controls=[bg_image, bg_overlay, fg_container], width=w, height=h)

    def on_resize(e):
        nw = page.width or page.window.width
        nh = page.height or page.window.height
        bg_image.width = nw
        bg_image.height = nh
        bg_overlay.width = nw
        bg_overlay.height = nh
        fg_container.width = nw
        fg_container.height = nh
        stack.width = nw
        stack.height = nh
        page.update()

    page.on_resized = on_resize
    return stack
