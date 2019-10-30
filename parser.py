from pyparsing import *


def parse(formula: str) -> list:
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_letters = "abcdefghijklmnopqrstuvwxyz"

    element_name = Word(upper_letters, lower_letters)
    index = Word(nums).setParseAction(lambda t: float(t.asList()[0]))
    element = (element_name('name') + Optional(index('index'))).setParseAction(lambda t: (t.name, float(1) if t.index == "" else t.index))

    compound = Forward()
    compound << element + Optional(compound)
    compound_with_brackets = Group(Suppress('(') + compound + Suppress(')') + index)

    parser = (compound | compound_with_brackets) + Optional((Group(compound) | compound_with_brackets))
    return parser.parseString(formula).asList()