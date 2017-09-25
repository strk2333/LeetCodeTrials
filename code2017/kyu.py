import sys

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
        if len(residue_list) == 0 or limit <= 0:
            return ai_count

        ai_count_list = []
        limit_copy = 0
        for i in range(len(residue_list)):
            if residue_list[i] is not None:
                residue_list_copy = residue_list.copy()
                limit_copy = limit
                ai_count_list.insert(i, ai_count)

                if i != 0:
                    residue_list_copy[i - 1] = None
                if i != len(food) - 1:
                    residue_list_copy[i + 1] = None
                residue_list_copy[i] = None
                print("Residue: ", residue_list_copy)

                limit_copy -= 1
                ai_count_list[i] += int(food[i])
                ai_count_list[i] = self.find_ai(ai_count_list[i], food, residue_list_copy, limit_copy)
                print("Branch Line Ai: ", ai_count_list[i])
            else:
                ai_count_list.insert(i, None)

        while ai_count_list.__contains__(None):
            ai_count_list.remove(None)

        if len(ai_count_list) == 0:
            return int(food[0])
        else:
            return max(ai_count_list)

    """
    最舒适的路线
    时间限制：5000 ms  |  内存限制：65535 KB
    难度：5
    描述
    异形卵潜伏在某区域的一个神经网络中。其网络共有N个神经元（编号为1,2,3,…,N），这些神经元由M条通道连接着。
    两个神经元之间可能有多条通道。异形卵可以在这些通道上来回游动，但在神经网络中任一条通道的游动速度必须是一定的。
    当然异形卵不希望从一条通道游动到另一条通道速度变化太大，否则它会很不舒服。现在异形卵聚居在神经元S点，
    想游动到神经元T点。它希望选择一条游动过程中通道最大速度与最小速度比尽可能小的路线，也就是所谓最舒适的路线。
    
    输入
    第一行： K 表示有多少组测试数据。 
    接下来对每组测试数据：
    第1行: N M
    第2~M+1行： Xi Yi Vi (i=1,…..,M)
    表示神经元Xi 到神经元Yi之间通道的速度必须是Vi
    最后一行： S T ( S  T )
    
    【约束条件】
    2≤K≤5 1<N≤500 0<M≤5000 1≤ Xi, Yi , S , T ≤N 0< Vi <30000，
    Vi是整数。数据之间有一个空格。
    输出
    对于每组测试数据，输出一行：如果神经元S到神经元T没有路线，输出“IMPOSSIBLE”。否则输出一个数，表示最小的速度比。
    如果需要，输出一个既约分数。
    样例输入
    2
    3 2
    1 2 2
    2 3 4
    1 3
    3 3
    1 2 10
    1 2 5
    2 3 8
    1 3
    样例输出
    2
    5/4
    """
    def alien_route(self):
        input1 = sys.argv[1].split('n')
        test_count = int(input1[0])
        index = 1
        result_list = []
        for i in range(test_count):
            spot_count = int(str.split(input1[index], '__')[0])
            route_count = int(str.split(input1[index], '__')[1])
            index += 1

            route_list = []
            for j in range(route_count):
                route_list.append([int(input1[index].split('__')[0]),
                                   int(input1[index].split('__')[1]),
                                   int(input1[index].split('__')[2])])
                index += 1
            s = int(str.split(input1[index], '__')[0])
            t = int(str.split(input1[index], '__')[1])
            index += 1

            speed_list = self.pack_route_data(spot_count, route_list)
            result_list = self.force_route(result_list, [], speed_list, 0, s, t)
            print("Source:", speed_list)
            print("Result:", result_list)
            result_list = []

    def alien_route2(self):
        input1 = int(input("Input the amount of test cases: "))

        result_list = []
        for i in range(input1):
            input2 = input("Input the amount of aliens routes: ")
            spot_count = int(input2.split(' ')[0])
            route_count = int(input2.split(' ')[1])

            route_list = []
            for j in range(route_count):
                input3 = input("Input the route: ")
                route_list.append([int(input3.split(' ')[0]), int(input3.split(' ')[1]), int(input3.split(' ')[2])])

            input4 = input("Input source & destination: ")
            s = int(input4.split(' ')[0])
            t = int(input4.split(' ')[1])

            speed_list = self.pack_route_data(spot_count, route_list)
            self.force_route(result_list, [], speed_list, 0, s, t)
            result_list = []

    def force_route(self, result_list, process_list, speed_list, index, s, t):
        if index == speed_list.__len__():
            return result_list

        if len(process_list) < 2:
            for i in speed_list:
                process_list.append(i[0])
            result_list = process_list.copy()

        for i in range(len(speed_list[index])):
            process_list[index] = speed_list[index][i]
            if max(process_list) / min(process_list) < max(result_list) / min(result_list):
                result_list = process_list.copy()
            index += 1
            result_list = self.force_route(result_list, process_list, speed_list, index, s, t)
            index -= 1

        return result_list

    def pack_route_data(self, spot_count, route_list):
        speed_list = []
        for i in range(spot_count - 1):
            speed_list.append([])
            for j in route_list:
                if j[0] == i + 1 and j[1] == i + 2:
                    speed_list[i].append(j[2])

        return speed_list

    """
    Travel in time
    时间限制：4000 ms  |  内存限制：65535 KB
    难度：5
    描述
    Bob gets tired of playing games, leaves Alice, and travels to Changsha alone. Yuelu Mountain, Orange Island, Window 
    of the World, the Provincial Museum etc...are scenic spots Bob wants to visit. However, his time is very limited, 
    he can’t visit them all.
    Assuming that there are N scenic spots in Changsha, Bob defines a satisfaction value Si to each spot. 
    If he visits this spot, his total satisfaction value will plus Si. Bob hopes that within the limited time T, 
    he can start at spot S, visit some spots selectively, and finally stop at spot E, so that 
    the total satisfaction value can be as large as possible. It's obvious that visiting the spot will also cost 
    some time, suppose that it takes Ci units of time to visit spot i ( 0 <= i < N ).
    Always remember, Bob can choose to pass by a spot without visiting it (including S and E), maybe he just want to 
    walk shorter distance for saving time.
    Bob also has a special need which is that he will only visit the spot whose satisfaction value is strictly larger 
    than that of which he visited last time. For example, if he has visited a spot whose satisfaction value is 50, 
    he would only visit spot whose satisfaction value is 51 or more then. The paths between the spots are 
    bi-directional, of course.
    输入
    The first line is an integer W, which is the number of testing cases, and the W sets of data are following.
    The first line of each test data contains five integers: N M T S E. N represents the number of spots, 1 < N < 100; 
    M represents the number of paths, 0 < M < 1000; T represents the time limitation, 0 < T <= 300; S means the spot 
    Bob starts from. E indicates the end spot. (0 <= S, E < N)
    The second line of the test data contains N integers Ci ( 0 <= Ci <= T ), which means the cost of time 
    if Bob visits the spot i.
    The third line also has N integers, which means the satisfaction value Si that can be obtained by visiting 
    the spot i ( 0 <= Si < 100 ).
    The next M lines, each line contains three integers u v L, means there is a bi-directional path between spot u 
    and v and it takes L units of time to walk from u to v or from v to u. (0 <= u, v < N, 0 <= L <= T)
    输出
    Output case number in the first line (formatted as the sample output).
    The second line contains an integer, which is the greatest satisfaction value.
    If Bob can’t reach spot E in T units of time, you should output just a “0” (without quotation marks).
    样例输入
    1
    4 4 22 0 3  # spots count, path count, time limitation, start, end 
    1 1 1 1     # spot time cost
    5 7 9 12    # satisfaction
    0 1 10      # start end cost
    1 3 10
    0 2 10
    2 3 10
    样例输出
    Case #1:    # Case #test_number:
    21          # the greast satisfaction value
    """
    def travel_in_time(self):
        input1 = str.split(sys.argv[1], 'n')
        test_count = input1[0]
        input_line2 = input1[1].split('__')
        spot_count = input_line2[0]
        path_count = input_line2[1]
        time_limit = input_line2[2]
        start = input_line2[3]
        end = input_line2[4]
        input_line3 = input1[2].split('__')
        spot_cost = []
        for i in input_line3:
            spot_cost.append(i)
        input_line4 = input1[3].split('__')
        satis = []
        for i in input_line4:
            satis.append(i)
        route = []
        for i in range(4, len(input1)):
            route.append(input1[i].split('__'))

        print(route)
        paths = self.force_route_spots(route, start, end, int(start), [], 0)
        for i in paths:
            i.insert(0, start)

        result = self.find_best_route(paths, route, spot_cost, satis, time_limit)
        print(paths)
        print(result)

    def force_route_spots(self, route, start, end, index, paths, path_index):
        route_copy = route.copy()
        for i in route:
            if int(i[0]) == int(index):
                if len(paths) <= path_index:
                    paths.append([])

                paths[path_index].append(i[1])
                route_copy.remove(i)

                if int(i[1]) != int(end):
                    paths = self.force_route_spots(route_copy, start, end, int(i[1]), paths, path_index)
                    pass

                if index == int(start):
                    path_index += 1

        return paths

    def find_best_route(self, paths, route, spot_cost, satis, time_limit):
        time_list = []
        for path in paths:
            time_list.append(0)
            for s in range(len(path)):
                for t in route:
                    if path[s] == t[0] and path[s + 1] == t[1]:
                        time_list[len(time_list) - 1] += int(t[2])
                        break

            for spot in range(len(path) - 2):
                time_list[len(time_list) - 1] += int(spot_cost[int(path[spot])])

        return min(time_list)

    """
        SUDOKU
    """
    def resolve_sudoku(self):
        sudoku = self.get_sudoku()

        self.force_resolve_sudoku(sudoku)

    def print_sudoku(self, sudoku):
        for line in sudoku:
            for i in line:
                print(i, end=" ")
            print()

    def force_resolve_sudoku(self, sudoku):
        result = []
        for i in range(len(sudoku)):
            for j in range(len(sudoku)):
                result.append([1, 2, 3, 4, 5, 6, 7, 8, 9])

        while self.sudoku_tokenai(sudoku):
            values1 = []
            values2 = []
            values3 = []
            v_lines = []
            b_lines = []
            for i in range(len(sudoku)):
                v_lines.append([])
            for i in range(len(sudoku)):
                b_lines.append([])
            # Horizontal
            for line in sudoku:
                values1.append(self.get_unvalued_nums(line))

            # Vertical
            for i in range(len(sudoku)):
                for j in range(len(sudoku)):
                    v_lines[j].append(sudoku[i][j])
            for line in v_lines:
                values2.append(self.get_unvalued_nums(line))

            # block
            for i in range(len(sudoku)):
                for j in range(len(sudoku)):
                    b_lines[int(i / 3) + int(j / 3) * 3].append(sudoku[i][j])
            for line in b_lines:
                values3.append(self.get_unvalued_nums(line))

            self.update_possible_values(result, values1, values2, values3, len(sudoku))
            self.try_fill_values(sudoku, result)

            print('_____________________________')
            print(values1)
            print(values2)
            print(values3)
            print(result)
        for i in result:
            if len(i) == 2:
                print(i, result.index(i))
        pass

    def sudoku_tokenai(self, sudoku):
        for i in sudoku:
            if i == 0:
                return False
        return True

    def try_fill_values(self, sudoku, possible_values):
        has_fixed_change = False
        nogoru = 1
        while not has_fixed_change:
            for i in range(len(possible_values)):
                if int(sudoku[int(i / len(sudoku))][int(i % len(sudoku))]) == 0 and len(possible_values[i]) == nogoru:
                    sudoku[int(i / len(sudoku))][int(i % len(sudoku))] = possible_values[i][0]
                    has_fixed_change = True
            nogoru += 1

    def update_possible_values(self, result, values1, values2, values3, s_len):
        for i in range(s_len):
            for j in range(s_len):
                result[i * s_len + j] = list(set(values1[i]) & set(values2[j]) & set(values3[int(i / 3) + int(j / 3) * 3]))

    def get_unvalued_nums(self, grids):
        tmp = []
        for i in grids:
            if int(i) != 0:
                tmp.append(i)

        re = [i for i in range(1, 10)]
        for i in tmp:
            re.remove(int(i))
        return re

    def get_sudoku(self):
        input1 = sys.argv[1]
        lines = input1.split('n')
        test_count = int(lines[0])
        list.remove(lines, lines[0])
        sudoku = []
        for i in range(len(lines)):
            sudoku.append(str.split(lines[i], '__'))

        return sudoku

    def run(self):
        # self.shuffling_card()
        # self.ant6()
        # self.alien_route()
        # self.travel_in_time()
        self.resolve_sudoku()
        pass


def run():
    print("September Code")
