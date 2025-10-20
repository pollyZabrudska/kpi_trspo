from concurrent.futures import ThreadPoolExecutor
import time

# Функція Коллатца
def collatz_steps(n: int) -> int:
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps

# Функція, яку виконує кожен потік — працює лише зі своїм діапазоном чисел
def process_range(start: int, end: int) -> int:
    total = 0
    for i in range(start, end):
        total += collatz_steps(i)
    return total

def main():
    N = 10_000_000
    THREADS = 8
    chunk = N // THREADS

    print(f"Запуск без синхронізації ({THREADS} потоків)...")
    start = time.time()

    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        futures = []
        for i in range(THREADS):
            start_i = i * chunk + 1
            end_i = (i + 1) * chunk + 1 if i < THREADS - 1 else N + 1
            futures.append(executor.submit(process_range, start_i, end_i))

        results = [f.result() for f in futures]

    total_steps = sum(results)
    avg_steps = total_steps / N

    print(f"Середня кількість кроків: {avg_steps:.2f}")
    print(f"Час виконання: {time.time() - start:.2f} с")

if __name__ == "__main__":
    main()
