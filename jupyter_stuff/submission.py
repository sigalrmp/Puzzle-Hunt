import checker

def run_puzzle_0(f, input):
    def puzzle_0(n):
        return chr(n + 97)

    checker.attempt_solution("puzzle_0", f, puzzle_0, {0, 10, 25}, 17, input)

def run_puzzle_1(f, input):
    def puzzle_1(c):
        return ord(c) - 97

    checker.attempt_solution("puzzle_1", f, puzzle_1, {'a', 'j', 'x'}, 'g', input)

def run_puzzle_2(f, input):
    def puzzle_0(n):
        return chr(n + 97)
    def puzzle_1(c):
        return ord(c) - 97
    def puzzle_2(c):
        return puzzle_0((((puzzle_1(c) + 2) * 7) + 6) % 26)

    checker.attempt_solution("puzzle_2", f, puzzle_2, {'a', 'j', 'x'}, 'd', input)

def run_puzzle_3(f, input):
    def puzzle_0(n):
        return chr(n + 97)
    def puzzle_1(c):
        return ord(c) - 97
    def puzzle_2(c):
        return puzzle_0((((puzzle_1(c) + 2) * 7) + 6) % 26)
    def puzzle_3(message):
        new = ""
        for c in message:
            new += puzzle_2(c)
        return new
    checker.attempt_solution("puzzle_3", f, puzzle_3, {"hello", "world", "abcdefghijklmnopqrstuvwxyz"}, "wlhczy", input)

def run_puzzle_4(f, input):
    def prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    def puzzle_4(ints):   
        sum = 0
        for n in ints:
            if prime(n):
                sum += n
        return sum
    checker.attempt_solution("puzzle_4", f, puzzle_4, {(1, 2, 3, 4, 5), (6, 7, 8, 9, 10), (11, 12, 13, 14, 15, 16, 17, 18, 19)}, 
                             [123, 1657, 4312, 7717, 5678467, 3793, 1292, 77339, 198273, 928, 3427], input)

def run_puzzle_5(f, input):
    def puzzle_0(n):
        return chr(n + 97)
    def puzzle_5(rom_nums):
        def rom_to_int(rom):
            values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
            n = 0
            for c in rom:
                n += values[c]
            return n
        word = ""
        for n in rom_nums:
            word += puzzle_0(rom_to_int(n) % 26)
        return word

    checker.attempt_solution("puzzle_5", f, puzzle_5, {("XIIX", "LCL", "VVV"), ("LVX"), ("MLV", "XVCI")}, ["XVVIMCDD", "CLXCDXCLXIIILC", "LXVICXILXICLX", "CLXVICLIIIXCLI", "IICCDXIXVLDIIMCILXCIX"], input)

def run_puzzle_6(f, input):
    def puzzle_1(c):
        return ord(c) - 97
    def prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    def puzzle_6(s):
        sum = 0
        for c in s:
            n = puzzle_1(c) * 102 - 1
            if prime(n):
                sum += n
        return sum
    checker.attempt_solution("puzzle_6", f, puzzle_6, {"abcdefgxyzw", "hijklasdfhuoasdtuv", "mnopqrsskdjf"}, "sdfhhazsdhbfuwqekmucrrronyuiydfwsfhajhbvnvqoal", input)

def run_puzzle_7(f, input):
    def puzzle_0(n):
        return chr(n + 97)
    def puzzle_1(c):
        return ord(c) - 97
    def prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    def puzzle_7(s):
        def puzzle_7_h(n):
            if prime(n):
                shift = 2 - n % 5
                if abs(shift) > 5 / 2:
                    return n + shift - 5
                return n + shift
            return n + 34858 + 2
        password = ""
        for c in s:
            password += puzzle_0(puzzle_7_h(puzzle_1(c)) % 26)
        return password
    checker.attempt_solution("puzzle_7", f, puzzle_7, {"abcdefghijklmnopqrstuvwxyz", "akshdfaciou", "poqweicrunsdfpoweri"}, "vgyyxutj", input)