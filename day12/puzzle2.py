# Need to find the closest a from z still using the valid elevation rules.
# Reverse the BFS from end to beginning and reverse the conditionals to only go 1 step down.
hills = []


class Node:
    # values are coords
    visited = []
    queue = []
    
    def __init__(self, value, coords, distance=100000):
        self.value = value
        self.coords = coords
        self.distance = distance
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        Node.visited.append(self.coords)

    def build_graph(self, hills):
        if self.value == 'a':
            print('found: ', self.distance)
            return
        if self.coords[0] > 0:
            u_val, u_coord = hills[self.coords[0] - 1][self.coords[1]], (
                self.coords[0] - 1,
                self.coords[1],
            )

            # check elevation and if node already visited
            if (ord(u_val) >= ord(self.value) - 1 or u_val == "S") and u_coord not in Node.visited:
                self.up = Node(u_val, u_coord, self.distance + 1)
                Node.queue.append(self.up)
        if self.coords[0] < (len(hills) - 1):
            d_val, d_coord = hills[self.coords[0] + 1][self.coords[1]], (
                self.coords[0] + 1,
                self.coords[1],
            )
            if (ord(d_val) >= ord(self.value) - 1 or d_val == "S") and d_coord not in Node.visited:
                self.down = Node(d_val, d_coord, self.distance + 1)
                Node.queue.append(self.down)
        if self.coords[1] > 0:
            l_val, l_coord = hills[self.coords[0]][self.coords[1] - 1], (
                self.coords[0],
                self.coords[1] - 1,
            )
            if (ord(l_val)>= ord(self.value) - 1 or l_val == "S") and l_coord not in Node.visited:
                self.left = Node(l_val, l_coord, self.distance + 1)
                Node.queue.append(self.left)
        if self.coords[1] < (len(hills[0]) - 1):
            r_val, r_coord = hills[self.coords[0]][self.coords[1] + 1], (
                self.coords[0],
                self.coords[1] + 1,
            )
            if (ord(r_val) >= ord(self.value) - 1 or r_val == "S") and r_coord not in Node.visited:
                self.right = Node(r_val, r_coord, self.distance + 1)
                Node.queue.append(self.right)
        return


def main():

    global hills
    with open("input.txt", "r") as file:
        for line in file:
            hills.append(list(line.rstrip("\n")))
    for i in range(len(hills)):
        if "E" in hills[i]:
            start = (i, hills[i].index("E"))

    begin = Node("z", (start[0], start[1]), 0)
    Node.queue.append(begin)
    while True:
        if not Node.queue:
            break      
        Node.queue.pop(0).build_graph(hills)
    print('works')

if __name__ == "__main__":
    main()
