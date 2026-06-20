import unittest
from unittest.mock import MagicMock, patch

import agents.program_recommendation_agent as program_recommendation_agent


class ProgramRecommendationPersonaTests(unittest.TestCase):
    def test_open_ended_ai_query_uses_persona_prompt_not_rigid_template(self):
        fake_llm = MagicMock()
        fake_llm.invoke.return_value = "ok"

        with patch.object(program_recommendation_agent, "llm", fake_llm):
            response = program_recommendation_agent.program_recommendation_agent(
                "best ai upskilling edtech in kochi",
                []
            )

        self.assertEqual(response, "ok")

        prompt = fake_llm.invoke.call_args[0][0]
        self.assertIn("expert representative of Technovalley", prompt)
        self.assertIn("Do not force templates", prompt)
        self.assertIn("Career guidance", prompt)
        self.assertNotIn("Recommended structure:", prompt)


if __name__ == "__main__":
    unittest.main()
