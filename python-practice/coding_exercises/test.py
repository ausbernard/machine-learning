
s = "{[]}"
def nile(s):
    stack = []
    hashtable = {
        "}" : "{",
        ")" : "(",
        "]" : "["
    }

    for char in s:
        if char in hashtable.values(): # opening bracket
            stack.append(char) # add to the list
        elif char in hashtable.keys(): # closing bracket
            if stack == [] or hashtable[char] != stack.pop():
                return False
    return stack == []

print(nile(s))
