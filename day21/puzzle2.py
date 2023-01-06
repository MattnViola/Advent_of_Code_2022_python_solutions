# Need to figure out what number humn needs to be so that root's numbers equal one another.
# Find the branch to humn, and then take each node's operation, reverse it,
# and apply the node's new operation with its available value to the root's available value



humn_value = ''
monkeys = {}


def main():
    global humn_value
    global monkeys

    with open('adventofcode\day21\input.txt','r') as file:
        for line in file:
            line = line.rstrip('\n').split()
            line[0] = line[0].rstrip(':')
            if not line[0] in monkeys:
                monkeys[line[0]] = {'value' : None, 'equation' : None}
            if len(line) == 2:
                if line[0] == 'humn':
                    line[1] = 'x'
                monkeys[line[0]]['value'] = line[1]
            else:
                monkeys[line[0]]['equation'] = ' '.join(line[1:])

    value_search('root')

    x = monkeys['root']['equation'].split()[0]
    y = monkeys['root']['equation'].split()[2]
    if monkeys[x]['value'] == 'x':
        monkeys[x]['value'] = monkeys[y]['value']
        find_humn(x)
    elif monkeys[y]['value'] == 'x':
        monkeys[y]['value'] = monkeys[x]['value']
        find_humn(y, monkeys['root']['value'])



def value_search(var):
    global monkeys
    if monkeys[var]['value']:
        return monkeys[var]['value']
    else:
        x = value_search(monkeys[var]['equation'].split()[0])
        y = value_search(monkeys[var]['equation'].split()[2])
        operator = monkeys[var]['equation'].split()[1]
        if x == 'x' or y == 'x':
            monkeys[var]['value'] = 'x'
            return 'x'
        else: 
            monkeys[var]['value'] = str(eval(x + operator + y))
        return  monkeys[var]['value']

def find_humn(var):
    global monkeys
    if var == 'humn':
        print(monkeys[var]['value'])
        return      
    x = monkeys[var]['equation'].split()[0]
    y = monkeys[var]['equation'].split()[2]   
    if monkeys[x]['value'] == 'x':
        monkeys[x]['value'] = inverse_operation(monkeys[var]['value'], monkeys[var]['equation'].split()[1], monkeys[y]['value'], first=True)
        find_humn(x)
    elif monkeys[y]['value'] == 'x':
        monkeys[y]['value'] = inverse_operation(monkeys[var]['value'], monkeys[var]['equation'].split()[1], monkeys[x]['value'], first=False)
        find_humn(y)
    return

def inverse_operation(parent, operator, const, first):
    global monkeys
    if operator == '+':
        return str(eval(parent + '-' + const))
    if operator == '*':
        return str(eval(parent + '/' + const))
    if operator == '-':
        if first:
            return str(eval(parent + '+' + const))
        else:
            return str(-eval(parent + '-' + const))
    if operator == '/':
        if first:
            return str(eval(parent + '*' + const))
        else:
            return str(eval('1' + '/' + parent + '*' + const))
    return

main()

# Need to figure out inverse operations.
# constant + x = parent -> parent - constant = x
# x - constant = parent -> parent + c
# c - x = parent -> -(parent - c)
# c * x = parent -> parent / c
# x / c = parent -> parent * c
# c / x = parent ->  1/parent * c


# 4945453364388 too high