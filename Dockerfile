# Stage 1: Dependencies
FROM python:3.11-slim AS dependencies
WORKDIR /app

# העתקה של קובץ הדרישות בלבד לניצול מיטבי של שכבות הקאש
COPY requirements.txt .

# התקנת ספריות ההתקנה עבור הסביבה הווירטואלית
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Test
FROM dependencies AS test
WORKDIR /app

# העתקת כל קוד הפרויקט
COPY . .

# הרצת בדיקות יחידה
RUN pytest addition-service/app/tests/

# Stage 3: Production
FROM dependencies AS production
WORKDIR /app

# העתקת קוד האפליקציה בלבד (ללא קבצי בדיקה וכלים לפיתוח)
COPY addition-service/ ./addition-service/
COPY app.py .

# הגדרת משתני סביבה לפרודקשן
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# חשיפת הפורט שבו האפליקציה רצה
EXPOSE 8000

# הפקודה להרצת האפליקציה
CMD ["python", "app.py"]