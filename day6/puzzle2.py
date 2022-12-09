# Same as puzzle 1 except need to find 14 distinct characters

subroutine = ''
with open('input.txt', 'r') as file:
    while True:
        x = file.read(1)
        if len(subroutine) < 14:
            subroutine += x
            continue 
        _set = set(subroutine[-14:])
        print(subroutine[-14:])
        if len(_set) == 14:
            print(_set)         
            print(len(subroutine))
            break
        if x == '':
            break
        subroutine += x