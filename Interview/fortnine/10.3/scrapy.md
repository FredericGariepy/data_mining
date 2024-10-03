#### Use the scrapy shell:
- `scrapy shell "http://quotes.toscrape.com"`
###### using css selectors
- `response.css("title::text")[0].extract()` \
 :: for css classes \
 \# for css IDs
###### using Xpath
- `response.xpath("//title/text()").extract()`
- `response.xpath("//span[@class='text']/text()").extract()` # Xpath w/ class



