import json
import os
from typing import List

import selenium as selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time
import logging

from selenium.webdriver.common.by import By

logging.basicConfig(filename='science_parser.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)
logging.info("Loading started !!!!! ")
logger = logging.getLogger('science_activity')

WINDOW_SIZE = "1920,1080"


class Watcher:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.service = Service('"C:\\Users\\Рамиль\\PycharmProjects\\wb_parser\\selenuim_approach\\chromedriver.exe"')
        # for ChromeDriver version 79.0.3945.16 or over
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        # self.options.add_argument("--headless")
        # self.options.add_argument("--window-size=%s" % WINDOW_SIZE)
        # user-agent
        self.options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/109.0.0.0 Safari/537.36")
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(
            service=self.service,
            options=self.options
        )
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            'source': '''
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
          '''
        })


if __name__ == '__main__':
    university = 'Баумана'
    # university = ''
    # author_name = 'Королева М Н'
    author_name = 'Блохин М А'
    year_from = '2018'
    year_till = '2023'
    login = "khikmatullin_ramil"
    password = ""

    ScienceParser = Watcher()

    ScienceParser.driver.get(url='https://elibrary.ru/querybox.asp?scope=newquery')
    # authorization

    ScienceParser.driver.find_element(By.XPATH,
                                      '//*[@id="win_login"]/table/tbody/tr/td/table[1]/tbody/tr['
                                      '6]/td/input').send_keys(login)

    ScienceParser.driver.find_element(By.XPATH,
                                      '//*[@id="win_login"]/table/tbody/tr/td/table[1]/tbody/tr['
                                      '8]/td/input').send_keys(password)
    ScienceParser.driver.find_element(By.XPATH,
                                      '//*[@id="win_login"]/table/tbody/tr/td/table[1]/tbody/tr['
                                      '9]/td/input').click()
    #author search
    ScienceParser.driver.get(url='https://elibrary.ru/querybox.asp?scope=newquery')
    add_author_button = ScienceParser.driver.find_element(By.XPATH,
                                                          '/html/body/table/tbody/tr/td/table/tbody/tr/td['
                                                          '2]/table/tbody/tr/td/table[6]/tbody/tr[1]/td[3]/a')
    add_author_button.click()
    # new window for author search
    window_before = ScienceParser.driver.window_handles[0]
    window_after = ScienceParser.driver.window_handles[1]
    ScienceParser.driver.switch_to.window(window_after)
    search_query_input = ScienceParser.driver.find_element(By.XPATH,
                                                           '/html/body/center/form/table[1]/tbody/tr/td[1]/input')
    search_query_input.send_keys(author_name)
    search_query_button = ScienceParser.driver.find_element(By.XPATH,
                                                            '/html/body/center/form/table[1]/tbody/tr/td[2]/table/tbody/tr/td[1]/a')
    search_query_button.click()
    author_search_results = ScienceParser.driver.find_elements(By.XPATH, '/html/body/center/form/table[2]/tbody/tr')
    target_author = 0
    for author in author_search_results[1:]:
        print(author.text.split(" ")[0:-1])
        if author.text.split(" ")[0:-1] == author_name.split(" "):
            target_author = author
    add_author_button = target_author.find_element(By.XPATH, 'td[2]/a/b')
    add_author_button.click()
    ScienceParser.driver.close()

    # added author name on query box
    ScienceParser.driver.switch_to.window(window_before)
    # adjust search filters
    # BMSTU in title
    ScienceParser.driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td'
                                                '/table[2]/tbody/tr/td[2]/textarea').send_keys(university)
    # in job position title serach
    ScienceParser.driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td'
                                                '/table[3]/tbody/tr/td[2]/table/tbody/tr[1]/td[3]/input').click()
    # book
    ScienceParser.driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td'
                                                '/table[4]/tbody/tr/td[2]/table/tbody/tr[2]/td[1]/input').click()
    # диссертация
    ScienceParser.driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td'
                                                '/table[4]/tbody/tr/td[2]/table/tbody/tr[1]/td[3]/input').click()
    # отчеты
    ScienceParser.driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td'
                                                '/table[4]/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/input').click()
    # патенты
    ScienceParser.driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td'
                                                '/table[4]/tbody/tr/td[2]/table/tbody/tr[3]/td[3]/input').click()
    # гранты
    ScienceParser.driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td'
                                                '/table[4]/tbody/tr/td[2]/table/tbody/tr[4]/td[3]/input').click()
    # год с
    select_year_from = Select(ScienceParser.driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/table/tbody'
                                                                          '/tr/td[2]/table/tbody/tr/td'
                                                                          '/table[10]/tbody/tr/td[2]/select'))
    select_year_from.select_by_value(year_from)
    # год до
    select_year_till = Select(ScienceParser.driver.find_element(By.XPATH,
                                                                '/html/body/table/tbody/tr/td/table/tbody/tr/td[2]'
                                                                '/table/tbody/tr/td/table[10]/tbody/tr/td[4]/select'))
    select_year_till.select_by_value(year_till)

    # Поиск кнопка
    search_button = ScienceParser.driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr/td[2]'
                                                                '/table/tbody/tr/td/table[11]/tbody/tr/td[6]/a')
    search_button.click()


    ## Coolecting link for all articles
    # hardcode for articles less than 100
    article_links = ScienceParser.driver.find_elements(By.XPATH, r'//td[2]/a')[:-7]
    print(len(article_links))
    article_links_list = []
    for article_element in article_links:
        article_links_list.append(article_element.get_attribute("href"))
    print(article_links_list)
    articles_with_author = {}
    ## cycle for links
    for link in article_links_list:
        time.sleep(1)
        ScienceParser.driver.get(url=link)
        ## parsing article page
        # title
        title_article = ScienceParser.driver.find_element(By.XPATH, '/html/body/table/tbody'
                                                                    '/tr/td/table[1]/tbody/tr/td[2]'
                                                                    '/table/tbody/tr[2]/td[1]/table[2]'
                                                                    '/tbody/tr/td[2]/span/b/p').text
        # print(title_article)
        # authors
        authors = ScienceParser.driver.find_elements(By.XPATH,
                                                     '/html/body/table/tbody/tr/td/table[1]/tbody/tr/td[2]/table/tbody'
                                                     '/tr[2]/td[1]/div/table[1]/tbody/tr/td[2]/div')
        if len(authors) > 1:
            authors = authors[:-1]
        authors_dict = {}
        for author in authors:
            text = author.text
            # print(text)
            if text[-1] == ',':
                text, job_place_id = text[:-3], text[-2]
                # print(text)
                # print(job_place_id)
            else:
                text, job_place_id = text[:-1], text[-1]
                # print(text)
                # print(job_place_id)
            authors_dict[f'{text}'] = {
                'job_place_id': job_place_id,
                'student': False,
                'job_two_or_more': False
            }
        # job
        job_places = ScienceParser.driver.find_elements(By.XPATH,
                                                        '/html/body/table/tbody/tr/td/table[1]/tbody/tr/td[2]/table'
                                                        '/tbody/tr[2]/td[1]/div/table[1]/tbody/tr/td[2]/span')
        # if len(job_places):
        #     job_places = ScienceParser.driver.find_elements(By.XPATH,
        #                                                     '/html/body/table/tbody/tr/td/table[1]/tbody/tr/td[2]/table'
        #                                                     '/tbody/tr[2]/td[1]/div/table[1]/tbody/tr/td[2]/font[2]')
        #     print(f'{len(job_places)=}')
        #     job_dict = {i + 1: f'{job.text}' for i, job in zip(range(len(job_places)), job_places)}
        #     print(f'{job_dict=}')
        # else:
        print(f'{len(job_places)=}')
        job_dict = {i + 1: f'{job.text}' for i, job in zip(range(len(job_places)), job_places)}
        print(f'{job_dict=}')

            # journal
        journal = ScienceParser.driver.find_element(By.XPATH,
                                                    '/html/body/table/tbody/tr/td/table[1]/tbody/tr/td['
                                                    '2]/table/tbody/tr[2]/td[1]/div/table[3]/tbody/tr[2]/td[2]/a')

        print(f'{journal.text=}')
        journal_title = journal.text
        journal.click()

        try:
            ScienceParser.driver.find_element(By.XPATH,
                                              '//*[@id="thepage"]/table/tbody/tr/td/table[1]/tbody/tr/td['
                                              '2]/form/table/tbody/tr[2]/td[1]/table[2]/tbody/tr/td/div['
                                              '1]/a/font/b').click()
        except:
            pass

        journal_link = ScienceParser.driver.current_url
        print(f'{journal_link=}')
        # new version pf representation
        if 'new' in journal_link:
            states = ScienceParser.driver.find_elements(By.XPATH, '//*[@id="thepage"]/table/tbody/tr/td/table/tbody'
                                                                  '/tr/td/form/table/tbody/tr/td/table/tbody/tr/td'
                                                                  '/table/tbody/tr/td/table/tbody/tr/td')
            print(states)
            wos_index = False
            scopus_index = False
            for state in states:

                if 'Web of Science' in state.text:
                    print(state.text)
                    if ': да' in state.text or ': переводная версия' in state.text:
                        wos_index = True
                if 'Scopus' in state.text:
                    print(state.text)
                    if ': да' in state.text or ': переводная версия' in state.text:
                        scopus_index = True
            print('WoS', wos_index, 'SCOPUS', scopus_index)
        else:
            states = ScienceParser.driver.find_elements(By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr/td'
                                                                  '/table/tbody/tr/td/table/tbody/tr/td')
            print(f'{states=}')
            print(f'{len(states)=}')
            wos_index = False
            scopus_index = False
            for i, state in enumerate(states):
                if 'Web of Science' in state.text:
                    print(f'{state.text=}')
                    print(f'{i=}')
                    if i + 1 == len(states):
                        wos_index = True
                    elif 'да' in states[i + 1].text or ': переводная версия' in state[i + 1].text:
                        wos_index = True
                if 'SCOPUS' in state.text:
                    print(f'{state.text=}')
                    print(f'{i=}')
                    if i + 1 == len(states):
                        wos_index = True
                    elif 'да' in states[i + 1].text or ': переводная версия' in state[i + 1].text:
                        scopus_index = True
            print('WoS', wos_index, 'SCOPUS', scopus_index)
        journal_dict = {
            'title': journal_title,
            'link': journal_link,
            'WoS': wos_index,
            'SCOPUS': scopus_index
        }
        articles_with_author[f'{link}'] = {
            'title': title_article,
            'authors': authors_dict,
            'job_places': job_dict,
            'journal': journal_dict
        }
    print(articles_with_author)
# {
#   "https://elibrary.ru/item.asp?id=49940309": {
#     "Название статьи": "К ВОПРОСУ О ФОРМАЛИЗАЦИИ ЭТИКИ ПОВЕДЕНИЯ КОЛЛАБОРАТИВНОГО РОБОТА",
#     "Авторы": {
#       "КАРПОВ ВАЛЕРИЙ ЭДУАРДОВИЧ":{
#         "Место работы": "НИЦ «Курчатовский институт», Россия, Москва",
#         "Студент": False,
#         "Указан(а) в двух местах работы": False,
#       },
#       "КОРОЛЕВА МАРИЯ НИКОЛАЕВНА":{
#         "Место работы": "МГТУ им. Н.Э. Баумана, Россия, Москва",
#         "Студент": False,
#         "Указан(а) в двух местах работы": False,
#       }
#     },
#     "Журнал": {
#       "Название" : "ИНФОРМАЦИОННЫЕ И МАТЕМАТИЧЕСКИЕ ТЕХНОЛОГИИ В НАУКЕ И УПРАВЛЕНИИ",
#       "Ссылка на платформе" : "https://elibrary.ru/title_about_new.asp?id=58066",
#       "Инедксируется в SCOPUS": False,
#       "Инедксируется в WoS": False,
#     },
#     "Дата публикации": 28.04.2022,
#     "Международное соавторство": False
#   }
# }
