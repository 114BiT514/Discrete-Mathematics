dict = {
    'f1': lambda x: x,
    'f2': lambda x: 1.0 / x,
    'f3': lambda x: 1.0 - x,
    'f4': lambda x: 1.0 / (1.0 - x),
    'f5': lambda x: (x - 1.0) / x,
    'f6': lambda x: x / (x - 1.0)
}

x_list = {0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9}

def check(func1, func2):
    yes = True
    for x in x_list:
        y = func2(func1(x))
        if abs(y - x) > 1e-5:
            yes = False
            break
    return yes

func = raw_input()
func = dict[func]
for i in dict:
    if check(func, dict[i]):
        tar = i
        break
print tar


