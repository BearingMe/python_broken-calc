class Expr(object):
    pass

class Times(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "({} * {})".format(self.left, self.right)

    def eval(self, env):
        return self.left.eval(env) * self.right.eval(env)

class Plus(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "({} + {})".format(self.left, self.right)

    def eval(self, env):
        return self.left.eval(env) + self.right.eval(env)

class Minus(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "({} - {})".format(self.left, self.right)

    def eval(self, env):
        return self.left.eval(env) - self.right.eval(env)

class Div(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "({} / {})".format(self.left, self.right)

    def eval(self, env):
        return self.left.eval(env) / self.right.eval(env)

class Const(Expr):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def eval(self, env):
        return self.value

class Var(Expr):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def eval(self, env):
        return env[self.name]

env = {'x': 3, 'y': 4}

e1 = Times(Const(3), Plus(Var('y'), Var('x')))
e2 = Plus(Times(Const(3), Var("y")), Var("x"))

print(e1.eval(env))
print(e2)