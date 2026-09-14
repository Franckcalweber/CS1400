import ast

def test_cuadrado_script():
    # Fix 1: Target the correct file name from your project folder
    with open("1cuadrado.py", "r", encoding="utf-8") as f:
        student_code = f.read()

    tree = ast.parse(student_code)

    # 1. Check if variable 'cuadrado' is defined
    has_cuadrado_variable = any(
        isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "cuadrado" for t in node.targets
        )
        for node in ast.walk(tree)
    )
    assert has_cuadrado_variable, "Debes definir la variable 'cuadrado'."

    # 2. Check for exponentiation operator (Pow)
    uses_pow_operator = any(
        isinstance(node, ast.BinOp) and isinstance(node.op, ast.Pow)
        for node in ast.walk(tree)
    )
    assert uses_pow_operator, "Debes calcular el cuadrado usando el operador de potencia '**'."

    # 3. Check for print() call
    has_print = any(
        isinstance(node, ast.Call) 
        and isinstance(node.func, ast.Name) 
        and node.func.id == "print"
        for node in ast.walk(tree)
    )
    assert has_print, "Debes utilizar la función 'print()' para mostrar el resultado."