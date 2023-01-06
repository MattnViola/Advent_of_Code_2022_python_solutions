monkeys = {}

def value_search(var):
    global monkeys
    if monkeys[var]['value']:
        return monkeys[var]['value']
    else:
        x = value_search(monkeys[var]['equation'].split()[0])
        y = value_search(monkeys[var]['equation'].split()[2])
        operator = monkeys[var]['equation'].split()[1]
        return str(eval(x + operator + y))


with open('input.txt','r') as file:
    for line in file:
        line = line.rstrip('\n').split()
        line[0] = line[0].rstrip(':')
        if not line[0] in monkeys:
            monkeys[line[0]] = {'value' : None, 'equation' : None}
        if len(line) == 2:
            monkeys[line[0]]['value'] = line[1]
        else:
            monkeys[line[0]]['equation'] = ' '.join(line[1:])

print(value_search('root'))




# Have to make a recursive function to dfs and get the true value of the variable
            