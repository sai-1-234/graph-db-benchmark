from db import Database
from utils import percentile, save_result, timer

db=Database()

QUERY="""
MATCH (u:User)
RETURN count(u)
"""

times=[]

@timer
def aggregate():

    with db.session() as session:

        session.run(QUERY).consume()

for _ in range(100):

    _,t=aggregate()

    times.append(t)

p50=percentile(times,0.50)
p95=percentile(times,0.95)

save_result(
    "aggregation_results.csv",
    "Count Users",
    p50,
    p95
)

print("Aggregation Benchmark")
print("P50:",round(p50,3),"ms")
print("P95:",round(p95,3),"ms")

db.close()