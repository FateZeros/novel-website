from toapi import Item, XPath

class HotBook(Item):
    # 需要解析的字段
    __base_url__ = 'http://91baby.mama.cn'
    title = XPath('//a[@class="xst"]/text()[1]')
    author = XPath('//a[@class="xst"]/text()[1]')
    url = XPath('//a[@class="xst"]/@href')
    book_id = XPath('//a[@class="xst"]/@href')

    # `clean__xxx`方法是用来进一步格式化信息用的
    def clean_title(self, title):
        if '《' in title:
            return title[title.find('\u300a') + 1:title.find('\u300b')][:10]
        else:
            return '广告贴'

    def clean_author(self, author):
        if ':' in author:
            return author[author.find(':') + 1:author.find('(')]
        elif '：' in author:
            return author[author.find('：') + 1:author.find('（')]
        else:
            return '广告贴'

    def clean_book_id(self, book_id):
        return book_id.split('-')[1]

    class Meta:
        source = XPath('//tbody[@class="thread_tbody"]')
        # 定义路由 左边是我们内网的url，右边是源站的url
        # 比如 我们访问  www.api.url/hotbook?page=1 
        # 框架就会向 www.xxx.com/form-171-1.html 发送请求
        route = {'/hotbook?page=:page': '/forum-171-:page.html'}