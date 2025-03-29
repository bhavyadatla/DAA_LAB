class NQueens:
    def __init__(self, n):
        self.n, self.board, self.count = n, [-1] * n, 1

    def solve(self, row=0):
        if row == self.n:
            print(f"Solution {self.count}:\n" + "=" * 13)
            for r in self.board:
                print(" ".join("Q" if c == r else "-" for c in range(self.n)))
            print(); self.count += 1
            return
        for col in range(self.n):
            if all(self.board[i] != col and abs(self.board[i] - col) != row - i for i in range(row)):
                self.board[row] = col
                self.solve(row + 1)

if __name__ == "__main__":
    if (n := int(input("Enter number of Queens: "))) not in {2, 3}:
        NQueens(n).solve()
    else:
        print("No Solution exists")
