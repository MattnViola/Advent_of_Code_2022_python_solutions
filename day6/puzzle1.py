# Need to find first four uniquely ordered characters. 
# Need to count how many characters read until then.
subroutine = ''
with open('input.txt', 'r') as file:
    while True:
        x = file.read(1)
        if len(subroutine) < 4:
            subroutine += x
            continue 
        _set = set(subroutine[-4:])
        print(x)
        if len(_set) == 4:
            print(_set)         
            print(file.tell())
            break
        if x == '':
            break
        subroutine += x



# Can use a string and string slicing, or a list and list.pop() and list.append()