# INTEGRAX - Enterprise Integration Platform

## Dependencies
- Node.js v18+
- Python 3.11+
- Docker & Docker Compose
- PostgreSQL
- Redis

## Installation
1. Clone the repository.
2. Backend: cd backend && python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt
3. Frontend: cd frontend && npm install

## Build
To build the frontend:
cd frontend && npm run build
To build docker containers:
docker compose build

## Run
To run locally:
1. Start infrastructure: docker compose up -d
2. Start backend: cd backend && uvicorn app.main:app --reload
3. Start frontend: cd frontend && npm run dev

## Usage
Navigate to http://localhost:5173 to access the integration dashboard.
