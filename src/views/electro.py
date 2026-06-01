import flet as ft
from views.PersonajeDetalle import PersonajeDetalle

PERSONAJES = [
    {"nombre": "Lisa",  "imagen": "lisa.jpg", "region": "text", "rol": "", "elemento": "Electro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Razor",  "imagen": "Razor.jpg", "region": "text", "rol": "", "elemento": "Electro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Fischl",  "imagen": "Fischl.jg", "region": "text", "rol": "", "elemento": "Electro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Beidou",  "imagen": "Beidou.jpg", "region": "text", "rol": "", "elemento": "Electro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Keching",  "imagen": "Keching.jpg", "region": "text", "rol": "", "elemento": "Electro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Shogun Raiden",  "imagen": "Raiden.jpg", "region": "text", "rol": "", "elemento": "Electro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Kujou Sara",  "imagen": "Sara.jpg", "region": "text", "rol": "", "elemento": "Electro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Yae Miko",  "imagen": "Miko.jpg", "region": "text", "rol": "", "elemento": "Electro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Kuki Shinobu",  "imagen": "Shinobu.jpg", "region": "text", "rol": "", "elemento": "Electro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Dori", "imagen": "Dori.jpg", "region": "text", "rol": "", "elemento": "Electro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Cyno", "imagen": "Cyno.jpg", "region": "text", "rol": "", "elemento": "Electro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Sethos", "imagen": "Sethos.jpg", "region": "text", "rol": "", "elemento": "Electro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Clorinde", "imagen": "Clorinde.jpg", "region": "text", "rol": "", "elemento": "Electro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Ororon", "imagen": "Ororon.jpg", "region": "text", "rol": "", "elemento": "Electro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Varesa", "imagen": "Varesa.jpg", "region": "text", "rol": "", "elemento": "Electro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Iansán", "imagen": "Iansan.jpg", "region": "text", "rol": "", "elemento": "Electro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Ineffa", "imagen": "Ineffa.jpg", "region": "text", "rol": "", "elemento": "Electro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Flins", "imagen": "Flins.jpg", "region": "text", "rol": "", "elemento": "Electro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
]


def ElectroView(page: ft.Page, user: dict, on_volver=None):
    from views.pyros import _ElementoView
    return _ElementoView(page, user, on_volver, "Electro", "#c084fc", PERSONAJES)
