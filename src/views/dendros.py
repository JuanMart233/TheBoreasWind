import flet as ft
from views.PersonajeDetalle import PersonajeDetalle

PERSONAJES = [
    {"nombre": "Personaje 1",  "imagen": "", "region": "text", "rol": "", "elemento": "Dendro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 2",  "imagen": "", "region": "text", "rol": "", "elemento": "Dendro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 3",  "imagen": "", "region": "text", "rol": "", "elemento": "Dendro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 4",  "imagen": "", "region": "text", "rol": "", "elemento": "Dendro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 5",  "imagen": "", "region": "text", "rol": "", "elemento": "Dendro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 6",  "imagen": "", "region": "text", "rol": "", "elemento": "Dendro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 7",  "imagen": "", "region": "text", "rol": "", "elemento": "Dendro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 8",  "imagen": "", "region": "text", "rol": "", "elemento": "Dendro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 9",  "imagen": "", "region": "text", "rol": "", "elemento": "Dendro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 10", "imagen": "", "region": "text", "rol": "", "elemento": "Dendro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 11", "imagen": "", "region": "text", "rol": "", "elemento": "Dendro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
    {"nombre": "Personaje 12", "imagen": "", "region": "text", "rol": "", "elemento": "Dendro", "reacciones": "text", "talentos": "text", "estadisticas": "text", "artefactos": ["","",""], "equipos": [["","","",""],["","","",""],["","","",""]], "armas5": ["","",""], "armas4": ["","",""]},
]


def DendroView(page: ft.Page, user: dict, on_volver=None):
    from views.pyros import _ElementoView
    return _ElementoView(page, user, on_volver, "Dendro", "#4ade80", PERSONAJES)
