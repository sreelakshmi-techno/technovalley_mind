import unittest
from unittest.mock import patch

from orchestrator.router import router


class IntentRoutingTests(unittest.TestCase):
    def test_router_uses_classifier_for_greetings(self):
        with patch("orchestrator.router.classify_intent", return_value="GREETING"):
            state = {"query": "HIII", "conversation_state": {}}
            self.assertEqual(router(state), "customer_experience")

    def test_router_uses_classifier_for_course_queries(self):
        with patch("orchestrator.router.classify_intent", return_value="COURSE_QUERY"):
            state = {"query": "best ai upskilling institute in kochi", "conversation_state": {}}
            self.assertEqual(router(state), "program_recommendation")


if __name__ == "__main__":
    unittest.main()
