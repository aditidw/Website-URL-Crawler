# Website-URL-Crawler

## Problem Statement
Create a web crawler app in python which, given a url seed, can crawl 
through all links on the page. While crawling the app should be able to return the url page, using gevent for asynchronous operations.

## Dependencies

```
pip install requests
pip install beautifulsoup4
```

## Features
* Created a code to get a list of URLs from a website.
* Multi-threaded.
* Enable or disable logging.
* Can return internal, external or both URLs.
* Can provide optional callback method for LIVE URL finds.

## Usage
The following code sample will scan site "https://news.ycombinator.com", with 0 threads and hiding all logging information.

### Find Internal & External URLs

```
crawler = UrlCrawler("https://news.ycombinator.com", 0, False)

# Print the found URLs
for url in crawler.crawl(UrlCrawler.Mode.ALL):
    print("Found: " + url)
```

Will output something like this:

![alt text](https://github.com/aditidw/Website-URL-Crawler/blob/main/Website_url_crawler_output.png?raw=true)

### Finding all the INTERNAL URLs
```
crawler = UrlCrawler("https://news.ycombinator.com", 0, False)

# Print the found URLs
for url in crawler.crawl(UrlCrawler.Mode.INTERNAL):
    print("Found: " + url)
```

Will Output:

```
Found: https://news.ycombinator.com
```

### Finding all the EXTERNAL URLs
```
crawler = UrlCrawler("https://news.ycombinator.com", 0, False)

# Print the found URLs
for url in crawler.crawl(UrlCrawler.Mode.EXTERNAL):
    print("Found: " + url)
```

Will Output:

```
Found: https://onivim.io/
Found: https://mark.mcnally.je/blog/post/My%20%C2%A34%20a%20month%20server%20can%20handle%204.2%20million%20requests%20a%20day
Found: https://commoncog.com/blog/the-problems-with-deliberate-practice/
Found: https://www.locserendipity.com/PushPlay.html
Found: https://join-lemmy.org/
Found: https://digitalrightswatch.org.au/2021/09/02/australias-new-mass-surveillance-mandate/
Found: https://esamultimedia.esa.int/docs/science/Webb-LaunchKit_EN.pdf
Found: https://www.rodrigoaraujo.me/posts/lets-build-an-lc-3-virtual-machine/
Found: http://www.paperterm.org/notes.html
Found: https://blog.coinbase.com/the-sec-has-told-us-it-wants-to-sue-us-over-lend-we-have-no-idea-why-a3a1b6507009
Found: https://www.reuters.com/world/china/chinese-activist-ai-weiwei-says-credit-suisse-closing-his-foundations-bank-2021-09-07/
Found: https://pvk.ca/Blog/2014/03/15/sbcl-the-ultimate-assembly-code-breadboard/
Found: https://www.fastcompany.com/90670635/ex-googlers-raise-40-million-to-democratize-natural-language-ai
Found: https://www.newenglandhistoricalsociety.com/great-boston-molasses-disaster-1919/
Found: https://rolltop-indigo.blogspot.com/2018/10/fantasy-cartography-just-add-something.html
Found: https://www.bloomberg.com/news/articles/2021-09-07/ford-is-said-to-hire-away-executive-leading-apple-s-car-project
Found: https://github.com/iperov/DeepFaceLive
Found: https://spectrum.ieee.org/climate-change-2654802125
Found: https://www.ycombinator.com/companies/swiftsku/jobs/YhllV1x-sales-account-executive
Found: https://quidplura.com/2021/09/07/but-down-in-the-underground-youll-find-someone-true-2/
Found: https://blog.spiceai.org/posts/2021/09/07/introducing-spice.ai-open-source-time-series-ai-for-developers/
Found: https://github.com/spikecodes/libreddit
Found: https://www.usgo.org/sites/default/files/pdf/TROMPFINAL5-6-16.pdf
Found: https://bonsaibrowser.com
Found: https://quuxplusone.github.io/blog/2021/09/05/float-format/
Found: https://spectrum.ieee.org/a-soft-wearable-brain-machine-interface
Found: https://twitter.com/id_aa_carmack/status/1435307747470454787
Found: https://www.wsj.com/articles/a-big-hurdle-to-fixing-the-chip-shortage-substrates-11630771200
Found: https://www.nationalboard.org/Index.aspx?pageID=164&ID=226
Found: https://protonmail.com/blog/sir-tim-berners-lee-advisory-board/
Found: https://www.ycombinator.com/apply/
Found: https://github.com/HackerNews/API
Found: http://www.ycombinator.com/legal/
Found: http://www.ycombinator.com/apply/

Process finished with exit code 0

```

### Using Callback (getting live URL finds as they happen)
If you wish to get each URL as it is found rather than at the end in an array, you can pass an optional argument to the crawl() method that will do exactly that. For example:

```
crawler = UrlCrawler("https://news.ycombinator.com")

def callback(url):
    print("Found: " + url)

# Get ALL urls and print them
crawler.crawl(UrlCrawler.Mode.ALL, callback)
```

### Complex Part / Not able to do
Unable to use gevent for asynchronous operation. Can you please help me understand how I can do that? I am just able to figure out just how to crawle the URLs but not asyncronously. 
