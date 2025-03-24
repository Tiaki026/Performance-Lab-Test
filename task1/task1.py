import sys
from typing import Tuple


def circular_path(n: int, m: int) -> list[int]:
    """Вычисляет путь по круговому массиву."""

    path: list[int] = []
    current = 1
    while True:
        path.append(current)
        next_pos = current + m - 1
        while next_pos > n:
            next_pos -= n
        if next_pos == 1:
            break
        current = next_pos

    return path


def validate_input() -> Tuple[int, int]:
    """Проверяет аргументы командной строки и возвращает n и m."""

    if len(sys.argv) != 3:
        print("Неверное количество аргументов")
        print("Пример: python task1.py 5 4")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
    except ValueError:
        print("Оба аргумента должны быть целыми числами")
        sys.exit(1)

    if n <= 0 or m <= 0:
        print("Оба аргумента должны быть положительными числами")
        sys.exit(1)

    return n, m


def main():
    n, m = validate_input()
    path = circular_path(n, m)
    print("".join(map(str, path)))


if __name__ == "__main__":
    main()
