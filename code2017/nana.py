class StrOpts:
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
    def str_str(self, source, target):
        j = 0
        mark = 0
        for i in range(0, len(target)):
            if source[j] == target[i]:
                j += 1
                if j == 0:
                    mark = i
                else:
                    j += 1
                if j == len(source) - 1:
                    return mark
            elif mark != 0:
                i = mark;
                mark = 0


def run():
    str_opt = StrOpts()
    print(str_opt.str_str())
