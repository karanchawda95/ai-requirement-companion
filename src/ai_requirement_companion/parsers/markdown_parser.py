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
        # Initialise the dataclass and keep the raw markdown for debugging.
        analysis = RequirementAnalysis()
        analysis.raw_response = markdown

        # Split the markdown into lines while preserving empty lines – they are useful for
        # detecting the end of a paragraph (e.g., the summary).
        lines = markdown.splitlines()

        # Normalise section names to a canonical set. This makes the parser tolerant to
        # minor variations in heading text (e.g., "## Requirement Summary" or "## Summary").
        SECTION_MAP = {
            "summary": "summary",
            "requirement summary": "summary",
            "ambiguities": "ambiguities",
            # The prompt uses a longer heading for questions.
            "questions": "questions",
            "questions for product owner": "questions",
            "risks": "risks",
            "positive test ideas": "positive_tests",
            "positive tests": "positive_tests",
            "negative test ideas": "negative_tests",
            "negative tests": "negative_tests",
            "boundary test ideas": "boundary_tests",
            "boundary tests": "boundary_tests",
            "security test ideas": "security_tests",
            "security tests": "security_tests",
        }

        current_section_key: str | None = None
        # Temporary buffer for multi‑line sections such as the summary.
        buffer: list[str] = []

        for raw_line in lines:
            line = raw_line.strip()
            # Detect a top‑level markdown heading (## Heading). Anything after the hashes
            # is considered the heading title.
            if line.startswith("## "):
                # When we encounter a new heading we need to flush any buffered content
                # for the previous section.
                if current_section_key == "summary" and buffer:
                    analysis.summary = "\n".join(buffer).strip()
                # Reset buffer for the next section.
                buffer = []

                heading = line[3:].strip().lower()
                # Map the heading to our canonical key if it exists.
                current_section_key = SECTION_MAP.get(heading)
                continue

            # If we are not inside a recognised section, skip the line.
            if not current_section_key:
                continue

            # Handle each recognised section.
            if current_section_key == "summary":
                # The summary may span multiple lines until the next heading. We collect
                # everything (including blank lines) to preserve paragraph breaks.
                buffer.append(raw_line)
            elif current_section_key == "ambiguities":
                if line:
                    analysis.ambiguities.append(line)
            elif current_section_key == "questions":
                # Questions are usually bullet‑pointed. Strip leading hyphens and whitespace.
                if not line:
                    continue
                cleaned = line.removeprefix("- ").strip()
                analysis.questions.append(cleaned)
            elif current_section_key == "risks":
                if line:
                    analysis.risks.append(line)
            elif current_section_key == "positive_tests":
                if line:
                    analysis.positive_tests.append(line)
            elif current_section_key == "negative_tests":
                if line:
                    analysis.negative_tests.append(line)
            elif current_section_key == "boundary_tests":
                if line:
                    analysis.boundary_tests.append(line)
            elif current_section_key == "security_tests":
                if line:
                    analysis.security_tests.append(line)

        # Flush any remaining buffered summary after the loop ends.
        if current_section_key == "summary" and buffer:
            analysis.summary = "\n".join(buffer).strip()

        # NOTE: We deliberately do **not** raise an exception if the summary is missing.
        # An empty summary is acceptable – downstream UI can display a placeholder.
        return analysis