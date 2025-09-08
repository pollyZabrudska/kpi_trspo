import matplotlib.pyplot as plt

threads = [1, 2, 4, 8, 16, 32, 64]
times = [0.2352, 0.2355, 0.2398, 0.2407, 0.2378, 0.2340, 0.2402]

plt.plot(threads, times, marker='o', linestyle='-', linewidth=1.5)
plt.title("Залежність часу обчислення від кількості потоків")
plt.xlabel("Кількість потоків")
plt.ylabel("Час (секунди)")
plt.xticks(threads)
plt.grid(True, linestyle="--", alpha=0.7)
plt.savefig("chart.png")
plt.show()
