"""
Lexer test cases for TyC compiler
100 test cases covering all token types and error handling
"""

import pytest
from tests.utils import Tokenizer


# ========== Simple Test Cases (10 types) ==========
def test_keyword_auto():
    """1. Keyword"""
    tokenizer = Tokenizer("auto")
    assert tokenizer.get_tokens_as_string() == "auto,<EOF>"


def test_operator_assign():
    """2. Operator"""
    tokenizer = Tokenizer("=")
    assert tokenizer.get_tokens_as_string() == "=,<EOF>"


def test_separator_semi():
    """3. Separator"""
    tokenizer = Tokenizer(";")
    assert tokenizer.get_tokens_as_string() == ";,<EOF>"


def test_integer_single_digit():
    """4. Integer literal"""
    tokenizer = Tokenizer("5")
    assert tokenizer.get_tokens_as_string() == "5,<EOF>"


def test_float_decimal():
    """5. Float literal"""
    tokenizer = Tokenizer("3.14")
    assert tokenizer.get_tokens_as_string() == "3.14,<EOF>"


def test_string_simple():
    """6. String literal"""
    tokenizer = Tokenizer('"hello"')
    assert tokenizer.get_tokens_as_string() == "hello,<EOF>"


def test_identifier_simple():
    """7. Identifier"""
    tokenizer = Tokenizer("x")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"


def test_line_comment():
    """8. Line comment"""
    tokenizer = Tokenizer("// This is a comment")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_integer_in_expression():
    """9. Mixed: integers and operator"""
    tokenizer = Tokenizer("5+10")
    assert tokenizer.get_tokens_as_string() == "5,+,10,<EOF>"


def test_complex_expression():
    """10. Complex: variable declaration"""
    tokenizer = Tokenizer("auto x = 5 + 3 * 2;")
    assert tokenizer.get_tokens_as_string() == "auto,x,=,5,+,3,*,2,;,<EOF>"
# =============================================================================
# KEYWORD TESTS (16 tests)
# =============================================================================

class TestKeywords:
    """Test all 16 TyC keywords"""
    
    def test_keyword_auto(self):
        """Test 'auto' keyword"""
        assert "KEYWORD_AUTO,auto" in Tokenizer("auto").get_tokens_as_string()
    
    def test_keyword_break(self):
        """Test 'break' keyword"""
        assert "KEYWORD_BREAK,break" in Tokenizer("break").get_tokens_as_string()
    
    def test_keyword_case(self):
        """Test 'case' keyword"""
        assert "KEYWORD_CASE,case" in Tokenizer("case").get_tokens_as_string()
    
    def test_keyword_continue(self):
        """Test 'continue' keyword"""
        assert "KEYWORD_CONTINUE,continue" in Tokenizer("continue").get_tokens_as_string()
    
    def test_keyword_default(self):
        """Test 'default' keyword"""
        assert "KEYWORD_DEFAULT,default" in Tokenizer("default").get_tokens_as_string()
    
    def test_keyword_else(self):
        """Test 'else' keyword"""
        assert "KEYWORD_ELSE,else" in Tokenizer("else").get_tokens_as_string()
    
    def test_keyword_float(self):
        """Test 'float' keyword"""
        assert "KEYWORD_FLOAT,float" in Tokenizer("float").get_tokens_as_string()
    
    def test_keyword_for(self):
        """Test 'for' keyword"""
        assert "KEYWORD_FOR,for" in Tokenizer("for").get_tokens_as_string()
    
    def test_keyword_if(self):
        """Test 'if' keyword"""
        assert "KEYWORD_IF,if" in Tokenizer("if").get_tokens_as_string()
    
    def test_keyword_int(self):
        """Test 'int' keyword"""
        assert "KEYWORD_INT,int" in Tokenizer("int").get_tokens_as_string()
    
    def test_keyword_return(self):
        """Test 'return' keyword"""
        assert "KEYWORD_RETURN,return" in Tokenizer("return").get_tokens_as_string()
    
    def test_keyword_string(self):
        """Test 'string' keyword"""
        assert "KEYWORD_STRING,string" in Tokenizer("string").get_tokens_as_string()
    
    def test_keyword_struct(self):
        """Test 'struct' keyword"""
        assert "KEYWORD_STRUCT,struct" in Tokenizer("struct").get_tokens_as_string()
    
    def test_keyword_switch(self):
        """Test 'switch' keyword"""
        assert "KEYWORD_SWITCH,switch" in Tokenizer("switch").get_tokens_as_string()
    
    def test_keyword_void(self):
        """Test 'void' keyword"""
        assert "KEYWORD_VOID,void" in Tokenizer("void").get_tokens_as_string()
    
    def test_keyword_while(self):
        """Test 'while' keyword"""
        assert "KEYWORD_WHILE,while" in Tokenizer("while").get_tokens_as_string()


# =============================================================================
# IDENTIFIER TESTS (10 tests)
# =============================================================================

class TestIdentifiers:
    """Test identifier recognition"""
    
    def test_simple_identifier(self):
        """Test simple identifier"""
        assert "IDENTIFIER,abc" in Tokenizer("abc").get_tokens_as_string()
    
    def test_identifier_with_underscore_prefix(self):
        """Test identifier starting with underscore"""
        assert "IDENTIFIER,_var" in Tokenizer("_var").get_tokens_as_string()
    
    def test_identifier_with_numbers(self):
        """Test identifier with numbers"""
        assert "IDENTIFIER,var123" in Tokenizer("var123").get_tokens_as_string()
    
    def test_identifier_mixed_case(self):
        """Test identifier with mixed case"""
        assert "IDENTIFIER,MyVariable" in Tokenizer("MyVariable").get_tokens_as_string()
    
    def test_identifier_all_uppercase(self):
        """Test identifier in all uppercase"""
        assert "IDENTIFIER,CONSTANT" in Tokenizer("CONSTANT").get_tokens_as_string()
    
    def test_identifier_underscore_only(self):
        """Test single underscore identifier"""
        assert "IDENTIFIER,_" in Tokenizer("_").get_tokens_as_string()
    
    def test_identifier_multiple_underscores(self):
        """Test identifier with multiple underscores"""
        assert "IDENTIFIER,__init__" in Tokenizer("__init__").get_tokens_as_string()
    
    def test_identifier_underscore_and_digits(self):
        """Test identifier with underscore and digits"""
        assert "IDENTIFIER,_123" in Tokenizer("_123").get_tokens_as_string()
    
    def test_identifier_long_name(self):
        """Test long identifier"""
        assert "IDENTIFIER,veryLongVariableNameForTesting" in Tokenizer("veryLongVariableNameForTesting").get_tokens_as_string()
    
    def test_identifier_not_keyword(self):
        """Test identifier that looks like keyword prefix"""
        assert "IDENTIFIER,integer" in Tokenizer("integer").get_tokens_as_string()


# =============================================================================
# INTEGER LITERAL TESTS (10 tests)
# =============================================================================

class TestIntegerLiterals:
    """Test integer literal recognition"""
    
    def test_single_digit(self):
        """Test single digit integer"""
        assert "INT_LITERAL,5" in Tokenizer("5").get_tokens_as_string()
    
    def test_zero(self):
        """Test zero"""
        assert "INT_LITERAL,0" in Tokenizer("0").get_tokens_as_string()
    
    def test_multi_digit(self):
        """Test multi-digit integer"""
        assert "INT_LITERAL,12345" in Tokenizer("12345").get_tokens_as_string()
    
    def test_large_number(self):
        """Test large integer"""
        assert "INT_LITERAL,999999999" in Tokenizer("999999999").get_tokens_as_string()
    
    def test_leading_zeros(self):
        """Test integer with leading zeros"""
        assert "INT_LITERAL,007" in Tokenizer("007").get_tokens_as_string()
    
    def test_two_digit(self):
        """Test two-digit integer"""
        assert "INT_LITERAL,42" in Tokenizer("42").get_tokens_as_string()
    
    def test_hundred(self):
        """Test one hundred"""
        assert "INT_LITERAL,100" in Tokenizer("100").get_tokens_as_string()
    
    def test_thousand(self):
        """Test one thousand"""
        assert "INT_LITERAL,1000" in Tokenizer("1000").get_tokens_as_string()
    
    def test_consecutive_integers(self):
        """Test consecutive integers separated by space"""
        result = Tokenizer("1 2 3").get_tokens_as_string()
        assert "INT_LITERAL,1" in result
        assert "INT_LITERAL,2" in result
        assert "INT_LITERAL,3" in result
    
    def test_integer_boundary(self):
        """Test integer boundary value"""
        assert "INT_LITERAL,2147483647" in Tokenizer("2147483647").get_tokens_as_string()


# =============================================================================
# FLOAT LITERAL TESTS (15 tests)
# =============================================================================

class TestFloatLiterals:
    """Test float literal recognition"""
    
    def test_simple_float(self):
        """Test simple float"""
        assert "FLOAT_LITERAL,3.14" in Tokenizer("3.14").get_tokens_as_string()
    
    def test_zero_point_float(self):
        """Test float starting with 0."""
        assert "FLOAT_LITERAL,0.5" in Tokenizer("0.5").get_tokens_as_string()
    
    def test_float_no_leading_digit(self):
        """Test float without leading digit (.5)"""
        assert "FLOAT_LITERAL,.5" in Tokenizer(".5").get_tokens_as_string()
    
    def test_float_no_trailing_digit(self):
        """Test float without trailing digit (1.)"""
        assert "FLOAT_LITERAL,1." in Tokenizer("1.").get_tokens_as_string()
    
    def test_scientific_notation_lowercase(self):
        """Test scientific notation with lowercase e"""
        assert "FLOAT_LITERAL,1e10" in Tokenizer("1e10").get_tokens_as_string()
    
    def test_scientific_notation_uppercase(self):
        """Test scientific notation with uppercase E"""
        assert "FLOAT_LITERAL,1E10" in Tokenizer("1E10").get_tokens_as_string()
    
    def test_scientific_positive_exponent(self):
        """Test scientific notation with positive exponent"""
        assert "FLOAT_LITERAL,1e+10" in Tokenizer("1e+10").get_tokens_as_string()
    
    def test_scientific_negative_exponent(self):
        """Test scientific notation with negative exponent"""
        assert "FLOAT_LITERAL,1e-10" in Tokenizer("1e-10").get_tokens_as_string()
    
    def test_float_with_exponent(self):
        """Test float with decimal and exponent"""
        assert "FLOAT_LITERAL,1.23e4" in Tokenizer("1.23e4").get_tokens_as_string()
    
    def test_float_zero(self):
        """Test float zero"""
        assert "FLOAT_LITERAL,0.0" in Tokenizer("0.0").get_tokens_as_string()
    
    def test_float_small_decimal(self):
        """Test small decimal float"""
        assert "FLOAT_LITERAL,0.001" in Tokenizer("0.001").get_tokens_as_string()
    
    def test_float_large_value(self):
        """Test large float value"""
        assert "FLOAT_LITERAL,123456.789" in Tokenizer("123456.789").get_tokens_as_string()
    
    def test_scientific_decimal_negative(self):
        """Test decimal with negative exponent"""
        assert "FLOAT_LITERAL,5.67E-2" in Tokenizer("5.67E-2").get_tokens_as_string()
    
    def test_dot_with_exponent(self):
        """Test .5e-2 format"""
        assert "FLOAT_LITERAL,.5e-2" in Tokenizer(".5e-2").get_tokens_as_string()
    
    def test_trailing_dot_with_exponent(self):
        """Test 1.e5 format"""
        assert "FLOAT_LITERAL,1.e5" in Tokenizer("1.e5").get_tokens_as_string()


# =============================================================================
# STRING LITERAL TESTS (12 tests)
# =============================================================================

class TestStringLiterals:
    """Test string literal recognition"""
    
    def test_empty_string(self):
        """Test empty string"""
        assert "STRING_LITERAL," in Tokenizer('""').get_tokens_as_string()
    
    def test_simple_string(self):
        """Test simple string"""
        assert "STRING_LITERAL,hello" in Tokenizer('"hello"').get_tokens_as_string()
    
    def test_string_with_spaces(self):
        """Test string with spaces"""
        assert "STRING_LITERAL,hello world" in Tokenizer('"hello world"').get_tokens_as_string()
    
    def test_escape_backslash(self):
        """Test escape sequence backslash"""
        assert "STRING_LITERAL,a\\\\b" in Tokenizer('"a\\\\b"').get_tokens_as_string()
    
    def test_escape_newline(self):
        """Test escape sequence newline"""
        assert "STRING_LITERAL,a\\nb" in Tokenizer('"a\\nb"').get_tokens_as_string()
    
    def test_escape_tab(self):
        """Test escape sequence tab"""
        assert "STRING_LITERAL,a\\tb" in Tokenizer('"a\\tb"').get_tokens_as_string()
    
    def test_escape_quote(self):
        """Test escape sequence double quote"""
        assert 'STRING_LITERAL,a\\"b' in Tokenizer('"a\\"b"').get_tokens_as_string()
    
    def test_escape_carriage_return(self):
        """Test escape sequence carriage return"""
        assert "STRING_LITERAL,a\\rb" in Tokenizer('"a\\rb"').get_tokens_as_string()
    
    def test_escape_backspace(self):
        """Test escape sequence backspace"""
        assert "STRING_LITERAL,a\\bb" in Tokenizer('"a\\bb"').get_tokens_as_string()
    
    def test_escape_formfeed(self):
        """Test escape sequence formfeed"""
        assert "STRING_LITERAL,a\\fb" in Tokenizer('"a\\fb"').get_tokens_as_string()
    
    def test_string_with_numbers(self):
        """Test string containing numbers"""
        assert "STRING_LITERAL,test123" in Tokenizer('"test123"').get_tokens_as_string()
    
    def test_multiple_escapes(self):
        """Test string with multiple escape sequences"""
        assert "STRING_LITERAL,\\n\\t\\r" in Tokenizer('"\\n\\t\\r"').get_tokens_as_string()


# =============================================================================
# OPERATOR TESTS (15 tests)
# =============================================================================

class TestOperators:
    """Test operator recognition"""
    
    def test_plus(self):
        """Test plus operator"""
        assert "PLUS,+" in Tokenizer("+").get_tokens_as_string()
    
    def test_minus(self):
        """Test minus operator"""
        assert "MINUS,-" in Tokenizer("-").get_tokens_as_string()
    
    def test_multiply(self):
        """Test multiply operator"""
        assert "MULTIPLY,*" in Tokenizer("*").get_tokens_as_string()
    
    def test_divide(self):
        """Test divide operator"""
        assert "DIVIDE,/" in Tokenizer("/").get_tokens_as_string()
    
    def test_modulo(self):
        """Test modulo operator"""
        assert "MODULO,%" in Tokenizer("%").get_tokens_as_string()
    
    def test_assign(self):
        """Test assignment operator"""
        assert "ASSIGN,=" in Tokenizer("=").get_tokens_as_string()
    
    def test_equal(self):
        """Test equality operator"""
        assert "EQUAL,==" in Tokenizer("==").get_tokens_as_string()
    
    def test_not_equal(self):
        """Test not equal operator"""
        assert "NOT_EQUAL,!=" in Tokenizer("!=").get_tokens_as_string()
    
    def test_less_than(self):
        """Test less than operator"""
        assert "LESS_THAN,<" in Tokenizer("<").get_tokens_as_string()
    
    def test_less_equal(self):
        """Test less than or equal operator"""
        assert "LESS_EQUAL,<=" in Tokenizer("<=").get_tokens_as_string()
    
    def test_greater_than(self):
        """Test greater than operator"""
        assert "GREATER_THAN,>" in Tokenizer(">").get_tokens_as_string()
    
    def test_greater_equal(self):
        """Test greater than or equal operator"""
        assert "GREATER_EQUAL,>=" in Tokenizer(">=").get_tokens_as_string()
    
    def test_logical_and(self):
        """Test logical AND operator"""
        assert "LOGICAL_AND,&&" in Tokenizer("&&").get_tokens_as_string()
    
    def test_logical_or(self):
        """Test logical OR operator"""
        assert "LOGICAL_OR,||" in Tokenizer("||").get_tokens_as_string()
    
    def test_logical_not(self):
        """Test logical NOT operator"""
        assert "LOGICAL_NOT,!" in Tokenizer("!").get_tokens_as_string()


# =============================================================================
# INCREMENT/DECREMENT TESTS (4 tests)
# =============================================================================

class TestIncrementDecrement:
    """Test increment and decrement operators"""
    
    def test_increment(self):
        """Test increment operator"""
        assert "INCREMENT,++" in Tokenizer("++").get_tokens_as_string()
    
    def test_decrement(self):
        """Test decrement operator"""
        assert "DECREMENT,--" in Tokenizer("--").get_tokens_as_string()
    
    def test_increment_with_identifier(self):
        """Test prefix increment with identifier"""
        result = Tokenizer("++x").get_tokens_as_string()
        assert "INCREMENT,++" in result
        assert "IDENTIFIER,x" in result
    
    def test_postfix_increment(self):
        """Test postfix increment with identifier"""
        result = Tokenizer("x++").get_tokens_as_string()
        assert "IDENTIFIER,x" in result
        assert "INCREMENT,++" in result


# =============================================================================
# SEPARATOR TESTS (6 tests)
# =============================================================================

class TestSeparators:
    """Test separator recognition (per spec line 176: { } ( ) ; , :)"""
    
    def test_left_paren(self):
        """Test left parenthesis"""
        assert "LEFT_PAREN,(" in Tokenizer("(").get_tokens_as_string()
    
    def test_right_paren(self):
        """Test right parenthesis"""
        assert "RIGHT_PAREN,)" in Tokenizer(")").get_tokens_as_string()
    
    def test_left_brace(self):
        """Test left brace"""
        assert "LEFT_BRACE,{" in Tokenizer("{").get_tokens_as_string()
    
    def test_right_brace(self):
        """Test right brace"""
        assert "RIGHT_BRACE,}" in Tokenizer("}").get_tokens_as_string()
    
    def test_semicolon(self):
        """Test semicolon"""
        assert "SEMICOLON,;" in Tokenizer(";").get_tokens_as_string()
    
    def test_comma(self):
        """Test comma"""
        assert "COMMA,," in Tokenizer(",").get_tokens_as_string()


# =============================================================================
# DOT AND COLON TESTS (2 tests)
# =============================================================================

class TestDotColon:
    """Test dot and colon operators"""
    
    def test_dot(self):
        """Test dot operator"""
        assert "DOT,." in Tokenizer(".").get_tokens_as_string()
    
    def test_colon(self):
        """Test colon separator"""
        assert "COLON,:" in Tokenizer(":").get_tokens_as_string()


# =============================================================================
# COMMENT TESTS (8 tests)
# =============================================================================

class TestComments:
    """Test comment handling (should be skipped)"""
    
    def test_line_comment(self):
        """Test line comment is skipped"""
        result = Tokenizer("// this is a comment").get_tokens_as_string()
        assert "this" not in result
        assert "EOF" in result
    
    def test_block_comment(self):
        """Test block comment is skipped"""
        result = Tokenizer("/* block comment */").get_tokens_as_string()
        assert "block" not in result
        assert "EOF" in result
    
    def test_multiline_block_comment(self):
        """Test multiline block comment"""
        result = Tokenizer("/* line1\nline2 */").get_tokens_as_string()
        assert "line1" not in result
        assert "EOF" in result
    
    def test_code_after_line_comment(self):
        """Test code after line comment on new line"""
        result = Tokenizer("// comment\nint").get_tokens_as_string()
        assert "KEYWORD_INT,int" in result
    
    def test_code_after_block_comment(self):
        """Test code after block comment"""
        result = Tokenizer("/* comment */ int").get_tokens_as_string()
        assert "KEYWORD_INT,int" in result
    
    def test_slash_in_block_comment(self):
        """Test // inside block comment has no meaning"""
        result = Tokenizer("/* // inside */ x").get_tokens_as_string()
        assert "IDENTIFIER,x" in result
    
    def test_block_star_in_line_comment(self):
        """Test /* inside line comment has no meaning (spec line 125)"""
        result = Tokenizer("// /* this is line comment\nint").get_tokens_as_string()
        assert "KEYWORD_INT,int" in result
        assert "/*" not in result
    
    def test_unclosed_block_comment(self):
        """Test unclosed block comment (spec line 114: ignores until EOF)"""
        # Unclosed block comment should consume everything until EOF
        result = Tokenizer("/* unclosed block comment").get_tokens_as_string()
        assert "unclosed" not in result


# =============================================================================
# ERROR HANDLING TESTS (8 tests)
# =============================================================================

class TestErrorHandling:
    """Test lexer error handling"""
    
    def test_error_char_at_sign(self):
        """Test unrecognized character @"""
        with pytest.raises(Exception) as exc_info:
            Tokenizer("@").get_tokens_as_string()
        assert "Error Token @" in str(exc_info.value)
    
    def test_error_char_hash(self):
        """Test unrecognized character #"""
        with pytest.raises(Exception) as exc_info:
            Tokenizer("#").get_tokens_as_string()
        assert "Error Token #" in str(exc_info.value)
    
    def test_error_char_dollar(self):
        """Test unrecognized character $"""
        with pytest.raises(Exception) as exc_info:
            Tokenizer("$").get_tokens_as_string()
        assert "Error Token $" in str(exc_info.value)
    
    def test_unclosed_string_simple(self):
        """Test unclosed string"""
        with pytest.raises(Exception) as exc_info:
            Tokenizer('"hello').get_tokens_as_string()
        assert "Unclosed String" in str(exc_info.value)
    
    def test_unclosed_string_with_escape(self):
        """Test unclosed string with valid escape"""
        with pytest.raises(Exception) as exc_info:
            Tokenizer('"hello\\n').get_tokens_as_string()
        assert "Unclosed String" in str(exc_info.value)
    
    def test_illegal_escape_invalid_char(self):
        """Test illegal escape sequence \\x"""
        with pytest.raises(Exception) as exc_info:
            Tokenizer('"hello\\x"').get_tokens_as_string()
        assert "Illegal Escape" in str(exc_info.value)
    
    def test_illegal_escape_a(self):
        """Test illegal escape sequence \\a"""
        with pytest.raises(Exception) as exc_info:
            Tokenizer('"test\\a"').get_tokens_as_string()
        assert "Illegal Escape" in str(exc_info.value)
    
    def test_error_char_backtick(self):
        """Test unrecognized character `"""
        with pytest.raises(Exception) as exc_info:
            Tokenizer("`").get_tokens_as_string()
        assert "Error Token `" in str(exc_info.value)
    
    def test_unclosed_string_with_newline(self):
        """Test unclosed string terminated by newline (spec line 199, 228)"""
        with pytest.raises(Exception) as exc_info:
            Tokenizer('"hello\nworld"').get_tokens_as_string()
        assert "Unclosed String" in str(exc_info.value)
    
    def test_unclosed_string_with_carriage_return(self):
        """Test unclosed string terminated by carriage return (spec line 199, 228)"""
        with pytest.raises(Exception) as exc_info:
            Tokenizer('"hello\rworld"').get_tokens_as_string()
        assert "Unclosed String" in str(exc_info.value)
    
    def test_error_single_ampersand(self):
        """Test single ampersand (not valid operator)"""
        with pytest.raises(Exception) as exc_info:
            Tokenizer("&").get_tokens_as_string()
        assert "Error Token &" in str(exc_info.value)
    
    def test_error_single_pipe(self):
        """Test single pipe (not valid operator)"""
        with pytest.raises(Exception) as exc_info:
            Tokenizer("|").get_tokens_as_string()
        assert "Error Token |" in str(exc_info.value)


# =============================================================================
# WHITESPACE TESTS (6 tests)
# =============================================================================

class TestWhitespace:
    """Test whitespace handling (spec line 108: space, tab, formfeed, CR, LF)"""
    
    def test_spaces_skipped(self):
        """Test spaces are skipped"""
        result = Tokenizer("   int   ").get_tokens_as_string()
        assert "KEYWORD_INT,int" in result
    
    def test_tabs_skipped(self):
        """Test tabs are skipped"""
        result = Tokenizer("\t\tint\t\t").get_tokens_as_string()
        assert "KEYWORD_INT,int" in result
    
    def test_newlines_skipped(self):
        """Test newlines are skipped"""
        result = Tokenizer("\n\nint\n\n").get_tokens_as_string()
        assert "KEYWORD_INT,int" in result
    
    def test_mixed_whitespace(self):
        """Test mixed whitespace"""
        result = Tokenizer(" \t\n int \t\n ").get_tokens_as_string()
        assert "KEYWORD_INT,int" in result
    
    def test_formfeed_skipped(self):
        """Test formfeed is skipped (spec line 108: form feed ASCII FF)"""
        result = Tokenizer("\f\fint\f\f").get_tokens_as_string()
        assert "KEYWORD_INT,int" in result
    
    def test_carriage_return_skipped(self):
        """Test carriage return is skipped (spec line 108)"""
        result = Tokenizer("\r\rint\r\r").get_tokens_as_string()
        assert "KEYWORD_INT,int" in result
