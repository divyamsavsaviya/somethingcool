import flet as ft
import pyperclip

def create_code_block_with_copy(code, language=""):
    code_block = ft.TextField(
        value=code,
        read_only=True,
        multiline=True,
        min_lines=3,
        max_lines=10,
        border_color=ft.colors.GREY_300,
        bgcolor=ft.colors.GREY_100,
    )
    
    def copy_code(e):
        pyperclip.copy(code)
        e.control.icon = ft.icons.CHECK
        e.control.update()
        e.page.update()
    
    copy_button = ft.IconButton(
        icon=ft.icons.COPY,
        tooltip="Copy code",
        on_click=copy_code
    )
    
    return ft.Column([
        ft.Row([
            ft.Text(f"Language: {language}", size=12, color=ft.colors.GREY_700),
            copy_button
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        code_block
    ])

def create_chat_ui(page: ft.Page, message_callback):
    chat_list = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True
    )

    message_input = ft.TextField(
        hint_text="Type your coding question here...",
        expand=True,
        border_radius=10,
        on_submit=lambda e: message_callback(e.control.value, chat_list),
        bgcolor=ft.colors.TRANSPARENT
    )

    send_button = ft.IconButton(
        icon=ft.icons.SEND,
        on_click=lambda _: message_callback(message_input.value, chat_list),
        icon_color=ft.colors.WHITE
    )

    input_row = ft.Row(
        controls=[message_input, send_button],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    return ft.Container(
        content=ft.Column(
            controls=[chat_list, input_row],
            spacing=10
        ),
        expand=True,
        padding=20
    )