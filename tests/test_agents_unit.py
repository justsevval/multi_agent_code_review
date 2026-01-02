import pytest
from app.agents.quality import QualityAgent
from app.agents.security import SecurityAgent
from app.agents.performance import PerformanceAgent
from app.agents.refactor import RefactorAgent

pytestmark = pytest.mark.unit

def test_quality_agent_detects_long_line():
    code = "a = '" + ("x" * 100) + "'"
    issues = QualityAgent().analyze(code)
    assert any("exceeds" in i["message"] for i in issues)

def test_security_agent_detects_eval():
    code = "eval('2+2')"
    issues = SecurityAgent().analyze(code)
    assert any("dangerous" in i["message"].lower() for i in issues)

def test_performance_agent_detects_nested_loop():
    code = """
for i in range(3):
    for j in range(3):
        print(i, j)
"""
    issues = PerformanceAgent().analyze(code)
    assert any("nested" in i["message"].lower() for i in issues)

def test_refactor_agent_returns_suggestion():
    issues = RefactorAgent().analyze("print('hi')")
    assert len(issues) > 0
