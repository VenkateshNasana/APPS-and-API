build:
	docker-compose build
	cd frontend && npm run build

run:
	docker-compose up -d
	cd backend && uvicorn app.main:app --reload

test:
	cd backend && pytest
