import flet as ft
from pages.routes import views_handler

class Main(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        page.title = "Whodunit?"
        page.window.width = 400
        page.window.height = 700
        page.window.resizable = False
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.page.spacing = 0

        self.page.on_route_change = self.route_change
        self.page.go('/signup')
    
    def route_change(self, route):
        print(self.page.route)
        self.page.views.clear()
        self.page.views.append(
            views_handler(self.page)[self.page.route]
        )
        self.page.update()

    def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)



ft.app(target=Main)
