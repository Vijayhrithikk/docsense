import time
from sentence_transformers import SentenceTransformer

start = time.time()

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

print(
    "Model load:",
    time.time() - start
)

start = time.time()

model.encode("hello")

print(
    "Encode:",
    time.time() - start
)