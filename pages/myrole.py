import flet as ft

class role(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.role = "Unschuldig"
        self.description = "Du bist ein normaler Teilnehmer ohne besondere Fähigkeiten. Dein Ziel ist es, die Mörder zu entlarven und zu eliminieren."

        

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
            ft.Container(height=50),
        ft.Container(
            ft.Column(
                spacing=0,
                scroll=ft.ScrollMode.HIDDEN,
                controls=[
                    ft.Container(),
                    ft.Container(
                        content=ft.Text(value=self.role, size= 25, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=ft.margin.only(left=50, right=50),
                        padding=10,
                    ),

                    ft.Container(
                        content=ft.Text(value=self.description, size= 15, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=ft.margin.only(left=60, right=60),
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.TRANSPARENT,
                        border=ft.border.all(width=1, color="#C72C42"),
                        width=250,
                        height=110,
                        border_radius=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="Notizen", size= 25, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=ft.margin.only(left=50, right=50, top=25),
                        padding=10,
                    ),

                    ft.Container(
                        content=ft.TextField(
                            multiline=True,
                            border="none",
                            cursor_color="#C72C42",
                            hint_text="...",
                            hint_style=ft.TextStyle(
                                font_family= "Times New Roman",
                                color="#C72C42"
                            ),
                            text_style=ft.TextStyle(
                                font_family= "Times New Roman",
                                color="#C72C42"
                            )
                                ),
                        margin=ft.margin.only(left=60, right=60),
                        padding=ft.padding.only(left=10, right=10),
                        bgcolor=ft.colors.TRANSPARENT,
                        border=ft.border.all(width=1, color="#C72C42"),
                        width=250,
                        height=110,
                        border_radius=10,
                    ),

                    
                ],
                alignment = ft.MainAxisAlignment.CENTER,
            ),
            height=600,
            alignment=ft.alignment.center,
            
        ),
        ]),
        
        ft.Container(
            content=ft.FloatingActionButton(icon=ft.Icons.ADD, bgcolor="#EE4540"),
            alignment=ft.alignment.bottom_right,
            margin=ft.margin.only(top=550, right=20)
        ),

        ft.Column(
            controls=[
                ft.Container(),
                ft.Row(
                    controls=[
                        ft.Container(content=ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#EE4540", on_click=lambda _: self.page.go("/signup")),),
                        ft.Container(content=ft.Text(value="Meine Rolle", size= 35, font_family= "Times New Roman", weight= "bold", color="#EE4540"),),
                        ft.Container(content=ft.IconButton(ft.Icons.MENU, icon_color="#EE4540", on_click=lambda _: self.page.go("/signup")),),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )
            ]
        ),
        
        
        ])
        return page
    
    # def openalert(self):
    #     self.page.open(self.dlg_modal)


    # def alertdialog(self):
    #     self.dlg_modal = ft.AlertDialog(
    #     modal=True,
    #     title=ft.Text("Achtung!"),
    #     content=ft.Text("Bist du sicher, dass niemand auf dein Handy schauen kann?"),
    #     actions=[
    #         ft.TextButton("Yes", on_click=self.page.close(self.dlg_modal)),
    #         ft.TextButton("No", on_click=lambda _: self.page.go("/")),
    #     ]
    #     )