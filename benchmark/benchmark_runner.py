import subprocess
import time

scripts = [
    "traversal.py",
    "lookup.py",
    "aggregation.py",
    "workload.py"
]

print("="*60)
print("GRAPH DATABASE BENCHMARK")
print("="*60)

start = time.time()

for script in scripts:

    print(f"\nRunning {script}")

    subprocess.run([
        "python",
        f"benchmark/{script}"
    ])

end = time.time()

print("\n===================================")
print("ALL BENCHMARKS COMPLETED")
print(f"Total Time : {end-start:.2f} sec")
print("===================================")