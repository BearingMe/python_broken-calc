import re

from interfaces import AbstractSymbolizer

class Symbolizer(AbstractSymbolizer):
    def validate_input(self, expression: str) -> bool:
        allowed_characters = set("0123456789+-*/.()")
        expression = re.sub(r"\s+", "", expression)

        # check if the input is empty
        if not expression:
            return False

        # check if the parentheses are balanced
        if expression.count("(") != expression.count(")"):
            return False

        # check if the input contains any invalid characters
        if not set(expression).issubset(allowed_characters):
            return False

        # check if the input contains two operators in a row, except for minus
        if re.search(r"[\*\/\+\.]{2,}", expression):
            return False

        # check if the input contains two minus signs in a row, except for negative numbers
        if re.search(r"[\*\/+-]-{2,}", expression):
            return False

        # check if starts or ends with a invalid operator
        if re.search(r"^[*/]|[*/\-\+]$", expression):
            return False

        # check if the input has a valid number
        if re.search(r"\d*\.+\d*\.+", expression):
            return False

        return True

    def create_symbol(self, expression: str) -> list:
        # create a list of tokens
        token_list = re.findall(r"[\d\.]+|[\+\-\*\/\(\)]", expression)
        
        # parse the first operator
        if token_list[0] in set("+-"):
            token_list[0] = token_list[0] + token_list[1]
            token_list.pop(1)

        # iterate over the list of tokens
        for index, token in enumerate(token_list):
            # if the token is a number
            if re.match(r"[+-]?[\d\.]+", token):
                token_list[index] = float(token)

        # find all the negative numbers
        aux = []
        counter = 0
        operators = set("+-*/")

        while counter < len(token_list):
            current_token = token_list[counter]
            next_token = token_list[counter + 1] if counter + 1 < len(token_list) else None

            if current_token in operators and next_token == "-":
                aux.append(current_token)
                aux.append(- token_list[counter + 2])

                counter += 2  
            else:
                aux.append(current_token)

            counter += 1

        token_list = aux

        return token_list