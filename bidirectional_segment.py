# -*- coding:utf-8 -*-

from backward_segment import backward_segment
from forward_segment import forward_segment
from load_dictionary import load_dictionary

def count_single_char(word_list: list):  # 统计单字成词的个数
    return sum(1 for word in word_list if len(word) == 1)

#双向最长匹配
def bidirectional_segment(text, dic):
    f = forward_segment(text, dic)
    b = backward_segment(text, dic)
    if len(f) < len(b):                                  # 词数更少优先级更高
        return f
    elif len(f) > len(b):
        return b
    else:
        if count_single_char(f) < count_single_char(b):  # 单字更少优先级更高
            return f
        else:
            return b                                     # 都相等时逆向匹配优先级更高

if __name__ == '__main__':
    dic = load_dictionary()
    print(bidirectional_segment('研究生命起源', dic))