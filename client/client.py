import os
import socket


def main():
    server_host = os.getenv("SERVER_HOST")
    server_port = int(os.getenv("SERVER_PORT"))
    N = os.getenv("COLLATZ_COUNT")

    if not server_host or not server_port or not N:
        raise ValueError("Не всі змінні оточення задані")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((server_host, server_port))
        sock.sendall(N.encode())

        response = sock.recv(1024).decode()
        print(f"Середня кількість кроків Колатца: {response}")


if __name__ == "__main__":
    main()
