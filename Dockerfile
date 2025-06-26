# Stage 1: Build frontend
FROM node:20 AS frontend-builder

WORKDIR /frontend
COPY frontend/ .
RUN npm install && npm run build


# Stage 2: Backend with Uvicorn + FastAPI
FROM python:3.11-slim

WORKDIR /app

# Install backend dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code and data
COPY backend ./backend
COPY data ./data

# Copy built frontend
COPY --from=frontend-builder /frontend/dist ./static



CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8080"]
