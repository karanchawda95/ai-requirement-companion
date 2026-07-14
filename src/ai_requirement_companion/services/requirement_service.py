from ai_requirement_companion.clients.openrouter_client import OpenRouterClient
from ai_requirement_companion.parsers.markdown_parser import MarkdownParser
from ai_requirement_companion.models.requirement_analysis import RequirementAnalysis


class RequirementService:
    def __init__(self):
        self.llm_client = OpenRouterClient()
        self.parser = MarkdownParser()

    def analyze(self, requirement: str) -> RequirementAnalysis:
        """
        Analyze the given requirement using the LLMService.

        Args:
            requirement (str): The requirement to analyze.

        Returns:
            MarkdownParser: The analysis results.
        """
        llm_result = self.llm_client.analyze_requirement(requirement)
        analysis = self.parser.parse(llm_result)
        return analysis # type: ignore

    def calculate_quality_score(self, analysis: RequirementAnalysis) -> float:
        """
        Calculate a quality score for the given requirement analysis.

        Args:
            analysis (RequirementAnalysis): The requirement analysis to evaluate.

        Returns:
            float: The calculated quality score.
        """
        score = 10
        score -= min(len(analysis.ambiguities), 3)
        score -= min(len(analysis.risks), 3)
        score = max(score, 1)
        return score