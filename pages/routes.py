import flet as ft
from pages.home import home
from pages.login import login
from pages.signup import signup


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
        '/signup':ft.View(
            route='/signup',
            controls=[
                signup(page)
            ]
        ),
    }