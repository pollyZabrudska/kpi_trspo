import socket

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
    HOST = "0.0.0.0"
    PORT = 9000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Сервер слухає порт {PORT}...")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Підключення від {addr}")
            data = conn.recv(1024).decode().strip()

            N = int(data)
            print(f"Отримано N = {N}")

            total_steps = 0
            for i in range(1, N + 1):
                total_steps += collatz_steps(i)

            avg_steps = total_steps / N
            result = f"{avg_steps}\n"

            conn.sendall(result.encode())
            print("Результат відправлено клієнту")

if __name__ == "__main__":
    main()
