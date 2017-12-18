# coding:utf8
import url_manager, html_downloader, html_parser, html_output

class Spider_Main(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = html_output.HtmlOutput()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d : %s"%(count, new_url))
                html_cont = self.downloader.downloader(new_url)
                new_urls, new_data = self.parser.parser(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.output.colletc_data(new_data)

                if count == 1000:
                    break
                count = count + 1
            except:
                print("craw failed")

        self.output.output_html()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
    obj_spider = Spider_Main()
    obj_spider.craw(root_url)
