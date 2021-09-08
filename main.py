from WebsiteUrlCrawler import UrlCrawler


def main():
    # Create a site crawler with 5 threads and allowing logging
    crawler = UrlCrawler("https://news.ycombinator.com")

    # Get ALL urls and print them
    for url in crawler.crawl(UrlCrawler.Mode.ALL):
        print("Found: " + url)


if __name__ == '__main__':
    main()
