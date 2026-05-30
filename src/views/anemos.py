import flet as ft
from views.PersonajeDetalle import PersonajeDetalle

PERSONAJES = [
    {"nombre": "Jean",  "imagen": "", "region": "Mondstadt", "elemento": "Anemo", "rol": "Healer", "reacciones": "Torbellinos", "talentos": "Habilidad Definitiva > Habilidad Elemental > Ataque Básico ", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 2",  "imagen": "", "region": "text", "elemento": "Anemo", "rol": "text", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 3",  "imagen": "", "region": "text", "elemento": "Anemo", "rol": "text", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 4",  "imagen": "", "region": "text", "elemento": "Anemo", "rol": "text", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 5",  "imagen": "", "region": "text", "elemento": "Anemo", "rol": "text", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 6",  "imagen": "", "region": "text", "elemento": "Anemo", "rol": "text", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 7",  "imagen": "", "region": "text", "elemento": "Anemo", "rol": "text", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 8",  "imagen": "", "region": "text", "elemento": "Anemo", "rol": "text", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 9",  "imagen": "", "region": "text", "elemento": "Anemo", "rol": "text", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 10", "imagen": "", "region": "text", "elemento": "Anemo", "rol": "text", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 11", "imagen": "", "region": "text", "elemento": "Anemo", "rol": "text", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 12", "imagen": "", "region": "text", "elemento": "Anemo", "rol": "text", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 13", "imagen": "", "region": "text", "elemento": "Anemo", "rol": "text", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 14", "imagen": "", "region": "text", "elemento": "Anemo", "rol": "text", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 15", "imagen": "", "region": "text", "elemento": "Anemo", "rol": "text", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 16", "imagen": "", "region": "text", "elemento": "Anemo", "rol": "text", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 17", "imagen": "", "region": "text", "elemento": "Anemo", "rol": "text", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 18", "imagen": "", "region": "text", "elemento": "Anemo", "rol": "text", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
]


def AnemoView(page: ft.Page, user: dict, on_volver=None):
    from views.pyros import _ElementoView
    return _ElementoView(page, user, on_volver, "Anemo", "#6ee7b7", PERSONAJES)
