import scrapy
import urllib.parse
from tokped.items import ProductItem

scrolling_script = """
    const scrollInterval = setInterval(() => {
        const elements = document.querySelectorAll('div.IOLazyloading');
        if (elements.length > 0) {
            elements[0].scrollIntoView();
        } else {
            clearInterval(scrollInterval);
        }
    }, 500);
"""


def get_meta_dict():
    return dict(
        playwright=True,
        playwright_include_page=True,
    )


def scrape_with_xpath(response, path):
    if "@href" in path:
        return urllib.parse.unquote(response.xpath(path).get().split("r=")[-1])
    return response.xpath(path).get()


product_dict = {
    "product_name": './/div[contains(@class, "prd_link-product-name")]/text()',
    "product_price": './/div[contains(@class, "prd_link-product-price")]/text()',
    "product_discount": './/div[contains(@class, "prd_badge-product-discount")]/text()',
    "original_price": './/div[contains(@class, "prd_label-product-slash-price")]/text()',
    "product_image": './/div[contains(@class, "pcv3_img_container")]/img/@src',
    "merchant_name": './/span[contains(@class, "prd_link-shop-name")]/text()',
    "merchant_loc": './/span[contains(@class, "prd_link-shop-loc")]/text()',
    "rating": './/span[contains(@class, "prd_rating-average-text")]/text()',
    "product_sold": './/span[contains(@class, "prd_label-integrity")]/text()',
    "product_detail_link": './/div[contains(@class, "prd_container-card")]//a/@href',
}


class SearchSpider(scrapy.Spider):
    name = "tokped-search"

    def __init__(self, keyword="samsung", max_items="100", *args, **kwargs):
        super(SearchSpider, self).__init__(*args, **kwargs)
        self.n_items = 0
        self.max_items = int(max_items)
        self.page = 1
        self.url = f"https://www.tokopedia.com/search?q={keyword}&page={self.page}"

    def start_requests(self):
        yield scrapy.Request(self.url, meta=get_meta_dict())

    async def parse(self, response):
        page = response.meta["playwright_page"]
        try:
            await page.evaluate(scrolling_script)
            await page.wait_for_timeout(6000)

            page_content = await page.content()
            sel = scrapy.Selector(text=page_content)

            products = sel.css(
                'div[data-testid="divSRPContentProducts"] div[data-testid="divProductWrapper"]'
            )
            if len(products) == 0:
                raise Exception("No product found")

            for product in products:
                if self.n_items == self.max_items:
                    return

                product_item = ProductItem(
                    **{
                        k: scrape_with_xpath(product, v)
                        for k, v in product_dict.items()
                    }
                )
                self.n_items += 1
                yield product_item

            pagination = sel.css(
                "ul.css-1ni9y5x-unf-pagination-items > li > button::text"
            ).getall()
            if pagination is not None and self.page < int(
                pagination[-1].replace(".", "")
            ):
                self.page += 1
                yield response.follow(
                    f"https://www.tokopedia.com/search?q=samsung&page={self.page}",
                    meta=get_meta_dict(),
                )

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            
        finally:
            await page.close()
