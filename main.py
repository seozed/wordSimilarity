from difflib import SequenceMatcher
from collections import Counter


def cacl_similarRatio(a, b):
    """
    返回两个单词之间的相似率

    """
    return  SequenceMatcher(None, a, b).ratio()

def find_similarWord(word, word_list, max=1):
    """
    寻找最相似的N个单词
    """

    word = word.strip()
    result = Counter()

    for k in word_list:
        k = k.strip()
        if word == k:
            continue

        similarRatio = cacl_similarRatio(word, k)
        result.update({k:similarRatio})

    return result.most_common(max)


if __name__ == '__main__':

    r = find_similarWord('abandon', open('words.txt').readlines(), max=5)
    print(r)
