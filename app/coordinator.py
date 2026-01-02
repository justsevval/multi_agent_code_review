from app.agents.quality import QualityAgent
from app.agents.security import SecurityAgent
from app.agents.performance import PerformanceAgent
from app.agents.refactor import RefactorAgent

class CoordinatorAgent:
    def __init__(self):
        self.agents = [
            QualityAgent(),
            SecurityAgent(),
            PerformanceAgent(),
            RefactorAgent()
        ]

    def run(self, code: str):
        issues = []
        for agent in self.agents:
            issues.extend(agent.analyze(code))
        return {"issues": issues}
