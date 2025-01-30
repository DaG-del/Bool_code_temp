def boolean(string):
    if string == "True":
        return True
    elif string == "False":
        return False
    else:
        print("what the fuck")

def LogicEval(p: bool, q: bool, r: bool, expression: str):
    new_exp = ""
    for char in range(len(expression)):
        if expression[char] == "p":
            new_exp += str(p)
        elif expression[char] == "q":
            new_exp += str(q)
        elif expression[char] == "r" and (expression[char - 1] != "o" and expression[char - 1] != "T"):
            new_exp += str(r)
        else:
            new_exp += expression[char]
            
    again = False

    if new_exp.count("(") != 0:
        for char in range(len(new_exp)):
            if new_exp[char] == "(":
                opening_bracket = char
                index = char
                temp = opening_bracket
                for ch in new_exp[char:]:
                    if ch == "(":
                        opening_bracket = index
                    index += 1
                    if ch == ")" and opening_bracket == temp:
                        again = True
                        new_exp = new_exp[:opening_bracket] + str(LogicEval(p, q, r, new_exp[opening_bracket + 1:index - 1])) + new_exp[index:]
                        break
                if again:
                    break
    else:
        parts = new_exp.split(" ")
        part = 0
        while True:
            if part >= len(parts):
                break
            if parts[part] == "not":
                temp = str(not boolean(parts[part + 1]))
                parts[part + 1] = temp
                parts.pop(part)
                part = part - 1
            part += 1
        part = 0
        while True:
            if part >= len(parts):
                break
            if parts[part] == "and":
                parts = parts[:part - 1] + [str(boolean(parts[part - 1]) and boolean(parts[part + 1]))] + parts[part + 2:]
            part += 1
        part = 0
        while True:
            if part >= len(parts):
                break
            if parts[part] == "or":
                parts = parts[:part - 1] + [str(boolean(parts[part - 1]) or boolean(parts[part + 1]))] + parts[part + 2:]
            part += 1

        if len(parts) == 1:
            return parts[0]
        else:
            temp = ""
            for part in parts:
                temp += str(part) + " "
            return LogicEval(p, q, r, temp.strip())

    
    if again:
        return LogicEval(p, q, r, new_exp)




print(LogicEval(True, True, False, "p and q"))

print(LogicEval(True, True, False, "(p and q) and r"))

print(LogicEval(True, False, True, "(p and q) or r"))

print(LogicEval(True, False, True, "(p and q) or (q and r)"))

print(LogicEval(True, False, True, "(not p and q) or (q and not r)"))