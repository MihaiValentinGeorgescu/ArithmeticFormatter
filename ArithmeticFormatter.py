problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

def arithmetic_arranger(problems, show_answer=False):
    # Initialize variables
    first_line = ""
    second_line = ""
    dash_line = ""
    answer_line = ""
    arranged_problems = ""
    # Check if the number of problems is greater than 5
    if len(problems) > 5:
        return "Error: Too many problems."
    # Split each problem into its components
    for problem in problems:
        components = problem.split()
        # Check if the operator is valid
        if components[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        # Check if the operands are valid numbers
        if not components[0].isdigit() or not components[2].isdigit():
            return "Error: Numbers must only contain digits."
        # Convert the operands to integers
        num1 = int(components[0])
        num2 = int(components[2])
        # Check if the operands have more than 4 digits
        if num1 > 9999 or num2 > 9999:
            return "Error: Numbers cannot be more than four digits."
        # Calculate the answer
        answer = num1 + num2 if components[1] == "+" else num1 - num2
        # Determine the maximum length of the operands
        max_length = max(len(components[0]), len(components[2])) + 2
        # Add the first operand to the first line
        first_line += components[0].rjust(max_length)
        # Add the second operand to the second line
        second_line += components[1] + " " + components[2].rjust(max_length - 2)
        # Add the dashes to the dash line
        dash_line += "-" * max_length
        # Add the answer to the answer line
        if show_answer:
            answer_line += str(answer).rjust(max_length)
    # Combine the lines into the arranged problems
    arranged_problems = first_line + "\n" + second_line + "\n" + dash_line
    if show_answer:
        arranged_problems += "\n" + answer_line
    return arranged_problems

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems))