# Generated from ./grammar/Comp.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,2,16,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,3,0,9,8,0,1,1,1,1,1,1,1,
        2,1,2,1,2,0,0,3,0,2,4,0,0,13,0,8,1,0,0,0,2,10,1,0,0,0,4,13,1,0,0,
        0,6,9,3,2,1,0,7,9,5,2,0,0,8,6,1,0,0,0,8,7,1,0,0,0,9,1,1,0,0,0,10,
        11,3,4,2,0,11,12,5,1,0,0,12,3,1,0,0,0,13,14,5,2,0,0,14,5,1,0,0,0,
        1,8
    ]

class CompParser ( Parser ):

    grammarFileName = "Comp.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "END" ]

    RULE_rule = 0
    RULE_init = 1
    RULE_expr = 2

    ruleNames =  [ "rule", "init", "expr" ]

    EOF = Token.EOF
    T__0=1
    END=2

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def init(self):
            return self.getTypedRuleContext(CompParser.InitContext,0)


        def END(self):
            return self.getToken(CompParser.END, 0)

        def getRuleIndex(self):
            return CompParser.RULE_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule" ):
                listener.enterRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule" ):
                listener.exitRule(self)




    def rule_(self):

        localctx = CompParser.RuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_rule)
        try:
            self.state = 8
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 7
                self.match(CompParser.END)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CompParser.RULE_init

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EvaluacionContext(InitContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CompParser.InitContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CompParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvaluacion" ):
                listener.enterEvaluacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvaluacion" ):
                listener.exitEvaluacion(self)



    def init(self):

        localctx = CompParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_init)
        try:
            localctx = CompParser.EvaluacionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.expr()
            self.state = 11
            self.match(CompParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END(self):
            return self.getToken(CompParser.END, 0)

        def getRuleIndex(self):
            return CompParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = CompParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.match(CompParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





