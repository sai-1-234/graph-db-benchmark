import random

from concurrent.futures import ThreadPoolExecutor

from db import Database

db=Database()

QUERY="""
MATCH (u:User {id:$id})
RETURN u
"""

def worker():

    with db.session() as session:

        session.run(
            QUERY,
            id=random.randint(0,75000)
        ).consume()

print("Running Mixed Workload...")

with ThreadPoolExecutor(max_workers=10) as executor:

    executor.map(
        lambda x: worker(),
        range(100)
    )

print("Mixed Workload Finished")

db.close()