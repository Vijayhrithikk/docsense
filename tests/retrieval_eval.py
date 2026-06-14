from app.services.retrieval_service import RetrievalService

from app.db.database import SessionLocal

from app.models.chunk_model import Chunk

TEST_CASES = [
    {
        "query": "how claude skill works",
        "expected": "what is a skill"
    },
    {
        "query": "yaml frontmatter",
        "expected": "yaml frontmatter"
    },
    {
        "query": "workflow automation",
        "expected": "workflow automation"
    },
    {
        "query": "mcp enhancement",
        "expected": "mcp enhancement"
    },
    {
        "query": "testing skills",
        "expected": "testing and iteration"
    },
    {
        "query": "Patterns and Troubleshooting",
        "expected": "Pattern"
    },
    {
        "query": "Troubleshoot large context issues",
        "expected": "Optimize skill.md size"
    }
]

service = RetrievalService()

db = SessionLocal()

chunks = db.query(Chunk).all()

passed = 0

for test in TEST_CASES:

    results = service.retrieve(
        db,
        test["query"],
        top_k=3,
    )

    found = False
    failed_chunk =None

    for result in results:



        chunk = result["chunk"]

        if test["expected"].lower() in chunk.content.lower():

            found = True
            break
        failed_chunk = None

    if found:
        passed += 1

    else:
        print(f"FAIL:{test['query']}")
        print(failed_chunk)

print(
    f"Recall@3 = {passed}/{len(TEST_CASES)}"
)