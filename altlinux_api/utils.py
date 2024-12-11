def compare_packages_by_arch(branch1_data, branch2_data, limit=None):
    """
    Сравнивает пакеты двух веток по архитектуре.
    """
    result = {}

    # Получаем список архитектур
    archs = set(pkg['arch'] for pkg in branch1_data['packages']) | set(pkg['arch'] for pkg in branch2_data['packages'])

    for arch in archs:
        # Фильтруем пакеты по архитектуре
        branch1_arch_packages = {pkg['name']: pkg['version'] for pkg in branch1_data['packages'] if pkg['arch'] == arch}
        branch2_arch_packages = {pkg['name']: pkg['version'] for pkg in branch2_data['packages'] if pkg['arch'] == arch}

        # Сравниваем пакеты
        only_in_branch1 = [pkg for pkg in branch1_arch_packages if pkg not in branch2_arch_packages]
        only_in_branch2 = [pkg for pkg in branch2_arch_packages if pkg not in branch1_arch_packages]
        version_greater_in_branch1 = [
            pkg for pkg in branch1_arch_packages
            if pkg in branch2_arch_packages and branch1_arch_packages[pkg] > branch2_arch_packages[pkg]
        ]

        # Ограничиваем количество выводимых пакетов, если указано
        if limit:
            only_in_branch1 = only_in_branch1[:limit]
            only_in_branch2 = only_in_branch2[:limit]
            version_greater_in_branch1 = version_greater_in_branch1[:limit]

        # Сохраняем результат для текущей архитектуры
        result[arch] = {
            'only_in_branch1': only_in_branch1,
            'only_in_branch2': only_in_branch2,
            'version_greater_in_branch1': version_greater_in_branch1,
        }

    return result