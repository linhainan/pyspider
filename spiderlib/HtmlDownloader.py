# coding:utf-8
from urllib import request
class HtmlDownloader(object):

    @staticmethod
    def download(url):
        if url is None:
            return
        user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"
        headers = {'User_Agent': user_agent}
        dl_request = request.Request(url, headers=headers)
        response = request.urlopen(dl_request)

        if response.getcode() == 200:
            response.encoding = 'utf-8'
            return response.read()

    @staticmethod
    def set_proxy(proxy_addr):
        proxy = request.ProxyHandler({'http': proxy_addr})
        opener = request.build_opener(proxy, request.HTTPHandler)
        request.install_opener(opener)

