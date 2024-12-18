import flet as ft
from pages.routes import views_handler

def main(page: ft.Page):
    page.title = "home"
    page.window.width = 400
    page.window.height = 700
    page.window.resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #page.bgcolor = "#2D142C"
    
    def route_change(route):
        print(page.route)
        page.views.clear()
        page.views.append(
            views_handler(page)[page.route]
        )
        page.update()


    page.on_route_change = route_change
    page.go('/')

ft.app(target=main)
