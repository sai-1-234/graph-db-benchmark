import random

from db import Database
from utils import percentile, save_result, timer

db = Database()

QUERY = """
MATCH (u:User {id:$id})
RETURN u
"""

times=[]

@timer
def lookup(node):

    with db.session() as session:

        session.run(
            QUERY,
            id=node
        ).consume()

for _ in range(100):

    node=random.randint(0,75000)

    _,t=lookup(node)

    times.append(t)

p50=percentile(times,0.50)
p95=percentile(times,0.95)

save_result(
    "lookup_results.csv",
    "Point Lookup",
    p50,
    p95
)

print("Lookup Benchmark")
print("P50:",round(p50,3),"ms")
print("P95:",round(p95,3),"ms")

db.close()