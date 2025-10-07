import concurrent.futures
import time

# Функція для обчислення кількості кроків
def collatz_steps(n: int) -> int:
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


def main():
    N = 10_000_000
    NUM_THREADS = 8
    numbers = range(1, N + 1)
    print(f"Починаємо обчислення для {N:,} чисел з {NUM_THREADS} потоками...\n")
    start_time = time.time()

    total_steps = 0
    processed = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        for steps in executor.map(collatz_steps, numbers, chunksize=1000):
            total_steps += steps
            processed += 1

    avg_steps = total_steps / processed
    duration = time.time() - start_time

    print(f"Оброблено чисел: {processed:,}")
    print(f"Середня кількість кроків: {avg_steps:.2f}")
    print(f"Час виконання: {duration:.2f} секунд")


if __name__ == "__main__":
    main()
