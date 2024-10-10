import unittest
from unittest.mock import patch
from src.utils.ai_service import NeurumAI

class TestNeurumAI(unittest.TestCase):
    def setUp(self):
        self.ai_service = NeurumAI('test_user')

    @patch('src.utils.ai_service.Neurum')
    def test_generate_response(self, mock_neurum):
        mock_neurum.return_value.generate.return_value = "Mocked AI response"
        
        response = self.ai_service.generate_response("Previous context", "User message")
        
        self.assertIn("Mocked AI response", response)
        mock_neurum.return_value.generate.assert_called_once()

if __name__ == '__main__':
    unittest.main()