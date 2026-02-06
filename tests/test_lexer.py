"""
Lexer test cases for TyC compiler
100 test cases covering all token types and error handling
"""

import pytest
from tests.utils import Tokenizer


# =============================================================================
# KEYWORD TESTS (16 tests)
# =============================================================================

class TestKeywords:
    """Test all 16 TyC keywords"""
    
    def test_keyword_auto(self):
        """Test 'auto' keyword"""
        assert Tokenizer("auto").get_tokens_as_string() == "auto,<EOF>"
    
    def test_keyword_break(self):
        """Test 'break' keyword"""
        assert Tokenizer("break").get_tokens_as_string() == "break,<EOF>"
    
    def test_keyword_case(self):
        """Test 'case' keyword"""
        assert Tokenizer("case").get_tokens_as_string() == "case,<EOF>"
    
    def test_keyword_continue(self):
        """Test 'continue' keyword"""
        assert Tokenizer("continue").get_tokens_as_string() == "continue,<EOF>"
    
    def test_keyword_default(self):
        """Test 'default' keyword"""
        assert Tokenizer("default").get_tokens_as_string() == "default,<EOF>"
    
    def test_keyword_else(self):
        """Test 'else' keyword"""
        assert Tokenizer("else").get_tokens_as_string() == "else,<EOF>"
    
    def test_keyword_float(self):
        """Test 'float' keyword"""
        assert Tokenizer("float").get_tokens_as_string() == "float,<EOF>"
    
    def test_keyword_for(self):
        """Test 'for' keyword"""
        assert Tokenizer("for").get_tokens_as_string() == "for,<EOF>"
    
    def test_keyword_if(self):
        """Test 'if' keyword"""
        assert Tokenizer("if").get_tokens_as_string() == "if,<EOF>"
    
    def test_keyword_int(self):
        """Test 'int' keyword"""
        assert Tokenizer("int").get_tokens_as_string() == "int,<EOF>"
    
    def test_keyword_return(self):
        """Test 'return' keyword"""
        assert Tokenizer("return").get_tokens_as_string() == "return,<EOF>"
    
    def test_keyword_string(self):
        """Test 'string' keyword"""
        assert Tokenizer("string").get_tokens_as_string() == "string,<EOF>"
    
    def test_keyword_struct(self):
        """Test 'struct' keyword"""
        assert Tokenizer("struct").get_tokens_as_string() == "struct,<EOF>"
    
    def test_keyword_switch(self):
        """Test 'switch' keyword"""
        assert Tokenizer("switch").get_tokens_as_string() == "switch,<EOF>"
    
    def test_keyword_void(self):
        """Test 'void' keyword"""
        assert Tokenizer("void").get_tokens_as_string() == "void,<EOF>"
    
    def test_keyword_while(self):
        """Test 'while' keyword"""
        assert Tokenizer("while").get_tokens_as_string() == "while,<EOF>"


# =============================================================================
# IDENTIFIER TESTS (10 tests)
# =============================================================================

class TestIdentifiers:
    """Test identifier recognition"""
    
    def test_simple_identifier(self):
        """Test simple identifier"""
        assert Tokenizer("abc").get_tokens_as_string() == "abc,<EOF>"
    
    def test_identifier_with_underscore_prefix(self):
        """Test identifier starting with underscore"""
        assert Tokenizer("_var").get_tokens_as_string() == "_var,<EOF>"
    
    def test_identifier_with_numbers(self):
        """Test identifier with numbers"""
        assert Tokenizer("var123").get_tokens_as_string() == "var123,<EOF>"
    
    def test_identifier_mixed_case(self):
        """Test identifier with mixed case"""
        assert Tokenizer("MyVariable").get_tokens_as_string() == "MyVariable,<EOF>"
    
    def test_identifier_all_uppercase(self):
        """Test identifier in all uppercase"""
        assert Tokenizer("CONSTANT").get_tokens_as_string() == "CONSTANT,<EOF>"
    
    def test_identifier_underscore_only(self):
        """Test single underscore identifier"""
        assert Tokenizer("_").get_tokens_as_string() == "_,<EOF>"
    
    def test_identifier_multiple_underscores(self):
        """Test identifier with multiple underscores"""
        assert Tokenizer("__init__").get_tokens_as_string() == "__init__,<EOF>"
    
    def test_identifier_underscore_and_digits(self):
        """Test identifier with underscore and digits"""
        assert Tokenizer("_123").get_tokens_as_string() == "_123,<EOF>"
    
    def test_identifier_long_name(self):
        """Test long identifier"""
        assert Tokenizer("veryLongVariableNameForTesting").get_tokens_as_string() == "veryLongVariableNameForTesting,<EOF>"
    
    def test_identifier_not_keyword(self):
        """Test identifier that looks like keyword prefix"""
        assert Tokenizer("integer").get_tokens_as_string() == "integer,<EOF>"


# =============================================================================
# INTEGER LITERAL TESTS (10 tests)
# =============================================================================

class TestIntegerLiterals:
    """Test integer literal recognition"""
    
    def test_single_digit(self):
        """Test single digit integer"""
        assert Tokenizer("5").get_tokens_as_string() == "5,<EOF>"
    
    def test_zero(self):
        """Test zero"""
        assert Tokenizer("0").get_tokens_as_string() == "0,<EOF>"
    
    def test_multi_digit(self):
        """Test multi-digit integer"""
        assert Tokenizer("12345").get_tokens_as_string() == "12345,<EOF>"
    
    def test_large_number(self):
        """Test large integer"""
        assert Tokenizer("999999999").get_tokens_as_string() == "999999999,<EOF>"
    
    def test_leading_zeros(self):
        """Test integer with leading zeros"""
        assert Tokenizer("007").get_tokens_as_string() == "007,<EOF>"
    
    def test_two_digit(self):
        """Test two-digit integer"""
        assert Tokenizer("42").get_tokens_as_string() == "42,<EOF>"
    
    def test_hundred(self):
        """Test one hundred"""
        assert Tokenizer("100").get_tokens_as_string() == "100,<EOF>"
    
    def test_thousand(self):
        """Test one thousand"""
        assert Tokenizer("1000").get_tokens_as_string() == "1000,<EOF>"
    
    def test_consecutive_integers(self):
        """Test consecutive integers separated by space"""
        assert Tokenizer("1 2 3").get_tokens_as_string() == "1,2,3,<EOF>"
    
    def test_integer_boundary(self):
        """Test integer boundary value"""
        assert Tokenizer("2147483647").get_tokens_as_string() == "2147483647,<EOF>"


# =============================================================================
# FLOAT LITERAL TESTS (15 tests)
# =============================================================================

class TestFloatLiterals:
    """Test float literal recognition"""
    
    def test_simple_float(self):
        """Test simple float"""
        assert Tokenizer("3.14").get_tokens_as_string() == "3.14,<EOF>"
    
    def test_zero_point_float(self):
        """Test float starting with 0."""
        assert Tokenizer("0.5").get_tokens_as_string() == "0.5,<EOF>"
    
    def test_float_no_leading_digit(self):
        """Test float without leading digit (.5)"""
        assert Tokenizer(".5").get_tokens_as_string() == ".5,<EOF>"
    
    def test_float_no_trailing_digit(self):
        """Test float without trailing digit (1.)"""
        assert Tokenizer("1.").get_tokens_as_string() == "1.,<EOF>"
    
    def test_scientific_notation_lowercase(self):
        """Test scientific notation with lowercase e"""
        assert Tokenizer("1e10").get_tokens_as_string() == "1e10,<EOF>"
    
    def test_scientific_notation_uppercase(self):
        """Test scientific notation with uppercase E"""
        assert Tokenizer("1E10").get_tokens_as_string() == "1E10,<EOF>"
    
    def test_scientific_positive_exponent(self):
        """Test scientific notation with positive exponent"""
        assert Tokenizer("1e+10").get_tokens_as_string() == "1e+10,<EOF>"
    
    def test_scientific_negative_exponent(self):
        """Test scientific notation with negative exponent"""
        assert Tokenizer("1e-10").get_tokens_as_string() == "1e-10,<EOF>"
    
    def test_float_with_exponent(self):
        """Test float with decimal and exponent"""
        assert Tokenizer("1.23e4").get_tokens_as_string() == "1.23e4,<EOF>"
    
    def test_float_zero(self):
        """Test float zero"""
        assert Tokenizer("0.0").get_tokens_as_string() == "0.0,<EOF>"
    
    def test_float_small_decimal(self):
        """Test small decimal float"""
        assert Tokenizer("0.001").get_tokens_as_string() == "0.001,<EOF>"
    
    def test_float_large_value(self):
        """Test large float value"""
        assert Tokenizer("123456.789").get_tokens_as_string() == "123456.789,<EOF>"
    
    def test_scientific_decimal_negative(self):
        """Test decimal with negative exponent"""
        assert Tokenizer("5.67E-2").get_tokens_as_string() == "5.67E-2,<EOF>"
    
    def test_dot_with_exponent(self):
        """Test .5e-2 format"""
        assert Tokenizer(".5e-2").get_tokens_as_string() == ".5e-2,<EOF>"
    
    def test_trailing_dot_with_exponent(self):
        """Test 1.e5 format"""
        assert Tokenizer("1.e5").get_tokens_as_string() == "1.e5,<EOF>"


# =============================================================================
# STRING LITERAL TESTS (12 tests)
# =============================================================================

class TestStringLiterals:
    """Test string literal recognition"""
    
    def test_empty_string(self):
        """Test empty string"""
        assert Tokenizer('""').get_tokens_as_string() == ",<EOF>"
    
    def test_simple_string(self):
        """Test simple string"""
        assert Tokenizer('"hello"').get_tokens_as_string() == "hello,<EOF>"
    
    def test_string_with_spaces(self):
        """Test string with spaces"""
        assert Tokenizer('"hello world"').get_tokens_as_string() == "hello world,<EOF>"
    
    def test_escape_backslash(self):
        """Test escape sequence backslash"""
        result = Tokenizer('"a\\\\b"').get_tokens_as_string()
        assert "a\\\\b" in result or "a\\b" in result
    
    def test_escape_newline(self):
        """Test escape sequence newline"""
        result = Tokenizer('"a\\nb"').get_tokens_as_string()
        assert "a\\nb" in result or "a\nb" in result
    
    def test_escape_tab(self):
        """Test escape sequence tab"""
        result = Tokenizer('"a\\tb"').get_tokens_as_string()
        assert "a\\tb" in result or "a\tb" in result
    
    def test_escape_quote(self):
        """Test escape sequence double quote"""
        result = Tokenizer('"a\\"b"').get_tokens_as_string()
        assert 'a\\"b' in result or 'a"b' in result
    
    def test_escape_carriage_return(self):
        """Test escape sequence carriage return"""
        result = Tokenizer('"a\\rb"').get_tokens_as_string()
        assert "a\\rb" in result or "a\rb" in result
    
    def test_escape_backspace(self):
        """Test escape sequence backspace"""
        result = Tokenizer('"a\\bb"').get_tokens_as_string()
        assert "a\\bb" in result or "a\bb" in result
    
    def test_escape_formfeed(self):
        """Test escape sequence formfeed"""
        result = Tokenizer('"a\\fb"').get_tokens_as_string()
        assert "a\\fb" in result or "a\fb" in result
    
    def test_string_with_numbers(self):
        """Test string containing numbers"""
        assert Tokenizer('"test123"').get_tokens_as_string() == "test123,<EOF>"
    
    def test_multiple_escapes(self):
        """Test string with multiple escape sequences"""
        result = Tokenizer('"\\n\\t\\r"').get_tokens_as_string()
        assert "<EOF>" in result


# =============================================================================
# OPERATOR TESTS (15 tests)
# =============================================================================

class TestOperators:
    """Test operator recognition"""
    
    def test_plus(self):
        """Test plus operator"""
        assert Tokenizer("+").get_tokens_as_string() == "+,<EOF>"
    
    def test_minus(self):
        """Test minus operator"""
        assert Tokenizer("-").get_tokens_as_string() == "-,<EOF>"
    
    def test_multiply(self):
        """Test multiply operator"""
        assert Tokenizer("*").get_tokens_as_string() == "*,<EOF>"
    
    def test_divide(self):
        """Test divide operator"""
        assert Tokenizer("/").get_tokens_as_string() == "/,<EOF>"
    
    def test_modulo(self):
        """Test modulo operator"""
        assert Tokenizer("%").get_tokens_as_string() == "%,<EOF>"
    
    def test_assign(self):
        """Test assignment operator"""
        assert Tokenizer("=").get_tokens_as_string() == "=,<EOF>"
    
    def test_equal(self):
        """Test equality operator"""
        assert Tokenizer("==").get_tokens_as_string() == "==,<EOF>"
    
    def test_not_equal(self):
        """Test not equal operator"""
        assert Tokenizer("!=").get_tokens_as_string() == "!=,<EOF>"
    
    def test_less_than(self):
        """Test less than operator"""
        assert Tokenizer("<").get_tokens_as_string() == "<,<EOF>"
    
    def test_less_equal(self):
        """Test less than or equal operator"""
        assert Tokenizer("<=").get_tokens_as_string() == "<=,<EOF>"
    
    def test_greater_than(self):
        """Test greater than operator"""
        assert Tokenizer(">").get_tokens_as_string() == ">,<EOF>"
    
    def test_greater_equal(self):
        """Test greater than or equal operator"""
        assert Tokenizer(">=").get_tokens_as_string() == ">=,<EOF>"
    
    def test_logical_and(self):
        """Test logical AND operator"""
        assert Tokenizer("&&").get_tokens_as_string() == "&&,<EOF>"
    
    def test_logical_or(self):
        """Test logical OR operator"""
        assert Tokenizer("||").get_tokens_as_string() == "||,<EOF>"
    
    def test_logical_not(self):
        """Test logical NOT operator"""
        assert Tokenizer("!").get_tokens_as_string() == "!,<EOF>"


# =============================================================================
# INCREMENT/DECREMENT TESTS (4 tests)
# =============================================================================

class TestIncrementDecrement:
    """Test increment and decrement operators"""
    
    def test_increment(self):
        """Test increment operator"""
        assert Tokenizer("++").get_tokens_as_string() == "++,<EOF>"
    
    def test_decrement(self):
        """Test decrement operator"""
        assert Tokenizer("--").get_tokens_as_string() == "--,<EOF>"
    
    def test_increment_with_identifier(self):
        """Test prefix increment with identifier"""
        assert Tokenizer("++x").get_tokens_as_string() == "++,x,<EOF>"
    
    def test_postfix_increment(self):
        """Test postfix increment with identifier"""
        assert Tokenizer("x++").get_tokens_as_string() == "x,++,<EOF>"


# =============================================================================
# SEPARATOR TESTS (6 tests)
# =============================================================================

class TestSeparators:
    """Test separator recognition (per spec line 176: { } ( ) ; , :)"""
    
    def test_left_paren(self):
        """Test left parenthesis"""
        assert Tokenizer("(").get_tokens_as_string() == "(,<EOF>"
    
    def test_right_paren(self):
        """Test right parenthesis"""
        assert Tokenizer(")").get_tokens_as_string() == "),<EOF>"
    
    def test_left_brace(self):
        """Test left brace"""
        assert Tokenizer("{").get_tokens_as_string() == "{,<EOF>"
    
    def test_right_brace(self):
        """Test right brace"""
        assert Tokenizer("}").get_tokens_as_string() == "},<EOF>"
    
    def test_semicolon(self):
        """Test semicolon"""
        assert Tokenizer(";").get_tokens_as_string() == ";,<EOF>"
    
    def test_comma(self):
        """Test comma"""
        assert Tokenizer(",").get_tokens_as_string() == ",,<EOF>"


# =============================================================================
# DOT AND COLON TESTS (2 tests)
# =============================================================================

class TestDotColon:
    """Test dot and colon operators"""
    
    def test_dot(self):
        """Test dot operator"""
        assert Tokenizer(".").get_tokens_as_string() == ".,<EOF>"
    
    def test_colon(self):
        """Test colon separator"""
        assert Tokenizer(":").get_tokens_as_string() == ":,<EOF>"


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
        assert "int" in result
    
    def test_code_after_block_comment(self):
        """Test code after block comment"""
        result = Tokenizer("/* comment */ int").get_tokens_as_string()
        assert "int" in result
    
    def test_slash_in_block_comment(self):
        """Test // inside block comment has no meaning"""
        result = Tokenizer("/* // inside */ x").get_tokens_as_string()
        assert "x" in result
    
    def test_block_star_in_line_comment(self):
        """Test /* inside line comment has no meaning (spec line 125)"""
        result = Tokenizer("// /* this is line comment\nint").get_tokens_as_string()
        assert "int" in result
        assert "/*" not in result
    
    def test_unclosed_block_comment(self):
        """Test unclosed block comment (spec line 114: ignores until EOF)"""
        result = Tokenizer("/* unclosed block comment").get_tokens_as_string()
        assert "unclosed" not in result


# =============================================================================
# ERROR HANDLING TESTS (12 tests)
# =============================================================================

class TestErrorHandling:
    """Test lexer error handling"""
    
    def test_error_char_at_sign(self):
        """Test unrecognized character @"""
        result = Tokenizer("@").get_tokens_as_string()
        assert "Error Token @" in result
    
    def test_error_char_hash(self):
        """Test unrecognized character #"""
        result = Tokenizer("#").get_tokens_as_string()
        assert "Error Token #" in result
    
    def test_error_char_dollar(self):
        """Test unrecognized character $"""
        result = Tokenizer("$").get_tokens_as_string()
        assert "Error Token $" in result
    
    def test_unclosed_string_simple(self):
        """Test unclosed string"""
        result = Tokenizer('"hello').get_tokens_as_string()
        assert "Unclosed String" in result
    
    def test_unclosed_string_with_escape(self):
        """Test unclosed string with valid escape"""
        result = Tokenizer('"hello\\n').get_tokens_as_string()
        assert "Unclosed String" in result
    
    def test_illegal_escape_invalid_char(self):
        """Test illegal escape sequence \\x"""
        result = Tokenizer('"hello\\x"').get_tokens_as_string()
        assert "Illegal Escape" in result
    
    def test_illegal_escape_a(self):
        """Test illegal escape sequence \\a"""
        result = Tokenizer('"test\\a"').get_tokens_as_string()
        assert "Illegal Escape" in result
    
    def test_error_char_backtick(self):
        """Test unrecognized character `"""
        result = Tokenizer("`").get_tokens_as_string()
        assert "Error Token `" in result
    
    def test_unclosed_string_with_newline(self):
        """Test unclosed string terminated by newline (spec line 199, 228)"""
        result = Tokenizer('"hello\nworld"').get_tokens_as_string()
        assert "Unclosed String" in result
    
    def test_unclosed_string_with_carriage_return(self):
        """Test unclosed string terminated by carriage return (spec line 199, 228)"""
        result = Tokenizer('"hello\rworld"').get_tokens_as_string()
        assert "Unclosed String" in result
    
    def test_error_single_ampersand(self):
        """Test single ampersand (not valid operator)"""
        result = Tokenizer("&").get_tokens_as_string()
        assert "Error Token &" in result
    
    def test_error_single_pipe(self):
        """Test single pipe (not valid operator)"""
        result = Tokenizer("|").get_tokens_as_string()
        assert "Error Token |" in result



# =============================================================================
# WHITESPACE TESTS (6 tests)
# =============================================================================

class TestWhitespace:
    """Test whitespace handling (spec line 108: space, tab, formfeed, CR, LF)"""
    
    def test_spaces_skipped(self):
        """Test spaces are skipped"""
        assert Tokenizer("   int   ").get_tokens_as_string() == "int,<EOF>"
    
    def test_tabs_skipped(self):
        """Test tabs are skipped"""
        assert Tokenizer("\t\tint\t\t").get_tokens_as_string() == "int,<EOF>"
    
    def test_newlines_skipped(self):
        """Test newlines are skipped"""
        assert Tokenizer("\n\nint\n\n").get_tokens_as_string() == "int,<EOF>"
    
    def test_mixed_whitespace(self):
        """Test mixed whitespace"""
        assert Tokenizer(" \t\n int \t\n ").get_tokens_as_string() == "int,<EOF>"
    
    def test_formfeed_skipped(self):
        """Test formfeed is skipped (spec line 108: form feed ASCII FF)"""
        assert Tokenizer("\f\fint\f\f").get_tokens_as_string() == "int,<EOF>"
    
    def test_carriage_return_skipped(self):
        """Test carriage return is skipped (spec line 108)"""
        assert Tokenizer("\r\rint\r\r").get_tokens_as_string() == "int,<EOF>"


# =============================================================================
# COMPLEX EXPRESSION TESTS (4 tests)
# =============================================================================

class TestComplexExpressions:
    """Test tokenization of complex expressions"""
    
    def test_integer_in_expression(self):
        """Test integers and operator together"""
        assert Tokenizer("5+10").get_tokens_as_string() == "5,+,10,<EOF>"
    
    def test_variable_declaration(self):
        """Test variable declaration tokenization"""
        assert Tokenizer("auto x = 5 + 3 * 2;").get_tokens_as_string() == "auto,x,=,5,+,3,*,2,;,<EOF>"
    
    def test_function_call(self):
        """Test function call tokenization"""
        assert Tokenizer("foo(x, y)").get_tokens_as_string() == "foo,(,x,,,y,),<EOF>"
    
    def test_member_access(self):
        """Test member access tokenization"""
        assert Tokenizer("p.x").get_tokens_as_string() == "p,.,x,<EOF>"


# =============================================================================
# ADDITIONAL ILLEGAL ESCAPE TESTS (8 tests) - Gap Coverage
# =============================================================================

class TestIllegalEscapeSequences:
    """Additional illegal escape sequence tests per spec lines 217-233"""
    
    def test_illegal_escape_zero(self):
        """Test illegal escape sequence \\0"""
        result = Tokenizer('"test\\0"').get_tokens_as_string()
        assert "Illegal Escape" in result
    
    def test_illegal_escape_v(self):
        """Test illegal escape sequence \\v (vertical tab not supported)"""
        result = Tokenizer('"test\\v"').get_tokens_as_string()
        assert "Illegal Escape" in result
    
    def test_illegal_escape_hex(self):
        """Test illegal escape sequence \\x41 (hex not supported per spec)"""
        result = Tokenizer('"\\x41"').get_tokens_as_string()
        assert "Illegal Escape" in result
    
    def test_illegal_escape_octal(self):
        """Test illegal escape sequence \\123 (octal not supported)"""
        result = Tokenizer('"\\123"').get_tokens_as_string()
        assert "Illegal Escape" in result
    
    def test_illegal_escape_unicode(self):
        """Test illegal escape sequence \\u0041 (unicode not supported)"""
        result = Tokenizer('"\\u0041"').get_tokens_as_string()
        assert "Illegal Escape" in result
    
    def test_illegal_escape_capital_N(self):
        """Test illegal escape sequence \\N"""
        result = Tokenizer('"test\\N"').get_tokens_as_string()
        assert "Illegal Escape" in result
    
    def test_illegal_escape_s(self):
        """Test illegal escape sequence \\s"""
        result = Tokenizer('"test\\s"').get_tokens_as_string()
        assert "Illegal Escape" in result
    
    def test_illegal_escape_c(self):
        """Test illegal escape sequence \\c"""
        result = Tokenizer('"test\\c"').get_tokens_as_string()
        assert "Illegal Escape" in result


# =============================================================================
# KEYWORD EDGE CASES (4 tests) - Gap Coverage
# =============================================================================

class TestKeywordEdgeCases:
    """Test keyword edge cases per spec lines 139-146"""
    
    def test_keyword_as_prefix(self):
        """Test 'autoVar' is identifier, not keyword + identifier"""
        assert Tokenizer("autoVar").get_tokens_as_string() == "autoVar,<EOF>"
    
    def test_keyword_as_suffix(self):
        """Test 'myauto' is identifier, not identifier + keyword"""
        assert Tokenizer("myauto").get_tokens_as_string() == "myauto,<EOF>"
    
    def test_keyword_uppercase_not_keyword(self):
        """Test 'AUTO' is identifier due to case sensitivity"""
        assert Tokenizer("AUTO").get_tokens_as_string() == "AUTO,<EOF>"
    
    def test_keyword_mixed_case_not_keyword(self):
        """Test 'Auto' is identifier due to case sensitivity"""
        assert Tokenizer("Auto").get_tokens_as_string() == "Auto,<EOF>"


# =============================================================================
# ADDITIONAL COMMENT TESTS (3 tests) - Gap Coverage
# =============================================================================

class TestCommentEdgeCases:
    """Additional comment edge cases"""
    
    def test_empty_block_comment(self):
        """Test empty block comment /**/"""
        result = Tokenizer("/**/x").get_tokens_as_string()
        assert "x" in result
        assert "<EOF>" in result
    
    def test_block_comment_extra_stars(self):
        """Test block comment with extra stars /*** ***/"""
        result = Tokenizer("/*** content ***/x").get_tokens_as_string()
        assert "x" in result
        assert "content" not in result
    
    def test_block_comment_with_nested_start(self):
        """Test /* outer /* inner */ - non-nested per spec"""
        result = Tokenizer("/* outer /* inner */ x").get_tokens_as_string()
        assert "x" in result


# =============================================================================
# OPERATOR SEQUENCE TESTS (4 tests) - Gap Coverage
# =============================================================================

class TestOperatorSequences:
    """Test operator tokenization sequences"""
    
    def test_triple_equals(self):
        """Test === is tokenized as == followed by ="""
        result = Tokenizer("===").get_tokens_as_string()
        assert "==" in result
        assert "=" in result
    
    def test_increment_decrement_sequence(self):
        """Test ++-- is two operators"""
        assert Tokenizer("++--").get_tokens_as_string() == "++,--,<EOF>"
    
    def test_not_equal_vs_not_assign(self):
        """Test != vs ! = distinction"""
        assert Tokenizer("!=").get_tokens_as_string() == "!=,<EOF>"
        assert Tokenizer("! =").get_tokens_as_string() == "!,=,<EOF>"
    
    def test_less_equal_vs_less_assign(self):
        """Test <= vs < = distinction"""
        assert Tokenizer("<=").get_tokens_as_string() == "<=,<EOF>"
        assert Tokenizer("< =").get_tokens_as_string() == "<,=,<EOF>"
