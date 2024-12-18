import flet as ft

class gameslots(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        head_container = ft.Column(
            spacing=0,
            controls=[
                ft.Container(
                        content=ft.Text(value="Deine Spiele", size= 50, font_family= "Times New Roman", weight= "bold", color="#EE4540"),
                        alignment=ft.alignment.center
                    ),

                    ft.Container(
                        content=ft.Text(value="Spiel beitreten:", size= 25, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=0,
                        alignment=ft.alignment.center
                    )
            ],
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        body_container = ft.Column(
            spacing=0,
            controls=[
                ft.Container(
                        content=ft.Text(value="Slot 1", size= 20, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                        alignment=ft.alignment.center,
                        bgcolor="#510A32",
                        width=250,
                        height=50,
                        border_radius=10,
                        on_click=lambda _: self.page.go("/login")
                    ),

                    ft.Container(
                        content=ft.Text(value="Slot 2", size= 20, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                        alignment=ft.alignment.center,
                        bgcolor="#510A32",
                        width=250,
                        height=50,
                        border_radius=10,
                        #on_click=lambda _: self.page.go("/login")
                    ),

                    ft.Container(
                        content=ft.Text(value="Slot 3", size= 20, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                        alignment=ft.alignment.center,
                        bgcolor="#510A32",
                        width=250,
                        height=50,
                        border_radius=10,
                        #on_click=lambda _: self.page.go("/login")
                    )
            ],
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        page_container = ft.Container(
            ft.Column(
                spacing=40,
                controls=[
                    head_container,
                    body_container
                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
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
        
        page = ft.Stack(
            controls=[
                page_container
            ]
        )

        return page