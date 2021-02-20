import requests
from lxml import etree
from pprint import pprint

class weibo_hot:
    '''
    解析微博热搜和要闻榜单
    '''
    def __init__(self,website):
        self.update(website)
        self.__url = website
        
    def update(self,website):
        request_result = requests.get(website)
        request_result_in_HTML_form = etree.HTML(request_result.text)
        self.__contents = request_result_in_HTML_form.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr[*]/td[2]/a/text()')
        
    def get_contents(self):
        return self.__contents
        
    def print_contents(self):
        pprint(self.__contents)
        
if __name__ == '__main__':
    
    website_realtimehot = 'https://s.weibo.com/top/summary?cate=realtimehot'
    website_socialevent = 'https://s.weibo.com/top/summary?cate=socialevent'
    
    realtimehot = weibo_hot(website_realtimehot)
    socialevent = weibo_hot(website_socialevent)
    
    pprint(realtimehot.get_contents())
    pprint(socialevent.get_contents())