from pydantic import BaseModel
from typing import List

class Issue(BaseModel):
    agent: str
    message: str
    severity: str

class ReviewResponse(BaseModel):
    issues: List[Issue]

class CodeRequest(BaseModel):
    code: str
