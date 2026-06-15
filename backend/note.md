Performance Bug #1

Problem:
86 sec retrieval

Root Cause:
SentenceTransformer loaded per request

Fix:
Singleton model instance

Result:
0.2 sec retrieval