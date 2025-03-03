from pydantic import BaseModel, Field
from typing import Optional

class OperationRequest(BaseModel):
    """מודל בקשת פעולה חשבונית"""
    a: float = Field(..., description="המספר הראשון בפעולה")
    b: float = Field(..., description="המספר השני בפעולה")

class OperationResponse(BaseModel):
    """מודל תגובה לפעולה חשבונית"""
    result: float = Field(..., description="תוצאת הפעולה")
    operation: str = Field(..., description="סוג הפעולה (addition/subtraction)")

class ErrorResponse(BaseModel):
    """מודל שגיאה"""
    error: str = Field(..., description="תיאור השגיאה")