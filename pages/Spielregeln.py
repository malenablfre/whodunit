import flet as ft  

class Spielregeln(ft.UserControl):
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
                        content=ft.Text(value="1.   Verdacht notieren: ", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="Wenn Verdacht besteht, muss er in den Notizen eingetragen werden.", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="2.   Veröffentlichung der Liste: ", size= 22, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                    ),
                    
                    ft.Container(
                        content=ft.Text(value="Die Liste wird täglich um 18 Uhr veröffentlicht.", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="3.   Eintrag nach Tod:", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="Direkt nach dem Tod muss der Name eingetragen werden.", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=10,
                    ),
        
                    ft.Container(
                        content=ft.Text(value="4.   Meeting Button: ", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                    ),

                    ft.Container(
                    content=ft.Text(value="Bei Betätigung des Meeting Buttons wird die Liste direkt veröffentlicht ", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="5.   Voting Liste: ", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="Die Voting Liste wird vom Host geführt", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="6.   Emergency Meeting: ", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="Ein Emergency Meeting muss spätestens um 18 Uhr einberufen werden.", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="7.   Tötungsstopp bei Meeting:", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="Sobald ein Emergency Meeting einberufen wurde, darf nicht mehr getötet werden, bis das Meeting abgeschlossen ist.", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="8.   Missbrauch des Emergency Buttons:", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="Sobald ein Emergency Meeting einberufen wurde, darf nicht mehr getötet werden, bis das Meeting abgeschlossen ist.", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="10.  Tötungsziel:", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="Innerhalb einer Woche müssen so viele Leute getötet werden, wie es Mörder gibt.", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="11.  Mordregel:", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="Ein Mord darf nur stattfinden, wenn sich zwei Lebende in einem Raum befinden (Mörder und Opfer).", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="12.  Kein Doppel-Kill:", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="Es darf kein Doppel-Kill stattfinden.", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="13.  Ziel des Spiels: ", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="Für Mörder: alle anderen Rollen töten ohne aufzufliegen; Für alle anderen Rollen: alle Mörder identifizieren und raus voten ", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=10,
                    ),

                    # ft.Container(
                    #     content=ft.Text(value="14.    Staatsgeheimnis:", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                    #     margin=10,
                    # ),

                    # ft.Container(
                    #     content=ft.Text(value="Der Anwalt muss private Notizen über sich selbst führen, aber in seinen Anwaltsnotizen über seine Mandanten schreiben.", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336"),
                    #     margin=10,
                    # ),
                    # ft.Container(
                    #     content=ft.Text(value="15.    Geisterregel:", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                    #     margin=10,
                    # ),

                    # ft.Container(
                    #     content=ft.Text(value="Ein Geist darf keine Namen nennen.", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336"),
                    #     margin=10,
                    # ),

                    ft.Container(
                        content=ft.Text(value="", size= 25, font_family= "Times New Roman", weight= "bold", color="#C72C42"),
                        margin=10,
                    ),

                    ft.Container(
                        content=ft.Text(value="", size= 20, font_family= "Times New Roman", weight= "bold", color="#801336"),
                        margin=10,
                    ),
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
                            ft.Container(content=ft.Text(value="Die 13 Gebote", size= 35, font_family= "Times New Roman", weight= "bold", color="#EE4540"),),
                            ft.Container(content=ft.IconButton(ft.Icons.MENU, icon_color="#EE4540", on_click=lambda _: self.page.go("/Uebersicht")),),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    )
                ]
            )
    ])
            

            return page