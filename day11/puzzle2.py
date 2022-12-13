# Have to switch to using modular arithmetic so that the integers aren't huge.
# Have a key that is the divisor:remainder.
# modular operations are just to do the operation on the remainder, and then modulo that.

class monkey:
    
    def __init__(self, name, items, operation, test, true, false):
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
    
def main():   
    # Get monkey info
    monkeys = parse_input()
    # Change items into remainders based on all monkeys' tests
    for mon in monkeys:
        remainders = [[[ _monke.test , item % _monke.test] for _monke in monkeys] for item in mon.items]
        mon.items = remainders
            
        
    monkey_inspect = [0] * len(monkeys)
    
    for _ in range(10000):
        for i in range(len(monkeys)):
            monkey_inspect[i] += len(monkeys[i].items)
            for _ in range(len(monkeys[i].items)):                
                item_remainders = monkeys[i].items.pop(0)
                new_remainders = monkey_operation(item_remainders, monkeys[i].operation)
                if new_remainders[i][1] == 0:
                    monkeys[monkeys[i].true].items.append(new_remainders)
                else:
                    monkeys[monkeys[i].false].items.append(new_remainders)
    print(monkey_inspect)
    top_2 = sorted(monkey_inspect)[-2:]
    print(top_2[0] * top_2[1])
                                        
                
    



# Returns a list of monkey objects
def parse_input():
    monkeys = []
    with open('input.txt', 'r') as file:
        for line in file:
            if line == '\n':
                continue
            line = line.strip().rstrip('\n').split()
            if line[0] == 'Monkey':
                monke = []
                monke.append("Monkey " + line[1].rstrip(':'))
            elif line[0] == 'Starting':
                monke.append([int(line[i].rstrip(',')) for i in range(2, len(line))])
            elif line[0] == 'Operation:':
                monke.append(' '.join(line[3:]))
            elif line[0] == 'Test:':
                monke.append(int(line[3]))
            elif line[1] == 'true:':
                monke.append(int(line[5]))
            elif line[1] == 'false:':
                monke.append(int(line[5]))
                monk = monkey(monke[0], monke[1], monke[2], monke[3], monke[4], monke[5])
                monkeys.append(monk)
                
    return monkeys

# Returns a list of divisor, new remainder pairs for each item
def monkey_operation(item_remainders, operation):
    for i in range(len(item_remainders)):
        old = item_remainders[i][1]
        item_remainders[i][1] = eval(operation) % item_remainders[i][0]
    return item_remainders
    

if __name__ == '__main__':
    main()