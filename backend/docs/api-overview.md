# api-overview.md

# DocSense API Overview

## Base URL

Local Development:

http://localhost:8000

Swagger Documentation:

/docs

OpenAPI Specification:

/openapi.json

---

# Tenant APIs

## Create Tenant

POST /tenants

Request:

{
"name": "Acme Corp"
}

Response:

{
"id": 1,
"name": "Acme Corp",
"created_at": "..."
}

Purpose:

Creates a new tenant for document isolation.

---

## List Tenants

GET /tenants

Response:

[
{
"id": 1,
"name": "Acme Corp"
}
]

Purpose:

Returns all registered tenants.

---

# Document APIs

## Upload Document

POST /documents

Form Data:

tenant_id
title
file

Response:

{
"id": 1,
"tenant_id": 1,
"title": "Insurance Policy",
"status": "uploaded"
}

Workflow:

Upload
→ Save File
→ Background Task
→ Extract Text
→ Chunk
→ Embed
→ Indexed

Document statuses:

* uploaded
* processing
* indexed
* failed

---

# Question APIs

## Ask Question

POST /questions/ask

Request:

{
"tenant_id": 1,
"question": "What benefits are covered?"
}

Response:

{
"answer": "...",
"sources": [
{
"document_title": "hdfc",
"start_page": 2,
"end_page": 2,
"score": 0.69
}
]
}

Purpose:

Retrieves relevant chunks and generates an answer.

---

## Question History

GET /questions/history/{tenant_id}

Response:

[
{
"id": 1,
"question": "...",
"answer": "...",
"retrieval_ms": 120,
"generation_ms": 2800,
"created_at": "..."
}
]

Purpose:

Returns previously asked questions.

---

## Question Details

GET /questions/history/question/{question_id}

Purpose:

Returns a single question log.

---

## Retrieval Debug

GET /questions/debug/retrieval

Parameters:

tenant_id
query

Purpose:

Returns retrieval results without generation.

Useful for:

* Debugging retrieval quality
* Chunk inspection
* Evaluation

---

# Evaluation APIs

## Create Evaluation Case

POST /evaluation/cases

Request:

{
"tenant_id": 1,
"question": "...",
"expected_answer": "..."
}

Purpose:

Creates evaluation dataset entries.

---

## Get Evaluation Cases

GET /evaluation/cases

Purpose:

Returns all evaluation test cases.

---

## Run Evaluation

POST /evaluation/run

Metrics:

* Recall@3
* Answer Relevancy
* Faithfulness

Response:

{
"total_cases": 26,
"passed_cases": 21,
"recall_at_3": 0.807,
"relevancy": 1.0,
"faithfulness": 1.0
}

Purpose:

Runs retrieval and answer quality evaluation.

---

## Evaluation History

GET /evaluation/results

Purpose:

Returns historical evaluation runs.

---

## Evaluation Summary

GET /evaluation/summary

Response:

{
"latest_recall": 0.807,
"best_recall": 0.846,
"avg_recall": 0.791
}

Purpose:

Provides aggregated evaluation metrics.

---

# Analytics APIs

## Analytics Summary

GET /analytics/summary

Parameters:

tenant_id

Response:

{
"total_questions": 50,
"avg_retrieval_ms": 145,
"avg_generation_ms": 3100,
"avg_top_score": 0.72,
"avg_chunk_count": 3,
"avg_context_length": 2800
}

Purpose:

Provides retrieval and generation analytics.

---

# Metrics APIs

## System Metrics

GET /metrics

Response:

{
"documents": 10,
"chunks": 840,
"questions": 124,
"evaluations": 7
}

Purpose:

Provides system-level operational metrics.

---

# Retrieval Architecture

Current Retrieval Pipeline:

Question
↓
Gemini Embedding
↓
Vector Similarity Search
↓
BM25 Search
↓
Reciprocal Rank Fusion (RRF)
↓
Top Chunks
↓
Generation

---

# Evaluation Architecture

Evaluation Dataset
↓
Retrieval
↓
Recall@3
↓
Answer Generation
↓
RAGAS-lite Metrics
↓
Evaluation History

Metrics Stored:

* Recall@3
* Answer Relevancy
* Faithfulness

---

# Version

Current Version:

DocSense Backend v1.0
