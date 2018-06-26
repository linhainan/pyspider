# coding:utf-8
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def has_new_url(self):
        return self.new_url_size() != 0

    def has_old_url(self):
        return self.old_url_size() != 0

    def add_new_url(self, url):
        if url is None:
            return
        self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        return len(self.new_urls)

    def old_url_size(self):
        return len(self.old_urls)