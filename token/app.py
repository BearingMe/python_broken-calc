from src import RecursiveParser, Symbolizer

def calc(expr):
    symbolizer = Symbolizer()
    parser = RecursiveParser()

    if not symbolizer.validate_input(expr):
        raise ValueError("Invalid input")
        
    symbols = symbolizer.create_symbol(expr)
    tree = parser.parse(symbols)

    return tree.evaluate()

def test_speed(f):
    import timeit

    expr = "3 / 4 + 5 * 6 - 7 * 8 + 9 / 10 + (3 / 4 + 5 * 6 - 7 * 8 + 9 / 10)"

    print(timeit.timeit(lambda: f(expr), number=100000))

def main():
    test_speed(calc)  
    test_speed(eval)

if __name__ == '__main__':
    main()