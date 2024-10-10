import flet as ft

def create_chat_ui(page: ft.Page, send_message_callback):
    chat_list = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True
    )

    new_message = ft.TextField(
        hint_text="Type your message here...",
        expand=True,
        border_radius=10,
        on_submit=lambda e: send_message_callback(e, new_message, chat_list),
        bgcolor=ft.colors.TRANSPARENT
    )

    send_button = ft.IconButton(
        icon=ft.icons.SEND,
        on_click=lambda e: send_message_callback(e, new_message, chat_list),
        icon_color=ft.colors.WHITE
    )

    input_container = ft.Row(
        controls=[new_message, send_button],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    chat_container = ft.Container(
        content=ft.Column(
            controls=[chat_list, input_container],
            spacing=10
        ),
        expand=True,
        padding=20
    )

    return chat_container