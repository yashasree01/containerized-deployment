# Containerized Application Deployment

Full-stack application containerized with Docker for consistent environments across development and deployment.

## Structure

```
app/
├── backend/           # FastAPI backend
└── frontend/          # React frontend
docker/
├── Dockerfile.app    # Application Dockerfile
├── Dockerfile.prod
└── docker-compose.yml
cicd/
└── pipeline.yml       # CI/CD pipeline
```

## Quick Start

```bash
# Development
docker-compose up --build

# Production
docker-compose -f docker-compose.prod.yml up -d
```

## Services

- **backend**: FastAPI REST API
- **frontend**: React SPA
- **nginx**: Reverse proxy and load balancer

## Build & Run

```bash
docker build -t app:latest -f docker/Dockerfile.app .
docker run -p 8000:8000 app:latest
```
