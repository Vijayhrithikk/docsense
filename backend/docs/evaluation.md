# evaluation.md

# Evaluation Journey

## Why Evaluation Was Added

Initially DocSense could answer questions but there was no way to measure retrieval quality.

The first goal became:

"How do we know the retriever is actually working?"

---

## Initial Evaluation

Metric:

Recall@3

Logic:

Expected answer must appear inside one of the retrieved chunks.

Results:

Recall@3 ≈ 25%

This revealed major retrieval issues.

---

## Improvements

### Chunk Overlap

Problem:

Important information was being split across chunk boundaries.

Solution:

Introduced chunk overlap.

Result:

Recall increased significantly.

---

### Better Chunking

Problem:

Paragraph boundaries were not preserved consistently.

Solution:

Improved chunk construction strategy.

Result:

Recall improved again.

---

### Hybrid Retrieval

Added:

* BM25
* Reciprocal Rank Fusion (RRF)

Goal:

Improve exact keyword matching.

Examples:

* Emails
* Numbers
* Product names

---

## RAGAS-Lite

A lightweight evaluation framework was introduced.

Metrics:

* Answer Relevancy
* Faithfulness

Implemented using Gemini as an evaluator.

Purpose:

Measure answer quality in addition to retrieval quality.

---

## Key Lesson

Most retrieval failures were not caused by embeddings.

The largest improvements came from:

* Better chunking
* Better evaluation
* Better retrieval design

rather than changing models.

---

## Current Status

Metrics tracked:

* Recall@3
* Answer Relevancy
* Faithfulness

Evaluation history is stored in the database for future analysis.
