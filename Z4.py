# Доп задача:
# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;


def custom_eval(string):
    string = string.replace(" ", "")

    def split_by(string, separators):

        operations_list = []
        current = ""
        for i in string:
            if i in separators:
                operations_list.append(current)
                operations_list.append(i)
                current = ""
            else:
                current += i
        operations_list.append(current)
        return operations_list

    operations_list = split_by(string, "+-")

    def eval_mul_div(string):
        operations_list = split_by(string, "*/")
        if len(operations_list) == 1:
            return operations_list[0]
        
        result = float(operations_list[0])
        operations_list = operations_list[1:]

        while len(operations_list) > 0:
            operator = operations_list[0]
            number = float(operations_list[1])
            operations_list = operations_list[2:]

            if operator == "*":
                result *= number

            elif operator == "/":
                result /= number

        return result

    
    for i in range(len(operations_list)):
        operations_list[i] = eval_mul_div(operations_list[i])

    result = float(operations_list[0])
    operations_list = operations_list[1:]

    while len(operations_list) > 0:
        operator = operations_list[0]
        number = float(operations_list[1])
        operations_list = operations_list[2:]

        if operator == "+":
            result += number
        elif operator == "-":
            result -= number

    return result

example_problems = ["2+2", "1+2*3", "1-2 * 3", "1+2*3 -4/5", "1+2*3/ 4+5*6", "6 * 2 * 5 / 4"]

for problem in example_problems:
    print(problem, "=", custom_eval(problem))