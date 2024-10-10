import flet as ft

class ChatLogic:
    def __init__(self, neurum):
        self.neurum = neurum
        self.conversation_history = []

    def send_message(self, e, new_message, chat_list):
        if new_message.value:
            user_message = f"User: {new_message.value}"
            self.conversation_history.append(user_message)
            chat_list.controls.append(ft.Text(user_message))

            context = "\n".join(self.conversation_history)
            prompt = self._create_prompt(context, new_message.value)
            res = self.neurum.generate(prompt)

            bot_message = f"AI: {res}"
            self.conversation_history.append(bot_message)
            chat_list.controls.append(ft.Text(bot_message))

            new_message.value = ""
            new_message.page.update()

    def _create_prompt(self, context, user_message):
        return f"""SYSTEM PROMPT: You are an advanced AI software engineering assistant, designed to help Python developers rapidly build cross-platform applications. Your primary goal is to enhance developer productivity by providing intelligent code suggestions, generating UI components, offering debugging assistance, and enabling real-time collaboration. Key Capabilities:
- Extensive knowledge of Python programming and best practices
- Familiarity with the Flet framework for building cross-platform UIs
- Context-aware code generation based on the current project
- Chain of thought reasoning to break down complex tasks
- Access to internet resources for up-to-date information and examples
- Integration with popular Python IDEs like VS Code and PyCharm

Previous conversation:
{context}

User: {user_message}
AI:"""