#!/usr/bin/python3
for i in range(ord('Z'), ord('A') - 1, -1):
    print(chr(i if i % 2 == 0 else i + 32), end='')
