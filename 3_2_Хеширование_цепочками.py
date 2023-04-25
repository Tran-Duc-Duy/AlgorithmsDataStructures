def hashFunc(s, m):
    p = 1000000007 #The value of p is a prime number that is used as a modulus in the hash function
    # x is used in the hash function to calculate the hash value of a string. 
    # Specifically, it is used to calculate the contribution of each character in the string to the final hash value.
    x = 263
    res = 0
    for i in range(len(s)):
        res += (ord(s[i]) * (x ** i))
    res %= p
    return res % m

def main():
    m = int(input())
    n = int(input())
    table = [[] for _ in range(m)]
    for i in range(n):
        command = input().split()
        if command[0] == 'add':
            key = hashFunc(command[1], m)
            if command[1] not in table[key]:
                table[key].insert(0, command[1])
        elif command[0] == 'del':
            key = hashFunc(command[1], m)
            if command[1] in table[key]:
                table[key].remove(command[1])
        elif command[0] == 'find':
            key = hashFunc(command[1], m)
            if command[1] in table[key]:
                print('yes')
            else:
                print('no')
        elif command[0] == 'check':
            index = int(command[1])
            if len(table[index]) == 0:
                print('')
            else:
                print(' '.join(table[index]))

if __name__ == '__main__':
    main()