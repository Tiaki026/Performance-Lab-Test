import json
import sys
from typing import Union, Dict, List


def load_json(file_path: str) -> Union[Dict, List]:
    """Загружает JSON из файла."""

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(file_path: str, data: Union[Dict, List]) -> None:
    """Сохраняет данные в JSON файл."""

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def build_values(values: List[Dict]) -> Dict[int, str]:
    """Создает словарь соответствия id -> value."""

    return dict((item["id"], item["value"]) for item in values)


def fill_values(node: Dict, values: Dict[int, str]) -> Dict:
    """Рекурсивно заполняет значения в структуре."""

    if "id" in node and node["id"] in values:
        node["value"] = values[node["id"]]

    if "values" in node:
        for child in node["values"]:
            fill_values(child, values)

    return node


def generate_report(structure: Dict, data: List[Dict]) -> Dict:
    """Генерирует отчет с заполненными значениями."""

    values = build_values(data)

    if "tests" in structure:
        structure["tests"] = [
            fill_values(obj, values) for obj in structure["tests"]
        ]
    else:
        structure = fill_values(structure, values)

    return structure


def validate_args():
    """Проверяет аргументы командной строки."""

    if len(sys.argv) != 4:
        print("Требуется 3 аргумента - пути к файлам")
        print("Пример: python task3.py values.json tests.json report.json")
        sys.exit(1)


def main():
    validate_args()

    try:
        values = load_json(sys.argv[1])["values"]
        structure = load_json(sys.argv[2])
        report = generate_report(structure, values)

        save_json(sys.argv[3], report)

    except FileNotFoundError as e:
        print(f"Файл не найден - {e.filename}")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Некорректный JSON формат")
        sys.exit(1)
    except KeyError as e:
        print(f"Отсутствует обязательное поле: '{e}'")
        sys.exit(1)
    except Exception as e:
        print(f"Неизвестная ошибка: '{str(e)}'")
        sys.exit(1)


if __name__ == "__main__":
    main()
