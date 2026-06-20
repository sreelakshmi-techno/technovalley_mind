import unittest

from orchestrator.router import router


class RouterGreetingPriorityTests(unittest.TestCase):
    def test_greeting_overrides_awaiting_program_recommendation(self):
        state = {
            "query": "hi",
            "conversation_state": {"awaiting": "educational_background"}
        }

        self.assertEqual(router(state), "customer_experience")


if __name__ == "__main__":
    unittest.main()
