from app.agents.base import BaseAgent

class SecurityAgent(BaseAgent):
    name = "SecurityAgent"

    def analyze(self, code: str):
        issues = []
        dangerous = ["eval(", "exec(", "subprocess.Popen"]
        for d in dangerous:
            if d in code:
                issues.append({
                    "agent": self.name,
                    "message": f"Use of dangerous function detected: {d}",
                    "severity": "high"
                })
        return issues
