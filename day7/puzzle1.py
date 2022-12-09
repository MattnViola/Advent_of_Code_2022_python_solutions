# Need to write a recursive function to go through a tree and record the sizes of directories, if a directory <= 1000000, add that value to a variable.


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
                    


    under_limit_sum(root)
    print(total)
# Recursively adds value to parent directories
def value_add(value, current_dir):
    if current_dir.parent:
        value_add(value, current_dir.parent)
    current_dir.value += value
    return

# Checks if a directory has <= 100000 value, adds the values together if so.
def under_limit_sum(_dir):
    global total
    if _dir.children:
        for child in _dir.children:
            under_limit_sum(child)
    if _dir.value <= 100000:
            total += _dir.value
       
    return
if __name__ == "__main__":
    main()

# There are dirs with the same name nested inside.
# Should change the names to be more directory like.