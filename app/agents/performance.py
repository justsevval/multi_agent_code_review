import ast
from app.agents.base import BaseAgent

class PerformanceAgent(BaseAgent):
    name = "PerformanceAgent"

    def analyze(self, code: str):
        issues = []
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.For):
                    for inner in ast.walk(node):
                        if isinstance(inner, ast.For):
                            issues.append({
                                "agent": self.name,
                                "message": "Nested loop detected (possible O(n^2))",
                                "severity": "medium"
                            })
        except SyntaxError:
            issues.append({
                "agent": self.name,
                "message": "Syntax error prevents full performance analysis",
                "severity": "low"
            })
        return issues
