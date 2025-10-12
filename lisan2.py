class formula:
    def __init__(self, target):
        self.target = target
        self.word = ['!', '&', '|', '-', '+', '(', ')']

    def num_elem(self):
        self.num = 0
        self.elems = []
        for elem in self.target:
            if elem not in self.word:
                self.elems.append(elem)
        self.elems = list(set(self.elems))
        self.elems.sort()
        self.num = len(self.elems)

    def split_it(self):
        copy = [c for c in self.target if c not in '()']
        self.hequ = ''.join(copy).split('&')

    def turn_to_set(self):
        self.set = set()
        for lst in self.hequ:
            lst = lst.split('|')
            lst = set(lst)
            self.set.add(frozenset(lst))

    def resolution(self,s0,s1,s2):
        for elem0 in s0:
            for elem1 in s1:
                for elem in self.elems:
                    test = False
                    new_elem0 = set(elem0)
                    new_elem1 = set(elem1)
                    if (elem in elem0) and ('!' + elem in elem1):
                        test = True
                        new_elem0.remove(elem)
                        new_elem1.remove('!' + elem)
                    elif (elem in elem1) and ('!' + elem in elem0):
                        test = True
                        new_elem1.remove(elem)
                        new_elem0.remove('!' + elem)
                    if test:
                        new_elem = new_elem0 | new_elem1
                        if not new_elem:
                            return 0
                        new_elem = frozenset(new_elem)
                        if (new_elem not in s0) and (new_elem not in s1) and (new_elem not in s2):
                            s2.add(new_elem)
                        break;
        for elem1 in s1:
            for elem2 in s1:
                if elem1 != elem2:
                    for elem in self.elems:
                        test = False
                        new_elem1 = set(elem1)
                        new_elem2 = set(elem2)
                        if (elem in elem1) and ('!' + elem in elem2):
                            test = True
                            new_elem1.remove(elem)
                            new_elem2.remove('!' + elem)
                        elif (elem in elem2) and ('!' + elem in elem1):
                            test = True
                            new_elem2.remove(elem)
                            new_elem1.remove('!' + elem)
                        if test:
                            new_elem = new_elem1 | new_elem2
                            if not new_elem:
                                return 0
                            new_elem = frozenset(new_elem)
                            if (new_elem not in s0) and (new_elem not in s1) and (new_elem not in s2):
                                s2.add(new_elem)
                            break;
        return 1

form = formula(raw_input())
form.num_elem()
form.split_it()
form.turn_to_set()
yes = True
s0 = set()
s1 = form.set
s2 = set()
result = form.resolution(s0, s1, s2)
if result == 0:
    print 'NO'
    yes = False
while s2 and yes:
    s0 = s0 | s1
    s1 = s2
    s2 = set()
    result = form.resolution(s0, s1, s2)
    if result == 0:
        print 'NO'
        yes = False
if yes:
    print 'YES'


"""debug日志
    set不可哈希，不能放进set，必须转成frozenset，用的时候再转回去
    set.remove()是就地修改，返回NoneTyoe，而不是返回删掉之后的集合
    split_it()逻辑有误，split（）函数只能按一个字符切割，不能传给他一个切割符列表
    消解p与！p的算法有误，已修改
    消解法第二次循环elem1和elem2必须是不相等的两个
    主函数while要判断yes是不是True，不然可能多次打印NO
    在每次消解之后，不要再遍历结果消去p|！p，会出现bug
"""




