import flet as ft

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