class StrOpts:
    """
    strStr
    leetcode: Implement strStr() | LeetCode OJ
    lintcode: lintcode - (13) strstr
    strstr (a.k.a find sub string), is a useful function in string operation.
    You task is to implement this function.
    For a given source string and a target string,
    you should output the "first" index(from 0) of target string in source st
    ring.
    If target is not exist in source, just return -1.
    Example
    If source="source" and target="target", return -1.
    If source="abcdabcdefg" and target="bcd", return 1.
    Challenge
    O(n) time.
    Clarification
    Do I need to implement KMP Algorithm in an interview?
    - Not necessary. When this problem occurs in an interview,
    the interviewer just want to test your basic implementation ability.
    """

    @staticmethod
    # single for with rollback
    def str_str1(source, target):
        if source is None or target is None:
            return -1
        j = 0
        mark = 0
        for i in range(0, len(target)):
            if source[j] == target[i]:
                if j == 0:
                    mark = i

                if j == len(source) - 1:
                    return mark

                j += 1
            elif j != 0:
                i = mark
                j = 0
                mark = 0
        return -1

    @staticmethod
    # double for
    def str_str2(source, target):
        if source is None or target is None:
            return -1
        mark = 0
        for i in range(0, len(target)):
            for j in range(0, len(source)):
                if target[i + j] != source[j]:
                    break

                if j == len(source) - 1:
                    return i
        return -1

    # KMP? NotExist

    @staticmethod
    def try_str_str():
        source = 'in'
        target = 'stronginstring'
        print('method1', StrOpts.str_str1(source, target))
        print('method2', StrOpts.str_str2(source, target))

    """
    CC150: (158) Two Strings Are Anagrams
    Write a method anagram(s,t) to decide if two strings are anagrams or not.
    Example
    Given s="abcd", t="dcab", return true.
    Challenge
    O(n) time, O(1) extra space
    """

    @staticmethod
    # simple compare
    def anagrams_word1(source, target):
        if source is None or target is None or len(source) != len(target):
            return False
        slen = len(source)
        for i in range(0, slen):
            for j in range(0, slen):
                if source[i] == target[j]:
                    target.replace(target[j], '', 1)
                    break
                elif j == slen - 1:
                    return False
        return True

    # reverse string and compare
    @staticmethod
    def anagrams_word2(source, target):
        if source is None or target is None or len(source) != len(target):
            return False
        return source[::-1] == target

    @staticmethod
    def try_anagrams_word():
        source = 'able wts I er'
        target = 're I saw elbt'
        print('source:able was I er', '\ntarget:re I saw elba')
        print('Method1 is anagrams:', StrOpts.anagrams_word1(source, target))
        print('Method2 is anagrams:', StrOpts.anagrams_word2(source, target))

    pass


def run():
    StrOpts.try_anagrams_word()
