import flet as ft
from neurum import Neurum
from googlesearch import search

n = Neurum('vansh')

def main(page: ft.Page):
    conversation_history = []

    def search_web(query):
        results = search(query, num_results=5)
        return "\n".join(results)

    def send_message(e):
        if new_message.value:
            # Add user message to conversation history
            user_message = f"User: {new_message.value}"
            conversation_history.append(user_message)

            # Display user message
            chat_list.controls.append(ft.Text(user_message))
            page.update()
            
            # Generate bot response
            context = "\n".join(conversation_history)
            prompt = f"""SYSTEM PROMPT: You are an advanced AI software engineering assistant, designed to help Python developers rapidly build cross-platform applications. Your primary goal is to enhance developer productivity by providing intelligent code suggestions, generating UI components, offering debugging assistance, and enabling real-time collaboration. Key Capabilities:
- Extensive knowledge of Python programming and best practices
- Familiarity with the Flet framework for building cross-platform UIs
- Context-aware code generation based on the current project
- Chain of thought reasoning to break down complex tasks
- Access to internet resources for up-to-date information and examples
- Integration with popular Python IDEs like VS Code and PyCharm

Previous conversation:
{context}

User: {new_message.value}
AI:"""

            res = n.generate(prompt)
            
            # Add bot response to conversation history
            bot_message = f"AI: {res}"
            conversation_history.append(bot_message)

            # Display bot response as plain text
            chat_list.controls.append(ft.Text(
                bot_message,
                selectable=True,
            ))
            
            # Clear the input field
            new_message.value = ""
            
            # Update the page to reflect the changes
            page.update()

    # Create a ListView to display chat messages
    chat_list = ft.ListView(
        expand=True,
        spacing=10,
    )

    # Create an input field for new messages
    new_message = ft.TextField(
        hint_text="Type your message here...",
        expand=True,
        border_radius=10,
        on_submit=send_message,
        bgcolor=ft.colors.TRANSPARENT
    )

    # Create a send button
    send_button = ft.IconButton(
        icon=ft.icons.SEND,
        on_click=send_message,
        icon_color=ft.colors.WHITE
    )

    # Create a container for the input field and send button
    input_container = ft.Row(
        controls=[
            new_message,
            send_button
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    # Create the main chat container
    chat_container = ft.Container(
        content=ft.Column(
            controls=[
                chat_list,
                input_container
            ],
            spacing=10
        ),
        expand=True,
        padding=20
    )

    # Add the chat container to the page
    page.add(chat_container)

    # Set the page title
    page.title = "AI Software Engineering Assistant"

    # Update the page
    page.update()

ft.app(target=main)