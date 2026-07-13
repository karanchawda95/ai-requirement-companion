from openai import OpenAI
from dotenv import load_dotenv
from ai_requirement_companion.core.settings import Settings
from ai_requirement_companion.prompts.requirement_analysis import SYSTEM_PROMPT

load_dotenv()  # Load environment variables from .env file
settings = Settings()

class OpenRouterClient:
    """Handles communication with configured LLM provider."""

    def __init__(self) -> None:
        self.client = OpenAI(
            api_key=settings.openrouter_api_key,
            base_url="https://openrouter.ai/api/v1",
        )

    def analyze_requirement(self, requirement: str) -> str:

        response = self.client.chat.completions.create(
            model=settings.llm_model or "gpt-5.4",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": requirement,
                },
            ],
        )
        return response.choices[0].message.content or ""