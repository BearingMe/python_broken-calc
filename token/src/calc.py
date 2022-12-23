from src import RecursiveParser, Symbolizer

def calc(expr):
    symbolizer = Symbolizer()
    parser = RecursiveParser()

    if not symbolizer.validate_input(expr):
        raise ValueError("Invalid input")
        
    symbols = symbolizer.create_symbol(expr)
    tree = parser.parse(symbols)

    return tree.evaluate()