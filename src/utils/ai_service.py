from neurum import Neurum

class NeurumAI:
    def __init__(self, user_id):
        self.neurum = Neurum(user_id)

    def generate_response(self, context, user_message):
        chain_of_thoughts = self._generate_chain_of_thoughts(context, user_message)
        final_response = self._generate_final_response(chain_of_thoughts)
        return chain_of_thoughts, final_response

    def _generate_chain_of_thoughts(self, context, user_message):
        prompt = self._create_chain_of_thoughts_prompt(context, user_message)
        thoughts = self.neurum.generate(prompt)
        return thoughts.split('\n')

    def _generate_final_response(self, chain_of_thoughts):
        prompt = self._create_final_response_prompt(chain_of_thoughts)
        return self.neurum.generate(prompt)

    def _create_chain_of_thoughts_prompt(self, context, user_message):
        return f"""SYSTEM PROMPT: You are an advanced AI coding assistant. Break down the solution into a chain of thoughts, each starting with "Thought:". Provide 3-5 thoughts that lead to the solution.

Previous conversation:
{context}

User: {user_message}
AI:
Thought 1: 
Thought 2: 
Thought 3: 
"""

    def _create_final_response_prompt(self, chain_of_thoughts):
        thoughts = "\n".join(chain_of_thoughts)
        return f"""SYSTEM PROMPT: Based on the following chain of thoughts, provide a comprehensive final response that incorporates all the insights.

Chain of Thoughts:
{thoughts}

Final Response:
"""