from ai_requirement_companion.clients.openrouter_client import OpenRouterClient


class RequirementService:
    def __init__(self):
        self.llm_service = OpenRouterClient()

    def analyze(self, requirement: str) -> str:
        """
        Analyze the given requirement using the LLMService.

        Args:
            requirement (str): The requirement to analyze.

        Returns:
            str: The analysis results.
        """
        return self.llm_service.analyze_requirement(requirement)