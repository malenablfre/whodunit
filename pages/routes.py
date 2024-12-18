import flet as ft
from pages.home import home
from pages.login import login
from pages.gameslots import gameslots


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
        '/gameslots':ft.View(
            route='/gameslots',
            controls=[
                gameslots(page)
            ]
        )
    }