# Used to exit program gracefully 
import time
import sys

# define separators, operators and reserved words
separator = [' ', '\t', ',', ';', '(', ')', '{', '}', '#']
operators = ['+', '-', '*', '/', '=', '<', '>', '<=', '=>', '==', '!=', '!']
keyword = ['if', 'else', 'endif' ,'while', 'function', 'integer', 'bool', 'real', 'ret', 'put', 'get', 'true', 'false']
begin_comment = '[*'
end_comment = '*]'

# define array to store all the words that have been read
words = []

# define dictionary to store tokens
tokens = []

# define current line
current_line = 1

# variables for parser
current_token = None
token_index = 0

# variables for output file
output_file = None

switch = False

# *********************************************************************************************************************************
# ******************************SYNTAX ANALYZER CODE STARTS HERE*******************************************************************
# *********************************************************************************************************************************
"""All the rules and functions for the syntax analyzer are here for top down parsing"""
def exit_syntax_analyzer():
    print("\nExiting Syntax Analyzer...")
    time.sleep(2)
    print("\nSyntax Analyzer Exited.")
    sys.exit(1)

def change_switch():
    global switch
    if switch == False:
        switch = True
    else:
        switch = False

def get_next_token():
    global current_token, token_index
    if token_index < len(tokens):
        current_token = tokens[token_index]
        token_index += 1
    else:
        print("\nReached end of file without parsing errors.\n")
        with open(output_file, "a") as file:
            file.write("\nReached end of file without parsing errors.\n\n")
        change_switch()
        # exit_syntax_analyzer()
    

def print_token():
    global current_token,  output_file, switch
    if switch == False:
        if current_token['token'] == 'illegal' or current_token['token'] == 'keyword' or current_token['token'] == 'integer' or current_token['token'] == 'real' or current_token['token'] == 'operator':
            print(f"Token: {current_token['token']}\t\t\tLexeme: {current_token['lexeme']}")
            with open(output_file, "a") as file:
                file.write(f"Token: {current_token['token']}\t\t\tLexeme: {current_token['lexeme']}\n")
        else:
            print(f"Token: {current_token['token']}\t\tLexeme: {current_token['lexeme']}")
            with open(output_file, "a") as file:
                file.write(f"Token: {current_token['token']}\t\tLexeme: {current_token['lexeme']}\n")

# Rule 1
# R1) <Rat23F> ::= # <Opt Declaration List> <Statement List> #
def Rat23F():
    global current_token, switch, output_file
    get_next_token()
    print_token()
    # print rule
    if switch == False:
        print("\t<Rat23F> ::= <Opt Function Definitions> # <Opt Declaration List> <Statement List> #")
        with open(output_file, "a") as file:
            file.write("\t<Rat23F> ::= <Opt Function Definitions> # <Opt Declaration List> <Statement List> #\n")
    if current_token['lexeme'] == '#':
        get_next_token()
        print_token()
        OptDeclarationList()
        StatementList()
        if current_token['lexeme'] == '#':
            get_next_token()
            print_token()
        else:
            
            print(f"Error: Expected '#' at line {current_token['line']}.")
            print(f"Reading token:", end="")
            with open(output_file, "a") as file:
                file.write(f"Error: Expected '#' at line {current_token['line']}.\n")
                file.write(f"Reading token:")
                print_token()
            exit_syntax_analyzer()
    else: 
        
        print(f"Error: Expected '#' at line {current_token['line']}.")
        print(f"Reading token:", end="")
        with open(output_file, "a") as file:
            file.write(f"Error: Expected '#' at line {current_token['line']}.\n")
            file.write(f"Reading token:")
        print_token()
        exit_syntax_analyzer()

# # Rule 2
# # R2) <Opt Function Definitions> ::= <Function Definitions> | <Empty>
# def OptFunctionDefinitions():
#     global current_token, switch, output_file
#     if switch == False:
#         print("\t<Opt Function Definitions> ::= <Function Definitions> | <Empty>")
#         with open(output_file, "a") as file:
#             file.write("\t<Opt Function Definitions> ::= <Function Definitions> | <Empty>\n")
#     if current_token['lexeme'] == 'function':
#         FunctionDefinitions()
#     if current_token['lexeme'] == '#':
#         if switch == False:
#             print("\t<Opt Function Definitions> ::= <Function Definitions> | <Empty>")
#             with open(output_file, "a") as file:
#                 file.write("\t<Opt Function Definitions> ::= <Function Definitions> | <Empty>\n")
#         Empty()
#     else:
#         print(f"Error: Expected 'function' or '#' at line {current_token['line']}.")
#         print(f"Reading token:", end="")
#         with open(output_file, "a") as file:
#             file.write(f"Error: Expected 'function' or '#' at line {current_token['line']}.\n")
#             file.write(f"Reading token:")
#         print_token()
#         exit_syntax_analyzer()


# # Rule 3
# # R3) <Function Definitions> ::= <Function> <Function Definitions Prime>
# def FunctionDefinitions():
#     global current_token, switch, output_file
#     if switch == False:
#         print("\t<Function Definitions> ::= <Function> <Function Definitions Prime>")
#         with open(output_file, "a") as file:
#             file.write("\t<Function Definitions> ::= <Function> <Function Definitions Prime>\n")
#     Function()
#     FunctionDefinitionsPrime()


# # Rule 4
# # R4) <Function Definitions Prime> ::= <Empty> | <Function Definitions>
# def FunctionDefinitionsPrime():
#     global current_token, switch, output_file
#     if switch == False:
#         print("\t<Function Definitions Prime> ::= <Empty> | <Function Definitions>")
#         with open(output_file, "a") as file:
#             file.write("\t<Function Definitions Prime> ::= <Empty> | <Function Definitions>\n")
#     if current_token['lexeme'] == 'function':
#         FunctionDefinitions()
#     else:
#         Empty()

# #Rule 5
# # R5) <Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>
# def Function():
#     global current_token, switch, output_file
#     if switch == False:
#         print("\t<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>")
#         with open(output_file, "a") as file:
#             file.write("\t<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>\n")
#     if current_token['lexeme'] == 'function':
#         get_next_token()
#         print_token()
#         if current_token['token'] == 'identifier':
#             get_next_token()
#             print_token()
#             if current_token['lexeme'] == '(':
#                 get_next_token()
#                 print_token()
#                 if current_token['lexeme'] != ')':
#                     OptParameterList()
#                 else:
#                     Empty()
#                 if current_token['lexeme'] == ')':
#                     get_next_token()
#                     print_token()
#                     if current_token['lexeme'] != '{':
#                         OptDeclarationList()
#                     else:
#                         Empty()
#                     Body()
#                 else:
                    
#                     print(f"Error: Expected ')' at line {current_token['line']}.")
#                     print(f"Reading token:", end="")
#                     with open(output_file, "a") as file:
#                         file.write(f"Error: Expected ')' at line {current_token['line']}.\n")
#                         file.write(f"Reading token:")
#                         print_token()
#                     exit_syntax_analyzer()
#             else:
                
#                 print(f"Error: Expected '(' at line {current_token['line']}.")
#                 print(f"Reading token:", end="")
#                 with open(output_file, "a") as file:
#                     file.write(f"Error: Expected '(' at line {current_token['line']}.\n")
#                     file.write(f"Reading token:")
#                     print_token()
#                 exit_syntax_analyzer()
#         else:
            
#             print(f"Error: Expected 'identifier' at line {current_token['line']}.")
#             print(f"Reading token:", end="")
#             with open(output_file, "a") as file:
#                 file.write(f"Error: Expected 'identifier' at line {current_token['line']}.\n")
#                 file.write(f"Reading token:")
#                 print_token()
#             exit_syntax_analyzer()
#     else:
        
#         print(f"Error: Expected 'function' keyword at line {current_token['line']}.")
#         print(f"Reading token:", end="")
#         with open(output_file, "a") as file:
#             file.write(f"Error: Expected 'function' keyword at line {current_token['line']}.\n")
#             file.write(f"Reading token:")
#         print_token()
#         exit_syntax_analyzer()


# # Rule 6
# # R6) <Opt Parameter List> ::= <Parameter List> | <Empty>
# def OptParameterList():
#     global current_token, switch, output_file
#     if switch == False:
#         print("\t<Opt Parameter List> ::= <Parameter List> | <Empty>")
#         with open(output_file, "a") as file:
#             file.write("\t<Opt Parameter List> ::= <Parameter List> | <Empty>\n")
#     ParameterList()


# # Rule 7
# # R7) <Parameter List> ::= <Parameter> <Parameter List Prime>
# def ParameterList():
#     global current_token, switch, output_file
#     if switch == False:
#         print("\t<Parameter List> ::= <Parameter> <Parameter List Prime>")
#         with open(output_file, "a") as file:
#             file.write("\t<Parameter List> ::= <Parameter> <Parameter List Prime>\n")
#     Parameter()
#     ParameterListPrime()


# # Rule 8
# # R8) <Parameter List Prime> ::= <Empty> | <Parameter List>
# def ParameterListPrime():
#     global current_token, switch, output_file
#     if switch == False:
#         print("\t<Parameter List Prime> ::= <Empty> | <Parameter List>")
#         with open(output_file, "a") as file:
#             file.write("\t<Parameter List Prime> ::= <Empty> | <Parameter List>\n")
#     if current_token['lexeme'] == ',':
#         get_next_token()
#         print_token()
#         ParameterList()
#     else:
#         Empty()


# # Rule 9
# # R9) <Parameter> ::= <IDs> <Qualifier>
# def Parameter():
#     global current_token, switch, output_file
#     if switch == False:
#         print("\t<Parameter> ::= <IDs> <Qualifier>")
#         with open(output_file, "a") as file:
#             file.write("\t<Parameter> ::= <IDs> <Qualifier>\n")
    
#     IDs()
#     Qualifier()


# Rule 10
# R10) <Qualifier> ::= integer | bool | real
def Qualifier():
    global current_token, switch, output_file
    # get_next_token()
    # print_token()
    if switch == False:
        print("\t<Qualifier> ::= integer | bool | real")
        with open(output_file, "a") as file:
            file.write("\t<Qualifier> ::= integer | boolean | real\n")
    if current_token['lexeme'] == 'integer':
        get_next_token()
        print_token()
    elif current_token['lexeme'] == 'bool':
        get_next_token()
        print_token()
    elif current_token['lexeme'] == 'real':
        get_next_token()
        print_token()
    else:
        
        print(f"Error: Expected 'integer', 'bool' or 'real' at line {current_token['line']}.")
        print(f"Reading token:", end="")
        with open(output_file, "a") as file:
            file.write(f"Error: Expected 'integer', 'bool' or 'real' at line {current_token['line']}.\n")
            file.write(f"Reading token:")
        print_token()
        exit_syntax_analyzer()


# Rule 11
# R11) <Body> ::= { <Statement List> }
# def Body():
#     global current_token, switch, output_file
#     if switch == False:
#         print("\t<Body> ::= { <Statement List> }")
#         with open(output_file, "a") as file:
#             file.write("\t<Body> ::= { <Statement List> }\n")
#     if current_token['lexeme'] == '{':
#         get_next_token()
#         print_token()

#         StatementList()
#         if current_token['lexeme'] == '}':
#             get_next_token()
#             print_token()
#         else:
            
#             print(f"Error: Expected '}}' at line {current_token['line']}.")
#             print(f"Reading token:", end="")
#             with open(output_file, "a") as file:
#                 file.write(f"Error: Expected '}}' at line {current_token['line']}.\n")
#                 file.write(f"Reading token:")
#                 print_token()
#             exit_syntax_analyzer()
#     else:
        
#         print(f"Error: Expected '{{' at line {current_token['line']}.")
#         print(f"Reading token:", end="")
#         with open(output_file, "a") as file:
#             file.write(f"Error: Expected '{{' at line {current_token['line']}.\n")
#             file.write(f"Reading token:")
#         print_token()
#         exit_syntax_analyzer()


# Rule 12
# R12) <Opt Declaration List> ::= <Declaration List> | <Empty>
def OptDeclarationList():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Opt Declaration List> ::= <Declaration List> | <Empty>")
        with open(output_file, "a") as file:
            file.write("\t<Opt Declaration List> ::= <Declaration List> | <Empty>\n")
    DeclarationList()
    Empty()


# Rule 13
# R13) <Declaration List> ::= <Declaration> ; <Declaration List Prime>
def DeclarationList():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Declaration List> ::= <Declaration> ; <Declaration List Prime>")
        with open(output_file, "a") as file:
            file.write("\t<Declaration List> ::= <Declaration> ; <Declaration List Prime>\n")
    Declaration()
    if current_token['lexeme'] == ';':
        get_next_token()
        print_token()
        DeclarationListPrime()
    else:
        
        print(f"Error: Expected ';' at line {current_token['line']}.")
        print(f"Reading token:", end="")
        with open(output_file, "a") as file:
            file.write(f"Error: Expected ';' at line {current_token['line']}.\n")
            file.write(f"Reading token:")
        print_token()
        exit_syntax_analyzer()


# Rule 14
# R14) <Declaration List Prime> ::= <Declaration List> | <Empty>
def DeclarationListPrime():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Declaration List Prime> ::= <Declaration List> | <Empty>")
        with open(output_file, "a") as file:
            file.write("\t<Declaration List Prime> ::= <Declaration List> | <Empty>\n")
    if current_token['lexeme'] == 'integer' or current_token['lexeme'] == 'bool' or current_token['lexeme'] == 'real':
        DeclarationList()
    else:
        Empty()


# Rule 15
# R15) <Declaration> ::= <Qualifier> <IDs>
def Declaration():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Declaration> ::= <Qualifier> <IDs>")
        with open(output_file, "a") as file:
            file.write("\t<Declaration> ::= <Qualifier> <IDs>\n")
    if current_token['lexeme'] == '{':
        get_next_token()
        print_token()
    Qualifier()
    IDs()


# Rule 16
# R16) <IDs> ::= <Identifier> <IDs Prime>
def IDs():
    global current_token, switch, output_file
    if switch == False:
        print("\t<IDs> ::= <Identifier> <IDs Prime>")
        with open(output_file, "a") as file:
            file.write("\t<IDs> ::= <Identifier> <IDs Prime>\n")
    if current_token['token'] == 'identifier':
        get_next_token()
        print_token()
        IDsPrime()
    else:
        
        print(f"Error: Expected 'identifier' at line {current_token['line']}.")
        print(f"Reading token:", end="")
        with open(output_file, "a") as file:
            file.write(f"Error: Expected 'identifier' at line {current_token['line']}.\n")
            file.write(f"Reading token:")
        print_token()
        exit_syntax_analyzer()


# Rule 17
# R17) <IDs Prime> ::= , <IDs> | <Empty>
def IDsPrime():
    global current_token, switch, output_file
    if switch == False:
        print("\t<IDs Prime> ::= , <IDs> | <Empty>")
        with open(output_file, "a") as file:
            file.write("\t<IDs Prime> ::= , <IDs> | <Empty>\n")
    if current_token['lexeme'] == ',':
        get_next_token()
        print_token()
        IDs()
    else:
        Empty()


# Rule 18
# R18) <Statement List> ::= <Statement> <Statement List Prime>
def StatementList():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Statement List> ::= <Statement> <Statement List Prime>")
        with open(output_file, "a") as file:
            file.write("\t<Statement List> ::= <Statement> <Statement List Prime>\n")
    Statement()
    if current_token['lexeme'] != '#':  #TODO: MIGHT NEED TO CHANGE THIS
        StatementListPrime()
    


# Rule 19
# R19) <Statement List Prime> ::= <Statement List> | <Empty>
def StatementListPrime():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Statement List Prime> ::= <Statement List> | <Empty>")
        with open(output_file, "a") as file:
            file.write("\t<Statement List Prime> ::= <Statement List> | <Empty>\n")
    if current_token['lexeme'] != '}':
        StatementList()
    else:
        Empty()


# Rule 20
# R20) <Statement> ::= <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While>
def Statement():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Statement> ::= <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While>")
        with open(output_file, "a") as file:
            file.write("\t<Statement> ::= <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While>\n")
    if current_token['lexeme'] == 'if':
        If()
    elif current_token['lexeme'] == 'while':
        While()
    elif current_token['lexeme'] == 'put':
        Print_put()
    elif current_token['lexeme'] == 'get':
        Scan()
    elif current_token['lexeme'] == 'ret':
        Return()
    elif current_token['token'] == 'identifier':
        Assign()
    elif current_token['lexeme'] == '{':
        Compound()
    else:
        
        print(f"Error: Expected 'if', 'while', 'put', 'get', 'ret', 'identifier' or '{{' at line {current_token['line']}.")
        print(f"Reading token:", end="")
        with open(output_file, "a") as file:
            file.write(f"Error: Expected 'if', 'while', 'put', 'get', 'ret', 'identifier' or '{{' at line {current_token['line']}.\n")
            file.write(f"Reading token:")
        print_token()
        exit_syntax_analyzer()


# Rule 21
# R21) <Compound> ::= { <Statement List> }
def Compound():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Compound> ::= { <Statement List> }")
        with open(output_file, "a") as file:
            file.write("\t<Compound> ::= { <Statement List> }\n")
    if current_token['lexeme'] == '{':
        get_next_token()
        print_token()
        StatementList()
        if current_token['lexeme'] == '}':
            get_next_token()
            print_token()
        else:
            
            print(f"Error: Expected '}}' at line {current_token['line']}.")
            print(f"Reading token:", end="")
            with open(output_file, "a") as file:
                file.write(f"Error: Expected '}}' at line {current_token['line']}.\n")
                file.write(f"Reading token:")
                print_token()
            exit_syntax_analyzer()
    else:
        
        print(f"Error: Expected '{{' at line {current_token['line']}.")
        print(f"Reading token:", end="")
        with open(output_file, "a") as file:
            file.write(f"Error: Expected '{{' at line {current_token['line']}.\n")
            file.write(f"Reading token:")
        print_token()
        exit_syntax_analyzer()


# Rule 22
# R22) <Assign> ::= <Identifier> = <Expression> ;
def Assign():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Assign> ::= <Identifier> = <Expression> ;")
        with open(output_file, "a") as file:
            file.write("\t<Assign> ::= <Identifier> = <Expression> ;\n")
    if current_token['token'] == 'identifier':
        get_next_token()
        print_token()
        if current_token['lexeme'] == '=':
            get_next_token()
            print_token()
            Expression()
            if current_token['lexeme'] == ';':
                get_next_token()
                print_token()
            else:
                
                print(f"Error: Expected ';' at line {current_token['line']}.")
                print(f"Reading token:", end="")
                with open(output_file, "a") as file:
                    file.write(f"Error: Expected ';' at line {current_token['line']}.\n")
                    file.write(f"Reading token:")
                    print_token()
                exit_syntax_analyzer()
        else:
            
            print(f"Error: Expected '=' at line {current_token['line']}.")
            print(f"Reading token:", end="")
            with open(output_file, "a") as file:
                file.write(f"Error: Expected '=' at line {current_token['line']}.\n")
                file.write(f"Reading token:")
                print_token()
            exit_syntax_analyzer()
    else:
        
        print(f"Error: Expected 'identifier' at line {current_token['line']}.")
        print(f"Reading token:", end="")
        with open(output_file, "a") as file:
            file.write(f"Error: Expected 'identifier' at line {current_token['line']}.\n")
            file.write(f"Reading token:")
        print_token()
        exit_syntax_analyzer()


# Rule 23
# R23) <If> ::= if ( <Condition> ) <Statement> <If Prime>
def If():
    global current_token, switch, output_file
    if switch == False:
        print("\t<If> ::= if ( <Condition> ) <Statement> <If Prime>")
        with open(output_file, "a") as file:
            file.write("\t<If> ::= if ( <Condition> ) <Statement> <If Prime>\n")
    if current_token['lexeme'] == 'if':
        get_next_token()
        print_token()
        if current_token['lexeme'] == '(':
            get_next_token()
            print_token()
            Condition()
            if current_token['lexeme'] == ')':
                get_next_token()
                print_token()
                Statement()

                IfPrime()
            else:
                
                print(f"Error: Expected ')' at line {current_token['line']}.")
                print(f"Reading token:", end="")
                with open(output_file, "a") as file:
                    file.write(f"Error: Expected ')' at line {current_token['line']}.\n")
                    file.write(f"Reading token:")
                    print_token()
                exit_syntax_analyzer()
        else:
            
            print(f"Error: Expected '(' at line {current_token['line']}.")
            print(f"Reading token:", end="")
            with open(output_file, "a") as file:
                file.write(f"Error: Expected '(' at line {current_token['line']}.\n")
                file.write(f"Reading token:")
                print_token()
            exit_syntax_analyzer()
    else:
        
        print(f"Error: Expected 'if' keyword at line {current_token['line']}.")
        print(f"Reading token:", end="")
        with open(output_file, "a") as file:
            file.write(f"Error: Expected 'if' keyword at line {current_token['line']}.\n")
            file.write(f"Reading token:")
        print_token()
        exit_syntax_analyzer()

# Rule 24
# R24) <If Prime> ::= endif | else <Statement> endif
def IfPrime():
    global current_token, switch, output_file
    if switch == False:
        print("\t<If Prime> ::= endif | else <Statement> endif")
        with open(output_file, "a") as file:
            file.write("\t<If Prime> ::= endif | else <Statement> endif\n")
    if current_token['lexeme'] == 'endif':
        get_next_token()
        print_token()
    elif current_token['lexeme'] == 'else':
        get_next_token()
        print_token()
        Statement()
        if current_token['lexeme'] == 'endif':
            get_next_token()
            print_token()
        else:
            
            print(f"Error: Expected 'endif' keyword at line {current_token['line']}.")
            print(f"Reading token:", end="")
            with open(output_file, "a") as file:
                file.write(f"Error: Expected 'endif' keyword at line {current_token['line']}.\n")
                file.write(f"Reading token:")
                print_token()
            exit_syntax_analyzer()
    else:
        
        print(f"Error: Expected 'endif' or 'else' keyword at line {current_token['line']}.")
        print(f"Reading token:", end="")
        with open(output_file, "a") as file:
            file.write(f"Error: Expected 'endif' or 'else' keyword at line {current_token['line']}.\n")
            file.write(f"Reading token:")
        print_token()
        exit_syntax_analyzer()

# Rule 25
# R25) <Return> ::= ret <Return Prime>
def Return():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Return> ::= return <Return Prime>")
        with open(output_file, "a") as file:
            file.write("\t<Return> ::= return <Return Prime>\n")
    if current_token['lexeme'] == 'ret':
        get_next_token()
        print_token()
        ReturnPrime()
    else:
        
        print(f"Error: Expected 'ret' keyword at line {current_token['line']}.")
        print(f"Reading token:", end="")
        with open(output_file, "a") as file:
            file.write(f"Error: Expected 'ret' keyword at line {current_token['line']}.\n")
            file.write(f"Reading token:")
        print_token()
        exit_syntax_analyzer()

# Rule 26
# R26) <Return Prime> ::= ; | <Expression> ;
def ReturnPrime():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Return Prime> ::= ; | <Expression> ;")
        with open(output_file, "a") as file:
            file.write("\t<Return Prime> ::= ; | <Expression> ;\n")
    if current_token['lexeme'] == ';':
        get_next_token()
        print_token()
    else:
        Expression()
        if current_token['lexeme'] == ';':
            get_next_token()
            print_token()
        else:
            
            print(f"Error: Expected ';' at line {current_token['line']}.")
            print(f"Reading token:", end="")
            with open(output_file, "a") as file:
                file.write(f"Error: Expected ';' at line {current_token['line']}.\n")
                file.write(f"Reading token:")
                print_token()
            exit_syntax_analyzer()

# Rule 27
# R27) <Print> ::= put ( <Expression> );
def Print_put():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Print> ::= put ( <Expression> );")
        with open(output_file, "a") as file:
            file.write("\t<Print> ::= put ( <Expression> );\n")
    if current_token['lexeme'] == 'put':
        get_next_token()
        print_token()
        if current_token['lexeme'] == '(':
            get_next_token()
            print_token()
            Expression()
            if current_token['lexeme'] == ')':
                get_next_token()
                print_token()
                if current_token['lexeme'] == ';':
                    get_next_token()
                    print_token()
                else:
                    
                    print(f"Error: Expected ';' at line {current_token['line']}.")
                    print(f"Reading token:", end="")
                    with open(output_file, "a") as file:
                        file.write(f"Error: Expected ';' at line {current_token['line']}.\n")
                        file.write(f"Reading token:")
                        print_token()
                    exit_syntax_analyzer()
            else:
                
                print(f"Error: Expected ')' at line {current_token['line']}.")
                print(f"Reading token:", end="")
                with open(output_file, "a") as file:
                    file.write(f"Error: Expected ')' at line {current_token['line']}.\n")
                    file.write(f"Reading token:")
                    print_token()
                exit_syntax_analyzer()
        else:
            
            print(f"Error: Expected '(' at line {current_token['line']}.")
            print(f"Reading token:", end="")
            with open(output_file, "a") as file:
                file.write(f"Error: Expected '(' at line {current_token['line']}.\n")
                file.write(f"Reading token:")
                print_token()
            exit_syntax_analyzer()
    else:
        
        print(f"Error: Expected 'put' keyword at line {current_token['line']}.")
        print(f"Reading token:", end="")
        with open(output_file, "a") as file:
            file.write(f"Error: Expected 'put' keyword at line {current_token['line']}.\n")
            file.write(f"Reading token:")
        print_token()
        exit_syntax_analyzer()

# Rule 28
# R28) <Scan> ::= get ( <IDs> );
def Scan():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Scan> ::= get ( <IDs> );")
        with open(output_file, "a") as file:
            file.write("\t<Scan> ::= get ( <IDs> );\n")
    if current_token['lexeme'] == 'get':
        get_next_token()
        print_token()
        if current_token['lexeme'] == '(':
            get_next_token()
            print_token()
            IDs()
            if current_token['lexeme'] == ')':
                get_next_token()
                print_token()
                if current_token['lexeme'] == ';':
                    get_next_token()
                    print_token()
                else:
                    
                    print(f"Error: Expected ';' at line {current_token['line']}.")
                    print(f"Reading token:", end="")
                    with open(output_file, "a") as file:
                        file.write(f"Error: Expected ';' at line {current_token['line']}.\n")
                        file.write(f"Reading token:")
                        print_token()
                    exit_syntax_analyzer()
            else:
                
                print(f"Error: Expected ')' at line {current_token['line']}.")
                print(f"Reading token:", end="")
                with open(output_file, "a") as file:
                    file.write(f"Error: Expected ')' at line {current_token['line']}.\n")
                    file.write(f"Reading token:")
                    print_token()
                exit_syntax_analyzer()
        else:
            
            print(f"Error: Expected '(' at line {current_token['line']}.")
            print(f"Reading token:", end="")
            with open(output_file, "a") as file:
                file.write(f"Error: Expected '(' at line {current_token['line']}.\n")
                file.write(f"Reading token:")
                print_token()
            exit_syntax_analyzer()
    else:
        
        print(f"Error: Expected 'get' keyword at line {current_token['line']}.")
        print(f"Reading token:", end="")
        with open(output_file, "a") as file:
            file.write(f"Error: Expected 'get' keyword at line {current_token['line']}.\n")
            file.write(f"Reading token:")
        print_token()
        exit_syntax_analyzer()

# Rule 29
# R29) <While> ::= while ( <Condition> ) <Statement>
def While():
    global current_token, switch, output_file
    if switch == False:
        print("\t<While> ::= while ( <Condition> ) <Statement>")
        with open(output_file, "a") as file:
            file.write("\t<While> ::= while ( <Condition> ) <Statement>\n")
    if current_token['lexeme'] == 'while':
        get_next_token()
        print_token()
        if current_token['lexeme'] == '(':
            get_next_token()
            print_token()
            Condition()
            if current_token['lexeme'] == ')':
                get_next_token()
                print_token()
                Statement()
            else:
                
                print(f"Error: Expected ')' at line {current_token['line']}.")
                print(f"Reading token:", end="")
                with open(output_file, "a") as file:
                    file.write(f"Error: Expected ')' at line {current_token['line']}.\n")
                    file.write(f"Reading token:")
                    print_token()
                exit_syntax_analyzer
        else:
            
            print(f"Error: Expected '(' at line {current_token['line']}.")
            print(f"Reading token:", end="")
            with open(output_file, "a") as file:
                file.write(f"Error: Expected '(' at line {current_token['line']}.\n")
                file.write(f"Reading token:")
                print_token()
            exit_syntax_analyzer()
    else:
        
        print(f"Error: Expected 'while' keyword at line {current_token['line']}.")
        print(f"Reading token:", end="")
        with open(output_file, "a") as file:
            file.write(f"Error: Expected 'while' keyword at line {current_token['line']}.\n")
            file.write(f"Reading token:")
        print_token()
        exit_syntax_analyzer()


# Rule 30
# R30) <Condition> ::= <Expression> <Relop> <Expression>
def Condition():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Condition> ::= <Expression> <Relop> <Expression>")
        with open(output_file, "a") as file:
            file.write("\t<Condition> ::= <Expression> <Relop> <Expression>\n")
    Expression()
    Relop()
    Expression()


# Rule 31
# R31) <Relop> ::= == | != | > | < | <= | =>
def Relop():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Relop> ::= == | != | > | < | <= | =>")
        with open(output_file, "a") as file:
            file.write("\t<Relop> ::= == | != | > | < | <= | =>\n")
    if current_token['lexeme'] == '==':
        get_next_token()
        print_token()
    elif current_token['lexeme'] == '!=':
        get_next_token()
        print_token()
    elif current_token['lexeme'] == '>':
        get_next_token()
        print_token()
    elif current_token['lexeme'] == '<':
        get_next_token()
        print_token()
    elif current_token['lexeme'] == '<=':
        get_next_token()
        print_token()
    elif current_token['lexeme'] == '=>':
        get_next_token()
        print_token()
    else:
        
        print(f"Error: Expected '==', '!=', '>', '<', '<=' or '=>' at line {current_token['line']}.")
        print(f"Reading token:", end="")
        with open(output_file, "a") as file:
            file.write(f"Error: Expected '==', '!=', '>', '<', '<=' or '=>' at line {current_token['line']}.\n")
            file.write(f"Reading token:")
        print_token()
        exit_syntax_analyzer()


# Rule 32
# R32) <Expression> ::= <Term> <Expression Prime>
def Expression():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Expression> ::= <Term> <Expression Prime>")
        with open(output_file, "a") as file:
            file.write("\t<Expression> ::= <Term> <Expression Prime>\n")
    Term()
    ExpressionPrime()


# Rule 33
# R33) <Expression Prime> ::= + <Term> <Expression Prime> | - <Term> <Expression Prime> | <Empty>
def ExpressionPrime():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Expression Prime> ::= + <Term> <Expression Prime> | - <Term> <Expression Prime> | <Empty>")
        with open(output_file, "a") as file:
            file.write("\t<Expression Prime> ::= + <Term> <Expression Prime> | - <Term> <Expression Prime> | <Empty>\n")
    if current_token['lexeme'] == '+':
        get_next_token()
        print_token()
        Term()
        ExpressionPrime()
    elif current_token['lexeme'] == '-':
        get_next_token()
        print_token()
        Term()
        ExpressionPrime()
    else:
        Empty()


# Rule 34
# R34) <Term> ::= <Factor> <Term Prime>
def Term():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Term> ::= <Factor> <Term Prime>")
        with open(output_file, "a") as file:
            file.write("\t<Term> ::= <Factor> <Term Prime>\n")
    Factor()
    TermPrime()


# Rule 35
# R35) <Term Prime> ::= * <Factor> <Term Prime> | / <Factor> <Term Prime> | <Empty>
def TermPrime():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Term Prime> ::= * <Factor> <Term Prime> | / <Factor> <Term Prime> | <Empty>")
        with open(output_file, "a") as file:
            file.write("\t<Term Prime> ::= * <Factor> <Term Prime> | / <Factor> <Term Prime> | <Empty>\n")
    if current_token['lexeme'] == '*':
        get_next_token()
        print_token()
        Factor()
        TermPrime()
    elif current_token['lexeme'] == '/':
        get_next_token()
        print_token()
        Factor()
        TermPrime()
    else:
        Empty()


# Rule 36
# R36) <Factor> ::= - <Primary> | <Primary>
def Factor():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Factor> ::= - <Primary> | <Primary>")
        with open(output_file, "a") as file:
            file.write("\t<Factor> ::= - <Primary> | <Primary>\n")
    if current_token['lexeme'] == '-':
        get_next_token()
        print_token()
        Primary()
    else:
        Primary()


# Rule 37
# R37) <Primary> ::= <Identifier> <Primary Prime> | <Integer> | ( <Expression> ) | <Real> | true | false
def Primary():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Primary> ::= <Identifier> <Primary Prime> | <Integer> | ( <Expression> ) | <Real> | true | false")
        with open(output_file, "a") as file:
            file.write("\t<Primary> ::= <Identifier> <Primary Prime> | <Integer> | ( <Expression> ) | <Real> | true | false\n")
    if current_token['token'] == 'identifier':
        get_next_token()
        print_token()
        PrimaryPrime()
    elif current_token['token'] == 'integer':
        get_next_token()
        print_token()
    elif current_token['lexeme'] == '(':
        get_next_token()
        print_token()
        Expression()
        if current_token['lexeme'] == ')':
            get_next_token()
            print_token()
        else:
            
            print(f"Error: Expected ')' at line {current_token['line']}.")
            print(f"Reading token:", end="")
            with open(output_file, "a") as file:
                file.write(f"Error: Expected ')' at line {current_token['line']}.\n")
                file.write(f"Reading token:")
                print_token()
            exit_syntax_analyzer()
    elif current_token['token'] == 'real':
        get_next_token()
        print_token()
    elif current_token['lexeme'] == 'true':
        get_next_token()
        print_token()
    elif current_token['lexeme'] == 'false':
        get_next_token()
        print_token()
    else:
        
        print(f"Error: Expected 'identifier', 'integer', '(', 'real', 'true' or 'false' at line {current_token['line']}.")
        print(f"Reading token:", end="")
        with open(output_file, "a") as file:
            file.write(f"Error: Expected 'identifier', 'integer', '(', 'real', 'true' or 'false' at line {current_token['line']}.\n")
            file.write(f"Reading token:")
        print_token()
        exit_syntax_analyzer()

# Rule 38
# R38) <Primary Prime> ::= <Empty> | ( <IDs> )
def PrimaryPrime():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Primary Prime> ::= <Empty> | ( <IDs> )")
        with open(output_file, "a") as file:
            file.write("\t<Primary Prime> ::= <Empty> | ( <IDs> )\n")
    if current_token['lexeme'] == '(':
        get_next_token()
        print_token()
        IDs()
        if current_token['lexeme'] == ')':
            get_next_token()
            print_token()
        else:
            
            print(f"Error: Expected ')' at line {current_token['line']}.")
            print(f"Reading token:", end="")
            with open(output_file, "a") as file:
                file.write(f"Error: Expected ')' at line {current_token['line']}.\n")
                file.write(f"Reading token:")
                print_token()
            exit_syntax_analyzer()
    else:
        Empty()


# Rule 39
# R39) <Empty> ::= <Empty>
def Empty():
    global current_token, switch, output_file
    if switch == False:
        print("\t<Empty> ::= <Empty>")
        with open(output_file, "a") as file:
            file.write("\t<Empty> ::= <Empty>\n")
    pass    
    

# *********************************************************************************************************************************
# ******************************SYNTAX ANALYZER CODE ENDS HERE********************************************************************* 
# *********************************************************************************************************************************



# Code to read the file and store its words in an array
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            # here we store the current word read
            word = ""
            while True:
                char = file.read(1)
                if not char:
                    break  # End of file, we exit loop
                # TODO: CHECK IF THIS FIXES ISSUE WITH NEWLINES
                # check for new line character
                if char == '\n':
                    if word:
                        words.append(word)
                        word = ""
                    words.append(char)
                # check for comments
                elif char == '[':
                    if word:
                        words.append(word)
                        word = ""
                    # check for correct opening comment
                    next_char = file.read(1)
                    if char + next_char == begin_comment:
                        words.append(char + next_char)
                    else:
                        # store single operator 
                        words.append(char)
                        # check if next character is a separator
                        if next_char in separator:
                            if next_char != ' ' and char != '\n' and char != '\t':
                                words.append(next_char)
                        else:    
                            word += next_char

                elif char in operators: # read operator
                    if word:
                        words.append(word)
                        word = ""
                    # check for double character operators
                    next_char = file.read(1)
                    # check for closing comment
                    if char + next_char == end_comment:
                        words.append(char + next_char)

                    elif char + next_char in operators:
                        words.append(char + next_char)
                    else:
                        # store single operator 
                        words.append(char)
                        # check if next character is a separator
                        if next_char in separator:
                            if next_char != ' ' and char != '\n' and char != '\t':
                                words.append(next_char)
                        # remove next if in case that we want to make this illegal
                        elif next_char in operators:
                            words.append(next_char)
                        else:    
                            word = next_char

                elif char in separator: # read separator
                    if word:
                        words.append(word)
                        word = ""
                    # in case that we dont want to store whitespaces
                    #remove "if" to keep whitespaces
                    if char != ' ' and char != '\t':
                        words.append(char)
                else:
                    word += char
            if word:
                words.append(word)
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
    except PermissionError:
        print(f"You do not have permission to read the file: '{file_name}'.")
    except OSError as systemError:  
        print(f"An error occurred while reading the file: '{file_name}'. The error was: {systemError}")
    except Exception as errorMessage:
        print(f"An unexpected error occurred while reading the file: '{file_name}'. The error was: {str(errorMessage)}")

# finite state machine for real and integer
def FSMReal(lexeme):
    current_state = 1
    for char in lexeme:
        # manage initial state
        # we need this because we can't have a "." as the first character
        if current_state == 1:
            if char.isdigit():
                current_state = 2
            else:
                current_state = 5
        # manage state 2 aka integer before "."
        if current_state == 2:
            if char.isdigit():
                current_state = 2
            elif char == '.':
                current_state = 3
            else:
                current_state = 5
        # manage state 3 aka "."
        elif current_state == 3:
            if char.isdigit():
                current_state = 4
            else:
                current_state = 5
        # manage state 4 aka integer after "."
        elif current_state == 4:
            if char.isdigit():
                current_state = 4
            else:
                current_state = 5

    # if our final state is 4, then we have a real
    if current_state == 4:
        # store token and lexeme
        tokens.append({'token': 'real', 'lexeme': lexeme, 'line': current_line})
    # if our final state is 2, then we have an integer
    elif current_state == 2:
        tokens.append({'token': 'integer', 'lexeme': lexeme, 'line': current_line})
    # in case of failure
    else:
        tokens.append({'token': 'illegal', 'lexeme': lexeme, 'line': current_line})

# finite state machine for identifiers
def FSMIdentifier(identifier):
    current_state = 1
    if len(identifier) == 1:
        if identifier.isalpha():
            tokens.append({'token': 'identifier', 'lexeme': identifier, 'line': current_line})
    else:
        for char in identifier:
            # check if the first character is a letter
            if current_state == 1:
                if char.isalpha():
                    current_state = 2
                else:
                    current_state = 4
            # now we can accept digits and letters
            elif current_state == 2:
                if char.isalpha():
                    # we stay in the same state if letter
                    current_state = 2
                elif char.isdigit():
                    # we move to state 3 if digit
                    current_state = 3
                else:
                    current_state = 4
            # still accepting digits and letters
            elif current_state == 3:
                if char.isalpha():
                    # we go back to state 2 if letter
                    current_state = 2
                elif char.isdigit():
                    # we stay in the same state if digit
                    current_state = 3
                else:
                    current_state = 4
        # final state must be 2 because we need to end in a letter
        if current_state == 2:
            tokens.append({'token': 'identifier', 'lexeme': identifier, 'line': current_line})
        else:
            tokens.append({'token': 'illegal', 'lexeme': identifier, 'line': current_line})

# this is the main lexer function, it is in charge of identifying the tokens
def lexer(word):
    if word in keyword:
        tokens.append({'token': 'keyword', 'lexeme': word, 'line': current_line})
    elif word in operators:
        # check that word is not the only illegal operator "!", only in list for "!="
        if word == '!':
            tokens.append({'token': 'illegal', 'lexeme': word, 'line': current_line})
        else:
            tokens.append({'token': 'operator', 'lexeme': word, 'line': current_line})
    elif word in separator:
        tokens.append({'token': 'separator', 'lexeme': word, 'line': current_line})
    # check if it is a real or an integer
    elif word[0].isdigit():
        FSMReal(word)
    # check if is in an identifier
    elif word[0].isalpha():
        FSMIdentifier(word)
    else:
        tokens.append({'token': 'illegal', 'lexeme': word, 'line': current_line})

# this functions removes comments from the code
def commentRemoval(words):
    global current_line
    # keep track if we are in a comment 
    comment = False
    # iterate through lexemes 
    for word in words:
        if word == "\n":
            current_line += 1
        elif word == begin_comment:
            comment = True
        elif comment == False:
            lexer(word)
        elif word == end_comment:
            comment = False

# this functions prints all the tokens to the main program console
def print_tokens(tokens):
    print("token\t\t\tlexeme\t\t\tline")
    print("_________________________________\n")
    for token in tokens:
        if token['token'] == 'illegal' or token['token'] == 'keyword' or token['token'] == 'integer' or token['token'] == 'real':
            print(f"{token['token']}\t\t\t{token['lexeme']}\t\t\t{token['line']}")
        else:
            print(f"{token['token']}\t\t{token['lexeme']}\t\t\t{token['line']}")

# this function generates a file name for the tokens file
def file_name_generator(file_name):
    return 'output_' + file_name

# this function writes all the tokens and lexemes to a file
def write_tokens(tokens):
    global output_file
    try:
        with open(output_file, 'w') as file:
            print(f"\nWriting tokens to file '{output_file}'...\n")
            file.write("token\t\t\tlexeme\t\t\tline\n")
            file.write("_________________________________\n")
            for token in tokens:
                if token['token'] == 'illegal' or token['token'] == 'keyword' or token['token'] == 'integer' or token['token'] == 'real':
                    file.write(f"{token['token']}\t\t\t{token['lexeme']}\t\t\t{token['line']}\n")
                else:
                    file.write(f"{token['token']}\t\t{token['lexeme']}\t\t\t{token['line']}\n")
            print(f"Tokens written to file '{output_file}' successfully!\n")
    except FileNotFoundError:
        print(f"The file '{output_file}' was not found.")
    except PermissionError:
        print(f"You do not have permission to create the file: '{output_file}'.")
    except OSError as systemError:  
        print(f"An error occurred while creating the file: '{output_file}'. The error was: {systemError}")
    except Exception as errorMessage:
        print(f"An unexpected error occurred while creating the file: '{output_file}'. The error was: {str(errorMessage)}")

# Function to analyze a file
def analyze_file():
    global current_line, output_file, switch, token_index
    while True:
        try:
            file_name = input("Please enter the name of the file you want to analyze (or 'q' to quit): ")
            if file_name == 'q':
                print("\nThank you for using our Lexical Analyzer!\n")
                print("Exiting program...")
                time.sleep(2)
                sys.exit(0) # Exit the loop and quit the program
            with open(file_name, 'r') as file:
                # The file exists, so continue with analysis
                # create output file name
                output_file = file_name_generator(file_name)
                # clear file in case that there was a previous analysis
                with open(output_file, "w") as file:
                    file.write("")  # This will clear the file's contents
                print(f"\nAnalyzing file '{file_name}'...\n")
                switch = False  # Set switch to False to print the rules
                words.clear()  # Clear the list of words from previous analyses
                tokens.clear()  # Clear the list of tokens from previous analyses
                current_line = 1  # Reset the current line to 1
                token_index = 0  # Reset the token index to 0
                read_file(file_name)
                commentRemoval(words)
                # TODO: remove print_tokens(tokens) and write_tokens(tokens) before submitting
                # print_tokens(tokens)
                # write_tokens(tokens)
                # TODO: add rat23f() call here
                Rat23F()
                break
        except FileNotFoundError:
            print(f"The file '{file_name}' was not found. Please enter a valid file name.")
        except PermissionError:
            print(f"You do not have permission to read the file: '{file_name}'. Please enter a different file name.")
        except Exception as errorMessage:
            print(f"An unexpected error occurred: {str(errorMessage)} Please enter a different file name.")

def main():
    # User interface
    print("\nWelcome to our Syntax Analyzer!")

    # call main function to analyze a file 
    analyze_file()
    # Main loop
    while True:
        another_analysis = input("Do you want to analyze another file? (yes/no): ").strip().lower()
        if another_analysis == 'no' or another_analysis == 'n':
            print("\nThank you for using our Syntax Analyzer!\n")
            print("Exiting program...")
            time.sleep(2)
            sys.exit(0)  # Exit the program if the user does not want to analyze another file
        elif another_analysis == 'yes' or another_analysis == 'y':
            analyze_file()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
