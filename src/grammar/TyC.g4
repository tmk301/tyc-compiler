grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

// ==================== PARSER RULES ====================

program: (structDeclaration | functionDeclaration)* EOF;

// Struct Declaration
// struct <identifier> { <member_list> };
structDeclaration
    : 'struct' IDENTIFIER '{' structMember* '}' ';'
    ;

structMember
    : typeSpec IDENTIFIER ';'
    ;

// Function Declaration
// <return_type>? <identifier>(<parameter_list>) { <statement_list> }
functionDeclaration
    : returnType? IDENTIFIER '(' parameterList? ')' block
    ;

returnType
    : primitiveType
    | IDENTIFIER  // struct type
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

// Parameters must have explicit type (no auto allowed)
parameter
    : typeSpec IDENTIFIER
    ;

// Type specification (no void, no auto for variable/parameter types)
typeSpec
    : 'int'
    | 'float'
    | 'string'
    | IDENTIFIER  // struct type
    ;

// Block and Statements
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

// Variable Declaration
// auto <identifier> = <expression>;
// auto <identifier>;
// <type> <identifier> = <expression>;
// <type> <identifier>;
// <struct_name> <identifier> = { <expression_list> };
// <struct_name> <identifier>;
varDeclaration
    : 'auto' IDENTIFIER ('=' expression)? ';'
    | typeSpec IDENTIFIER ('=' expression)? ';'
    | IDENTIFIER IDENTIFIER '=' '{' expressionList? '}' ';'  // struct initialization
    | IDENTIFIER IDENTIFIER ';'  // struct without initialization
    ;

expressionList
    : expression (',' expression)*
    ;

// Assignment Statement
// <identifier> = <expression>;
// <identifier>.<member> = <expression>;
assignmentStatement
    : lhs '=' expression ';'
    ;

lhs
    : IDENTIFIER ('.' IDENTIFIER)*
    ;

// If Statement
// if (<expression>) <statement>
// if (<expression>) <statement> else <statement>
ifStatement
    : 'if' '(' expression ')' statement ('else' statement)?
    ;

// While Statement
// while (<expression>) <statement>
whileStatement
    : 'while' '(' expression ')' statement
    ;

// For Statement
// for (<init>; <condition>; <update>) <statement>
forStatement
    : 'for' '(' forInit? ';' expression? ';' forUpdate? ')' statement
    ;

// For init - NO semicolon here (already in forStatement)
forInit
    : 'auto' IDENTIFIER '=' expression
    | 'auto' IDENTIFIER
    | typeSpec IDENTIFIER '=' expression
    | typeSpec IDENTIFIER
    | IDENTIFIER IDENTIFIER '=' '{' expressionList? '}'  // struct init
    | IDENTIFIER IDENTIFIER                               // struct decl
    | IDENTIFIER '=' expression                           // assignment
    ;

forUpdate
    : lhs '=' expression
    | lhs '++'
    | lhs '--'
    | '++' lhs
    | '--' lhs
    ;

// Switch Statement
// switch (<expression>) { case <constant>: <statements> ... default: <statements> }
// Note: default can appear anywhere (spec line 720)
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

// Case expression - allows constant expressions per spec
// Semantic analysis validates it's a compile-time constant int
caseExpression
    : expression
    ;

defaultClause
    : 'default' ':' statement*
    ;

// Break, Continue, Return
breakStatement
    : 'break' ';'
    ;

continueStatement
    : 'continue' ';'
    ;

returnStatement
    : 'return' expression? ';'
    ;

// Expression Statement
expressionStatement
    : expression ';'
    ;

// ==================== EXPRESSIONS ====================
// Precedence (lowest to highest):
// 1. Assignment (=) - right associative
// 2. Logical OR (||) - left associative
// 3. Logical AND (&&) - left associative
// 4. Equality (==, !=) - left associative
// 5. Relational (<, <=, >, >=) - left associative
// 6. Additive (+, -) - left associative
// 7. Multiplicative (*, /, %) - left associative
// 8. Unary (!, -, +, ++, --) - right associative
// 9. Postfix (++, --, function call, member access) - left associative
// 10. Primary (identifier, literal, parenthesized)

expression
    : assignmentExpression
    ;

// Assignment: right associative
assignmentExpression
    : logicalOrExpression
    | lhs '=' assignmentExpression
    ;

// Logical OR: left associative
logicalOrExpression
    : logicalAndExpression ('||' logicalAndExpression)*
    ;

// Logical AND: left associative
logicalAndExpression
    : equalityExpression ('&&' equalityExpression)*
    ;

// Equality: left associative
equalityExpression
    : relationalExpression (('==' | '!=') relationalExpression)*
    ;

// Relational: left associative
relationalExpression
    : additiveExpression (('<' | '<=' | '>' | '>=') additiveExpression)*
    ;

// Additive: left associative
additiveExpression
    : multiplicativeExpression (('+' | '-') multiplicativeExpression)*
    ;

// Multiplicative: left associative
multiplicativeExpression
    : unaryExpression (('*' | '/' | '%') unaryExpression)*
    ;

// Unary: right associative (prefix operators)
unaryExpression
    : postfixExpression
    | '!' unaryExpression
    | '-' unaryExpression
    | '+' unaryExpression
    | '++' unaryExpression
    | '--' unaryExpression
    ;

// Postfix: left associative (++, --, function call, member access)
postfixExpression
    : primaryExpression postfixOp*
    ;

postfixOp
    : '++'
    | '--'
    | '(' argumentList? ')'       // function call
    | '.' IDENTIFIER              // member access
    ;

// Primary expressions
primaryExpression
    : IDENTIFIER
    | INT_LITERAL
    | FLOAT_LITERAL
    | STRING_LITERAL
    | '(' expression ')'
    | '{' expressionList? '}'  // struct literal for function args: f({1, 2})
    ;

argumentList
    : expression (',' expression)*
    ;

// ==================== LEXER RULES ====================

// Keywords (must be before IDENTIFIER)
KEYWORD_AUTO: 'auto';
KEYWORD_BREAK: 'break';
KEYWORD_CASE: 'case';
KEYWORD_CONTINUE: 'continue';
KEYWORD_DEFAULT: 'default';
KEYWORD_ELSE: 'else';
KEYWORD_FLOAT: 'float';
KEYWORD_FOR: 'for';
KEYWORD_IF: 'if';
KEYWORD_INT: 'int';
KEYWORD_RETURN: 'return';
KEYWORD_STRING: 'string';
KEYWORD_STRUCT: 'struct';
KEYWORD_SWITCH: 'switch';
KEYWORD_VOID: 'void';
KEYWORD_WHILE: 'while';

// Identifiers
// Begin with letter (A-Z, a-z) or underscore (_)
// May contain letters, underscores, and digits (0-9)
IDENTIFIER
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

// Integer Literals
// Decimal (base 10) only, at least one digit
INT_LITERAL
    : [0-9]+
    ;

// Float Literals
// Decimal notation: 3.14, 0.5, 123.456, 1., .5
// Scientific notation: 1.23e4, 5.67E-2
FLOAT_LITERAL
    : [0-9]+ '.' [0-9]*                              // 123. or 123.456
    | [0-9]* '.' [0-9]+                              // .5 or 0.5
    | [0-9]+ ('e' | 'E') ('+' | '-')? [0-9]+         // 1e10, 1E-5
    | [0-9]+ '.' [0-9]* ('e' | 'E') ('+' | '-')? [0-9]+  // 1.23e4
    | [0-9]* '.' [0-9]+ ('e' | 'E') ('+' | '-')? [0-9]+  // .5e-2
    ;

// String Literals
// Enclosed by double quotes
// Escape sequences: \b \f \r \n \t \" \\
STRING_LITERAL
    : '"' (~["\\\r\n] | '\\' [bfrnt"\\])* '"' 
    { self.text = self.text[1:-1] }
    ;

// Operators
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
MODULO: '%';
ASSIGN: '=';
EQUAL: '==';
NOT_EQUAL: '!=';
LESS_THAN: '<';
LESS_EQUAL: '<=';
GREATER_THAN: '>';
GREATER_EQUAL: '>=';
LOGICAL_AND: '&&';
LOGICAL_OR: '||';
LOGICAL_NOT: '!';
INCREMENT: '++';
DECREMENT: '--';
DOT: '.';

// Separators
LEFT_PAREN: '(';
RIGHT_PAREN: ')';
LEFT_BRACE: '{';
RIGHT_BRACE: '}';
SEMICOLON: ';';
COMMA: ',';
COLON: ':';

// Comments and Whitespace
WS : [ \t\r\n\f]+ -> skip;

// Line comment: // to end of line
LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

// Block comment: /* to */ (or to EOF if unclosed per spec line 114)
// Note: .*? is non-greedy but will consume to EOF if no */ found
BLOCK_COMMENT
    : '/*' (~[*] | '*' ~[/])* ('*/')? -> skip
    ;

// Error handling tokens - ORDER MATTERS!
// These must be AFTER valid tokens but BEFORE ERROR_CHAR
// Per spec: illegal escape is detected FIRST, then unclosed string

// Illegal escape: string with invalid escape sequence
// Detected first per spec line 226
ILLEGAL_ESCAPE
    : '"' (~["\\\r\n] | '\\' [bfrnt"\\])* '\\' ~[bfrnt"\\]
    ;

// Unclosed string: starts with " but no closing "
// Content can have valid escapes or non-special chars
UNCLOSE_STRING
    : '"' (~["\\\r\n] | '\\' [bfrnt"\\])*
    ;

// Error character: any character not matched above
ERROR_CHAR: .;
