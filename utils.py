import json


def load_candidates():
    """
    Загрузка данных из файла
    """
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_candidates_all():
    """
    Показать всех кандидатов
    """
    return load_candidates()


def get_candidate_by_pk(pk):
    """
    Показать кандидата по номеру
    """
    for candidate in load_candidates():
        if candidate['id'] == pk:
            return candidate
    return 'Not Found'


def get_candidates_by_name(candidate_name):
    """
    Показать кандидатов по имени
    """
    result = []
    for candidate in load_candidates():
        if candidate_name.lower() in candidate['name'].lower():
            result.append(candidate)
    return result


def get_candidates_by_skill(skill):
    """
    Показать кандидатов по навыку
    """
    result = []
    for candidate in load_candidates():
        skills = candidate['skills'].lower().split(', ')
        if skill in skills:
            result.append(candidate)
    return result
