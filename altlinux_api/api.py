import requests

BASE_URL = "https://rdb.altlinux.org/api"

def get_branch_binary_packages(branch):
    """
    Получает список бинарных пакетов для указанной ветки.
    """
    url = f"{BASE_URL}/export/branch_binary_packages/{branch}"
    response = requests.get(url)
    response.raise_for_status()  # Проверяем, что запрос успешен
    return response.json()