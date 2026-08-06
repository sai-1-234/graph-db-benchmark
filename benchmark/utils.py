import csv
import os
import statistics
import time

RESULT_FOLDER = "results"

os.makedirs(RESULT_FOLDER, exist_ok=True)


def timer(function):

    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        result = function(*args, **kwargs)

        end = time.perf_counter()

        return result, (end-start)*1000

    return wrapper


def percentile(values, p):

    values = sorted(values)

    index = int(len(values)*p)

    if index >= len(values):
        index = len(values)-1

    return values[index]


def save_result(filename, benchmark, p50, p95):

    filepath = os.path.join(RESULT_FOLDER, filename)

    exists = os.path.exists(filepath)

    with open(filepath, "a", newline="") as f:

        writer = csv.writer(f)

        if not exists:
            writer.writerow([
                "Benchmark",
                "P50(ms)",
                "P95(ms)"
            ])

        writer.writerow([
            benchmark,
            round(p50,3),
            round(p95,3)
        ])