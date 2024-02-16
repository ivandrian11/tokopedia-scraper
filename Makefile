run-search:
	scrapy crawl tokped-search -a keyword=samsung -a max_items=50 -o output/search.json
run-review:
	scrapy crawl tokped-review -o output/review.json
