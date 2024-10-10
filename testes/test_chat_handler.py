import unittest
from unittest.mock import MagicMock
from src.logic.chat_handler import ChatHandler

class TestChatHandler(unittest.TestCase):
    def setUp(self):
        self.ai_service_mock = MagicMock()
        self.chat_handler = ChatHandler(self.ai_service_mock)

    def test_process_message(self):
        chat_list_mock = MagicMock()
        self.ai_service_mock.generate_response.return_value = "AI response"

        self.chat_handler.process_message("Test message", chat_list_mock)

        self.assertEqual(len(self.chat_handler.conversation_history), 2)
        self.assertIn("User: Test message", self.chat_handler.conversation_history)
        self.assertIn("AI: AI response", self.chat_handler.conversation_history)
        self.assertEqual(chat_list_mock.controls.append.call_count, 2)

if __name__ == '__main__':
    unittest.main()