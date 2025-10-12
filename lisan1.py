# -*- coding: utf-8 -*-

def hequ(a,b):
    if a == '1' and b == '1':
        return '1'
    else:
        return '0'

def xiqu(a,b):
    if a == '0' and b == '0':
        return '0'
    else:
        return '1'

def yunhan(a,b):
    if a == '1' and b == '0':
        return '0'
    else:
        return '1'

def dengjia(a,b):
    if a == b:
        return '1'
    else:
        return '0'

def fouding(a):
    if a == '1':
        return '0'
    else:
        return '1'

class token:
    def __init__(self,prec,assoc,arity,func):
        self.prec = prec
        self.assoc = assoc
        self.arity = arity
        self.func = func

    def use(self, a, b=None):
        if self.arity == 1:
            return self.func(a)
        else:
            return self.func(a, b)

operators = {}
operators['!'] = token(1,'R',1,func=fouding)
operators['&'] = token(2,'L',2,func=hequ)
operators['|'] = token(3,'L',2,func=xiqu)
operators['-'] = token(4,'L',2,func=yunhan)
operators['+'] = token(5,'L',2,func=dengjia)

class formula:
    def __init__(self, target):
        self.target = list(target)
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

    def getRPN(self, copy):
        copy = list(copy)
        token_stack = []
        RPN = []
        for elem in copy:
            if elem in ['0', '1']:
                RPN.append(elem)
            else:
                if elem == '(':
                    token_stack.append(elem)
                elif elem == ')':
                    while  token_stack[-1] != '(':
                        RPN.append(token_stack.pop())
                    token_stack.pop()
                else:
                    if not token_stack or token_stack[-1] == '(':
                        token_stack.append(elem)
                    else:
                        if operators[elem].prec < operators[token_stack[-1]].prec:
                            token_stack.append(elem)
                        elif operators[elem].prec > operators[token_stack[-1]].prec:
                            RPN.append(token_stack.pop())
                            token_stack.append(elem)
                        else:
                            if operators[token_stack[-1]].assoc == 'L':
                                RPN.append(token_stack.pop())
                                token_stack.append(elem)
                            else :
                                token_stack.append(elem)
        while token_stack:
            RPN.append(token_stack.pop())
        return RPN

    def calRPN(self, RPN):
        stack = []
        for elem in RPN:
            if elem in ['0', '1']:
                stack.append(elem)
            else:
                if operators[elem].arity == 1:
                    a = stack.pop()
                    a = operators[elem].use(a)
                    stack.append(a)
                else:
                    b = stack.pop()
                    a = stack.pop()
                    a = operators[elem].use(a, b)
                    stack.append(a)
        return stack

    def solve(self):
        self.value = {}
        for i in range(2**self.num):
            ib = list(bin(i)[2:])
            ib = ''.join(ib).zfill(self.num)
            ib = list(ib)
            copy = self.target[:]
            for k in range(len(copy)) :
                if copy[k] in self.elems:
                    j = self.elems.index(copy[k])
                    copy[k] = ib[j]
            RPN = self.getRPN(copy)
            self.value[i]= self.calRPN(RPN)

    def print_result(self):
        m = []
        M = []
        for i in self.value:
            if self.value[i][0] == '1':
                if not m:
                    m.append('m')
                    m.append(str(i))
                else :
                    m.append(' ∨ m')
                    m.append(str(i))
            else:
                if not M:
                    M.append('M')
                    M.append(str(i))
                else:
                    M.append(' ∧ M')
                    M.append(str(i))
        m = ''.join(m)
        M = ''.join(M)
        if m and M:
            print m + ' ; ' + M
        elif not m:
            print '0' + ' ; ' + M
        else:
            print m + ' ; ' + '1'

form = formula(raw_input())
form.num_elem()
form.solve()
form.print_result()