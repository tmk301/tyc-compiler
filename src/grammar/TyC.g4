grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text[1:]);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text[1:]);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options {
    language=Python3;
}

// ==================== PARSER ====================

program
    : (structDeclaration | functionDeclaration)* EOF
    ;

// --- Struct ---

structDeclaration
    : 'struct' IDENTIFIER '{' structMember* '}' ';'
    ;

structMember
    : typeSpec IDENTIFIER ';'
    ;

// --- Function ---

functionDeclaration
    : returnType? IDENTIFIER '(' parameterList? ')' block
    ;

returnType
    : primitiveType
    | IDENTIFIER
    ;

primitiveType
    : 'int'
    | 'float'
    | 'string'
    | 'void'
    ;

parameterList
    : parameter (',' parameter)*
    ;

parameter
    : typeSpec IDENTIFIER
    ;

typeSpec
    : 'int'
    | 'float'
    | 'string'
    | IDENTIFIER
    ;

// --- Block & Statements ---

block
    : '{' statement* '}'
    ;

statement
    : varDeclaration
    | assignmentStatement
    | ifStatement
    | whileStatement
    | forStatement
    | switchStatement
    | breakStatement
    | continueStatement
    | returnStatement
    | expressionStatement
    | block
    ;

varDeclaration
    : 'auto' IDENTIFIER ('=' expression)? ';'
    | typeSpec IDENTIFIER ('=' expression)? ';'
    | IDENTIFIER IDENTIFIER '=' '{' expressionList? '}' ';'
    | IDENTIFIER IDENTIFIER ';'
    ;

expressionList
    : expression (',' expression)*
    ;

assignmentStatement
    : lhs '=' expression ';'
    ;

lhs
    : IDENTIFIER ('.' IDENTIFIER)*
    ;

// --- Control Flow ---

ifStatement
    : 'if' '(' expression ')' statement ('else' statement)?
    ;

whileStatement
    : 'while' '(' expression ')' statement
    ;

forStatement
    : 'for' '(' forInit? ';' expression? ';' forUpdate? ')' statement
    ;

forInit
    : 'auto' IDENTIFIER '=' expression
    | 'auto' IDENTIFIER
    | typeSpec IDENTIFIER '=' expression
    | typeSpec IDENTIFIER
    | IDENTIFIER IDENTIFIER '=' '{' expressionList? '}'
    | IDENTIFIER IDENTIFIER
    | IDENTIFIER '=' expression
    ;

forUpdate
    : lhs '=' expression
    | lhs '++'
    | lhs '--'
    | '++' lhs
    | '--' lhs
    ;

// --- Switch ---

switchStatement
    : 'switch' '(' expression ')' '{' switchCase* '}'
    ;

switchCase
    : caseClause
    | defaultClause
    ;

caseClause
    : 'case' caseExpression ':' statement*
    ;

caseExpression
    : expression
    ;

defaultClause
    : 'default' ':' statement*
    ;

// --- Jump Statements ---

breakStatement
    : 'break' ';'
    ;

continueStatement
    : 'continue' ';'
    ;

returnStatement
    : 'return' expression? ';'
    ;

expressionStatement
    : expression ';'
    ;

// ==================== EXPRESSIONS ====================

expression
    : assignmentExpression
    ;

assignmentExpression
    : logicalOrExpression
    | lhs '=' assignmentExpression
    ;

logicalOrExpression
    : logicalAndExpression ('||' logicalAndExpression)*
    ;

logicalAndExpression
    : equalityExpression ('&&' equalityExpression)*
    ;

equalityExpression
    : relationalExpression (('==' | '!=') relationalExpression)*
    ;

relationalExpression
    : additiveExpression (('<' | '<=' | '>' | '>=') additiveExpression)*
    ;

additiveExpression
    : multiplicativeExpression (('+' | '-') multiplicativeExpression)*
    ;

multiplicativeExpression
    : unaryExpression (('*' | '/' | '%') unaryExpression)*
    ;

unaryExpression
    : postfixExpression
    | '!' unaryExpression
    | '-' unaryExpression
    | '+' unaryExpression
    | '++' unaryExpression
    | '--' unaryExpression
    ;

postfixExpression
    : primaryExpression postfixOp*
    ;

postfixOp
    : '++'
    | '--'
    | '(' argumentList? ')'
    | '.' IDENTIFIER
    ;

primaryExpression
    : IDENTIFIER
    | INT_LITERAL
    | FLOAT_LITERAL
    | STRING_LITERAL
    | '(' expression ')'
    | '{' expressionList? '}'
    ;

argumentList
    : expression (',' expression)*
    ;

// ==================== LEXER ====================

// --- Keywords ---

KEYWORD_AUTO     : 'auto';
KEYWORD_BREAK    : 'break';
KEYWORD_CASE     : 'case';
KEYWORD_CONTINUE : 'continue';
KEYWORD_DEFAULT  : 'default';
KEYWORD_ELSE     : 'else';
KEYWORD_FLOAT    : 'float';
KEYWORD_FOR      : 'for';
KEYWORD_IF       : 'if';
KEYWORD_INT      : 'int';
KEYWORD_RETURN   : 'return';
KEYWORD_STRING   : 'string';
KEYWORD_STRUCT   : 'struct';
KEYWORD_SWITCH   : 'switch';
KEYWORD_VOID     : 'void';
KEYWORD_WHILE    : 'while';

// --- Literals ---

IDENTIFIER
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

INT_LITERAL
    : [0-9]+
    ;

FLOAT_LITERAL
    : [0-9]+ '.' [0-9]*
    | [0-9]* '.' [0-9]+
    | [0-9]+ ('e' | 'E') ('+' | '-')? [0-9]+
    | [0-9]+ '.' [0-9]* ('e' | 'E') ('+' | '-')? [0-9]+
    | [0-9]* '.' [0-9]+ ('e' | 'E') ('+' | '-')? [0-9]+
    ;

STRING_LITERAL
    : '"' (~["\\\r\n] | '\\' [bfrnt"\\])* '"' 
      { self.text = self.text[1:-1] }
    ;

// --- Operators ---

PLUS          : '+';
MINUS         : '-';
MULTIPLY      : '*';
DIVIDE        : '/';
MODULO        : '%';
ASSIGN        : '=';
EQUAL         : '==';
NOT_EQUAL     : '!=';
LESS_THAN     : '<';
LESS_EQUAL    : '<=';
GREATER_THAN  : '>';
GREATER_EQUAL : '>=';
LOGICAL_AND   : '&&';
LOGICAL_OR    : '||';
LOGICAL_NOT   : '!';
INCREMENT     : '++';
DECREMENT     : '--';
DOT           : '.';

// --- Separators ---

LEFT_PAREN    : '(';
RIGHT_PAREN   : ')';
LEFT_BRACE    : '{';
RIGHT_BRACE   : '}';
SEMICOLON     : ';';
COMMA         : ',';
COLON         : ':';

// --- Skip ---

WS
    : [ \t\r\n\f]+ -> skip
    ;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

BLOCK_COMMENT
    : '/*' .*? '*/' -> skip
    ;

// --- Error Tokens ---

ILLEGAL_ESCAPE
    : '"' (~["\\\r\n] | '\\' [bfrnt"\\])* '\\' ~[bfrnt"\\]
    ;

UNCLOSE_STRING
    : '"' (~["\\\r\n] | '\\' [bfrnt"\\])*
    ;

ERROR_CHAR
    : .
    ;
