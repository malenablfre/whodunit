import flet as ft
from pages.home import home
from pages.login import login
from pages.Uebersicht import Uebersicht 
from pages.Rollenuebersicht import Rollenuebersicht
from pages.Spielregeln import Spielregeln

def views_handler(page):
    return {
        '/':ft.View(
            route='/',
            controls=[
                home(page)
            ]
        ),
        '/login':ft.View(
            route='/login',
            controls=[
                login(page)
            ]
        ),
        '/Uebersicht':ft.View(
            route='/Uebersicht',
            controls=[
                Uebersicht(page)
            ]
        ), 
        '/Rollenuebersicht':ft.View(
            route='/Rollenuebersicht',
            controls=[
                Rollenuebersicht(page)
            ]
        ), 
        '/Spielregeln':ft.View(
            route='/Spielregeln',
            controls=[
                Spielregeln(page)
            ]
        )
    }