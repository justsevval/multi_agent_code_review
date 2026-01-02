from app.agents.quality import QualityAgent
from app.agents.security import SecurityAgent
from app.agents.performance import PerformanceAgent

def test_quality_agent_detects_long_line():
    code = "a = '" + ("x" * 100) + "'\n"
    issues = QualityAgent().analyze(code)
    assert any("exceeds 79 characters" in i["message"] for i in issues)

def test_security_agent_detects_eval():
    code = "eval('2+2')\n"
    issues = SecurityAgent().analyze(code)
    assert any("eval(" in i["message"] for i in issues)

def test_performance_agent_detects_nested_loop():
    code = """
for i in range(3):
    for j in range(3):
        print(i, j)
"""
    issues = PerformanceAgent().analyze(code)
    assert any("Nested loop" in i["message"] for i in issues)

def test_performance_agent_handles_syntax_error():
    code = "def broken(\n    pass\n"
    issues = PerformanceAgent().analyze(code)
    assert any("Syntax error" in i["message"] for i in issues)
