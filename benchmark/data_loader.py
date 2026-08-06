import os
import time

from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")

DATASET = "datasets/soc-Epinions1.txt"

BATCH_SIZE = 1000

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)


def insert_batch(tx, batch):
    tx.run("""
    UNWIND $rows AS row

    MERGE (a:User {id: row.source})
    MERGE (b:User {id: row.target})

    MERGE (a)-[:TRUSTS]->(b)
    """, rows=batch)


batch = []

relationships = 0

start = time.time()

with driver.session() as session:

    with open(DATASET, "r") as file:

        for line in file:

            if line.startswith("#"):
                continue

            source, target = line.strip().split()

            batch.append({
                "source": int(source),
                "target": int(target)
            })

            relationships += 1

            if len(batch) >= BATCH_SIZE:
                session.execute_write(insert_batch, batch)
                print(f"Loaded {relationships} relationships...")
                batch = []

        if batch:
            session.execute_write(insert_batch, batch)

end = time.time()

elapsed = end - start

print("\n===================================")
print("LOAD COMPLETED")
print("===================================")
print(f"Relationships Loaded : {relationships}")
print(f"Total Time           : {elapsed:.2f} seconds")
print(f"Relationships/Second : {relationships/elapsed:.2f}")

driver.close()