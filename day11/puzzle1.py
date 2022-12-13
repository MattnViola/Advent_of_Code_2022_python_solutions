class monkey:
    
    def __init__(self, name, items, operation, test, true, false):
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
    
def main():   

    monkeys = parse_input()
    monkey_inspect = [0] * len(monkeys)
    
    for _ in range(20):
        for i in range(len(monkeys)):
            monkey_inspect[i] += len(monkeys[i].items)
            for _ in range(len(monkeys[i].items)):                
                old = monkeys[i].items.pop(0)
                new = eval(monkeys[i].operation) // 3
                if new % monkeys[i].test == 0:
                    monkeys[monkeys[i].true].items.append(new)
                else:
                    monkeys[monkeys[i].false].items.append(new)
    
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

if __name__ == '__main__':
    main()