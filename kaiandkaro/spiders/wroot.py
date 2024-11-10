import scrapy

class WrootSpider(scrapy.Spider):
    name = "wroot"
    start_urls = [
        'https://kaiandkaro.com/vehicles?model_make_vehicle_type=Automobile'  # Replace with actual URL if different
    ]

    def parse(self, response):
        # Loop through each car listing on the page
        for car in response.css('div.car-listing'):  # Adjust if the class is different
            yield {
                'name': car.css('h2::text').get(),  # Adjust if needed to target the car model
                'price': car.css('span.price::text').get()  # Adjust to match the price selector
            }

        # Follow pagination links if available to scrape all pages
        next_page = response.css('a.next-page::attr(href)').get()  # Adjust for actual pagination link
        if next_page is not None:
            yield response.follow(next_page, self.parse)
