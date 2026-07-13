from ai_requirement_companion.clients.openrouter_client import OpenRouterClient
from ai_requirement_companion.parsers.markdown_parser import MarkdownParser


class RequirementService:
    def __init__(self):
        self.llm_service = OpenRouterClient()

    def analyze(self, requirement: str) -> MarkdownParser:
        """
        Analyze the given requirement using the LLMService.

        Args:
            requirement (str): The requirement to analyze.

        Returns:
            MarkdownParser: The analysis results.
        """
        llm_result = self.llm_service.analyze_requirement(requirement)
        parser = MarkdownParser()
        analysis = parser.parse(llm_result)
        return analysis # type: ignore