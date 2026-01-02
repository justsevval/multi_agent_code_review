from app.agents.base import BaseAgent

class RefactorAgent(BaseAgent):
    name = "RefactorAgent"

    def analyze(self, code: str):
        return [{
            "agent": self.name,
            "message": "Consider splitting large functions into smaller ones",
            "severity": "low"
        }]
