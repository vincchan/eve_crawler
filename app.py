import scrapy
from scrapy.http.request import Request
import w3lib.html

class ScienceDirectSpider(scrapy.Spider):
    name = 'crawler'
    selector_link_title = [
        '.result-list-title-link',
        '.publication_title',
    ]
    selector_next_link = [
        'li.next-link a ::attr(href)',
        '.pagination__btn--next ::attr(href)',
    ]
    base_url = [
        'https://www.sciencedirect.com',
        '',
    ]
    start_urls = [
         [
            'https://www.sciencedirect.com/search?qs=Biodiversity%20%C2%ABeconomic%20valuation%C2%BB%20%C2%ABvalue%20of%20nature%C2%BB%20%C2%ABecosystem%20services%C2%BB&date=2000-2020&articleTypes=REV%2CFLA&show=50',
            'https://www.sciencedirect.com/search?qs=Biodiversity%20%C2%ABwillingness%20to%20pay%C2%BB%20%C2%ABvalue%20of%20nature%C2%BB%20%C2%ABecosystem%20services%C2%BB&date=2000-2020&articleTypes=REV%2CFLA&show=50',
            'https://www.sciencedirect.com/search?qs=Biodiversity%20%C2%ABeconomic%20valuation%C2%BB%20%C2%ABtravel%20costs%C2%BB%20%C2%ABecosystem%20services%C2%BB&date=2000-2020&articleTypes=REV%2CFLA&show=50',
            'https://www.sciencedirect.com/search?qs=Biodiversity%20%C2%ABwillingness%20to%20pay%C2%BB%20%C2%ABtravel%20costs%C2%BB%20%C2%ABecosystem%20services%C2%BB&date=2000-2020&articleTypes=REV%2CFLA&show=50',
            'https://www.sciencedirect.com/search?qs=Biodiversity%20%C2%ABeconomic%20valuation%C2%BB%20%C2%ABhedonic%20pricing%C2%BB%20%C2%ABecosystem%20services%C2%BB&date=2000-2020&articleTypes=REV%2CFLA&show=50',
            'https://www.sciencedirect.com/search?qs=Biodiversity%20%C2%ABwillingness%20to%20pay%C2%BB%20%C2%ABhedonic%20pricing%C2%BB%20%20%C2%ABecosystem%20services%C2%BB&date=2000-2020&articleTypes=REV%2CFLA&show=50',
            'https://www.sciencedirect.com/search?qs=Biodiversity%20%C2%ABeconomic%20valuation%C2%BB%20%C2%ABstated%20preference%C2%BB%20%C2%ABcontingent%20valuation%C2%BB%20%C2%ABecosystem%20services%C2%BB&date=2000-2020&articleTypes=REV%2CFLA&show=50',
            'https://www.sciencedirect.com/search?qs=Biodiversity%20%C2%ABwillingness%20to%20pay%C2%BB%20%C2%ABstated%20preference%C2%BB%20%C2%ABcontingent%20valuation%C2%BB%20%C2%ABecosystem%20services%C2%BB&date=2000-2020&articleTypes=REV%2CFLA&show=50',
            'https://www.sciencedirect.com/search?qs=Biodiversity%20%C2%ABeconomic%20valuation%C2%BB%20%C2%ABstated%20preference%C2%BB%20%C2%ABchoice%20experiment%C2%BB%20%C2%ABecosystem%20services%C2%BB&date=2000-2020&articleTypes=REV%2CFLA&show=50',
            'https://www.sciencedirect.com/search?qs=Biodiversity%20%C2%ABwillingness%20to%20pay%C2%BB%20%C2%ABstated%20preference%C2%BB%20%C2%ABchoice%20experiment%C2%BB%20%C2%ABecosystem%20services%C2%BB&date=2000-2020&articleTypes=REV%2CFLA&show=50',
            'https://www.sciencedirect.com/search?qs=Biodiversity%20%C2%ABeconomic%20valuation%C2%BB%20%C2%ABstated%20preference%C2%BB%20%C2%ABchoice%20modelling%C2%BB%20%C2%ABecosystem%20services%C2%BB&date=2000-2020&articleTypes=REV%2CFLA&show=50',
            'https://www.sciencedirect.com/search?qs=Biodiversity%20%C2%ABwillingness%20to%20pay%C2%BB%20%C2%ABstated%20preference%C2%BB%20%C2%ABchoice%20modelling%C2%BB%20%C2%ABecosystem%20services%C2%BB&date=2000-2020&articleTypes=REV%2CFLA&show=50',
        ],
        [
            'https://onlinelibrary.wiley.com/action/doSearch?AllField=Biodiversity+%C2%ABeconomic+valuation%C2%BB+%C2%ABvalue+of+nature%C2%BB+%C2%ABecosystem+services%C2%BB&PubType=journal&content=articlesChapters&countTerms=true&target=default&AfterYear=2000&BeforeYear=2020',
            'https://onlinelibrary.wiley.com/action/doSearch?AfterYear=2000&AllField=Biodiversity+%C2%ABwillingness+to+pay%C2%BB+%C2%ABvalue+of+nature%C2%BB+%C2%ABecosystem+services%C2%BB&BeforeYear=2020&content=articlesChapters&countTerms=true&target=default&startPage=&PubType=journal',
            'https://onlinelibrary.wiley.com/action/doSearch?AfterYear=2000&AllField=Biodiversity+%C2%ABeconomic+valuation%C2%BB+%C2%ABtravel+costs%C2%BB+%C2%ABecosystem+services%C2%BB&BeforeYear=2020&content=articlesChapters&countTerms=true&target=default&startPage=&PubType=journal',
            'https://onlinelibrary.wiley.com/action/doSearch?AllField=Biodiversity+%C2%ABwillingness+to+pay%C2%BB+%C2%ABtravel+costs%C2%BB+%C2%ABecosystem+services%C2%BB&PubType=journal&content=articlesChapters&countTerms=true&target=default&AfterYear=2000&BeforeYear=2020',
            'https://onlinelibrary.wiley.com/action/doSearch?AfterYear=2000&AllField=Biodiversity+%C2%ABeconomic+valuation%C2%BB+%C2%ABhedonic+pricing%C2%BB+%C2%ABecosystem+services%C2%BB&BeforeYear=2020&content=articlesChapters&countTerms=true&target=default&startPage=&PubType=journal',
            'https://onlinelibrary.wiley.com/action/doSearch?AllField=Biodiversity+%C2%ABwillingness+to+pay%C2%BB+%C2%ABhedonic+pricing%C2%BB+%C2%ABecosystem+services%C2%BB&PubType=journal&content=articlesChapters&countTerms=true&target=default&AfterYear=2000&BeforeYear=2020',
            'https://onlinelibrary.wiley.com/action/doSearch?AllField=Biodiversity+%C2%ABeconomic+valuation%C2%BB+%C2%ABstated+preference%C2%BB+%C2%ABcontingent+valuation%C2%BB+%C2%ABecosystem+services%C2%BB&PubType=journal&content=articlesChapters&countTerms=true&target=default&AfterYear=2000&BeforeYear=2020',
            'https://onlinelibrary.wiley.com/action/doSearch?AllField=Biodiversity+%C2%ABwillingness+to+pay%C2%BB+%C2%ABstated+preference%C2%BB+%C2%ABcontingent+valuation%C2%BB+%C2%ABecosystem+services%C2%BB&PubType=journal&content=articlesChapters&countTerms=true&target=default&AfterYear=2000&BeforeYear=2020',
            'https://onlinelibrary.wiley.com/action/doSearch?AllField=Biodiversity+%C2%ABeconomic+valuation%C2%BB+%C2%ABstated+preference%C2%BB+%C2%ABchoice+experiment%C2%BB+%C2%ABecosystem+services%C2%BB&PubType=journal&content=articlesChapters&countTerms=true&target=default&AfterYear=2000&BeforeYear=2020',
            'https://onlinelibrary.wiley.com/action/doSearch?AllField=Biodiversity+%C2%ABwillingness+to+pay%C2%BB+%C2%ABstated+preference%C2%BB+%C2%ABchoice+experiment%C2%BB+%C2%ABecosystem+services%C2%BB&PubType=journal&content=articlesChapters&countTerms=true&target=default&AfterYear=2000&BeforeYear=2020',
            'https://onlinelibrary.wiley.com/action/doSearch?AllField=Biodiversity+%C2%ABeconomic+valuation%C2%BB+%C2%ABstated+preference%C2%BB+%C2%ABchoice+modelling%C2%BB+%C2%ABecosystem+services%C2%BB&PubType=journal&content=articlesChapters&countTerms=true&target=default&AfterYear=2000&BeforeYear=2020',
            'https://onlinelibrary.wiley.com/action/doSearch?AllField=Biodiversity+%C2%ABwillingness+to+pay%C2%BB+%C2%ABstated+preference%C2%BB+%C2%ABchoice+modelling%C2%BB+%C2%ABecosystem+services%C2%BB&PubType=journal&content=articlesChapters&countTerms=true&target=default&AfterYear=2000&BeforeYear=2020',
        ]
    ]

    
    result_set = set()

    headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

    def start_requests(self):
        index = 0
        for sites in self.start_urls:
            for url in sites:
                request = Request(url, callback=self.parse, headers=self.headers)
                request.meta["site_index"] = index
                yield request
            index = index + 1

    def parse(self, response):
        site_index = response.meta["site_index"]
        for title in response.css(self.selector_link_title[site_index]):
            title_property = w3lib.html.remove_tags(title.get())
            set_len_old = len(self.result_set)
            self.result_set.add(title_property)
            if(len(self.result_set) > set_len_old):
                yield {"title" : title_property}
            #yield {"title" : title_property}

        next_page = response.css(self.selector_next_link[site_index]).get()
        if next_page is not None:
            next_page_full = self.base_url[site_index] + next_page

            request =  Request(next_page_full, callback=self.parse, headers = self.headers)
            request.meta["site_index"] = site_index
            yield request