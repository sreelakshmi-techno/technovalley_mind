import unittest

from agents.program_recommendation_agent import sanitize_history


class PromptContaminationTests(unittest.TestCase):
    def test_sanitize_history_removes_profile_and_greeting_content(self):
        history = [
            {"user": "My name is Sreelekshmi", "assistant": "Hello Sreelekshmi!"},
            {"user": "tell me about AI", "assistant": "Artificial Intelligence Programs at Technovalley"},
        ]

        sanitized = sanitize_history(history)

        self.assertEqual(sanitized, [
            {"user": "tell me about AI", "assistant": "Artificial Intelligence Programs at Technovalley"},
        ])

    def test_sanitize_history_returns_empty_list_for_empty_input(self):
        self.assertEqual(sanitize_history([]), [])


if __name__ == "__main__":
    unittest.main()
