from app.agents.base import BaseAgent

class QualityAgent(BaseAgent):
    name = "QualityAgent"

    def analyze(self, code: str):
        issues = []
        for i, line in enumerate(code.splitlines(), start=1):
            if len(line) > 79:
                issues.append({
                    "agent": self.name,
                    "message": f"Line {i} exceeds 79 characters",
                    "severity": "medium"
                })
        return issues
