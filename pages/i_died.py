import flet as ft

class dead(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

        self.place_of_death: ft.TextField = ft.TextField(label='Tippe den Ort...',
            label_style=ft.TextStyle(
            font_family= "Times New Roman",
                color="#EE4540"
            ),
            text_style=ft.TextStyle(
                font_family= "Times New Roman",
                color="#EE4540"
            ),
            text_align=ft.TextAlign.LEFT,
            width=300,
            border_color="#510A32",
            border_radius=10,
            cursor_color="#EE4540"
            )
        self.submit_button = ft.ElevatedButton(text='Abschicken',
            style=ft.ButtonStyle(
                color="#EE4540",
                bgcolor="#510A32",
                text_style=ft.TextStyle(
                    font_family= "Times New Roman",
                    color="#EE4540"
                ),
                overlay_color="#801336",
            ),
            width=200,
            disabled=True
        )

        self.place_of_death.on_change = self.validate

    def build(self):
        page = ft.Stack([
        ft.Container(   
            width=400,
            height=700,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#2D142C","#510A32"]),
            border_radius=10,
            alignment=ft.alignment.center
            ),
        
        ft.Column(
            controls=[
                ft.Container(height=250),
                ft.Container(
                    content=ft.Text(value="Wo bist du gestorben?", size= 30, font_family= "Times New Roman", weight= "bold", color="#EE4540"),
                        #margin=ft.margin.only(left=50, right=50),
                        padding=10,
                ),
                ft.Container(
                    content=self.place_of_death
                ),
                ft.Container(
                    content=self.submit_button
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),

        ft.Column(
            controls=[
                ft.Container(),
                ft.Row(
                    controls=[
                        ft.Container(content=ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#EE4540", on_click=lambda _: self.page.go("/role")),),
                        ft.Container(width=150),
                        ft.Container(content=ft.IconButton(ft.Icons.MENU, icon_color="#EE4540", on_click=lambda _: self.page.go("/role")),),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )
            ]
        ),
        
        
        ])
        return page
    
    def validate(self, e: ft.ControlEvent) -> None:
        if all([self.place_of_death.value]):
            self.submit_button.disabled = False
        else:
            self.submit_button.disabled = True

        self.update()