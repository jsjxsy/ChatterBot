# -*- coding: utf-8 -*-
# scrapy runspider shiwanwhy.py


import scrapy
from time import gmtime, strftime
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class ShiwanSpider(scrapy.Spider):
    name = "shiwan"
    count = 0
    file = open("shiwanwhy_" + strftime("%Y_%m_%d _%H%M%S", gmtime()), 'w')
    file.write('categories:\n- shiwanwhy\nconversations:\n')
		
    start_urls = [
        'http://www.tom61.com/shiwangeweishime/qimiaoderenti/',
        'http://www.tom61.com/shiwangeweishime/qimiaoderenti/index_2.html',
        'http://www.tom61.com/shiwangeweishime/qimiaoderenti/index_3.html',
        'http://www.tom61.com/shiwangeweishime/qimiaoderenti/index_4.html',
        'http://www.tom61.com/shiwangeweishime/qimiaoderenti/index_5.html',
        'http://www.tom61.com/shiwangeweishime/qimiaoderenti/index_6.html',
        'http://www.tom61.com/shiwangeweishime/qimiaoderenti/index_7.html',
        'http://www.tom61.com/shiwangeweishime/qimiaoderenti/index_8.html',
        'http://www.tom61.com/shiwangeweishime/qimiaoderenti/index_9.html',
        'http://www.tom61.com/shiwangeweishime/qimiaoderenti/index_10.html',
        'http://www.tom61.com/shiwangeweishime/qimiaoderenti/index_11.html',
        'http://www.tom61.com/shiwangeweishime/qimiaoderenti/index_12.html',
        'http://www.tom61.com/shiwangeweishime/qimiaoderenti/index_13.html',
        'http://www.tom61.com/shiwangeweishime/jiankangdeshenghuo/',
        'http://www.tom61.com/shiwangeweishime/jiankangdeshenghuo/index_2.html',
        'http://www.tom61.com/shiwangeweishime/jiankangdeshenghuo/index_3.html',
        'http://www.tom61.com/shiwangeweishime/jiankangdeshenghuo/index_4.html',
        'http://www.tom61.com/shiwangeweishime/shenbiandechangshi/',
        'http://www.tom61.com/shiwangeweishime/shenbiandechangshi/index_2.html',
        'http://www.tom61.com/shiwangeweishime/shenbiandechangshi/index_3.html',
        'http://www.tom61.com/shiwangeweishime/shenbiandechangshi/index_4.html',
        'http://www.tom61.com/shiwangeweishime/shenbiandechangshi/index_5.html',
        'http://www.tom61.com/shiwangeweishime/shenbiandechangshi/index_6.html',
        'http://www.tom61.com/shiwangeweishime/keaidedongwu/',
        'http://www.tom61.com/shiwangeweishime/keaidedongwu/index_2.html',
        'http://www.tom61.com/shiwangeweishime/keaidedongwu/index_3.html',
        'http://www.tom61.com/shiwangeweishime/keaidedongwu/index_4.html',
        'http://www.tom61.com/shiwangeweishime/keaidedongwu/index_5.html',
        'http://www.tom61.com/shiwangeweishime/keaidedongwu/index_6.html',
        'http://www.tom61.com/shiwangeweishime/keaidedongwu/index_7.html',
        'http://www.tom61.com/shiwangeweishime/keaidedongwu/index_8.html',
        'http://www.tom61.com/shiwangeweishime/keaidedongwu/index_9.html',
        'http://www.tom61.com/shiwangeweishime/keaidedongwu/index_10.html',
        'http://www.tom61.com/shiwangeweishime/keaidedongwu/index_11.html',
        'http://www.tom61.com/shiwangeweishime/keaidedongwu/index_12.html',
        'http://www.tom61.com/shiwangeweishime/keaidedongwu/index_13.html',
        'http://www.tom61.com/shiwangeweishime/keaidedongwu/index_14.html',
        'http://www.tom61.com/shiwangeweishime/youqudezhiwu/',
        'http://www.tom61.com/shiwangeweishime/youqudezhiwu/index_2.html',
        'http://www.tom61.com/shiwangeweishime/youqudezhiwu/index_3.html',
        'http://www.tom61.com/shiwangeweishime/youqudezhiwu/index_4.html',
        'http://www.tom61.com/shiwangeweishime/youqudezhiwu/index_5.html',
        'http://www.tom61.com/shiwangeweishime/youqudezhiwu/index_6.html',
        'http://www.tom61.com/shiwangeweishime/youqudezhiwu/index_7.html',
        'http://www.tom61.com/shiwangeweishime/youqudezhiwu/index_8.html',
        'http://www.tom61.com/shiwangeweishime/meilidediqiu/',
        'http://www.tom61.com/shiwangeweishime/meilidediqiu/index_2.html',
        'http://www.tom61.com/shiwangeweishime/meilidediqiu/index_3.html',
        'http://www.tom61.com/shiwangeweishime/meilidediqiu/index_4.html',
        'http://www.tom61.com/shiwangeweishime/meilidediqiu/index_5.html',
        'http://www.tom61.com/shiwangeweishime/meilidediqiu/index_6.html',
        'http://www.tom61.com/shiwangeweishime/meilidediqiu/index_7.html',
        'http://www.tom61.com/shiwangeweishime/meilidediqiu/index_8.html',
        'http://www.tom61.com/shiwangeweishime/shenmideyuzhou/',
        'http://www.tom61.com/shiwangeweishime/shenmideyuzhou/index_2.html',
        'http://www.tom61.com/shiwangeweishime/shenmideyuzhou/index_3.html',
        'http://www.tom61.com/shiwangeweishime/shenmideyuzhou/index_4.html',
        'http://www.tom61.com/shiwangeweishime/shenqidekeji/',
        'http://www.tom61.com/shiwangeweishime/shenqidekeji/index_2.html',
        'http://www.tom61.com/shiwangeweishime/shenqidekeji/index_3.html',
        'http://www.tom61.com/shiwangeweishime/shenqidekeji/index_4.html',
        'http://www.tom61.com/shiwangeweishime/shenqidekeji/index_5.html',
        'http://www.tom61.com/shiwangeweishime/junshiyujiaotong/',
        'http://www.tom61.com/shiwangeweishime/junshiyujiaotong/index_2.html',
        'http://www.tom61.com/shiwangeweishime/junshiyujiaotong/index_3.html',
        'http://www.tom61.com/shiwangeweishime/junshiyujiaotong/index_4.html',
        'http://www.tom61.com/shiwangeweishime/junshiyujiaotong/index_5.html',
        'http://www.tom61.com/shiwangeweishime/junshiyujiaotong/index_6.html',
        'http://www.tom61.com/shiwangeweishime/shulihuazhimi/',
        'http://www.tom61.com/shiwangeweishime/shulihuazhimi/index_2.html',
        'http://www.tom61.com/shiwangeweishime/shulihuazhimi/index_3.html',
        'http://www.tom61.com/shiwangeweishime/shulihuazhimi/index_4.html',
        'http://www.tom61.com/shiwangeweishime/wenhuayishu/',
        'http://www.tom61.com/shiwangeweishime/wenhuayishu/index_2.html',
        'http://www.tom61.com/shiwangeweishime/tiyuyuguojia/',
        'http://www.tom61.com/shiwangeweishime/tiyuyuguojia/index_2.html',
        'http://www.tom61.com/shiwangeweishime/zhongwailishi/',
        'http://www.tom61.com/shiwangeweishime/zhongwailishi/index_2.html',
        'http://www.tom61.com/shiwangeweishime/zhongwailishi/index_3.html',

    '''
        'http://www.tom61.com/shiwangeweishime/jiankangdeshenghuo/',
        'http://www.tom61.com/shiwangeweishime/shenbiandechangshi/',
        'http://www.tom61.com/shiwangeweishime/keaidedongwu/',
        'http://www.tom61.com/shiwangeweishime/youqudezhiwu/',
        'http://www.tom61.com/shiwangeweishime/meilidediqiu/',
        'http://www.tom61.com/shiwangeweishime/shenmideyuzhou/',
        'http://www.tom61.com/shiwangeweishime/shenqidekeji/',
        'http://www.tom61.com/shiwangeweishime/junshiyujiaotong/',
        'http://www.tom61.com/shiwangeweishime/shulihuazhimi/',
        'http://www.tom61.com/shiwangeweishime/wenhuayishu/',
        'http://www.tom61.com/shiwangeweishime/tiyuyuguojia/',
        'http://www.tom61.com/shiwangeweishime/zhongwailishi/',
    '''
    ]
	
    '''
    def start_requests(self):
        pages = []
        for url in self.start_urls:
            page = scrapy.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"})
            pages.append(page)
        return pages
    '''
	
    def parse(self, response):
		
        for each in response.xpath('//*[@id="Mhead2_0"]/dl/dd'):
            href = response.urljoin(each.xpath('a/@href').extract()[0])
            text = each.xpath('a/@title').extract()[0]
            #print(href)
            #print(text)		
            request = scrapy.Request(href, callback=self.parse_answer);
            request.meta["question"] = text;
            yield request

    ''' 
                    print('11111111111\n')
                    #if(response.xpath('//*[@class="nextpage"]')='')
                    if (response.xpath('//*[@class="nextpage"]')):
                        print(response.xpath('//*[@class="nextpage"]'))
                        print(self）
                    print('333333333333333\n')
    '''
			
    def parse_answer(self, response):
        answer = ''
        for each in response.xpath('//*[@id="t_lb_box"]/div[1]/div/div[1]/div[3]/p'):
            extracted = each.xpath('text()').extract()
            for x in extracted:
                answer = answer + x.strip().replace('\r','').replace('\n','').replace('\t','')
        question = response.meta['question']
        self.count = self.count + 1		
        print(question)
        print(answer)
        print(self.count)
        self.file.write('- - ' + question + '\n')
        self.file.write('  - ' + answer + '\n')
        self.file.flush()

		