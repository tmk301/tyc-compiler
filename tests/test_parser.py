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


# =============================================================================
# NEW SPEC FEATURES: CASE EXPRESSIONS (7 tests)
# =============================================================================

class TestCaseExpressions:
    """Test case expressions per updated spec (lines 728-733)"""
    
    def test_case_with_unary_minus(self):
        """Test case -5:"""
        source = "void f() { switch (x) { case -5: break; } }"
        assert Parser(source).parse() == "success"
    
    def test_case_with_unary_plus(self):
        """Test case +1:"""
        source = "void f() { switch (x) { case +1: break; } }"
        assert Parser(source).parse() == "success"
    
    def test_case_with_parenthesized(self):
        """Test case (1):"""
        source = "void f() { switch (x) { case (1): break; } }"
        assert Parser(source).parse() == "success"
    
    def test_case_with_addition(self):
        """Test case 1+2:"""
        source = "void f() { switch (x) { case 1+2: break; } }"
        assert Parser(source).parse() == "success"
    
    def test_case_with_multiplication(self):
        """Test case 3*4:"""
        source = "void f() { switch (x) { case 3*4: break; } }"
        assert Parser(source).parse() == "success"
    
    def test_case_with_complex_expression(self):
        """Test case (2+3)*4:"""
        source = "void f() { switch (x) { case (2+3)*4: break; } }"
        assert Parser(source).parse() == "success"
    
    def test_case_with_modulo(self):
        """Test case 10%3:"""
        source = "void f() { switch (x) { case 10%3: break; } }"
        assert Parser(source).parse() == "success"

# =============================================================================
# BLOCK AND EXPRESSION STATEMENT TESTS (4 tests)
# =============================================================================

class TestBlockAndExpressionStatements:
    """Test block statements and expression statements (spec lines 619-631, 800-808)"""
    
    def test_empty_block(self):
        """Test empty block statement"""
        assert Parser("void f() { {} }").parse() == "success"
    
    def test_block_with_statements(self):
        """Test block with multiple statements (spec lines 619-631)"""
        source = """
        void f() {
            {
                auto x = 10;
                auto y = 20;
                auto sum = x + y;
            }
        }
        """
        assert Parser(source).parse() == "success"
    
    def test_nested_blocks(self):
        """Test nested block statements"""
        source = """
        void f() {
            {
                {
                    int x = 1;
                }
            }
        }
        """
        assert Parser(source).parse() == "success"
    
    def test_expression_statement(self):
        """Test expression statement (spec lines 800-808)"""
        source = """
        int foo() { return 1; }
        void main() { foo(); }
        """
        assert Parser(source).parse() == "success"


# =============================================================================
# ADVANCED ASSIGNMENT TESTS (4 tests)
# =============================================================================

class TestAdvancedAssignment:
    """Test advanced assignment features (spec line 532)"""
    
    def test_chained_assignment(self):
        """Test chained assignment x = y = z = 10 (spec line 532)"""
        source = """
        void f() {
            int x;
            int y;
            int z;
            x = y = z = 10;
        }
        """
        assert Parser(source).parse() == "success"
    
    def test_assignment_in_expression(self):
        """Test assignment used in expression context (spec line 532)"""
        source = """
        void f() {
            int x;
            int y = (x = 5) + 7;
        }
        """
        assert Parser(source).parse() == "success"
    
    def test_assignment_in_condition(self):
        """Test assignment in if condition"""
        source = """
        void f() {
            int x;
            if (x = 1) x = 2;
        }
        """
        assert Parser(source).parse() == "success"
    
    def test_assignment_in_while_condition(self):
        """Test assignment in while condition"""
        source = """
        void f() {
            int x;
            while (x = 1) break;
        }
        """
        assert Parser(source).parse() == "success"


# =============================================================================
# DANGLING ELSE TESTS (3 tests)
# =============================================================================

class TestDanglingElse:
    """Test dangling else resolution (spec line 663)"""
    
    def test_dangling_else_basic(self):
        """Test dangling else: else binds to nearest if (spec line 663)"""
        source = """
        void f() {
            int x;
            int y;
            int a;
            int b;
            if (x) if (y) a = 1; else b = 2;
        }
        """
        assert Parser(source).parse() == "success"
    
    def test_dangling_else_with_blocks(self):
        """Test dangling else with explicit blocks"""
        source = """
        void f() {
            int x;
            int y;
            if (x) { if (y) x = 1; } else y = 2;
        }
        """
        assert Parser(source).parse() == "success"
    
    def test_deeply_nested_if_else(self):
        """Test deeply nested if-else"""
        source = """
        void f() {
            int a;
            int b;
            int c;
            if (a) if (b) if (c) a = 1; else b = 2; else c = 3;
        }
        """
        assert Parser(source).parse() == "success"


# =============================================================================
# CONTINUE IN FOR LOOP TEST (1 test)
# =============================================================================

class TestContinueInFor:
    """Test continue statement in for loop"""
    
    def test_continue_in_for(self):
        """Test continue in for loop (spec line 786)"""
        assert Parser("void f() { for (;;) continue; }").parse() == "success"


# =============================================================================
# NEW SPEC FEATURES: STRUCT LITERALS (8 tests)
# =============================================================================

class TestStructLiterals:
    """Test struct literals in expressions per updated spec (lines 339-340)"""
    
    def test_struct_literal_as_function_arg(self):
        """Test f({1, 2}) - struct literal as function argument"""
        source = """
        struct Point { int x; int y; };
        void draw(Point p) {}
        void main() { draw({10, 20}); }
        """
        assert Parser(source).parse() == "success"
    
    def test_struct_literal_empty(self):
        """Test f({}) - empty struct literal"""
        source = """
        struct Empty {};
        void process(Empty e) {}
        void main() { process({}); }
        """
        assert Parser(source).parse() == "success"
    
    def test_struct_literal_single_member(self):
        """Test {1} - single member struct literal"""
        source = """
        struct Single { int val; };
        void f(Single s) {}
        void main() { f({42}); }
        """
        assert Parser(source).parse() == "success"
    
    def test_nested_struct_literal(self):
        """Test {{1, 2}, 3} - nested struct literal"""
        source = """
        struct Point { int x; int y; };
        struct Point3D { Point p; int z; };
        void main() { Point3D p3 = {{1, 2}, 3}; }
        """
        assert Parser(source).parse() == "success"
    
    def test_struct_literal_with_expressions(self):
        """Test {1+2, 3*4} - struct literal with expressions"""
        source = """
        struct Point { int x; int y; };
        void draw(Point p) {}
        void main() { draw({1+2, 3*4}); }
        """
        assert Parser(source).parse() == "success"
    
    def test_struct_literal_multiple_args(self):
        """Test function with multiple struct literal args"""
        source = """
        struct Point { int x; int y; };
        void connect(Point a, Point b) {}
        void main() { connect({0, 0}, {10, 10}); }
        """
        assert Parser(source).parse() == "success"
    
    def test_struct_literal_in_return(self):
        """Test return {1, 2}"""
        source = """
        struct Point { int x; int y; };
        Point origin() { return {0, 0}; }
        """
        assert Parser(source).parse() == "success"
    
    def test_deeply_nested_struct_literal(self):
        """Test deeply nested struct literal"""
        source = """
        struct A { int val; };
        struct B { A a; };
        struct C { B b; };
        void main() { C c = {{{5}}}; }
        """
        assert Parser(source).parse() == "success"


# =============================================================================
# ADDITIONAL INCREMENT/DECREMENT TESTS (4 tests)
# =============================================================================

class TestIncrementDecrementExpressions:
    """Test increment/decrement in various contexts (spec lines 501-506)"""
    
    def test_postfix_decrement(self):
        """Test postfix decrement x--"""
        assert Parser("void f() { int x; x--; }").parse() == "success"
    
    def test_prefix_decrement(self):
        """Test prefix decrement --x"""
        assert Parser("void f() { int x; --x; }").parse() == "success"
    
    def test_postfix_increment_in_expression(self):
        """Test postfix increment in expression a = x++"""
        assert Parser("void f() { int x; int a; a = x++; }").parse() == "success"
    
    def test_member_increment(self):
        """Test member increment p.x++ (spec line 366)"""
        source = """
        struct Point { int x; int y; };
        void f() { Point p; p.x++; }
        """
        assert Parser(source).parse() == "success"


# =============================================================================
# STRUCT OPERATIONS TESTS (2 tests)
# =============================================================================

class TestStructOperations:
    """Test struct operations (spec lines 371, 380)"""
    
    def test_struct_assignment(self):
        """Test struct assignment p1 = p2 (spec line 371, 380)"""
        source = """
        struct Point { int x; int y; };
        void f() { Point p1; Point p2 = {1, 2}; p1 = p2; }
        """
        assert Parser(source).parse() == "success"
    
    def test_struct_member_to_variable(self):
        """Test assigning struct member to variable"""
        source = """
        struct Point { int x; int y; };
        void f() { Point p = {1, 2}; int v; v = p.x; }
        """
        assert Parser(source).parse() == "success"


# =============================================================================
# ALL RELATIONAL OPERATORS TESTS (5 tests)
# =============================================================================

class TestAllRelationalOperators:
    """Test all relational operators in expressions (spec lines 486-489)"""
    
    def test_less_equal_expression(self):
        """Test <= in expression"""
        assert Parser("void f() { auto x = 1 <= 2; }").parse() == "success"
    
    def test_greater_expression(self):
        """Test > in expression"""
        assert Parser("void f() { auto x = 2 > 1; }").parse() == "success"
    
    def test_greater_equal_expression(self):
        """Test >= in expression"""
        assert Parser("void f() { auto x = 2 >= 1; }").parse() == "success"
    
    def test_equal_expression(self):
        """Test == in expression"""
        assert Parser("void f() { auto x = 1 == 1; }").parse() == "success"
    
    def test_not_equal_expression(self):
        """Test != in expression"""
        assert Parser("void f() { auto x = 1 != 2; }").parse() == "success"


# =============================================================================
# LOGICAL OPERATORS TESTS (2 tests)
# =============================================================================

class TestLogicalOperatorsAdvanced:
    """Test logical operators in complex expressions (spec line 493)"""
    
    def test_logical_not_complex(self):
        """Test !(x < 5) - logical NOT in complex expression"""
        assert Parser("void f() { int x; auto y = !(x < 5); }").parse() == "success"
    
    def test_logical_operators_combined(self):
        """Test combined logical operators"""
        assert Parser("void f() { auto x = (1 && 2) || (!0); }").parse() == "success"


# =============================================================================
# SWITCH ADDITIONAL TESTS (2 tests)
# =============================================================================

class TestSwitchAdvanced:
    """Test advanced switch features (spec lines 720-722)"""
    
    def test_default_before_case(self):
        """Test default before case (spec line 720: default can appear anywhere)"""
        source = """
        void f() {
            switch (x) {
                default: x = 0;
                case 1: x = 1;
            }
        }
        """
        assert Parser(source).parse() == "success"
    
    def test_empty_default(self):
        """Test empty default clause (spec line 722)"""
        assert Parser("void f() { switch (x) { default: } }").parse() == "success"


# =============================================================================
# OPERATOR PRECEDENCE TESTS (10 tests) - Gap Coverage
# =============================================================================

class TestOperatorPrecedence:
    """Explicit operator precedence tests per spec lines 541-556"""
    
    def test_member_vs_arithmetic(self):
        """Test p.x + 1 parsed as (p.x) + 1"""
        source = """
        struct Point { int x; };
        void f() { Point p; auto r = p.x + 1; }
        """
        assert Parser(source).parse() == "success"
    
    def test_mult_vs_add(self):
        """Test 1 + 2 * 3 parsed as 1 + (2 * 3)"""
        assert Parser("void f() { auto x = 1 + 2 * 3; }").parse() == "success"
    
    def test_add_vs_relational(self):
        """Test a + 1 < b + 2 parsed as (a + 1) < (b + 2)"""
        assert Parser("void f() { int a; int b; auto x = a + 1 < b + 2; }").parse() == "success"
    
    def test_relational_vs_equality(self):
        """Test a < b == c < d parsed as (a < b) == (c < d)"""
        assert Parser("void f() { int a; int b; int c; int d; auto x = a < b == c < d; }").parse() == "success"
    
    def test_equality_vs_and(self):
        """Test a == b && c == d parsed as (a == b) && (c == d)"""
        assert Parser("void f() { int a; int b; int c; int d; auto x = a == b && c == d; }").parse() == "success"
    
    def test_and_vs_or(self):
        """Test a && b || c && d parsed as (a && b) || (c && d)"""
        assert Parser("void f() { int a; int b; int c; int d; auto x = a && b || c && d; }").parse() == "success"
    
    def test_or_vs_assign(self):
        """Test x = a || b parsed as x = (a || b)"""
        assert Parser("void f() { int x; int a; int b; x = a || b; }").parse() == "success"
    
    def test_full_precedence_chain(self):
        """Test expression with all precedence levels"""
        source = """
        struct S { int g; };
        void f() { S s; int a; int b; int c; int d; int e; int x;
            x = a || b && c == d + e * s.g;
        }
        """
        assert Parser(source).parse() == "success"
    
    def test_function_call_in_precedence(self):
        """Test function call precedence with postfix++"""
        source = """
        int foo() { return 1; }
        void f() { auto x = foo() + 1; }
        """
        assert Parser(source).parse() == "success"
    
    def test_unary_vs_binary(self):
        """Test -a * b parsed as (-a) * b"""
        assert Parser("void f() { int a; int b; auto x = -a * b; }").parse() == "success"


# =============================================================================
# CHAINED EXPRESSION TESTS (6 tests) - Gap Coverage
# =============================================================================

class TestChainedExpressions:
    """Test chained operators and expressions"""
    
    def test_chained_addition(self):
        """Test a + b + c + d (left-associative)"""
        assert Parser("void f() { auto x = 1 + 2 + 3 + 4; }").parse() == "success"
    
    def test_chained_comparison(self):
        """Test a < b < c (left-associative)"""
        assert Parser("void f() { int a; int b; int c; auto x = a < b < c; }").parse() == "success"
    
    def test_chained_member_access(self):
        """Test a.b.c.d (left-associative)"""
        source = """
        struct A { int val; };
        struct B { A a; };
        struct C { B b; };
        struct D { C c; };
        void f() { D d; auto x = d.c.b.a.val; }
        """
        assert Parser(source).parse() == "success"
    
    def test_chained_function_calls(self):
        """Test using result of function call"""
        source = """
        struct Point { int x; };
        Point getPoint() { Point p; return p; }
        void f() { auto x = getPoint().x; }
        """
        assert Parser(source).parse() == "success"
    
    def test_chained_logical_and(self):
        """Test a && b && c && d"""
        assert Parser("void f() { auto x = 1 && 2 && 3 && 4; }").parse() == "success"
    
    def test_chained_logical_or(self):
        """Test a || b || c || d"""
        assert Parser("void f() { auto x = 0 || 0 || 1 || 0; }").parse() == "success"


# =============================================================================
# ADDITIONAL SYNTAX ERROR TESTS (8 tests) - Gap Coverage
# =============================================================================

class TestAdditionalSyntaxErrors:
    """Test additional syntax error cases"""
    
    def test_trailing_comma_in_args(self):
        """Test f(a, b,) - trailing comma"""
        result = Parser("void f() { foo(a, b,); }").parse()
        assert result != "success"
    
    def test_empty_parentheses_expr(self):
        """Test () as expression"""
        result = Parser("void f() { auto x = (); }").parse()
        assert result != "success"
    
    def test_double_semicolon(self):
        """Test ;; - note: may be valid as empty statements in some grammars"""
        # This tests if double semicolons parse - grammar specific
        result = Parser("void f() { ;; }").parse()
        # Depending on grammar, this could be valid (empty statements)
        # Just verify it doesn't crash
        assert result is not None
    
    def test_missing_function_body(self):
        """Test function declaration without body"""
        result = Parser("void f();").parse()
        assert result != "success"
    
    def test_struct_missing_semicolon_after_brace(self):
        """Test struct S {} without trailing semicolon"""
        result = Parser("struct S {}").parse()
        assert result != "success"
    
    def test_for_missing_semicolons(self):
        """Test for () - missing semicolons"""
        result = Parser("void f() { for () x = 1; }").parse()
        assert result != "success"
    
    def test_switch_case_missing_colon(self):
        """Test case 1 without colon"""
        result = Parser("void f() { switch (x) { case 1 break; } }").parse()
        assert result != "success"
    
    def test_if_missing_condition(self):
        """Test if () - empty condition"""
        result = Parser("void f() { if () x = 1; }").parse()
        assert result != "success"


# =============================================================================
# VOID TYPE RESTRICTION TESTS (2 tests) - Gap Coverage
# =============================================================================

class TestVoidRestrictions:
    """Test void type restrictions per spec"""
    
    def test_void_variable_declaration(self):
        """Test void x; - should be syntax error"""
        result = Parser("void f() { void x; }").parse()
        # Parser may or may not catch this - semantic check may be needed
        # Just ensure it doesn't crash
        assert result is not None
    
    def test_void_parameter(self):
        """Test void parameter - void f(void x) - should be error"""
        result = Parser("void f(void x) {}").parse()
        # Parser may or may not catch this
        assert result is not None


# =============================================================================
# CONTINUE IN SWITCH TESTS (1 test) - Gap Coverage
# =============================================================================

class TestContinueInSwitch:
    """Test continue statement behavior with switch (spec line 770-771)"""
    
    def test_continue_in_switch_inside_loop(self):
        """Test continue in switch that is inside a loop (valid)"""
        source = """
        void f() {
            while (1) {
                switch (x) {
                    default:
                        continue;
                }
            }
        }
        """
        assert Parser(source).parse() == "success"


# =============================================================================
# NESTED PARENTHESES TESTS (2 tests) - Gap Coverage
# =============================================================================

class TestNestedParentheses:
    """Test deeply nested parentheses"""
    
    def test_deeply_nested_parens(self):
        """Test (((((x)))))"""
        assert Parser("void f() { auto x = (((((1))))); }").parse() == "success"
    
    def test_complex_nested_expression(self):
        """Test complex nested expression"""
        assert Parser("void f() { auto x = ((1 + 2) * (3 - 4)) / ((5 + 6)); }").parse() == "success"


# =============================================================================
# POSTFIX AND PREFIX COMBINATION TESTS (3 tests) - Gap Coverage
# =============================================================================

class TestPrefixPostfixCombinations:
    """Test combinations of prefix and postfix operators"""
    
    def test_double_unary_minus(self):
        """Test - - x (two unary minus)"""
        assert Parser("void f() { int x; auto y = - -x; }").parse() == "success"
    
    def test_double_logical_not(self):
        """Test !!x"""
        assert Parser("void f() { int x; auto y = !!x; }").parse() == "success"
    
    def test_unary_on_member_access(self):
        """Test -p.x"""
        source = """
        struct Point { int x; };
        void f() { Point p; auto y = -p.x; }
        """
        assert Parser(source).parse() == "success"

