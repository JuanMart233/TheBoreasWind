import flet as ft

PREGUNTAS = [
    {
        "pregunta": "Pregunta 1: ¿Cual de estas reacciones elementales no esta en el juego?",
        "opciones": ["Derretido lunar", "Vaporizado", "Electro cargado lunar"],
        "correcta": 0,
    },
    {
        "pregunta": "Pregunta 2: ¿Cual es el material principal para subir las estatuas de arconte?",
        "opciones": ["Mariposa de cristal", "Oculous", "Cristaloptero"],
        "correcta": 1,
    },
    {
        "pregunta": "Pregunta 3: ¿Cual es el modo de juego menos jugado de genshin?",
        "opciones": ["El abismo", "El TSG", "El teatro"],
        "correcta": 1,
    },
    {
        "pregunta": "Pregunta 4: ¿Cual es el personaje mas inutil del juego?",
        "opciones": ["Aloy", "Mavuika", "Skirk"],
        "correcta": 0,
    },
    {
        "pregunta": "Pregunta 5: ¿Cual es el material de mundo mas importante de estos 3?",
        "opciones": ["Ranas", "Cristaloptero", "Perlas de loncha"],
        "correcta": 1,
    },
    {
        "pregunta": "Pregunta 6: ¿Cual de estos es el arconte pyro?",
        "opciones": ["Mavuika", "Yoimiya", "Bennett"],
        "correcta": 2,
    },
    {
        "pregunta": "Pregunta 7: El elemento hydro es caracterizado por: ",
        "opciones": ["Daño y aplicacion elemental", "Escudos", "healers"],
        "correcta": 0,
    },
    {
        "pregunta": "Pregunta 8: Cual de estas fraces caracteriza mas a paimon en internet: ",
        "opciones": ["bardo de pacotilla", "Ejete nandayo", "comida de emergencia"],
        "correcta": 1,
    },
    {
        "pregunta": "Pregunta 9: ¿Cual es la mision mas larga y tediosa asi que odio y aborrezco?",
        "opciones": ["Misiones legendarias", "Mision de acompañante", "Los aranaras"],
        "correcta": 2,
    },
    {
        "pregunta": "Pregunta 10: ¿Cual el nuke mas fuerte del juego?",
        "opciones": ["Mavuika", "Skirk", "bennett"],
        "correcta": 0,
    },
]

def calcular_nivel(correctas):
    if correctas <= 4:
        return "Aprendiz"
    elif correctas <= 7:
        return "Experimentado"
    else:
        return "Experto"

def TestView(page: ft.Page, user, on_resultado):
    estado = {"pregunta_actual": 0, "correctas": 0, "respondida": False}

    pregunta_text = ft.Text("", size=18, weight=ft.FontWeight.BOLD, color="#e8d5a3",
                            text_align=ft.TextAlign.CENTER)
    progreso_text = ft.Text("", size=12, color="#a0c4ff", text_align=ft.TextAlign.CENTER)
    feedback_text = ft.Text("", size=13, text_align=ft.TextAlign.CENTER)

    barra_progreso = ft.ProgressBar(width=400, value=0, bgcolor="#1a1a2e", color="#4fc3f7")

    botones_opciones = [
        ft.ElevatedButton(
            width=380, height=50,
            bgcolor="#1a1a2e",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                side=ft.BorderSide(1, "#3949ab"),
            ),
        )
        for _ in range(3)
    ]

    btn_siguiente = ft.ElevatedButton(
        "Siguiente →",
        width=200, height=45,
        bgcolor="#1a237e",
        color="#e8d5a3",
        visible=False,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
    )

    contenido = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=16,
        tight=True,
    )

    def cargar_pregunta():
        i = estado["pregunta_actual"]
        p = PREGUNTAS[i]
        estado["respondida"] = False
        feedback_text.value = ""
        pregunta_text.value = p["pregunta"]
        progreso_text.value = f"Pregunta {i + 1} de {len(PREGUNTAS)}"
        barra_progreso.value = i / len(PREGUNTAS)
        btn_siguiente.visible = False

        for idx, btn in enumerate(botones_opciones):
            texto = p["opciones"][idx]
            btn.content = ft.Text(texto, size=14, color="#e0e0e0", text_align=ft.TextAlign.CENTER)
            btn.bgcolor = "#1a1a2e"
            btn.style = ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                side=ft.BorderSide(1, "#3949ab"),
            )
            btn.data = idx
            btn.on_click = responder
            btn.disabled = False

        page.update()

    def responder(e):
        if estado["respondida"]:
            return
        estado["respondida"] = True
        i = estado["pregunta_actual"]
        correcta = PREGUNTAS[i]["correcta"]
        elegida = e.control.data

        for idx, btn in enumerate(botones_opciones):
            btn.disabled = True
            if idx == correcta:
                btn.bgcolor = "#1b5e20"
                btn.style = ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10),
                    side=ft.BorderSide(2, "#66bb6a"),
                )
            elif idx == elegida:
                btn.bgcolor = "#7f0000"
                btn.style = ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10),
                    side=ft.BorderSide(2, "#ef5350"),
                )

        if elegida == correcta:
            estado["correctas"] += 1
            feedback_text.value = "✦ ¡Correcto! Los Archons sonríen ante tu sabiduría ✦"
            feedback_text.color = "#66bb6a"
        else:
            feedback_text.value = "✦ Incorrecto. El Abismo te ha engañado esta vez ✦"
            feedback_text.color = "#ef5350"

        btn_siguiente.visible = True
        if i == len(PREGUNTAS) - 1:
            btn_siguiente.text = "Ver resultado ✦"
        page.update()

    def siguiente(e):
        estado["pregunta_actual"] += 1
        if estado["pregunta_actual"] >= len(PREGUNTAS):
            mostrar_resultado()
        else:
            cargar_pregunta()

    def mostrar_resultado():
        correctas = estado["correctas"]
        nivel = calcular_nivel(correctas)

        NIVEL_INFO = {
            "Aprendiz":      {"color": "#4fc3f7", "emoji": "🌱", "msg": "¡El viaje apenas comienza, Viajero!"},
            "Experimentado": {"color": "#ab47bc", "emoji": "⚔️", "msg": "¡Eres un digno aventurero de Teyvat!"},
            "Experto":       {"color": "#e53935", "emoji": "🔥", "msg": "¡Los Archons te reconocen como igual!"},
        }
        info = NIVEL_INFO[nivel]

        contenido.controls = [
            ft.Text("✦ Resultados del Test ✦", size=12, color="#a0c4ff",
                    text_align=ft.TextAlign.CENTER),
            ft.Text(f"{info['emoji']} {nivel}", size=34, weight=ft.FontWeight.BOLD,
                    color=info["color"], text_align=ft.TextAlign.CENTER),
            ft.Text(info["msg"], size=15, color="#e8d5a3", text_align=ft.TextAlign.CENTER),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(f"Respuestas correctas: {correctas} / {len(PREGUNTAS)}",
                                size=16, color="#e0e0e0", text_align=ft.TextAlign.CENTER),
                        ft.Text(f"Respuestas incorrectas: {len(PREGUNTAS) - correctas} / {len(PREGUNTAS)}",
                                size=16, color="#e0e0e0", text_align=ft.TextAlign.CENTER),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=6,
                ),
                bgcolor=ft.Colors.with_opacity(0.25, "#0d0d1f"),
                border_radius=14,
                padding=ft.padding.symmetric(horizontal=40, vertical=20),
                border=ft.border.all(1, info["color"]),
                width=380,
            ),
            ft.ElevatedButton(
                "¡Comenzar mi aventura! ✦",
                width=260, height=50,
                bgcolor="#1a237e",
                color="#e8d5a3",
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=12),
                    shadow_color=info["color"],
                    elevation=8,
                ),
                on_click=lambda e: on_resultado(user, nivel),
            ),
        ]
        page.update()

    btn_siguiente.on_click = siguiente

    contenido.controls = [
        ft.Text("✦ Test de Conocimiento ✦", size=12, color="#a0c4ff",
                text_align=ft.TextAlign.CENTER),
        progreso_text,
        barra_progreso,
        pregunta_text,
        ft.Column(
            controls=botones_opciones,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        ),
        feedback_text,
        btn_siguiente,
    ]

    cargar_pregunta()

    w = page.window.width or 800
    h = page.window.height or 600

    bg = ft.Image(src="fondito.jpeg", fit="cover", width=w, height=h)
    overlay = ft.Container(bgcolor=ft.Colors.with_opacity(0.78, "#0a0a1a"), width=w, height=h)

    def on_resize(e):
        nw = page.window.width or 800
        nh = page.window.height or 600
        bg.width, bg.height = nw, nh
        overlay.width, overlay.height = nw, nh
        page.update()
    page.on_resized = on_resize

    return ft.Container(
        expand=True,
        content=ft.Stack(
            controls=[
                bg,
                overlay,
                ft.Container(
                    expand=True,
                    alignment=ft.Alignment(0, 0),
                    content=contenido,
                ),
            ],
            expand=True,
        ),
    )
