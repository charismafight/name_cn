# encoding=utf-8
import jieba
from jieba import analyse
from collections import defaultdict
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def remove_punctuation(str):
    punct = set(u''':!),.:;?]}¢'"、。〉》」』】〕〗〞︰︱︳﹐､﹒
﹔﹕﹖﹗﹚﹜﹞！），．：；？｜｝︴︶︸︺︼︾﹀﹂﹄﹏､～￠
々‖•·ˇˉ―--′’”([{£¥'"‵〈《「『【〔〖（［｛￡￥〝︵︷︹︻
︽︿﹁﹃﹙﹛﹝（｛“‘-—_… 　''')
    return ''.join(filter(lambda x: x not in punct, str))


def remove_useless_word(str):
    words = open('material/interjections.txt', encoding='utf8').readlines()
    for x in words:
        str = str.replace(x.replace('\n', ''), '')
    return str


chuci = remove_punctuation((''.join(open("material/chuci.txt", encoding='utf8').readlines()).replace(' ', '')))
# replace useless words TODO
chuci = remove_useless_word(chuci)
seg_list = jieba.cut(chuci, cut_all=False)
word_count = defaultdict(int)
for word in seg_list:
    word_count[word] += 1


# print("/".join(seg_list))
# print(word_count)

# top_words_frequency = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:200]
# print(top_words_frequency)


# for word, fre in top_words_frequency[:200]:
#     print(word, fre)

# key_words = jieba.analyse.textrank(chuci, topK=200, withWeight=True,
#                                    allowPOS=('nb', 'n', 'nr', 'ns', 'a', 'ad', 'an', 'nt', 'nz', 'v', 'd'))
#
# print(key_words)


def show_img(wc):
    plt.figure()
    plt.imshow(wc)
    plt.axis("off")


wc = WordCloud(font_path=u"static/fonts/simhei.ttf",
               max_words=200,
               width=1920,
               height=1080,
               background_color="black",
               margin=5)

wc.generate_from_frequencies(word_count)
wc.to_file('result/chuci.png')
show_img(wc)
