import flet as ft

class Uebersicht(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        page = ft.Container(
                ft.Column(
                spacing=0,
                controls=[
                    ft.Container(
                        content=ft.Text(value="Übersicht", size= 50, font_family= "Times New Roman", weight= "bold", color="#EE4540"),
                        margin=10,
                        padding=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="Rollenübersicht", size= 20, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor="#510A32",
                        width=250,
                        height=50,
                        border_radius=10,
                        ink = True, 
                        on_click=lambda _: self.page.go("/Rollenuebersicht")
                    ),

                    ft.Container(
                        content=ft.Text(value="Spielregeln", size= 20, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor="#510A32",
                        width=250,
                        height=50,
                        border_radius=10,
                        ink= True ,
                        ink_color=ft.colors.RED_900,
                        on_click=lambda _: self.page.go("/Spielregeln")
                    ),
                    ft.Container(
                        content=ft.Text(value="↩", size= 20, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor="#510A32",
                        width=250,
                        height=50,
                        border_radius=10,
                        ink= True ,
                        ink_color=ft.colors.RED_900,
                        on_click=lambda _: self.page.go("/")
                    ),

                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=400,
            height=700,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#2D142C","#510A32"]),
            border_radius=10,
            alignment=ft.alignment.center
        )
        
        return page