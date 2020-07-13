import time
import sys

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from pars_search_v1_0.spiders.spider1 import ScrapingSPIDER, ScrapingSPIDER2, ScrapingSPIDER3, ScrapingSPIDER4

from googlesearch import search
from messages import start_message, after_search_message
from logic import handling_input

print(start_message)

message = "Продолжить?  да/нет___:"

out_message, action = handling_input(message)
print(out_message)
action()

search_result_list = list(search('Junior python developer', stop=4, pause=1))

print("Вот что выдал google")
print(*search_result_list, "\n", sep='\n', end='\n')

time.sleep(3)
print(after_search_message)

message = "Хотите запарсить? да/нет___:"
out_message, action = handling_input(message)
print(out_message)
action()

try:
    process = CrawlerProcess(get_project_settings())
    process.crawl(ScrapingSPIDER2)
    process.crawl(ScrapingSPIDER3)
    process.crawl(ScrapingSPIDER4)
    process.crawl(ScrapingSPIDER)
    process.start(stop_after_crawl=True)
except:
    print("К сожалению что-то пошло не так. Закрываемся")
    sys.exit()

print('Готово, в папке с этим файлом должны появиться данные в формате json')
