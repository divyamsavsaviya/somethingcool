import flet as ft
from ui.chat_interface import create_chat_ui
from logic.chat_handler import ChatHandler
from utils.ai_service import NeurumAI

def main(page: ft.Page):
    ai_service = NeurumAI('vansh')
    chat_handler = ChatHandler(ai_service)
    
    chat_container = create_chat_ui(page, chat_handler.process_message)
    
    page.add(chat_container)
    page.title = "AI Coding Assistant"
    page.update()

if __name__ == "__main__":
    ft.app(target=main)