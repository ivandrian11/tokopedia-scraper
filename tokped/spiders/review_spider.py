import scrapy
import os
import json


scrolling_script = """
    const scrollInterval = setInterval(() => {
        const elements = document.querySelectorAll('span[data-testid="lblItemUlasan"] + button');
        console.log(elements.length);
        if (elements.length > 0) {
            elements[0].scrollIntoView();
            elements[0].click();
        } else {
            clearInterval(scrollInterval);
        }
    }, 500);
"""


root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file_path = os.path.join(root, "output", "search.json")


def get_meta_dict():
    return dict(playwright=True, playwright_include_page=True)


class ReviewSpider(scrapy.Spider):
    name = "tokped-review"

    def __init__(self, *args, **kwargs):
        super(ReviewSpider, self).__init__(*args, **kwargs)
        self.access_page = 0

        with open(json_file_path, "r") as file:
            search_data = json.load(file)
            self.start_urls = [
                obj["product_detail_link"].split("?extParam=")[0] + "/review"
                for obj in search_data
                if obj["rating"] is not None
                and obj["product_sold"] is not None
                and len(obj["product_sold"].split()[0]) > 1
            ]

    def start_requests(self):
        yield scrapy.Request(self.start_urls[self.access_page], meta=get_meta_dict())

    async def parse(self, response):
        page = response.meta["playwright_page"]
        print(response.status)
        try:
            await page.wait_for_selector('span[data-testid="lblItemUlasan"]')
            await page.evaluate(scrolling_script)
            await page.wait_for_timeout(4200)

            page_content = await page.content()
            sel = scrapy.Selector(text=page_content)

            reviews = sel.css("section#review-feed > article")
            for review in reviews:
                rating = review.xpath(
                    './/div[@data-testid="icnStarRating"]/@aria-label'
                ).get()
                text = review.xpath(
                    './/span[@data-testid="lblItemUlasan"]/text()'
                ).get()
                if text is not None:
                    yield {"rating": rating, "review": text, "url": response.url}

            if self.access_page < len(self.start_urls) - 1:
                self.access_page += 1
                yield response.follow(
                    self.start_urls[self.access_page], meta=get_meta_dict()
                )

        except Exception as e:
            print(f"An error occurred: {str(e)}")

        finally:
            await page.close()
