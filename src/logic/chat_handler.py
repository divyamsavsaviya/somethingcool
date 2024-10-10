import flet as ft

class ChatHandler:
    def __init__(self, ai_service):
        self.ai_service = ai_service
        self.conversation_history = []

    def process_message(self, message, chat_list):
        if message:
            self._add_message_to_chat("User", message, chat_list)
            
            context = "\n".join(self.conversation_history)
            chain_of_thoughts, final_response = self.ai_service.generate_response(context, message)
            
            self._add_chain_of_thoughts_to_chat(chain_of_thoughts, chat_list)
            self._add_message_to_chat("AI", final_response, chat_list)

    def _add_message_to_chat(self, sender, message, chat_list):
        formatted_message = f"{sender}: {message}"
        self.conversation_history.append(formatted_message)
        chat_list.controls.append(ft.Text(formatted_message))
        chat_list.update()

    def _add_chain_of_thoughts_to_chat(self, thoughts, chat_list):
        for thought in thoughts:
            chat_list.controls.append(ft.Text(thought, italic=True, color=ft.colors.GREY_400))
        chat_list.update()