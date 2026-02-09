expression = {"left": 3, "operator": "+", "right": {"left": 2, "operator": "*", "right": 3}}

def evaluate_expression(node):
    if isinstance(node, (int, float)):
        return node
    
    left = evaluate_expression(node["left"])
    operator = node["operator"]
    right = evaluate_expression(node["right"])
    
    if operator == "+":
        return left + right
    elif operator == "-":
        return left - right
    elif operator == "*":
        return left * right
    elif operator == "/":
        return left / right
    elif operator == "**":
        return left ** right

print(evaluate_expression(expression))
