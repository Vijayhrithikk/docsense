# deployment.md

# Deployment Roadmap

## Current State

Development Environment:

* FastAPI
* PostgreSQL
* Local Machine

All services currently run locally.

---

## Phase 1 - Docker

Goals:

* Containerize FastAPI
* Containerize PostgreSQL
* Standardize development environments

Deliverables:

* Dockerfile
* .dockerignore

---

## Phase 2 - Docker Compose

Goals:

Run entire stack with:

docker compose up

Services:

* docsense-api
* postgres

---

## Phase 3 - GitHub Actions

Goals:

Automate:

* Linting
* Testing
* Docker Builds

Benefits:

* Consistent quality
* CI/CD foundation

---

## Phase 4 - AWS Deployment

Target:

AWS EC2

Topics to Learn:

* SSH
* Linux Administration
* Security Groups
* Process Management

---

## Phase 5 - Nginx

Goals:

* Reverse Proxy
* HTTPS
* Domain Routing

Traffic Flow:

User
→ Nginx
→ FastAPI

---

## Phase 6 - Monitoring

Planned Endpoints:

* /health
* /metrics

Future Tools:

* Prometheus
* Grafana

---

## Long-Term Goal

Deploy DocSense as a production-ready SaaS platform with:

* Multi-tenancy
* Evaluation
* Analytics
* CI/CD
* Cloud Infrastructure

Milestone:
Successfully containerized FastAPI application.

Image Size:
~902 MB

Lessons:
- Removed unnecessary dependencies.
- Replaced psycopg2 with psycopg2-binary.
- Removed legacy genai package.
- Learned container environment variables.
- Learned Docker networking fundamentals.