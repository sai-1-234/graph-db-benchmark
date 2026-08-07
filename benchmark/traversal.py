import random

from db import Database
from utils import percentile, save_result, timer

db = Database()

QUERIES = {
    "1-Hop Traversal": """
        MATCH (u:User {id:$id})-[:TRUSTS]->(n)
        RETURN count(n)
    """,
    "2-Hop Traversal": """
        MATCH (u:User {id:$id})-[:TRUSTS]->()-[:TRUSTS]->(n)
        RETURN count(n)
    """,
    "3-Hop Traversal": """
        MATCH (u:User {id:$id})-[:TRUSTS]->()-[:TRUSTS]->()-[:TRUSTS]->(n)
        RETURN count(n)
    """
}

@timer
def traversal(query, node):
    with db.session() as session:
        session.run(query, id=node).consume()

print("Traversal Benchmark")

for name, query in QUERIES.items():

    times = []

    for _ in range(100):
        node = random.randint(0, 75000)
        _, t = traversal(query, node)
        times.append(t)

    p50 = percentile(times, 0.50)
    p95 = percentile(times, 0.95)

    save_result(
        "traversal_results.csv",
        name,
        p50,
        p95
    )

    print(f"{name}")
    print("P50:", round(p50, 3), "ms")
    print("P95:", round(p95, 3), "ms")
    print()

db.close()