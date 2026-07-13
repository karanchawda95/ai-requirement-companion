from ai_requirement_companion.models.requirement_analysis import RequirementAnalysis


class MarkdownParser:

    def parse(self, markdown: str) -> RequirementAnalysis:
        """
        Parses the given markdown string and extracts the requirement analysis information.

        Args:
            markdown (str): The markdown string to parse.

        Returns:
            RequirementAnalysis: The parsed requirement analysis information.
        """
        analysis = RequirementAnalysis()
        lines = markdown.splitlines()

        current_section = None
        for line in lines:
            line = line.strip()
            if line.startswith("## "):
                current_section = line[3:].strip().lower()
            elif current_section:
                if current_section == "summary":
                    analysis.summary += line + "\n"
                elif current_section == "ambiguities":
                    analysis.ambiguities.append(line)
                elif current_section == "questions":
                    analysis.questions.append(line)
                elif current_section == "risks":
                    analysis.risks.append(line)
                elif current_section == "positive tests":
                    analysis.positive_tests.append(line)
                elif current_section == "negative tests":
                    analysis.negative_tests.append(line)
                elif current_section == "boundary tests":
                    analysis.boundary_tests.append(line)
                elif current_section == "security tests":
                    analysis.security_tests.append(line)

        return analysis