import flet as ft
from neurum import Neurum

n=Neurum(key="vansh")

def main(page: ft.Page):
    page.title = "flet ai"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def submit(e):
        res=n.generate(prompt=promptfield.value)
        promptfield.value=""
        page.update()
    
    promptfield=ft.CupertinoTextField(placeholder_text=">>>prompt", 
                                                   placeholder_style=ft.TextStyle(color="grey"),
                                                   height=50,
                                                   border_radius=10,
                                                   on_submit=submit
                                                   )

    col=ft.Container(ft.Column(controls=[promptfield]),padding=ft.Padding(left=0, right=0, top=850, bottom=0))

    page.add(col)

ft.app(main)