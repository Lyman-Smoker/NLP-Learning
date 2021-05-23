# -*- coding:utf-8 -*-
from load_dictionary import load_dictionary

#完全切分
def fully_segment(text, dic):
    word_list = []
    for i in range(len(text)):                  # i 从 0 到text的最后一个字的下标遍历
        for j in range(i + 1, len(text) + 1):   # j 遍历[i + 1, len(text)]区间
            word = text[i:j]                    # 取出连续区间[i, j]对应的字符串
            if word in dic:                     # 如果在词典中，则认为是一个词
                word_list.append(word)
    return word_list

if __name__ == '__main__':
    dic = load_dictionary()
    print(fully_segment('商品和服务', dic))