#!/usr/bin/python3
for i in range(26):
    if i != 16 and i != 4:  # 'q' is 16th letter, 'e' is 4th letter (0-indexed)
        print("{:c}".format(97 + i), end="")
