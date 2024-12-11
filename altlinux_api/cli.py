import json
import sys
from altlinux_api.api import get_branch_binary_packages
from altlinux_api.utils import compare_packages_by_arch

def main():
    """
    Основная функция CLI.
    """
    if len(sys.argv) < 3:
        print("Usage: altlinux-compare <branch1> <branch2> [limit] [output_file]")
        sys.exit(1)

    branch1 = sys.argv[1]
    branch2 = sys.argv[2]
    limit = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3].isdigit() else None  # Ограничение на количество пакетов
    output_file = sys.argv[4] if len(sys.argv) > 4 else None  # Имя файла для сохранения результата

    # Получаем данные для обеих веток
    print(f"Fetching data for branch: {branch1}...")
    branch1_data = get_branch_binary_packages(branch1)

    print(f"Fetching data for branch: {branch2}...")
    branch2_data = get_branch_binary_packages(branch2)

    # Сравниваем пакеты
    print("Comparing packages...")
    comparison = compare_packages_by_arch(branch1_data, branch2_data, limit)

    # Выводим результат в JSON
    print(json.dumps(comparison, indent=4))

    # Сохраняем результат в файл, если указано имя файла
    if output_file:
        try:
            print(f"Saving results to {output_file}...")  # Отладочный вывод
            with open(output_file, 'w') as f:
                json.dump(comparison, f, indent=4)
            print(f"Comparison results saved to {output_file}")
        except Exception as e:
            print(f"Error saving results to {output_file}: {e}")