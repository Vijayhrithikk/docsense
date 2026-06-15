# architecture.md

# DocSense Architecture

## Overview

DocSense is a multi-tenant Retrieval-Augmented Generation (RAG) platform designed for document ingestion, retrieval, evaluation, and analytics.

The system allows organizations to upload documents, process them into chunks, generate embeddings, retrieve relevant information, and answer user questions using large language models.

---

## High-Level Architecture

Tenant
↓
Documents
↓
Pages
↓
Chunks
↓
Embeddings
↓
Retrieval Layer
↓
Generation Layer
↓
Question Answering

Supporting Systems:

* Evaluation Framework
* Analytics
* Question History
* Metrics
* Health Monitoring

---

## Core Components

### Multi-Tenancy

Each document belongs to a tenant.

Retrieval is scoped to the tenant to prevent cross-tenant information leakage.

---

### Document Processing Pipeline

Upload
→ Save File
→ Background Processing
→ Text Extraction
→ Chunk Generation
→ Embedding Creation
→ Indexed

Document statuses:

* uploaded
* processing
* indexed
* failed

---

### Retrieval Pipeline

Current retrieval stack:

1. Gemini Embeddings
2. BM25 Keyword Search
3. Reciprocal Rank Fusion (RRF)

This creates a hybrid retrieval system combining semantic and lexical search.

---

### Generation Pipeline

Question
→ Retrieve Top Chunks
→ Build Context
→ Gemini Generation
→ Source Attribution

Returned response:

* Answer
* Sources
* Retrieval Score

---

### Evaluation System

Evaluation datasets contain:

* Question
* Expected Answer

Metrics:

* Recall@3
* Answer Relevancy
* Faithfulness

---

### Analytics

Question logs store:

* Retrieval latency
* Generation latency
* Top retrieval score
* Context size
* Chunk count

---

## Technology Stack

Backend:

* FastAPI
* SQLAlchemy
* Alembic

Database:

* PostgreSQL

AI:

* Gemini
* Gemini Embeddings

Retrieval:

* Vector Similarity
* BM25
* RRF

---

## Future Architecture

Planned:

* Docker
* Docker Compose
* GitHub Actions
* Nginx
* AWS EC2
* Monitoring
* CI/CD
