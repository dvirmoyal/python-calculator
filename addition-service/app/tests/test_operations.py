from fastapi.testclient import TestClient
import pytest
from ..main import app

client = TestClient(app)

def test_health_check():
    """בדיקת תקינות נקודת הקצה health"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_addition():
    """בדיקת פעולת חיבור תקינה"""
    response = client.post(
        "/add",
        json={"a": 5, "b": 3}
    )
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["result"] == 8
    assert response_data["operation"] == "addition"

def test_addition_negative():
    """בדיקת פעולת חיבור עם מספרים שליליים"""
    response = client.post(
        "/add",
        json={"a": -5, "b": 3}
    )
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["result"] == -2
    assert response_data["operation"] == "addition"

def test_subtraction():
    """בדיקת פעולת חיסור תקינה"""
    response = client.post(
        "/subtract",
        json={"a": 10, "b": 4}
    )
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["result"] == 6
    assert response_data["operation"] == "subtraction"

def test_subtraction_negative_result():
    """בדיקת פעולת חיסור שתוצאתה שלילית"""
    response = client.post(
        "/subtract",
        json={"a": 4, "b": 10}
    )
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["result"] == -6
    assert response_data["operation"] == "subtraction"

def test_addition_large_numbers():
    """בדיקת פעולת חיבור עם מספרים גדולים"""
    response = client.post(
        "/add",
        json={"a": 1000000, "b": 2000000}
    )
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["result"] == 3000000
    assert response_data["operation"] == "addition"

def test_addition_decimal_numbers():
    """בדיקת פעולת חיבור עם מספרים עשרוניים"""
    response = client.post(
        "/add",
        json={"a": 0.1, "b": 0.2}
    )
    assert response.status_code == 200
    response_data = response.json()
    assert abs(response_data["result"] - 0.3) < 1e-10  # נשתמש בהשוואה מקורבת בגלל אי-דיוקים בשברים עשרוניים
    assert response_data["operation"] == "addition"

def test_addition_invalid_input():
    """בדיקת שגיאת קלט לא תקין בפעולת חיבור"""
    response = client.post(
        "/add",
        json={"a": "invalid", "b": 3}
    )
    assert response.status_code == 422  # Unprocessable Entity - שגיאת וולידציה של Pydantic

def test_missing_parameters():
    """בדיקת שגיאת חוסר פרמטרים בפעולת חיבור"""
    response = client.post(
        "/add",
        json={"a": 5}  # חסר פרמטר b
    )
    assert response.status_code == 422  # Unprocessable Entity - שגיאת וולידציה של Pydantic