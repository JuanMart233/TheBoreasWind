import flet as ft
from views.PersonajeDetalle import PersonajeDetalle

PERSONAJES = [
    {"nombre": "Arlecchino",  "imagen": "Arle.jpg", "region": "Fontaine", "rol": "Main dps", "elemento": "Pyro", "reacciones": "Derretidos/Sobrecarga", "talentos": "Ataque Básico > Habilidad Definitiva > Habilidad Elemental", "estadisticas": "2000 ataque %, 1500 defensa %, 1000 vida %, 160 Recarga de Energía, 200 Maestría Elemental, 200 Daño crítico %, 90 Probabilidad Crítica", "artefactos": ["ArleSet.webp","Gladiador.webp","Pabellon.webp"], "equipos": [["Arle.jpg","Citlali.jpg","Xilonen.jpg","Bennett.jpg"],["Arle.jpg","Citlali.jpg","Xilonen.jpg","Kazuha.jpg"],["Arle.jpg","Charlotte.jpg","Xilonen.jpg","Bennett.jpg"]], "armas5": ["LunaCarmesi.webp","Halcon.webp","ArenasEscarlatas.webp"], "armas4": ["LanzadelDuelo.webp","LanzaPeñascoOscuro.webp","CharlaPabellon.webp"]},
    {"nombre": "Amber",  "imagen": "Amber.jpg", "region": "Mondstadt", "rol": "Sub dps", "elemento": "Pyro", "reacciones": "Derretidos", "talentos": "Habilidad Definitiva > Habilidad Elemental > Ataque Básico", "estadisticas": "2000 ataque %, 1500 defensa %, 1000 vida %, 190 Recarga de Energía, 200 Maestría Elemental, 200 Daño crítico %, 90 Probabilidad Crítica", "artefactos": ["Reminiscencia.webp","OrquestaErrante.webp","Objeto_Flor_en_Llamas_de_la_Bruja.webp"], "equipos": [["Amber.jpg","Xingchiu.jpg","Kazuha.jpg","Bennett.jpg"],["Amber.jpg","Ayaka.jpg","Zhongli.jpg","Bennett.jpg"],["Amber.jpg","Raiden.jpg","Kazuha.jpg","Bennett.jpg"]], "armas5": ["NumerodeMagia.webp","AquaSimulacra.webp","AgitadordelRelampago.webp"], "armas4": ["PrototipoluzdeLuna.webp","Objeto_Ultimo_Acorde.webp","SolAbrasador.webp"]},
    {"nombre": "Diluc",  "imagen": "Diluc.jpg", "region": "Mondstadt", "rol": "Main dps", "elemento": "Pyro", "reacciones": "Sobrecargados/Derretidos", "talentos": "Habilidad Elemental > Habilidad Definitiva > Ataque Básico", "estadisticas": "2000 ataque %, 1500 defensa %, 1000 vida %, 170 Recarga de Energía, 250 Maestría Elemental, 200 Daño crítico %, 90 Probabilidad Crítica", "artefactos": ["Objeto_Flor_en_Llamas_de_la_Bruja.webp","SueñosAureos.webp","OrquestaErrante.webp"], "equipos": [["Diluc.jpg","Xingchiu.jpg","Kazuha.jpg","Zhongli.jpg"],["Diluc.jpg","Xingchiu.jpg","Venti.jpg","Zhongli.jpg"],["Diluc.jpg","Xingchiu.jpg","Albedo.jpg","Zhongli.jpg"]], "armas5": ["MardeJuncos.webp","MilSolesAbrasadores.webp","ColmillodelRey.webp"], "armas4": ["MeduladelaSerpiente.webp","SombradelaMarea.webp","GranEspadaSacrificio.webp"]},
    {"nombre": "Klee",  "imagen": "Klee.jpg", "region": "Mondstadt", "rol": "Main dps", "elemento": "Pyro", "reacciones": "Sobrecarga/Derretidos", "talentos": "Ataque Básico > Habilidad Elemental > Habilidad Definitiva", "estadisticas": "2000 ataque %, 1500 defensa %, 1000 vida %, 180 Recarga de Energía, 200 Maestría Elemental, 200 Daño crítico %, 90 Probabilidad Crítica", "artefactos": ["DiadelosVientos.webp","Objeto_Flor_en_Llamas_de_la_Bruja.webp","EcodelSacrificio.webp"], "equipos": [["Klee.jpg","Xilonen.jpg","Furina.jpg","Bennett.jpg"],["Klee.jpg","Kazuha.jpg","Furina.jpg","Bennett.jpg"],["Klee.jpg","Xilonen.jpg","Durin.jpg","Bennett.jpg"]], "armas5": ["Relicario.webp","OracionPerdida.webp","AxiomadelaKagura.webp"], "armas4": ["SinfoniadelosMerodeadores.webp","PerlaSolar.webp","CartaNautica.webp"]},
    {"nombre": "Bennett",  "imagen": "Bennett.jpg", "region": "Mondstadt", "rol": "Suport", "elemento": "Pyro", "reacciones": "Derretidos", "talentos": "Habilidad Definitiva > Habilidad Elemental > Ataque Básico", "estadisticas": "2500 ataque %, 1500 defensa %, 3000 vida %, 250 Recarga de Energía, 150 Maestría Elemental, 190 Daño crítico %, 80 Probabilidad Crítica", "artefactos": ["RitualDeLaNobleza.webp","Instructor.webp","PergaminoHeroe.webp"], "equipos": [["Tartaglia.jpg","Xiangling.jpg","Kazuha.jpg","Bennett.jpg"],["Raiden.jpg","Kazuha.jpg","Sara.jpg","Bennett.jpg"],["Yoimiya.jpg","Xingchiu.jpg","Kazuha.jpg","Bennett.jpg"]], "armas5": ["ReflejodelasTinieblas.webp","Objeto_Cortador_de_Jade_Primordial.webp","Futsu.webp"], "armas4": ["Objeto_Colmillo_Lupino.webp","Requiem_Abisal.webp","Objeto_Espada_de_Favonius.webp"]},
    {"nombre": "Durin",  "imagen": "Durin.jpg", "region": "Mondstadt", "rol": "Suport/Buffer", "elemento": "Pyro", "reacciones": "Sobrecargados/Quemadura", "talentos": "Habilidad Definitiva > Habilidad Elemental > Ataque Básico", "estadisticas": "4000 ataque %, 1500 defensa %, 1000 vida %, 200 Recarga de Energía, 50 Maestría Elemental, 100 Daño crítico %, 40 Probabilidad Crítica", "artefactos": ["DiadelosVientos.webp","SueñosAureos.webp","Objeto_Flor_en_Llamas_de_la_Bruja.webp"], "equipos": [["Venti.jpg","Faruzan.jpg","Durin.jpg","Bennett.jpg"],["Kinich.jpg","Emilie.jpg","Durin.jpg","Bennett.jpg"],["Kinich.jpg","Emilie.jpg","Durin.jpg","Iansan.jpg"]], "armas5": ["DurinEspada.webp","Objeto_Cortador_de_Jade_Primordial.webp","ReflejodelasTinieblas.webp"], "armas4": ["Objeto_Colmillo_Lupino.webp","Rugido.webp","Requiem_Abisal.webp"]},
    {"nombre": "Nicole",  "imagen": "Nicole.jpg", "region": "Mondstadt", "rol": "Buffer/Escudo", "elemento": "Pyro", "reacciones": "Quemadura/Sobrecargados", "talentos": "Habilidad Definitiva > Habilidad Elemental > Ataque Básico", "estadisticas": "2500 ataque %, 1500 defensa %, 1000 vida %, 180 Recarga de Energía, 200 Maestría Elemental, 200 Daño crítico %, 90 Probabilidad Crítica", "artefactos": ["Dadiva.webp","PergaminoHeroe.webp","RitualDeLaNobleza.webp"], "equipos": [["Varka.jpg","Prune.jpg","Nicole.jpg","Bennett.jpg"],["Varka.jpg","Prune.jpg","Nicole.jpg","Durin.jpg"],["Venti.jpg","Prune.jpg","Nicole.jpg","Durin.jpg"]], "armas5": ["Heptadas.webp","CandadoTerrenal.webp","ReverberacionGrulla.webp"], "armas4": ["OjodelJuramento.webp","Hakushin.webp","FluenciaImpoluta.webp"]},
    {"nombre": "Xiangling",  "imagen": "Xiangling.jpg", "region": "text", "rol": "Sub dps", "elemento": "Pyro", "reacciones": "Quemadura/Sobrecargados/Derretidos", "talentos": "Habilidad Definitiva > Habilidad Elemental > Ataque Básico", "estadisticas": "3000 ataque %, 1500 defensa %, 1000 vida %, 200 Recarga de Energía, 200 Maestría Elemental, 200 Daño crítico %, 90 Probabilidad Crítica", "artefactos": ["EmblemadelDestino.webp","Objeto_Flor_en_Llamas_de_la_Bruja.webp","SueñosAureos.webp"], "equipos": [["Tartaglia.jpg","Xiangling.jpg","Kazuha.jpg","Bennett.jpg"],["Kokomi.jpg","Xiangling.jpg","Kazuha.jpg","Bennett.jpg"],["Xingchiu.jpg","Xiangling.jpg","Sacarosa.jpg","Bennett.jpg"]], "armas5": ["ArenasEscarlatas.webp","Lumidulce.webp","Homa.webp"], "armas4": ["LaCaptura.webp","LanzadelDuelo.webp","PerdiciondelDragon.webp"]},
    {"nombre": "Xinyan",  "imagen": "Xinyan.jpg", "region": "text", "rol": "Escudo/Main dps", "elemento": "Pyro", "reacciones": "Sobrecargados/Derretidos", "talentos": "Habilidad Definitiva > Habilidad Elemental > Ataque Básico", "estadisticas": "3000 ataque %, 2000 defensa %, 2000 vida %, 180 Recarga de Energía, 200 Maestría Elemental, 200 Daño crítico %, 90 Probabilidad Crítica", "artefactos": ["LlamasAlbinas.webp","EmblemadelDestino.webp","Gladiador.webp"], "equipos": [["Eula.jpg","Beidou.jpg","Xinyan.jpg","Bennett.jpg"],["Razor.jpg","Qiqi.jpg","Xinyan.jpg","Bennett.jpg"],["Fischl.jpg","Kazuha.jpg","Xinyan.jpg","Bennett.jpg"]], "armas5": ["Cornirrojo.webp","OrgulloCelestial.webp","OdadelosPinos.webp"], "armas4": ["ReydelosMares.webp","PrototipoArcaico.webp","MeduladelaSerpiente.webp"]},
    {"nombre": "Hu Tao", "imagen": "HuTao.jpg", "region": "text", "rol": "Main dps", "elemento": "Pyro", "reacciones": "Sobrecargados/Vaporizados", "talentos": "Ataque Básico > Habilidad Definitiva > Habilidad Elemental", "estadisticas": "2500 ataque %, 1500 defensa %, 4000 vida %, 180 Recarga de Energía, 400 Maestría Elemental, 200 Daño crítico %, 90 Probabilidad Crítica", "artefactos": ["Objeto_Flor_en_Llamas_de_la_Bruja.webp","Reminiscencia.webp","SueñosAureos.webp"], "equipos": [["HuTao.jpg","HuTao.jpg","Xingchiu.jpg","Zhongli.jpg"],["HuTao.jpg","Yelan.jpg","Xingchiu.jpg","Zhongli.jpg"],["HuTao.jpg","Xingchiu.jpg","Albedo.jpg","Zhongli.jpg"]], "armas5": ["Homa.webp","ArenasEscarlatas.webp","Lumidulce.webp"], "armas4": ["PerdiciondelDragon.webp","LanzadelDuelo.webp","LaCaptura.webp"]},
    {"nombre": "Yanfei", "imagen": "Yanfei.jpg", "region": "text", "rol": "Main dps", "elemento": "Pyro", "reacciones": "Sobrecargados/Quemadura", "talentos": "Habilidad Elemental > Habilidad Definitiva > Ataque Básico", "estadisticas": "2500 ataque %, 1500 defensa %, 1000 vida %, 170 Recarga de Energía, 200 Maestría Elemental, 200 Daño crítico %, 90 Probabilidad Crítica", "artefactos": ["Objeto_Flor_en_Llamas_de_la_Bruja.webp","SueñosAureos.webp","OrquestaErrante.webp"], "equipos": [["Yanfei.jpg","Yelan.jpg","Nahida.jpg","Zhongli.jpg"],["Yanfei.jpg","Xingchiu.jpg","Kazuha.jpg","Zhongli.jpg"],["Yanfei.jpg","Xingchiu.jpg","Venti.jpg","Zhongli.jpg"]], "armas5": ["Relicario.webp","Supervision.webp","MilNoches.webp"], "armas4": ["FluenciaImpoluta.webp","SinfoniadelosMerodeadores.webp","OjodelJuramento.webp"]},
    {"nombre": "Gaming", "imagen": "Gaming.jpg", "region": "text", "rol": "Main dps", "elemento": "Pyro", "reacciones": "Sobrecargados", "talentos": "Ataque Básico > Habilidad Definitiva > Habilidad Elemental", "estadisticas": "3000 ataque %, 1500 defensa %, 2000 vida %, 200 Recarga de Energía, 250 Maestría Elemental, 200 Daño crítico %, 90 Probabilidad Crítica", "artefactos": ["Objeto_Flor_en_Llamas_de_la_Bruja.webp","CazadorFantasmal.webp","JuramentodelaNoche.webp"], "equipos": [["Gaming.jpg","Ganyu.jpg","Layla.jpg","Xianyun.jpg"],["Gaming.jpg","Xiangling.jpg","Xianyun.jpg","Bennett.jpg"],["Gaming.jpg","Xianyun.jpg","Furina.jpg","Bennett.jpg"]], "armas5": ["CantardelLobo.webp","Cornirrojo.webp","MilSolesAbrasadores.webp"], "armas4": ["MeduladelaSerpiente.webp","SegadoradelaLluvia.webp","SombradelaMarea.webp"]},
    {"nombre": "Yoimiya", "imagen": "Yoimiya.jpg", "region": "text", "rol": "Main dps", "elemento": "Pyro", "reacciones": "Sobrecargados/Vaporizados", "talentos": "Ataque Básico > Habilidad Definitiva > Habilidad Elemental", "estadisticas": "2500 ataque %, 1500 defensa %, 1000 vida %, 200 Recarga de Energía, 200 Maestría Elemental, 200 Daño crítico %, 90 Probabilidad Crítica", "artefactos": ["Reminiscencia.webp","Objeto_Flor_en_Llamas_de_la_Bruja.webp","SueñosAureos.webp"], "equipos": [["Yoimiya.jpg","Xingchiu.jpg","Yunjin.jpg","Zhongli.jpg"],["Yoimiya.jpg","Ayato.jpg","Yunjin.jpg","Zhongli.jpg"],["Yoimiya.jpg","Yelan.jpg","Yunjin.jpg","Zhongli.jpg"]], "armas5": ["AgitadordelRelampago.webp","AquaSimulacra.webp","NumerodeMagia.webp"], "armas4": ["SolAbrasador.webp","Objeto_Ultimo_Acorde.webp","PrototipoluzdeLuna.webp"]},
    {"nombre": "Thoma", "imagen": "Thoma.jpg", "region": "text", "rol": "Escudo/Suport", "elemento": "Pyro", "reacciones": "Sobrecargados", "talentos": "Habilidad Elemental > Habilidad Definitiva > Ataque Básico", "estadisticas": "3000 ataque %, 1500 defensa %, 2500 vida %, 180 Recarga de Energía, 300 Maestría Elemental, 170 Daño crítico %, 70 Probabilidad Crítica", "artefactos": ["FlorOlvidada.webp","SueñosAureos.webp","OrquestaErrante.webp"], "equipos": [["Ayato.jpg","Yelan.jpg","Nahida.jpg","Thoma.jpg"],["Xingchiu.jpg","Yelan.jpg","Nahida.jpg","Thoma.jpg"],["HuTao.jpg","Xingchiu.jpg","Chongyun.jpg","Thoma.jpg"]], "armas5": ["Halcon.webp","ArenasEscarlatas.webp","Homa.webp"], "armas4": ["Kitain.webp","LanzadeFavonius.webp","PerdiciondelDragon.webp"]},
    {"nombre": "Dehya", "imagen": "Dehya.jpg", "region": "text", "rol": "Sub dps/Main dps", "elemento": "Pyro", "reacciones": "Quemadura", "talentos": "Habilidad Definitiva > Habilidad Elemental > Ataque Básico", "estadisticas": "3000 ataque %, 1500 defensa %, 1000 vida %, 200 Recarga de Energía, 200 Maestría Elemental, 200 Daño crítico %, 90 Probabilidad Crítica", "artefactos": ["EmblemadelDestino.webp","vurukasha.webp","Objeto_Flor_en_Llamas_de_la_Bruja.webp"], "equipos": [["Ganyu.jpg","Dehya.jpg","Nahida.jpg","Bennett.jpg"],["Ganyu.jpg","Dehya.jpg","Kazuha.jpg","Bennett.jpg"],["Ayaka.jpg","Dehya.jpg","Kazuha.jpg","Bennett.jpg"]], "armas5": ["MardeJuncos.webp","Cornirrojo.webp","Verdicto.webp"], "armas4": ["MeduladelaSerpiente.webp","MailedFlower.webp","SegadoradelaLluvia.webp"]},
    {"nombre": "Lyney", "imagen": "Lyney.jpg", "region": "text", "rol": "Main dps", "elemento": "Pyro", "reacciones": "Vaporizados", "talentos": "Habilidad Definitiva > Habilidad Elemental > Ataque Básico", "estadisticas": "3000 ataque %, 1500 defensa %, 3000 vida %, 190 Recarga de Energía, 250 Maestría Elemental, 200 Daño crítico %, 90 Probabilidad Crítica", "artefactos": ["CazadorFantasmal.webp","Reminiscencia.webp","Objeto_Flor_en_Llamas_de_la_Bruja.webp"], "equipos": [["Lyney.jpg","Xiangling.jpg","Kazuha.jpg","Bennett.jpg"],["Lyney.jpg","Xiangling.jpg","Lynette.jpg","Bennett.jpg"],["Lyney.jpg","Dehya.jpg","Kazuha.jpg","Bennett.jpg"]], "armas5": ["NumerodeMagia.webp","Buitreastral.webp","AquaSimulacra.webp"], "armas4": ["PrototipoluzdeLuna.webp","Objeto_Ultimo_Acorde.webp","SolAbrasador.webp"]},
    {"nombre": "Chevreuse", "imagen": "Chevreuse.jpg", "region": "text", "rol": "Buffer/Healer", "elemento": "Pyro", "reacciones": "Sobrecargados", "talentos": "Habilidad Elemental > Habilidad Definitiva > Ataque Básico", "estadisticas": "1500 ataque %, 1500 defensa %, 4000 vida %, 180 Recarga de Energía, 200 Maestría Elemental, 200 Daño crítico %, 90 Probabilidad Crítica", "artefactos": ["RitualDeLaNobleza.webp","PergaminoHeroe.webp","PerlaOceanica.webp"], "equipos": [["Cyno.jpg","Chevreuse.jpg","Xiangling.jpg","Bennett.jpg"],["Raiden.jpg","Chevreuse.jpg","Xiangling.jpg","Bennett.jpg"],["Yoimiya.jpg","Chevreuse.jpg","Raiden.jpg","Bennett.jpg"]], "armas5": ["SinfonistadeAromas.webp","LuzdelSegador.webp","Homa.webp"], "armas4": ["LaCaptura.webp","LanzadelDuelo.webp","LanzadeFavonius.webp"]},
    {"nombre": "Mavuika", "imagen": "Mavuika.jpg", "region": "text", "rol": "Main dps/Sub dps", "elemento": "Pyro", "reacciones": "Sobrecargados/Derretidos/Quemadura/Vaporizados", "talentos": "Habilidad Definitiva > Habilidad Elemental > Ataque Básico", "estadisticas": "3000 ataque %, 1500 defensa %, 1000 vida %, 0 Recarga de Energía, 450 Maestría Elemental, 200 Daño crítico %, 90 Probabilidad Crítica", "artefactos": ["Obsidiana.webp","PergaminoHeroe.webp","CazadorFantasmal.webp"], "equipos": [["Mavuika.jpg","Ororon.jpg","Chevreuse.jpg","Bennett.jpg"],["Mavuika.jpg","Furina.jpg","Xilonen.jpg","Bennett.jpg"],["Mavuika.jpg","Furina.jpg","Citlali.jpg","Bennett.jpg"]], "armas5": ["MilSolesAbrasadores.webp","Cornirrojo.webp","Verdicto.webp"], "armas4": ["MailedFlower.webp","MeduladelaSerpiente.webp","SombradelaMarea.webp"]},
]


def PyroView(page: ft.Page, user: dict, on_volver=None):
    return _ElementoView(page, user, on_volver, "Pyro", "#ef4444", PERSONAJES)


def _ElementoView(page, user, on_volver, titulo, color, personajes):
    detalle = ft.Container(expand=True, visible=False)

    def abrir(p):
        detalle.content = PersonajeDetalle(page, p, on_volver=volver_grid)
        detalle.visible = True
        grid_view.visible = False
        page.update()

    def volver_grid():
        detalle.visible = False
        detalle.content = None
        grid_view.visible = True
        page.update()

    def cubito(p):
        return ft.Container(
            width=100, height=120,
            border_radius=14,
            bgcolor="#1e0a3c",
            border=ft.Border.all(1, "#4c1d95"),
            ink=True,
            on_click=lambda e, per=p: abrir(per),
            content=ft.Column(
                spacing=6,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Image(src=p.get("imagen") or "placeholder.png", width=56, height=56, fit="contain",
                             error_content=ft.Container(width=56, height=56, bgcolor="#2a1a4e", border_radius=8)),
                    ft.Text(p["nombre"], size=11, color="#e9d5ff", weight=ft.FontWeight.W_600,
                            text_align=ft.TextAlign.CENTER),
                ],
            ),
        )

    cubitos = [cubito(p) for p in personajes]
    filas = []
    for i in range(0, len(cubitos) - 1, 2):
        filas.append(ft.Row(controls=[cubitos[i], cubitos[i + 1]], spacing=14,
                            alignment=ft.MainAxisAlignment.CENTER))
    if len(cubitos) % 2 != 0:
        filas.append(ft.Row(controls=[cubitos[-1]], alignment=ft.MainAxisAlignment.CENTER))

    grid_view = ft.Container(
        expand=True,
        bgcolor="#0d001f",
        padding=20,
        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=14,
            controls=[
                ft.Text(f"Personajes {titulo}", size=16, color=color, weight=ft.FontWeight.BOLD),
                *filas,
            ],
        ),
    )

    topbar = ft.Container(
        bgcolor="#12002e",
        padding=ft.Padding.symmetric(horizontal=16, vertical=10),
        content=ft.Row(controls=[
            ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#c084fc",
                          on_click=lambda e: on_volver() if on_volver else None),
            ft.Text(titulo, size=18, weight=ft.FontWeight.BOLD, color=color),
        ], spacing=8),
    )

    return ft.Column(
        spacing=0, expand=True,
        controls=[topbar, ft.Stack(expand=True, controls=[grid_view, detalle])],
    )
