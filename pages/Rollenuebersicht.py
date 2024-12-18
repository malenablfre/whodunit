import flet as ft

class Rollenuebersicht(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

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
                        content=ft.Text(value="Unschuldiger", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="Der Unschuldige ist ein normaler Teilnehmer ohne besondere Fähigkeiten. Sein Ziel ist es, die Mörder zu entlarven und zu eliminieren.", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336" ),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="Mörder", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="Der Mörder kann jede andere Rolle im Spiel töten. Ziel ist es dabei unerkannt zu bleiben.", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=10,  
                    ),
                    # ft.Container(
                    #     content=ft.Text(value="Jäger", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                    #     margin=10,
                    # ),

                    # ft.Container(
                    #     content=ft.Text(value="Der Jäger kann, wenn er raus gevotet wird, zwei Personen mit in den Tod ziehen. Sein Ziel ist es, die Mörder zu entlarven und zu eliminieren.", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336" ),
                    #     margin=10,
                    # ),
                    # ft.Container(
                    #     content=ft.Text(value="Spion", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                    #     margin=10,
                    # ),

                    # ft.Container(
                    #     content=ft.Text(value="Der Spion darf bis zu dreimal täglich auf die geheime Liste der Toten schauen, um Informationen über die toten Spieler zu sammeln. Sein Ziel ist es, die Mörder zu entlarven und zu eliminieren.", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336" ),
                    #     margin=10,
                    # ),
                    # ft.Container(
                    #     content=ft.Text(value="Gerichtsmediziner", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                    #     margin=10,
                    # ),

                    # ft.Container(
                    #     content=ft.Text(value="Der Gerichtsmediziner kann nach Veröffentlichung der Todesliste die Notizen der Toten und einen Zeitrahmen von drei Stunden um den möglichen Todeszeitpunkt einsehen. Sein Ziel ist es, die Mörder zu entlarven und zu eliminieren.", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336" ),
                    #     margin=10,
                    # ),
                    # ft.Container(
                    #     content=ft.Text(value="Priester", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                    #     margin=10,
                    # ),

                    # ft.Container(
                    #     content=ft.Text(value="Der Priester kann nach der Veröffentlichung der Todesliste (zu Beginn eines neuen Spieltages) eine Person schützen. Kein Spieler darf doppelt in einer Runde geschützt werden. Sein Ziel ist es, die Mörder zu entlarven und zu eliminieren.", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336" ),
                    #     margin=10,
                    # ),
                    # ft.Container(
                    #     content=ft.Text(value="Doppelgänger", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                    #     margin=10,
                    # ),

                    # ft.Container(
                    #     content=ft.Text(value="Der Doppelgänger kann die Rolle einer anderen Person kopieren.o	Er wählt zufällig eine Person aus und übernimmt deren Rolle, ohne vorher deren Identität zu kennen.", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336" ),
                    #     margin=10,
                    # ),
                    # ft.Container(
                    #     content=ft.Text(value="Geist", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                    #     margin=10,
                    # ),

                    # ft.Container(
                    #     content=ft.Text(value="Der Geist hat die Möglichkeit, eine Nachricht von maximal 60 Zeichen zu hinterlassen, die nach seinem Tod veröffentlicht wird, er darf aber keine Namen nennen. Sein Ziel ist es, die Mörder zu entlarven und zu eliminieren", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336" ),
                    #     margin=10,
                    # ),
                    # ft.Container(
                    #     content=ft.Text(value="Anwalt", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                    #     margin=10,
                    # ),

                    # ft.Container(
                    #     content=ft.Text(value="Der Anwalt wählt einen Angeklagten, den er bis zum Tod des Angeklagten verteidigen muss, wobei die Rolle des Angeklagten egal ist. Der Anwalt muss bei der Abstimmung dieselbe Person wählen, wie sein Mandant, selbst wenn der Mandant ein Mörder ist.", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336" ),
                    #     margin=10,
                    # ),
                    # ft.Container(
                    #     content=ft.Text(value="", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                    #     margin=10,
                    # ),

                    # ft.Container(
                    #     content=ft.Text(value="", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336" ),
                    #     margin=10,
                    # ),

                ],
                alignment = ft.MainAxisAlignment.CENTER,
            ), 
            height=600,
            alignment=ft.alignment.center, 
        ),
        ]), 


            ft.Column(
                controls=[
                    ft.Container(),
                    ft.Row(
                        controls=[
                            ft.Container(content=ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#EE4540", on_click=lambda _: self.page.go("/Uebersicht")),),
                            ft.Container(content=ft.Text(value="Rollenübersicht", size= 35, font_family= "Times New Roman", weight= "bold", color="#EE4540"),),
                            ft.Container(content=ft.IconButton(ft.Icons.MENU, icon_color="#EE4540", on_click=lambda _: self.page.go("/Uebersicht")),),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    )
                ]
            )
    ])
            

        return page