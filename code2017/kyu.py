
class MFuns:

    """
    God of gamblers
    时间限制：1000 ms  |  内存限制：65535 KB
    难度：5
    描述
    Have you ever seen the movie "God if gamblers"?
    Yes, it's very exciting! You must be attracted by the deft skill of the god of gamblers.
    He can play the cards as he wish. The action of shuffling cards is extramely handsome.
    How I wish I had such a pair of hands! However, it will be only a dream forever.

    There is a popular method of shuffling cards. Suppose you have a stack of 2*n cards.
    Then mix the two stacks of cards uniformly. That is, the ith card of the original stack is placed in the p(i)th
    position of the new stack of the new stack where p(i) is a function defined like this:
                              p(i) = 2 * i         ( i <= n )
                           p(i) = 2 * ( i - n ) - 1     ( i > n)
    Give you an inter n. Calculate the minimum positive number of shuffling that makes the cards have the same order
    the original stack.

    输入
    A line containing an integer n whish is less than 10^9
    There are multiple test cases. Input will be terminated EOF
    输出
    A line containing an integer which indicates the minimum positive number of shuffles.
    样例输入
    1
    样例输出
    2
    """

    def shuffling_card(self):
        n = int(input("Input n:"))
        s = list(range(1, 2 * n + 1))
        result = s.copy()
        count = 1

        self.shuffling(n, result)
        while not result == s:
            self.shuffling(n, result)
            count += 1

        print(count)
        pass

    def shuffling(self, n, result):
        for i in range(1, 2 * n + 1):
            if result[i - 1] <= n:
                result[i - 1] = 2 * result[i - 1]
            else:
                result[i - 1] = 2 * (result[i - 1] - n) - 1

    """
    蚂蚁的难题(六)
    时间限制：1000 ms  |  内存限制：65535 KB
    难度：5
    描述
    经过一系列的训练，蚂蚁的烹饪手艺终于可以见人了。他烹饪了n盘食品，编号1~n，每一盘都有一个美味价值Ai。
    现在他要选取不超过 k 盘并且任意两盘编号不能够相邻，送给好朋友PIAOYI品尝。因为上次的“试吃”事件让PIAOYI很不开心，
    所以蚂蚁决定选取足够大的美味价值来向PIAOYI道歉。但是蚂蚁又不知道该选那些食品，请你帮帮他吧？
    
    输入
    有多组测试数据。
    对于每组测试数：
    第一行有两个数n,k(n<=100000, k <= n/2)分别代表蚂蚁烹饪了n盘食品，最多选取k盘.
    第二行有n个数字 Ai (|Ai| <= 1000000)表示每一盘食品的美味价值。
    输出
    对于每组数据，输出蚂蚁能够选取的最大值。
    样例输入
    6 3 
    100 1 -1 100 1 -1
    样例输出
    200
    """

    def ant6(self):
        input1 = input("总盘数, 最多选取数量:")
        limit = int(input1.split(" ")[1])
        input2 = input("输入食品数据:")
        food = input2.split(" ")
        self.get_max_ai(food, limit)

    def get_max_ai(self, food, limit):
        print("Max Ai: ", self.find_ai(0, food, food, limit))

    def find_ai(self, ai_count, food, residue_list, limit):
        if len(residue_list) == 0 or limit == 0 or self.is_all_negative(residue_list):
            return ai_count

        ai_count_list = []
        for i in range(0, len(residue_list)):
            residue_list_copy = residue_list.copy()
            limit_copy = limit
            ai_count_list.insert(i, ai_count)
            food_index = food.index(residue_list_copy[i])

            if food_index != 0 and residue_list_copy.__contains__(food[food_index - 1]):
                residue_list_copy.remove(food[food_index - 1])
            if food_index != len(food) - 1 and residue_list_copy.__contains__(food[food_index + 1]):
                residue_list_copy.remove(food[food_index + 1])
            residue_list_copy.remove(food[food_index])

            limit_copy -= 1
            ai_count_list[i] += int(food[food_index])
            ai_count_list[i] = self.find_ai(ai_count_list[i], food, residue_list_copy, limit_copy)
            print("Branch Line Ai: ", ai_count_list[i])

        return max(ai_count_list)

    def is_all_negative(self, residue_list):
        for i in residue_list:
            if int(i) > 0:
                return False
        return True

    def run(self):
        #MFuns.shuffling_card(self)
        MFuns.ant6(self)
        pass

    pass


def run():
    print("September Code")
