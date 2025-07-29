import ast

class PathVisitor(ast.NodeVisitor):
    def __init__(self):
        self.paths = []
        self.current_path = []

    def visit_If(self, node):
        test = ast.unparse(node.test)

        # Caminho if True
        self.current_path.append(f"if {test} [True]")
        for stmt in node.body:
            self.visit(stmt)
        self.current_path.pop()

        # Caminho if False (else)
        self.current_path.append(f"if {test} [False]")
        for stmt in node.orelse:
            self.visit(stmt)
        self.current_path.pop()

    def visit_Return(self, node):
        self.paths.append(list(self.current_path) + [f"return {ast.unparse(node.value)}"])

    def visit_For(self, node):
        target = ast.unparse(node.target)
        iter_expr = ast.unparse(node.iter)

        # Caminho onde o loop é executado pelo menos uma vez
        self.current_path.append(f"for {target} in {iter_expr} [entered]")
        for stmt in node.body:
            self.visit(stmt)
        self.current_path.pop()

        # Caminho onde o loop não é executado
        self.current_path.append(f"for {target} in {iter_expr} [skipped]")
        for stmt in node.orelse:
            self.visit(stmt)
        self.current_path.pop()

