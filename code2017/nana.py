class BasicOpts:
    """
    strStr
    Source
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
    # Single for with rollback
    def str_str1(source, target):
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
    # Double for
    def str_str2(source, target):
        mark = 0
        for i in range(0, len(target)):
            for j in range(0, len(source)):
                if target[i + j] != source[j]:
                    break

                if j == len(source) - 1:
                    return i

        return -1


def run():
    str_opt = BasicOpts()
    print(str_opt.str_str1('in', 'stonginstring'))
    print(str_opt.str_str2('in', 'stonginstring'))
