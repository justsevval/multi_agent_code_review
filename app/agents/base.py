class BaseAgent:
    name = "BaseAgent"

    def analyze(self, code: str):
        raise NotImplementedError
