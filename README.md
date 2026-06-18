# DocSense

Production-ready multi-tenant RAG platform for document intelligence.

## Features
- PDF document ingestion
- Semantic search
- AI-powered question answering
- Evaluation datasets
- Background job processing
- Multi-tenant architecture

## Tech Stack
- FastAPI
- PostgreSQL
- Redis
- Docker
- Gemini/OpenAI

## Architecture
User
  ↓
FastAPI
  ↓
Postgres
  ↓
Redis Queue
  ↓
Worker
  ↓
LLM

## Local Setup
... clone and compose up
