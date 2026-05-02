# Generated from ./grammar/Comp.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CompParser import CompParser
else:
    from CompParser import CompParser

# This class defines a complete listener for a parse tree produced by CompParser.
class CompListener(ParseTreeListener):

    # Enter a parse tree produced by CompParser#rule.
    def enterRule(self, ctx:CompParser.RuleContext):
        pass

    # Exit a parse tree produced by CompParser#rule.
    def exitRule(self, ctx:CompParser.RuleContext):
        pass


    # Enter a parse tree produced by CompParser#Evaluacion.
    def enterEvaluacion(self, ctx:CompParser.EvaluacionContext):
        pass

    # Exit a parse tree produced by CompParser#Evaluacion.
    def exitEvaluacion(self, ctx:CompParser.EvaluacionContext):
        pass


    # Enter a parse tree produced by CompParser#expr.
    def enterExpr(self, ctx:CompParser.ExprContext):
        pass

    # Exit a parse tree produced by CompParser#expr.
    def exitExpr(self, ctx:CompParser.ExprContext):
        pass



del CompParser