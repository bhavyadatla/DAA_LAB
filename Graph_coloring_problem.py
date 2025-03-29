class GraphColoring:
    def __init__(self, graph, n, m):
        self.graph, self.n, self.m = graph, n, m
        self.color = [0] * n  

    def solve(self, v=0):
        if v == self.n:
            print("Assigned colors:", self.color)
            return True
        for c in range(1, self.m + 1):
            if all(self.graph[v][i] == 0 or self.color[i] != c for i in range(self.n)):
                self.color[v] = c
                if self.solve(v + 1):
                    return True
                self.color[v] = 0  
        return False

if __name__ == "__main__":
    n = int(input("Enter number of vertices: "))
    graph = [list(map(int, input().split())) for _ in range(n)]
    m = int(input("Enter number of colors: "))
    if not GraphColoring(graph, n, m).solve():
        print("No solution found!")
