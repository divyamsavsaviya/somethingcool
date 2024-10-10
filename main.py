import flet as ft
from neurum import Neurum
from chat_ui import create_chat_ui
from chat_logic import ChatLogic

def main(page: ft.Page):
    neurum = Neurum('vansh')
    chat_logic = ChatLogic(neurum)
    
    chat_container = create_chat_ui(page, chat_logic.send_message)
    
    page.add(chat_container)
    page.title = "AI Software Engineering Assistant"
    page.update()

if __name__ == "__main__":
    ft.app(target=main)