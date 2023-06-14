from typing import List

example = {'https://elibrary.ru/item.asp?id=42965403': {
    'title': 'ОБЕСПЕЧЕНИЕ ДИНАМИЧЕСКОЙ УСТОЙЧИВОСТИ МНОГОПИЛЬНОГО МОДУЛЯ, СОВЕРШАЮЩЕГО ПЛОСКОЕ ВРАЩАТЕЛЬНО-ПОСТУПАТЕЛЬНОЕ ДВИЖЕНИЕ В СОСТАВЕ ПИЛЬНОГО БЛОКА',
    'authors': {'БЛОХИН МИХАИЛ АНАТОЛЬЕВИ': {'job_place_id': '1', 'student': False, 'job_two_or_more': False},
                'ЦЫЖИПОВ ДАМДИН ЖАРГАЛОВИЧ': {'job_place_id': '1', 'student': False, 'job_two_or_more': False}},
    'job_places': {1: 'МГТУ им. Н.Э.Баумана'}, 'journal': {'title': 'ПРОБЛЕМЫ МАШИНОСТРОЕНИЯ И АВТОМАТИЗАЦИИ',
                                                           'link': 'https://elibrary.ru/title_about_new.asp?id=7307',
                                                           'WoS': True, 'SCOPUS': True}},
           'https://elibrary.ru/item.asp?id=44840621': {
               'title': 'АВТОМАТИЗАЦИЯ ПРОЦЕССА РАСПИЛОВКИ ОБОРУДОВАНИЕМ НОВОГО ВИДА, ВЫПОЛНЕННЫМ ПО СХЕМЕ "КОЛЕНЧАТОЙ ПИЛЫ"',
               'authors': {
                   'БЛОХИН МИХАИЛ АНАТОЛЬЕВИ': {'job_place_id': '1', 'student': False, 'job_two_or_more': False},
                   'ГРАЧЁВА ЭЛЕОНОРА ЮРЬЕВН': {'job_place_id': '1', 'student': False, 'job_two_or_more': False},
                   'ПАВЛОВА ИЗАБЕЛЛА ИГОРЕВНА': {'job_place_id': '1', 'student': False, 'job_two_or_more': False}},
               'job_places': {1: 'Московский государственный технический университет имени Н.Э. Баумана'},
               'journal': {'title': 'ПРОБЛЕМЫ МАШИНОСТРОЕНИЯ И АВТОМАТИЗАЦИИ',
                           'link': 'https://elibrary.ru/title_about_new.asp?id=7307', 'WoS': True, 'SCOPUS': True}},
           'https://elibrary.ru/item.asp?id=47115680': {
               'title': 'УПРАВЛЕНИЕ РЕСУРСОМ РАБОТЫ ПИЛЬНОГО БЛОКА С ПЛОСКИМ ВРАЩАТЕЛЬНО-ПОСТУПАТЕЛЬНЫМ ДВИЖЕНИЕМ ПИЛЬНЫХ ПОЛОТЕН',
               'authors': {'БЛОХИН М.А.': {'job_place_id': '1', 'student': False, 'job_two_or_more': False},
                           'ГРАЧЁВА Э.Ю': {'job_place_id': '1', 'student': False, 'job_two_or_more': False},
                           'ПАВЛОВА И.И.': {'job_place_id': '1', 'student': False, 'job_two_or_more': False}},
               'job_places': {1: 'Московский государственный технический университет им. Н.Э. Баумана'},
               'journal': {'title': 'ПРОБЛЕМЫ МАШИНОСТРОЕНИЯ И НАДЕЖНОСТИ МАШИН',
                           'link': 'https://elibrary.ru/title_about_new.asp?id=7959', 'WoS': True, 'SCOPUS': True}}}


def articles_with_indexation(articles: dict) -> dict:
    result_dict = {}
    for key, value in articles.items():
        if value['journal']['WoS'] or value['journal']['SCOPUS']:
            result_dict[key] = value
    return result_dict


def calculate_compensation_for_article(dict_with_data: dict) -> dict:
    student_in_authors = False
    print(dict_with_data['job_places'].keys())
    sum_of_employee_in_places = {job_place: 0 for job_place in dict_with_data['job_places'].keys()}
    for author in dict_with_data['authors'].values():
        if author['student']:
            student_in_authors = True

        sum_of_employee_in_places[int(author['job_place_id'])] = sum_of_employee_in_places[
                                                                     int(author['job_place_id'])] + 1
    print(sum_of_employee_in_places)

    kf1 = 0.1 if student_in_authors else 0
    kf2 = 0
    kf3 = 0
    kf4 = 0.4 if dict_with_data['journal']['WoS'] and dict_with_data['journal']['SCOPUS'] else 0
    kf5 = 0


if __name__ == '__main__':

    articles = articles_with_indexation(example)
    print(articles)

    for article in example.values():
        calculate_compensation_for_article(article)
