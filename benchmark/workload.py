import random
import time

from concurrent.futures import ThreadPoolExecutor

from db import Database

db = Database()

READ_QUERY = """
MATCH (u:User {id:$id})
RETURN u
"""

WRITE_QUERY = """
MERGE (u:BenchmarkUser {id:$id})
SET u.lastSeen = timestamp()
"""

def worker(_):
    with db.session() as session:

        # 80% reads, 20% writes
        if random.random() < 0.8:
            session.run(
                READ_QUERY,
                id=random.randint(0, 75000)
            ).consume()
        else:
            session.run(
                WRITE_QUERY,
                id=random.randint(1000000, 2000000)
            ).consume()

CONCURRENCY = 10
OPERATIONS = 100

print("Running Mixed Workload...")

start = time.time()

with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
    list(executor.map(worker, range(OPERATIONS)))

elapsed = time.time() - start

throughput = OPERATIONS / elapsed

print("Mixed Workload Finished")
print(f"Concurrency : {CONCURRENCY}")
print(f"Operations  : {OPERATIONS}")
print(f"Throughput  : {throughput:.2f} queries/sec")

db.close()