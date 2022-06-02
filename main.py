import operator
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
memory = 0
msg = ("Enter an equation\n",  # 0
       "Do you even know what numbers are? Stay focused!",  # 1
       "Yes ... an interesting math operation. You've slept through all classes, haven't you?",  # 2
       "Yeah... division by zero. Smart move...",  # 3
       "Do you want to store the result? (y / n):\n",  # 4
       "Do you want to continue calculations? (y / n):\n",  # 5
       " ... lazy",  # 6
       " ... very lazy",  # 7
       " ... very, very lazy",  # 8
       "You are",  # 9
       "Are you sure? It is only one digit! (y / n)\n",  # 10
       "Don't be silly! It's just one number! Add to the memory? (y / n)\n",  # 11
       "Last chance! Do you really want to embarrass yourself? (y / n)\n")  # 12


def check(v1, v2, v3):
    msg_2 = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg_2 = msg_2 + msg[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg_2 = msg_2 + msg[7]
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg_2 = msg_2 + msg[8]
    if msg_2 != "":
        print(msg[9] + msg_2)


def is_one_digit(v):
    return -10 < v < 10 and v.is_integer()


def question(message):
    while True:
        answer = input(message)
        if answer == "y":
            return True
        elif answer == "n":
            return False


while True:
    try:
        calc = input(msg[0]).split()
        calc = [i if i != "M" else memory for i in calc]
        x, oper, y = float(calc[0]), calc[1], float(calc[2])
        check(x, y, oper)
        result = ops[oper](x, y)
        print(result)

        if question(msg[4]):
            if is_one_digit(result):
                msg_index = 10
                while question(msg[msg_index]):
                    if msg_index < 12:
                        msg_index += 1
                    else:
                        memory = result
                        break
            else:
                memory = result

        if not question(msg[5]):
            break

    except ValueError:
        print(msg[1])
    except KeyError:
        print(msg[2])
    except ZeroDivisionError:
        print(msg[3])
