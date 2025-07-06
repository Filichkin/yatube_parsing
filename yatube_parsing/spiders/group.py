import scrapy


class GroupSpider(scrapy.Spider):
    name = 'group'
    allowed_domains = ['158.160.177.221']
    start_urls = ['http://158.160.177.221/']

    def parse(self, response):
        all_groups = response.css('a.group_link::attr(href)')
        for group_link in all_groups:
            yield response.follow(group_link, callback=self.parse_group)
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_group(self, response):
        yield {
            'group_name': response.css('.card-body h2::text').get(),
            'description': response.css('.group_descr::text').get(),
            'posts_count': (
                int(response.css(
                    '.posts_count::text'
                    ).get().replace('Записей:', '').strip())
                ),
        }
