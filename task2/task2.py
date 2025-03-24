import sys
import math


def read_circle(file_path: str) -> tuple[tuple[float, float], float]:
    """Читает параметры окружности из файла."""

    with open(file_path, "r") as file:
        x, y = map(float, file.readline().split())
        radius = float(file.readline())
    return (x, y), radius


def read_points(file_path: str) -> list[tuple[float, float]]:
    """Читает координаты точек из файла."""

    points = []
    with open(file_path, "r") as file:
        for line in file:
            x, y = map(float, line.split())
            points.append((x, y))
    return points


def position(
    center: tuple[float, float], radius: float, point: tuple[float, float]
) -> int:
    """Определяет положение точки относительно окружности."""

    cx, cy = center
    px, py = point

    distance_squared = (px - cx) ** 2 + (py - cy) ** 2
    radius_squared = radius**2

    if math.isclose(distance_squared, radius_squared, rel_tol=1e-9):
        return 0
    elif distance_squared < radius_squared:
        return 1
    else:
        return 2


def validate_input():
    """Проверяет входные данные и возвращает кортежи с координатами."""

    if len(sys.argv) != 3:
        print("Неверное количество аргументов")
        print("Пример: python task2.py circle.txt points.txt")
        sys.exit(1)

    try:
        center, radius = read_circle(sys.argv[1])
        points = read_points(sys.argv[2])
    except FileNotFoundError as e:
        print(f"Файл не найден - {e.filename}")
        sys.exit(1)
    except ValueError:
        print("Неверный формат данных в файле")
        sys.exit(1)
    except Exception as e:
        print(f"Неизвестная ошибка: {str(e)}")
        sys.exit(1)

    if radius <= 0:
        print("Радиус должен быть положительным")
        sys.exit(1)

    return center, radius, points


def main():
    center, radius, points = validate_input()

    for point in points:
        pos = position(center, radius, point)
        print(pos)


if __name__ == "__main__":
    main()
