from fastapi import APIRouter, HTTPException
from app.models.operation import OperationRequest, OperationResponse, ErrorResponse
import logging

# הגדרת לוגר
logger = logging.getLogger("addition-service.operations")

# יצירת ראוטר
router = APIRouter(
    prefix="",
    tags=["Operations"],
    responses={404: {"model": ErrorResponse}}
)


@router.post("/add", response_model=OperationResponse)
async def add(request: OperationRequest):
    """ביצוע פעולת חיבור בין שני מספרים"""
    logger.info(f"Addition request: {request.a} + {request.b}")

    try:
        # ביצוע הפעולה
        result = request.a + request.b

        logger.info(f"Addition result: {result}")
        return OperationResponse(result=result, operation="addition")
    except Exception as e:
        logger.error(f"Error in addition operation: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing addition: {str(e)}")


@router.post("/subtract", response_model=OperationResponse)
async def subtract(request: OperationRequest):
    """ביצוע פעולת חיסור בין שני מספרים"""
    logger.info(f"Subtraction request: {request.a} - {request.b}")

    try:
        # ביצוע הפעולה
        result = request.a - request.b

        logger.info(f"Subtraction result: {result}")
        return OperationResponse(result=result, operation="subtraction")
    except Exception as e:
        logger.error(f"Error in subtraction operation: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing subtraction: {str(e)}")