from dataclasses import dataclass, field

@dataclass
class RequirementAnalysis:
    summary: str = ""
    ambiguities: list[str] = field(default_factory=list)
    questions: list[str] = field(default_factory=list)
    risks: list[str] = field(default_factory=list)
    positive_tests: list[str] = field(default_factory=list)
    negative_tests: list[str] = field(default_factory=list)
    boundary_tests: list[str] = field(default_factory=list)
    security_tests: list[str] = field(default_factory=list)

    raw_response: str = ""