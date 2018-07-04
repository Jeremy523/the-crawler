import scrapy


class RecipeSpider(scrapy.Spider):
    name = "ingredients"
    start_urls = [
        'http://www.geniuskitchen.com/recipe/best-banana-bread-2886',
        'http://www.geniuskitchen.com/recipe/oatmeal-raisin-cookies-35813'
    ]

    def parse(self, response):
        for recipe in response.css('span.food'):
            yield {
                #'food': recipe.css('a.text::text').extract_first(),
                'food': recipe.xpath('a/text()').extract_first(),
            }

        # next_page = response.css('lpi.next a::attr("href")').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)