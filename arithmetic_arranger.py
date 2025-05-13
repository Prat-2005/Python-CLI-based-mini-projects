# Arithmetic Arranger

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems"
    
    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()

        if len(parts) != 3:
            return "Error: Must contains two operands and one operator."
        
        operand1, operator, operand2 = parts
        
        if operator not in ['+', '-']:
            return "Error: Operators must be '+' or '-'."
        
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain in digits."
        
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        width = max(len(operand1), len(operand2)) + 2

        first_line.append(operand1.rjust(width)) 
        second_line.append(operator + operand2.rjust(width - 1))
        dashes.append('-'*width)

        if show_answers:
            result = str(eval(problem))
            answers.append(result.rjust(width))

        arithmetic_problems = (
            '    '.join(first_line) + '\n' +
            '    '.join(second_line) + '\n' +
            '    '.join(dashes)
        )

        if show_answers:
            arithmetic_problems += '\n' + '    '.join(answers)

    return arithmetic_problems

print(arithmetic_arranger(["123 + 5", "56 + 4578", "567 + 3421", "4 + 1365"], True)) 
