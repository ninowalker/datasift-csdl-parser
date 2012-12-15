import pyparsing as pp
import re

def _build_parser():
    # supported operators
    operator = pp.Regex(r"<=|>=|<>|\!=|==|<|>|not|in|regex_partial|regex_exact|geo_box|geo_radius|geo_polygon|contains_any|substr|contains_near|any|contains_substr|near|contains").setName("operator")

    # literals
    number = pp.Regex(r"[+-]?\d+(:?\.\d*)?(:?[eE][+-]?\d+)?").setName("number")
    numberList = pp.Group(pp.Suppress('[') + number + pp.ZeroOrMore("," + number) + pp.Suppress(']')).setName("numberList")
    string = pp.dblQuotedString
    literals = number | numberList | string

    # symbols
    identifier = pp.Regex(r"[a-z][a-z_]+(?:\.[a-z][a-z_]+)+").setName("identifier")

    # we'll get there...
    subExpr = pp.Forward()

    # predicates
    stream = pp.Group(pp.Literal("stream") + string).setName("stream")
    exists = pp.Group(identifier + pp.Literal("exists")).setName("exists")

    # boolean predicates
    comparison = pp.Group(
        identifier + operator + literals
        | literals + operator + identifier
    ).setName("comparison")

    condition = comparison | stream | exists | subExpr
    subExpr << pp.Suppress('(') + condition + pp.Suppress(')')
    negation = pp.Group(pp.CaselessLiteral("not") + condition).setName("negation")
    condition = condition | negation

    # standard boolean operator precedence
    expr = pp.operatorPrecedence(condition,[
        (pp.CaselessLiteral("AND"), 2, pp.opAssoc.LEFT, ),
        (pp.CaselessLiteral("OR"), 2, pp.opAssoc.LEFT, ),
        ])

    # tag "thing" { expr }
    tag = pp.Group(pp.CaselessLiteral("tag") + pp.quotedString + pp.Suppress('{') + expr + pp.Suppress('}')).setName("tag")

    # return { expr }
    a_return = pp.Group(pp.Literal("return") + pp.Suppress('{') + expr + pp.Suppress('}')).setName("return")

    # a single expression or tag [, tag, ...] return { expression }
    parser = expr | (pp.OneOrMore(tag) + a_return)

    # handle multilines
    parser.setDefaultWhitespaceChars(" \t\n\r")

    # handle // comments
    parser.ignore("//" + pp.restOfLine)
    return parser

CSDLParser = parser = _build_parser()
