import sys

string = list(sys.stdin.readline().replace(" ", "").strip().lower())
print("true" if string == string[::-1] else "false")
