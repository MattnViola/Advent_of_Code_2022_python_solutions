
# Need to change to determine total used space, and then determine the smallest directory's value that makes unused space >= 30000000


class dir:
    instances = {}
    
    def __init__(self, name):
        self.children = []
        self.name = name
        self.value = 0
        self.parent = None
        dir.instances[self.name] = self

root = dir('root')
current_dir = root
total = 0
def main():
    with open('input.txt','r') as file:
        for line in file:
            # Parse the input into a list and feed that into the -r function.
            data = line.rstrip('\n').split()
            # Checks if command
            if data[0] == '$':
                if data[1] == 'cd':
                    if data[2] == '/':
                        current_dir = root
                    elif data[2] == '..':
                        if not current_dir == root:
                            current_dir = current_dir.parent
                    else:
                        if current_dir.name + '/' + data[2] in dir.instances:
                            current_dir = dir.instances[current_dir.name + '/' + data[2]]
                        else:
                            parent = current_dir
                            current_dir = dir(current_dir.name + '/' + data[2])
                            current_dir.parent = parent
                if data[1] == 'ls':
                    continue
            # Checks if it's a directory, and then checks if its already a child of current_dir
            elif data[0] == 'dir':
                if not current_dir.name + '/' + data[1] in current_dir.children:
                    child = dir(current_dir.name + '/' + data[1])
                    child.parent = current_dir
                    current_dir.children.append(child)
                    
            # Adds the value to the current_dir and its parent folders
            else:
                value = int(data[0])
                value_add(value, current_dir)
                    

    lowest = min_required_value(root)
    print(lowest)
# Recursively adds value to parent directories
def value_add(value, current_dir):
    if current_dir.parent:
        value_add(value, current_dir.parent)
    current_dir.value += value
    return



def min_required_value(_dir):
    needed = root.value - 40000000
    lowest = -1
    for direc in  dir.instances.values():
        if (direc.value >= needed and direc.value < lowest) or lowest == -1:
            lowest = direc.value
    return lowest
    
    
if __name__ == "__main__":
    main()
