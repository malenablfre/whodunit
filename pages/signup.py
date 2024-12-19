import flet as ft

class signup(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.text_email: ft.TextField = ft.TextField(label='E-Mail',
                                            label_style=ft.TextStyle(
                                                font_family= "Times New Roman",
                                                color="#EE4540"
                                            ),
                                            text_style=ft.TextStyle(
                                                font_family= "Times New Roman",
                                                color="#EE4540"
                                            ),
                                            text_align=ft.TextAlign.LEFT,
                                            width=200,
                                            border_color="#510A32",
                                            border_radius=10,
                                            cursor_color="#EE4540"
                                            )
        self.text_username: ft.TextField = ft.TextField(label='Benutzername',
                                            label_style=ft.TextStyle(
                                                font_family= "Times New Roman",
                                                color="#EE4540"
                                            ),
                                            text_style=ft.TextStyle(
                                                font_family= "Times New Roman",
                                                color="#EE4540"
                                            ),
                                            text_align=ft.TextAlign.LEFT,
                                            width=200,
                                            border_color="#510A32",
                                            border_radius=10,
                                            cursor_color="#EE4540"
                                            )
        self.text_password: ft.TextField = ft.TextField(label='Passwort',
                                            label_style=ft.TextStyle(
                                                font_family= "Times New Roman",
                                                color="#EE4540"
                                            ),
                                            text_style=ft.TextStyle(
                                                font_family= "Times New Roman",
                                                color="#EE4540"
                                            ),
                                            text_align=ft.TextAlign.LEFT,
                                            width=200,
                                            border_color="#510A32",
                                            border_radius=10,
                                            cursor_color="#EE4540",
                                            password=True,
                                            )
        self.checkbox_signup: ft.Checkbox = ft.Checkbox(label='Ich stimme allem zu',
                                            value=False,
                                            label_style=ft.TextStyle(
                                                font_family= "Times New Roman",
                                                color="#EE4540"
                                            ),
                                            check_color="#EE4540",
                                            fill_color="#510A32",
                                            overlay_color="#801336",
                                            border_side=ft.BorderSide(color="#EE4540", width=1)
                                            )
        self.button_submit: ft.ElevatedButton = ft.ElevatedButton(text='Registrieren',
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
        self.button_account: ft.TextButton = ft.TextButton(text="Du hast schon einen Account?",
                                              style=ft.ButtonStyle(
                                                  text_style=ft.TextStyle(
                                                      size=15,
                                                      font_family= "Times New Roman",
                                                      decoration=ft.TextDecoration.UNDERLINE,
                                                      decoration_color="#EE4540",
                                                      ),
                                                  color="#EE4540",
                                                  overlay_color="#801336"
                                                  ),
                                              on_click=lambda _: self.page.go("/login")
                                              )

        self.checkbox_signup.on_change = self.validate
        self.text_email.on_change = self.validate
        self.text_password.on_change = self.validate
        self.text_username.on_change = self.validate
        self.button_submit.on_click = self.submit


    def validate(self, e: ft.ControlEvent) -> None:
        special_characters = set("/!@#$%^&*(),.?\":|<>")
        password = self.text_password.value
        # general validation 
        if all([
            self.text_username.value and
            self.text_email.value and
            self.checkbox_signup.value and
            password and
            len(password) >= 7 and
            any(char in special_characters for char in password) and
            self.valid_email(self.text_email.value)
            ]):
            self.button_submit.disabled = False
        else:
            self.button_submit.disabled = True

        # password validation/error text
        if len(password) < 7 and len(password) != 0:
            self.text_password.error_text = "Passwort zu kurz"
        elif not any(char in special_characters for char in password) and len(password) != 0:
            self.text_password.error_text = "Min. ein Sonderzeichen"
        else:
            self.text_password.error_text = ""
        # email validation/error text
        if not self.valid_email(self.text_email.value) and len(self.text_email.value) != 0:
            self.text_email.error_text = "E-Mail ungültig"
        else:
            self.text_email.error_text = ""

        self.update()

    def valid_email(self, email):
        if email.count('@') != 1:
            return False
        local_part, domain_part = email.split('@')
        if not local_part or not domain_part:
            return False
        if '.' not in domain_part:
            return False
        domain_name, domain_suffix = domain_part.rsplit('.', 1)
        if not domain_name or not domain_suffix:
            return False
        return True

    def submit(self, e: ft.ControlEvent) -> None:
        print("Email:", self.text_email.value)
        print("Username:", self.text_username.value)
        print("Password:", self.text_password.value)
        self.page.go("/")


    def build(self):
        page = ft.Container(
            ft.Column(
                spacing=0,
                controls=[
                    ft.Container(
                        content=ft.Text(value="Whodunit?", size= 50, font_family= "Times New Roman", weight= "bold", color="#EE4540"),
                    ),

                    ft.Container(
                        content=ft.Text(value="Signup", size= 25, font_family= "Times New Roman", weight= "bold", color="#801336"),
                    ),

                    ft.Container(
                        ft.Column(
                            controls=[
                                self.text_email,
                                self.text_username,
                                self.text_password,
                                ft.Container(content=self.checkbox_signup, width=200),
                                self.button_submit,
                                self.button_account
                            ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment= ft.CrossAxisAlignment.CENTER
                        ),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center
                    ),
                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment= ft.CrossAxisAlignment.CENTER
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