import scrapy
from pars_search_v1_0.items import ParsSearchV10Item


class ScrapingSPIDER(scrapy.Spider):
    name = '3dnews'
    start_urls = [
        'https://3dnews.ru/news/main'
    ]
    custom_settings = {'FEED_URI': "3dnews.json",
                       }

    def parse(self, response):
        items = ParsSearchV10Item()

        for article in response.css('div.article-entry'):
            title = article.css('.entry-header h1::text').extract()[0]
            items['title'] = title

            body = article.css('div.entry-body p::text').extract()
            items['body'] = "".join(body)

            image = article.css('div.source-wrapper img::attr(src)').extract()
            items['video'] = article.css('div.entry-body iframe::attr(src)').extract()
            if not image:
                items['image'] = article.css('div.entry-body div img::attr(src)').extract()

            yield items

            next_page = response.css('div.content-block-header.navlinkspan span.left.half a::attr(href)').get()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)


class ScrapingSPIDER2(scrapy.Spider):
    name = 'HeadHanter'
    start_urls = [
        'https://spb.hh.ru/search/vacancy?text=Python+developer'
    ]
    custom_settings = {'FEED_URI': "HH.json",
                       }

    def parse(self, response):
        items = ParsSearchV10Item()

        for article in response.css('.vacancy-serp-item'):
            items['title'] = article.css('.vacancy-serp-item__info a::text').extract()
            items['domain'] = article.css('.vacancy-serp-item__info a::attr(href)').extract()
            items['company'] = article.css('.vacancy-serp-item__meta-info a::text').extract()

            city = article.css('div.vacancy-serp-item__meta-info')[-1]
            city = city.css('div.vacancy-serp-item__meta-info span::text').extract()
            items['city'] = "".join(city)

            body = article.css('.vacancy-serp-item__row div.g-user-content div::text').extract()
            items['body'] = "".join(body)

            items['salary'] = article.css('.vacancy-serp-item__sidebar span::text').extract()
            yield items

            next_page = response.css('a.bloko-button.HH-Pager-Controls-Next.HH-Pager-Control::attr(href)').extract()
            if next_page:
                next_page = next_page[0]

            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse, dont_filter=False)


class ScrapingSPIDER3(scrapy.Spider):
    name = 'indeed'
    start_urls = [
        'https://www.indeed.com/q-Junior-Python-Developer-jobs.html'
    ]
    custom_settings = {'FEED_URI': "Indeed.json",
                       }
    items = ParsSearchV10Item()

    def parse(self, response):
        items = ParsSearchV10Item()

        for article in response.css('.jobsearch-SerpJobCard'):
            items['title'] = article.css('a::attr(title)').get()

            domain = article.css('a::attr(href)').get()
            items['domain'] = 'https://www.indeed.com' + domain

            company = article.css('div.sjcl a::text').get()
            if not company:
                items['company'] = article.css('div.sjcl span::text').get()

            items['city'] = article.css('div.sjcl span.location::text').get()
            items['body'] = article.css('div.summary li::text').get()

            yield items

        next_page = response.css('div.pagination a::attr(href)').extract()[-1]
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse, dont_filter=False)


class ScrapingSPIDER4(scrapy.Spider):
    name = 'jooble'
    start_urls = {
        'https://ru.jooble.org/работа-junior-python/Санкт+Петербург'
    }
    custom_settings = {'FEED_URI': "jooble.json",
                       }

    def parse(self, response):
        url = 'https://ru.jooble.org/работа-junior-python/Санкт+Петербург'
        items = ParsSearchV10Item()

        for article in response.css('.vacancy_wrapper'):
            title = article.css('h2.position span::text').extract()
            items['title'] = "".join(title)

            items['domain'] = article.css('div.left-static-block a::attr(href)').extract()
            items['salary'] = article.css('span.salary::text').get()
            items['company'] = article.css('p.company_region span.gray_text.company-name::text').get()

            body = article.css('div.desc span.description::text').get()

            if body and len(body) < 20:
                body = article.css('div.desc span.description span::text').extract()
                items['body'] = "".join(body)
            else:
                items['body'] = body

            yield items

        page = response.css('div.paging a.active::text').get()
        if page:
            count = int(page) + 1
            next_page = url + "?p=" + str(count)
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse, dont_filter=False)
