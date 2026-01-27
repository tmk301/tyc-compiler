"""
Parser test cases for TyC compiler
100 test cases covering all grammar rules
"""

import pytest
from tests.utils import Parser


# =============================================================================
# PROGRAM STRUCTURE TESTS (5 tests)
# =============================================================================

class TestProgramStructure:
    """Test program structure"""
    
    def test_empty_program(self):
        """Test empty program"""
        assert Parser("").parse() == "success"
    
    def test_single_function(self):
        """Test single function program"""
        assert Parser("void main() {}").parse() == "success"
    
    def test_multiple_functions(self):
        """Test multiple functions"""
        source = """
        int add(int x, int y) { return x + y; }
        void main() {}
        """
        assert Parser(source).parse() == "success"
    
    def test_struct_and_function(self):
        """Test struct and function together"""
        source = """
        struct Point { int x; int y; };
        void main() {}
        """
        assert Parser(source).parse() == "success"
    
    def test_multiple_structs_and_functions(self):
        """Test multiple structs and functions"""
        source = """
        struct Point { int x; int y; };
        struct Rect { int w; int h; };
        int area(int w, int h) { return w * h; }
        void main() {}
        """
        assert Parser(source).parse() == "success"


# =============================================================================
# STRUCT DECLARATION TESTS (8 tests)
# =============================================================================

class TestStructDeclarations:
    """Test struct declarations"""
    
    def test_empty_struct(self):
        """Test empty struct (no members)"""
        assert Parser("struct Empty {};").parse() == "success"
    
    def test_single_member_struct(self):
        """Test struct with single member"""
        assert Parser("struct Point { int x; };").parse() == "success"
    
    def test_multiple_members_struct(self):
        """Test struct with multiple members"""
        source = "struct Person { string name; int age; float height; };"
        assert Parser(source).parse() == "success"
    
    def test_struct_with_int_member(self):
        """Test struct with int member"""
        assert Parser("struct S { int value; };").parse() == "success"
    
    def test_struct_with_float_member(self):
        """Test struct with float member"""
        assert Parser("struct S { float value; };").parse() == "success"
    
    def test_struct_with_string_member(self):
        """Test struct with string member"""
        assert Parser("struct S { string value; };").parse() == "success"
    
    def test_struct_member_same_type(self):
        """Test struct with members of same type"""
        assert Parser("struct Point { int x; int y; int z; };").parse() == "success"
    
    def test_struct_with_struct_member(self):
        """Test struct with another struct type member"""
        source = """
        struct Point { int x; int y; };
        struct Line { Point start; Point end; };
        """
        assert Parser(source).parse() == "success"


# =============================================================================
# FUNCTION DECLARATION TESTS (12 tests)
# =============================================================================

class TestFunctionDeclarations:
    """Test function declarations"""
    
    def test_void_function(self):
        """Test void function"""
        assert Parser("void foo() {}").parse() == "success"
    
    def test_int_function(self):
        """Test int return type function"""
        assert Parser("int foo() { return 0; }").parse() == "success"
    
    def test_float_function(self):
        """Test float return type function"""
        assert Parser("float foo() { return 0.0; }").parse() == "success"
    
    def test_string_function(self):
        """Test string return type function"""
        assert Parser('string foo() { return "hello"; }').parse() == "success"
    
    def test_function_no_return_type(self):
        """Test function without return type (inferred)"""
        assert Parser("foo() { return 0; }").parse() == "success"
    
    def test_function_one_parameter(self):
        """Test function with one parameter"""
        assert Parser("void foo(int x) {}").parse() == "success"
    
    def test_function_multiple_parameters(self):
        """Test function with multiple parameters"""
        assert Parser("void foo(int x, float y, string z) {}").parse() == "success"
    
    def test_function_struct_parameter(self):
        """Test function with struct parameter"""
        source = """
        struct Point { int x; int y; };
        void draw(Point p) {}
        """
        assert Parser(source).parse() == "success"
    
    def test_function_struct_return_type(self):
        """Test function with struct return type"""
        source = """
        struct Point { int x; int y; };
        Point createPoint() { Point p; return p; }
        """
        assert Parser(source).parse() == "success"
    
    def test_main_function(self):
        """Test main function"""
        assert Parser("void main() {}").parse() == "success"
    
    def test_function_with_body(self):
        """Test function with statements"""
        source = """
        int add(int a, int b) {
            auto sum = a + b;
            return sum;
        }
        """
        assert Parser(source).parse() == "success"
    
    def test_function_with_multiple_statements(self):
        """Test function with multiple statements"""
        source = """
        void foo() {
            int x = 1;
            int y = 2;
            int z = x + y;
        }
        """
        assert Parser(source).parse() == "success"


# =============================================================================
# VARIABLE DECLARATION TESTS (12 tests)
# =============================================================================

class TestVariableDeclarations:
    """Test variable declarations"""
    
    def test_auto_with_int(self):
        """Test auto with int initialization"""
        assert Parser("void f() { auto x = 10; }").parse() == "success"
    
    def test_auto_with_float(self):
        """Test auto with float initialization"""
        assert Parser("void f() { auto x = 3.14; }").parse() == "success"
    
    def test_auto_with_string(self):
        """Test auto with string initialization"""
        assert Parser('void f() { auto x = "hello"; }').parse() == "success"
    
    def test_auto_without_init(self):
        """Test auto without initialization"""
        assert Parser("void f() { auto x; }").parse() == "success"
    
    def test_int_declaration(self):
        """Test int variable declaration"""
        assert Parser("void f() { int x = 10; }").parse() == "success"
    
    def test_float_declaration(self):
        """Test float variable declaration"""
        assert Parser("void f() { float x = 3.14; }").parse() == "success"
    
    def test_string_declaration(self):
        """Test string variable declaration"""
        assert Parser('void f() { string x = "hello"; }').parse() == "success"
    
    def test_int_without_init(self):
        """Test int without initialization"""
        assert Parser("void f() { int x; }").parse() == "success"
    
    def test_struct_var_without_init(self):
        """Test struct variable without initialization"""
        source = """
        struct Point { int x; int y; };
        void f() { Point p; }
        """
        assert Parser(source).parse() == "success"
    
    def test_struct_var_with_init(self):
        """Test struct variable with initialization"""
        source = """
        struct Point { int x; int y; };
        void f() { Point p = {1, 2}; }
        """
        assert Parser(source).parse() == "success"
    
    def test_struct_var_empty_init(self):
        """Test struct variable with empty init list"""
        source = """
        struct Empty {};
        void f() { Empty e = {}; }
        """
        assert Parser(source).parse() == "success"
    
    def test_auto_with_expression(self):
        """Test auto with expression initialization"""
        assert Parser("void f() { auto x = 1 + 2 * 3; }").parse() == "success"


# =============================================================================
# ASSIGNMENT STATEMENT TESTS (6 tests)
# =============================================================================

class TestAssignmentStatements:
    """Test assignment statements"""
    
    def test_simple_assignment(self):
        """Test simple assignment"""
        assert Parser("void f() { int x; x = 10; }").parse() == "success"
    
    def test_assignment_with_expression(self):
        """Test assignment with expression"""
        assert Parser("void f() { int x; x = 1 + 2; }").parse() == "success"
    
    def test_member_assignment(self):
        """Test struct member assignment"""
        source = """
        struct Point { int x; int y; };
        void f() { Point p; p.x = 10; }
        """
        assert Parser(source).parse() == "success"
    
    def test_nested_member_assignment(self):
        """Test nested struct member assignment"""
        source = """
        struct Point { int x; int y; };
        struct Line { Point start; Point end; };
        void f() { Line l; l.start.x = 10; }
        """
        assert Parser(source).parse() == "success"
    
    def test_chain_member_access(self):
        """Test chain member access"""
        source = """
        struct A { int val; };
        struct B { A a; };
        struct C { B b; };
        void f() { C c; c.b.a.val = 5; }
        """
        assert Parser(source).parse() == "success"
    
    def test_assignment_to_variable(self):
        """Test assignment from variable"""
        assert Parser("void f() { int x; int y; y = x; }").parse() == "success"


# =============================================================================
# IF STATEMENT TESTS (8 tests)
# =============================================================================

class TestIfStatements:
    """Test if statements"""
    
    def test_simple_if(self):
        """Test simple if statement"""
        assert Parser("void f() { if (1) x = 1; }").parse() == "success"
    
    def test_if_with_block(self):
        """Test if with block"""
        assert Parser("void f() { if (1) { x = 1; } }").parse() == "success"
    
    def test_if_else(self):
        """Test if-else statement"""
        assert Parser("void f() { if (1) x = 1; else x = 2; }").parse() == "success"
    
    def test_if_else_blocks(self):
        """Test if-else with blocks"""
        assert Parser("void f() { if (1) { x = 1; } else { x = 2; } }").parse() == "success"
    
    def test_nested_if(self):
        """Test nested if"""
        assert Parser("void f() { if (1) if (2) x = 1; }").parse() == "success"
    
    def test_if_with_comparison(self):
        """Test if with comparison expression"""
        assert Parser("void f() { int x; if (x > 0) x = 1; }").parse() == "success"
    
    def test_if_with_logical_and(self):
        """Test if with logical AND"""
        assert Parser("void f() { if (1 && 2) x = 1; }").parse() == "success"
    
    def test_if_with_logical_or(self):
        """Test if with logical OR"""
        assert Parser("void f() { if (1 || 0) x = 1; }").parse() == "success"


# =============================================================================
# WHILE STATEMENT TESTS (5 tests)
# =============================================================================

class TestWhileStatements:
    """Test while statements"""
    
    def test_simple_while(self):
        """Test simple while"""
        assert Parser("void f() { while (1) x = 1; }").parse() == "success"
    
    def test_while_with_block(self):
        """Test while with block"""
        assert Parser("void f() { while (1) { x = 1; } }").parse() == "success"
    
    def test_while_with_condition(self):
        """Test while with condition"""
        assert Parser("void f() { int i; while (i < 10) i = i + 1; }").parse() == "success"
    
    def test_nested_while(self):
        """Test nested while"""
        assert Parser("void f() { while (1) while (2) x = 1; }").parse() == "success"
    
    def test_while_with_break(self):
        """Test while with break"""
        assert Parser("void f() { while (1) { break; } }").parse() == "success"


# =============================================================================
# FOR STATEMENT TESTS (10 tests)
# =============================================================================

class TestForStatements:
    """Test for statements"""
    
    def test_complete_for(self):
        """Test complete for loop"""
        assert Parser("void f() { for (auto i = 0; i < 10; i++) x = 1; }").parse() == "success"
    
    def test_for_with_block(self):
        """Test for with block"""
        assert Parser("void f() { for (auto i = 0; i < 10; i++) { x = 1; } }").parse() == "success"
    
    def test_for_empty_init(self):
        """Test for with empty init"""
        assert Parser("void f() { for (; 1; ) x = 1; }").parse() == "success"
    
    def test_for_empty_condition(self):
        """Test for with empty condition"""
        assert Parser("void f() { for (auto i = 0;; i++) x = 1; }").parse() == "success"
    
    def test_for_empty_update(self):
        """Test for with empty update"""
        assert Parser("void f() { for (auto i = 0; i < 10;) x = 1; }").parse() == "success"
    
    def test_for_all_empty(self):
        """Test for with all parts empty"""
        assert Parser("void f() { for (;;) x = 1; }").parse() == "success"
    
    def test_for_with_int_init(self):
        """Test for with int variable init"""
        assert Parser("void f() { for (int i = 0; i < 10; i++) x = 1; }").parse() == "success"
    
    def test_for_with_decrement(self):
        """Test for with decrement update"""
        assert Parser("void f() { for (auto i = 10; i > 0; i--) x = 1; }").parse() == "success"
    
    def test_for_with_prefix_increment(self):
        """Test for with prefix increment"""
        assert Parser("void f() { for (auto i = 0; i < 10; ++i) x = 1; }").parse() == "success"
    
    def test_for_with_assignment_update(self):
        """Test for with assignment in update"""
        assert Parser("void f() { for (auto i = 0; i < 10; i = i + 1) x = 1; }").parse() == "success"


# =============================================================================
# SWITCH STATEMENT TESTS (8 tests)
# =============================================================================

class TestSwitchStatements:
    """Test switch statements"""
    
    def test_simple_switch(self):
        """Test simple switch"""
        source = "void f() { switch (x) { case 1: break; } }"
        assert Parser(source).parse() == "success"
    
    def test_switch_multiple_cases(self):
        """Test switch with multiple cases"""
        source = """
        void f() {
            switch (x) {
                case 1: x = 1;
                case 2: x = 2;
            }
        }
        """
        assert Parser(source).parse() == "success"
    
    def test_switch_with_default(self):
        """Test switch with default"""
        source = """
        void f() {
            switch (x) {
                case 1: x = 1;
                default: x = 0;
            }
        }
        """
        assert Parser(source).parse() == "success"
    
    def test_switch_only_default(self):
        """Test switch with only default"""
        source = "void f() { switch (x) { default: x = 0; } }"
        assert Parser(source).parse() == "success"
    
    def test_switch_empty_case(self):
        """Test switch with empty case"""
        source = "void f() { switch (x) { case 1: } }"
        assert Parser(source).parse() == "success"
    
    def test_switch_case_with_break(self):
        """Test switch case with break"""
        source = """
        void f() {
            switch (x) {
                case 1: x = 1; break;
                case 2: x = 2; break;
            }
        }
        """
        assert Parser(source).parse() == "success"
    
    def test_switch_multiple_statements(self):
        """Test switch case with multiple statements"""
        source = """
        void f() {
            switch (x) {
                case 1:
                    x = 1;
                    y = 2;
                    break;
            }
        }
        """
        assert Parser(source).parse() == "success"
    
    def test_empty_switch(self):
        """Test empty switch body"""
        assert Parser("void f() { switch (x) {} }").parse() == "success"


# =============================================================================
# BREAK/CONTINUE/RETURN TESTS (6 tests)
# =============================================================================

class TestControlFlow:
    """Test control flow statements"""
    
    def test_break_in_while(self):
        """Test break in while"""
        assert Parser("void f() { while (1) break; }").parse() == "success"
    
    def test_continue_in_while(self):
        """Test continue in while"""
        assert Parser("void f() { while (1) continue; }").parse() == "success"
    
    def test_break_in_for(self):
        """Test break in for"""
        assert Parser("void f() { for (;;) break; }").parse() == "success"
    
    def test_return_void(self):
        """Test return without value"""
        assert Parser("void f() { return; }").parse() == "success"
    
    def test_return_value(self):
        """Test return with value"""
        assert Parser("int f() { return 42; }").parse() == "success"
    
    def test_return_expression(self):
        """Test return with expression"""
        assert Parser("int f() { return 1 + 2 * 3; }").parse() == "success"


# =============================================================================
# EXPRESSION TESTS (15 tests)
# =============================================================================

class TestExpressions:
    """Test expressions"""
    
    def test_arithmetic_add(self):
        """Test addition"""
        assert Parser("void f() { auto x = 1 + 2; }").parse() == "success"
    
    def test_arithmetic_sub(self):
        """Test subtraction"""
        assert Parser("void f() { auto x = 5 - 3; }").parse() == "success"
    
    def test_arithmetic_mul(self):
        """Test multiplication"""
        assert Parser("void f() { auto x = 2 * 3; }").parse() == "success"
    
    def test_arithmetic_div(self):
        """Test division"""
        assert Parser("void f() { auto x = 10 / 2; }").parse() == "success"
    
    def test_arithmetic_mod(self):
        """Test modulo"""
        assert Parser("void f() { auto x = 10 % 3; }").parse() == "success"
    
    def test_precedence_mul_over_add(self):
        """Test precedence: multiplication over addition"""
        assert Parser("void f() { auto x = 1 + 2 * 3; }").parse() == "success"
    
    def test_parentheses(self):
        """Test parentheses"""
        assert Parser("void f() { auto x = (1 + 2) * 3; }").parse() == "success"
    
    def test_function_call(self):
        """Test function call"""
        source = """
        int foo() { return 1; }
        void main() { auto x = foo(); }
        """
        assert Parser(source).parse() == "success"
    
    def test_function_call_with_args(self):
        """Test function call with arguments"""
        source = """
        int add(int a, int b) { return a + b; }
        void main() { auto x = add(1, 2); }
        """
        assert Parser(source).parse() == "success"
    
    def test_unary_minus(self):
        """Test unary minus"""
        assert Parser("void f() { auto x = -5; }").parse() == "success"
    
    def test_unary_plus(self):
        """Test unary plus"""
        assert Parser("void f() { auto x = +5; }").parse() == "success"
    
    def test_unary_not(self):
        """Test unary not"""
        assert Parser("void f() { auto x = !0; }").parse() == "success"
    
    def test_member_access(self):
        """Test member access"""
        source = """
        struct Point { int x; int y; };
        void f() { Point p; auto v = p.x; }
        """
        assert Parser(source).parse() == "success"
    
    def test_relational_expression(self):
        """Test relational expression"""
        assert Parser("void f() { auto x = 1 < 2; }").parse() == "success"
    
    def test_complex_expression(self):
        """Test complex expression"""
        assert Parser("void f() { auto x = (1 + 2) * 3 - 4 / 2 % 3; }").parse() == "success"


# =============================================================================
# SYNTAX ERROR TESTS (5 tests)
# =============================================================================

class TestSyntaxErrors:
    """Test syntax error detection"""
    
    def test_missing_semicolon(self):
        """Test missing semicolon"""
        result = Parser("void f() { int x }").parse()
        assert result != "success"
    
    def test_missing_closing_brace(self):
        """Test missing closing brace"""
        result = Parser("void f() { int x;").parse()
        assert result != "success"
    
    def test_missing_closing_paren(self):
        """Test missing closing parenthesis"""
        result = Parser("void f( { }").parse()
        assert result != "success"
    
    def test_invalid_statement(self):
        """Test invalid statement"""
        result = Parser("void f() { struct; }").parse()
        assert result != "success"
    
    def test_missing_expression(self):
        """Test missing expression in return"""
        result = Parser("int f() { return; }").parse()
        # This is actually valid for void inference, so test different case
        result = Parser("void f() { if () x = 1; }").parse()
        assert result != "success"
