"""

"""

from icrawler.builtin import GoogleImageCrawler
import time
import os
class IClawer:
    KEYWORD_DONE_FILE = 'keywords_done.log'
    KEYWORD_NEW_FILE = 'keywords_new.log'
    new_keywords =set()
    done_keywords = set()
    def __init__(self):
        pass

    def claw(self, keyword, size=10):
        start =time.time()
        self._load_keywords_done()
        if keyword in self.done_keywords:
            print 'keyword: [' + keyword + '] has already done.'
            return

        google_crawler = GoogleImageCrawler(
            feeder_threads=1,
            parser_threads=2,
            downloader_threads=4,
            storage={'root_dir': '/home/zluo/food'})
        google_crawler.crawl(keyword=keyword + ' dishes', max_num=size)
        end = time.time()
        print(end - start)
        self.write_log(self.KEYWORD_DONE_FILE, keyword)

    def write_log(self, filename, message):
        with open(filename, 'a') as f:
            f.write(message)
            f.write('\n')

    def _load_keywords_done(self):
        with open(self.KEYWORD_DONE_FILE, 'r') as f:
            line = f.readline().rstrip('\n')
            while line:
                self.done_keywords.add(line)
                line = f.readline().rstrip('\n')
        pass


keydict = {'healthy': {'scallop'}}

keywords={'burger', 'seafood', 'salard', 'egg', 'fish', 'meat', 'veg', 'fruit', 'fast food', 'coconut', 'mushroom', 'pizza', 'soup','cheese','stew',
          'beef','lamb', 'sausage', 'seasame seed', 'pork', 'shrimp', 'bread', 'breakfast', 'dumpling', 'noddle','bread','potato','rice', 'maize', 'Sushi','chicken',
          'duck','ham', 'sandwich', 'turkey','pineapple', 'grape','pasta','goose', 'pudding', 'chunky', 'bean', 'rib','barbecue','eggplant','tomato','seaweed', 'tofu',
          'wraps','pepper','onion','micheline starred', 'meatball','pickled', 'omelette','pancake','bacon','spaghetti','carrot','pumpkin','celery','cucumber', 'cabbage','cauliflower','keto','vegan', 'curry','restaurant','moule', 'fries'}



seafoods={'crab', 'crab cake', 'thai crab', 'lobster', 'fish egg','scallop', 'squid', 'oyster', 'salmon', 'tuna'}
vegs={}
fruits={'mango', 'mango tenderloin','avocado', 'avocado pasta', 'avocado omelette','stawberry', 'banana'}
meats={}

main={'rice', 'noodle', 'pancake'}

rice_dishes={'paella', 'filipino', 'rice egg', 'arroz', 'rice seafood', 'con leche', 'rice pudding', 'rice soup', 'vietnamese pho soup'}
soups = {'chicken soup', 'french soup', 'burger soup', 'vegetable soup', 'healthy soup', 'chunky soup', 'fish soup', 'filipino soup', 'bean soup', 'carrot soup','cabbage soup','irish potatoes','mashed potatos', 'beef stew'}
porks = {'pork stuffed', 'lettuce wraps', 'pulled pork', 'healthy pulled pork', 'pork tenderloin', 'lamb tenderloin', 'beef tenderloin'}

cookmethods ={'boiled', 'steam', 'fried', 'stew', 'roast','bbq', 'smoked','stir fry', 'soup', 'pickled'}
nationals ={'french','italian', 'indian', 'chinese', 'greek' ,'mexico', 'japanese','korean','sichuan','arabian', 'brazil','guangdong', 'spanish','russian', 'german', 'thai', 'irish', 'jamaican','cuba','british','scottish', 'sweden','singapore','vietnamese'}
clawer = IClawer()

def generate_keyword(first, second):
    for one in first:
        for two in second:
            if (one not in second) and (two not in one):
                clawer.write_log(clawer.KEYWORD_NEW_FILE, one + ' ' + two)

generate_keyword(nationals, keywords)

new_keywords =set()
def load_keywords_new():
    with open(clawer.KEYWORD_NEW_FILE, 'r') as f:
        line = f.readline().rstrip('\n')
        while line:
            new_keywords.add(line)
            line = f.readline().rstrip('\n')

    os.remove(clawer.KEYWORD_NEW_FILE)
    print len(new_keywords)
    with open(clawer.KEYWORD_NEW_FILE, 'a') as f:
        for keyword in new_keywords:
            f.write(keyword)
            f.write('\n')
    pass

load_keywords_new()

for keyword in new_keywords:
    clawer.claw(keyword, 1000)
