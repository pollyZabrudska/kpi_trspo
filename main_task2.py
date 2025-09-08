import random
import time
import threading

TOTAL_POINTS = 1_000_000

# --- Однопотоковий варіант ---
def monte_carlo_pi(points):
    inside_circle = 0
    for _ in range(points):
        x, y = random.random(), random.random()
        if x*x + y*y <= 1:
            inside_circle += 1
    return 4 * inside_circle / points


# --- Робітник для потоку ---
def monte_carlo_pi_worker(points, results, index):
    inside_circle = 0
    for _ in range(points):
        x, y = random.random(), random.random()
        if x*x + y*y <= 1:
            inside_circle += 1
    results[index] = inside_circle


# --- Багатопотоковий варіант ---
def calculate_pi(num_threads):
    points_per_thread = TOTAL_POINTS // num_threads
    threads = []
    results = [0] * num_threads

    start = time.perf_counter()

    for i in range(num_threads):
        t = threading.Thread(target=monte_carlo_pi_worker, args=(points_per_thread, results, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total_inside_circle = sum(results)
    pi_estimate = 4 * total_inside_circle / TOTAL_POINTS
    elapsed = time.perf_counter() - start

    return pi_estimate, elapsed


if __name__ == "__main__":
    # --- 1. Однопотоковий ---
    start = time.perf_counter()
    pi = monte_carlo_pi(TOTAL_POINTS)
    elapsed = time.perf_counter() - start
    print(f"Threads: 1 (main) | π ≈ {pi:.6f} | Time: {elapsed:.4f} s")

    # --- 2. Багатопотокові ---
    thread_counts = [2, 4, 8, 16, 32, 64]

    for n in thread_counts:
        pi, t = calculate_pi(n)
        print(f"Threads: {n:2d} | π ≈ {pi:.6f} | Time: {t:.4f} s")
