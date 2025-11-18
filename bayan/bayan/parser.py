"""
Hybrid Parser for Bayan Language
محلل نحوي هجين للغة بيان
"""

from .lexer import TokenType
from .ast_nodes import *
from .logical_engine import Term, Predicate, Fact, Rule

class HybridParser:
    """Hybrid parser for Bayan language"""

    def __init__(self, tokens, filename=None):
        self.tokens = tokens
        self.position = 0
        self.current_token = self.tokens[0] if tokens else None
        self.filename = filename

    def advance(self):
        """Move to the next token"""
        self.position += 1
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
        else:
            self.current_token = None

    def peek(self, lookahead=1):
        """Look ahead at the next token"""
        pos = self.position + lookahead
        if pos < len(self.tokens):
            return self.tokens[pos]
        return None

    def match(self, *token_types):
        """Check if current token matches any of the given types"""
        if self.current_token is None:
            return False
        return self.current_token.type in token_types

    def _unescape_string(self, s: str) -> str:
        """Unescape common escape sequences in string literals."""
        out = []
        i = 0
        L = len(s)
        while i < L:
            ch = s[i]
            if ch != '\\':
                out.append(ch)
                i += 1
                continue
            i += 1
            if i >= L:
                out.append('\\')
                break
            esc = s[i]
            i += 1
            if esc == 'n': out.append('\n')
            elif esc == 't': out.append('\t')
            elif esc == 'r': out.append('\r')
            elif esc == '"': out.append('"')
            elif esc == "'": out.append("'")
            elif esc == '\\': out.append('\\')
            elif esc == 'u' and i + 4 <= L:
                hex_digits = s[i:i+4]
                try:
                    out.append(chr(int(hex_digits, 16)))
                    i += 4
                except Exception:
                    out.append('\\u')
            else:
                out.append('\\' + esc)
        return ''.join(out)

    def peek_ahead(self, offset=1):
        """Peek ahead at token at position + offset"""
        peek_pos = self.position + offset
        if peek_pos < len(self.tokens):
            return self.tokens[peek_pos]
        return None

    def eat(self, token_type):
        """Consume a token of the given type"""
        if self.current_token is None or self.current_token.type != token_type:
            raise SyntaxError(
                f"Expected {token_type}, got {self.current_token.type if self.current_token else 'EOF'}"
            )
        token = self.current_token
        self.advance()
        return token

    def eat_attribute_name(self):
        """Consume an attribute/method name - can be IDENTIFIER or certain reserved keywords"""
        if self.match(TokenType.IDENTIFIER):
            return self.eat(TokenType.IDENTIFIER)
        # Allow semantic programming keywords as attribute names
        elif self.match(TokenType.SIMILARITY, TokenType.BASED_ON, TokenType.DOMAIN,
                        TokenType.MEMORY, TokenType.KNOWLEDGE, TokenType.PATTERN,
                        TokenType.CONCEPT, TokenType.ROLE, TokenType.DEGREE,
                        TokenType.STATE_CHANGES, TokenType.ENTITIES, TokenType.RESULT,
                        TokenType.PARTICIPANTS, TokenType.STRENGTH, TokenType.TRANSFORM,
                        TokenType.REACTIONS, TokenType.STRUCTURE, TokenType.EXPRESS,
                        TokenType.LINGUISTIC_FORMS, TokenType.CONTENT, TokenType.CONTEXT,
                        TokenType.TIME, TokenType.PLACE, TokenType.SOURCE, TokenType.CERTAINTY,
                        TokenType.CURRENT_VALUE, TokenType.HISTORY, TokenType.FUTURE_PREDICTION,
                        TokenType.ROOT, TokenType.TAXONOMY, TokenType.CHARACTERS, TokenType.EVENT,
                        TokenType.DEFAULT, TokenType.MATCH, TokenType.LIMIT):
            tok = self.current_token
            self.advance()
            return tok
        else:
            raise SyntaxError(f"Expected attribute name, got {self.current_token}")

    def _with_pos(self, node, tok):
        """Attach source position from token to node if supported"""
        if node is not None and hasattr(node, 'with_pos') and tok is not None:
            node.with_pos(getattr(tok, 'line', None), getattr(tok, 'column', None), getattr(self, 'filename', None))
        return node


    def parse(self):
        """Parse the entire program"""
        statements = []

        while self.current_token and self.current_token.type != TokenType.EOF:
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)

        return Program(statements)

    def parse_statement(self):
        """Parse a single statement"""
        # Check for decorators
        decorators = []
        while self.match(TokenType.AT):
            decorators.append(self.parse_decorator())

        if self.match(TokenType.HYBRID):
            return self.parse_hybrid_block()
        elif self.match(TokenType.ASYNC):
            return self.parse_async_function_def(decorators)
        elif self.match(TokenType.DEF):
            return self.parse_function_def(decorators)
        elif self.match(TokenType.CLASS):
            return self.parse_class_def(decorators)
        elif self.match(TokenType.IF):
            return self.parse_if_statement()
        elif self.match(TokenType.FOR):
            return self.parse_for_loop()
        elif self.match(TokenType.WHILE):
            return self.parse_while_loop()
        elif self.match(TokenType.RETURN):
            return self.parse_return_statement()
        elif self.match(TokenType.YIELD):
            return self.parse_yield_statement()
        elif self.match(TokenType.WITH):
            return self.parse_with_statement()
        elif self.match(TokenType.TRY):
            return self.parse_try_statement()
        elif self.match(TokenType.RAISE):
            return self.parse_raise_statement()
        elif self.match(TokenType.BREAK):
            self.advance()
            return BreakStatement()
        elif self.match(TokenType.CONTINUE):
            self.advance()
            return ContinueStatement()
        elif self.match(TokenType.PRINT):
            return self.parse_print_statement()
        elif self.match(TokenType.QUERY):
            return self.parse_query()
        elif self.match(TokenType.FACT):
            return self.parse_fact()
        elif self.match(TokenType.RULE):
            return self.parse_rule()
        elif self.match(TokenType.IMPORT):
            return self.parse_import_statement()
        elif self.match(TokenType.FROM):
            # Check if this is 'from import' or just 'from' used as identifier
            if self.peek() and self.peek().type == TokenType.ASSIGN:
                # This is assignment: from = value
                return self.parse_expression_statement()
            else:
                return self.parse_from_import_statement()
        elif self.match(TokenType.ENTITY):
            return self.parse_entity_def()
        elif self.match(TokenType.CONCEPT):
            return self.parse_concept_def()
        elif self.match(TokenType.APPLY):
            return self.parse_apply_action()
        elif self.match(TokenType.ONCE):
            return self.parse_once_statement()
        elif self.match(TokenType.REACTIVE):
            return self.parse_reactive_declaration()
        elif self.match(TokenType.WATCH):
            return self.parse_watch_block()
        elif self.match(TokenType.COMPUTED):
            return self.parse_computed_property()
        elif self.match(TokenType.COGNITIVE_ENTITY):
            return self.parse_cognitive_entity()
        elif self.match(TokenType.COGNITIVE_EVENT):
            return self.parse_cognitive_event()
        elif self.match(TokenType.TRIGGER):
            return self.parse_trigger_event()
        elif self.match(TokenType.CONCURRENT):
            return self.parse_concurrent_events()
        elif self.match(TokenType.PATTERN):
            return self.parse_linguistic_pattern()
        elif self.match(TokenType.IDEA):
            return self.parse_idea_def()
        elif self.match(TokenType.CONCEPTUAL_BLUEPRINT):
            return self.parse_conceptual_blueprint()
        # Semantic Programming & Knowledge Management
        elif self.match(TokenType.MEANING):
            return self.parse_semantic_meaning()
        elif self.match(TokenType.QUERY):
            return self.parse_semantic_query()
        elif self.match(TokenType.INFORMATION):
            return self.parse_knowledge_info()
        elif self.match(TokenType.INFERENCE_RULE):
            return self.parse_inference_rule()
        elif self.match(TokenType.INFER_FROM):
            return self.parse_infer_from()
        elif self.match(TokenType.CONTRADICTION):
            return self.parse_contradiction()
        elif self.match(TokenType.KNOWLEDGE):
            return self.parse_evolving_knowledge()
        elif self.match(TokenType.ONTOLOGY):
            return self.parse_ontology()
        elif self.match(TokenType.NARRATIVE):
            return self.parse_narrative()
        elif self.match(TokenType.GENERATE_NARRATIVE):
            return self.parse_generate_narrative()
        elif self.match(TokenType.CURRENT_CONTEXT):
            return self.parse_current_context()
        # Existential Model
        elif self.match(TokenType.DOMAIN):
            return self.parse_domain()
        elif self.match(TokenType.ENVIRONMENT):
            return self.parse_generic_environment()
        elif self.match(TokenType.EXISTENTIAL_BEING):
            return self.parse_existential_being()
        elif self.match(TokenType.DOMAIN_RELATION):
            return self.parse_domain_relation()
        elif self.match(TokenType.DOMAIN_ACTION):
            return self.parse_domain_action()
        elif self.match(TokenType.METAPHORICAL_MEANING):
            return self.parse_metaphorical_meaning()
        elif self.match(TokenType.DOMAIN_LAW):
            return self.parse_domain_law()
        elif self.match(TokenType.EXISTENTIAL_QUERY):
            return self.parse_existential_query()
        elif self.match(TokenType.LIMIT):
            # Check if this is 'limit N { ... }' or 'limit = ...' (assignment)
            next_tok = self.peek()
            if next_tok and next_tok.type == TokenType.NUMBER:
                # This is 'limit N { ... }' or 'limit N goal.'
                return self.parse_limit_statement()
            elif next_tok and (next_tok.type == TokenType.ASSIGN or next_tok.type == TokenType.LBRACKET or next_tok.type == TokenType.DOT or next_tok.type == TokenType.LPAREN):
                # This is an assignment, attribute access, or function call
                return self._parse_limit_as_identifier()
            else:
                # Ambiguous, try to parse as statement
                return self.parse_limit_statement()
        elif self.match(TokenType.MATCH):
            # Distinguish between:
            # 1. 'match value: { case ... }' - new pattern matching
            # 2. 'match ... in ... as' - old syntax
            # 3. 'match = ...' - assignment
            # Look ahead to determine which one
            next_tok = self.peek()

            if next_tok and (next_tok.type == TokenType.ASSIGN or next_tok.type == TokenType.LBRACKET or next_tok.type == TokenType.DOT):
                # This is an assignment or attribute access, treat 'match' as identifier
                return self._parse_match_as_identifier()
            else:
                # Need to look further ahead to distinguish between pattern matching and match...in...as
                # Save position and try to parse expression
                saved_pos = self.position
                self.advance()  # consume 'match'

                # Skip to find either COLON (pattern matching) or IN (match...in...as)
                depth = 0
                found_colon = False
                found_in = False
                temp_pos = self.position

                while temp_pos < len(self.tokens):
                    tok = self.tokens[temp_pos]
                    if tok.type in (TokenType.LPAREN, TokenType.LBRACKET, TokenType.LBRACE):
                        depth += 1
                    elif tok.type in (TokenType.RPAREN, TokenType.RBRACKET, TokenType.RBRACE):
                        depth -= 1
                    elif depth == 0:
                        if tok.type == TokenType.COLON:
                            found_colon = True
                            break
                        elif tok.type == TokenType.IN:
                            found_in = True
                            break
                        elif tok.type in (TokenType.NEWLINE, TokenType.EOF):
                            break
                    temp_pos += 1

                # Reset position
                self.position = saved_pos
                self.current_token = self.tokens[self.position] if self.position < len(self.tokens) else None

                if found_colon:
                    # This is 'match value: { case ... }' - new pattern matching
                    return self.parse_match_statement()
                elif found_in:
                    # This is 'match ... in ... as' - old syntax
                    return self.parse_match_in_as()
                else:
                    # Treat as identifier
                    return self._parse_match_as_identifier()
        elif self.match(TokenType.TEMPORAL):
            return self.parse_temporal_block()
        elif self.match(TokenType.WITHIN):
            return self.parse_within_block()
        elif self.match(TokenType.SCHEDULE):
            return self.parse_schedule_block()
        elif self.match(TokenType.DELAY):
            return self.parse_delay_statement()
        elif self.match(TokenType.IDENTIFIER):
            # Delegate to expression statement; it will also handle assignment forms
            return self.parse_expression_statement()
        elif self.match(TokenType.SELF):
            # Delegate to expression statement; it will handle self.x = v and self[i] = v
            return self.parse_expression_statement()
        else:
            return self.parse_expression_statement()

    def parse_hybrid_block(self):
        """Parse a hybrid block"""
        self.eat(TokenType.HYBRID)
        self.eat(TokenType.LBRACE)

        traditional_stmts = []
        logical_stmts = []

        while self.current_token and self.current_token.type != TokenType.RBRACE:
            if self.match(TokenType.QUERY):
                logical_stmts.append(self.parse_query())
            elif self.match(TokenType.RULE):
                logical_stmts.append(self.parse_rule())
            elif self.match(TokenType.FACT):
                logical_stmts.append(self.parse_fact())
            elif self.is_logical_rule():
                # Parse as logical rule
                logical_stmts.append(self.parse_rule())
            elif self.is_logical_fact():
                # Parse as logical fact
                logical_stmts.append(self.parse_fact())
            elif self.is_nominal_phrase():
                # Grammar sugar: nominal phrase like "محمد الطبيب." or with relation hint: "عصير العنب[of]."
                traditional_stmts.append(self.parse_nominal_phrase())
            else:
                stmt = self.parse_statement()
                if stmt:
                    traditional_stmts.append(stmt)

        self.eat(TokenType.RBRACE)
        return HybridBlock(traditional_stmts, logical_stmts)

    def parse_logical_block_as_hybrid(self, name_tok):
        """Parse 'logical { ... }' as a hybrid block with only logical statements"""
        self.eat(TokenType.LBRACE)

        logical_stmts = []

        while self.current_token and self.current_token.type != TokenType.RBRACE:
            if self.match(TokenType.QUERY):
                logical_stmts.append(self.parse_query())
            elif self.match(TokenType.RULE):
                logical_stmts.append(self.parse_rule())
            elif self.match(TokenType.FACT):
                logical_stmts.append(self.parse_fact())
            elif self.is_logical_rule():
                # Parse as logical rule
                logical_stmts.append(self.parse_rule())
            elif self.is_logical_fact():
                # Parse as logical fact
                logical_stmts.append(self.parse_fact())
            else:
                raise SyntaxError(f"Expected logical statement in logical block, got {self.current_token}")

        self.eat(TokenType.RBRACE)
        # Return as HybridBlock with empty traditional statements
        return self._with_pos(HybridBlock([], logical_stmts), name_tok)

    def is_nominal_phrase(self):
        """Lookahead for a nominal phrase statement requiring a trailing DOT.
        Pattern: (IDENT|STRING) (IDENT|STRING) [ '[' (IDENT|STRING) ']' ] '.'
        """
        t1 = self.current_token
        t2 = self.peek(1)
        if not t1 or not t2:
            return False
        if t1.type not in (TokenType.IDENTIFIER, TokenType.STRING):
            return False
        if t2.type not in (TokenType.IDENTIFIER, TokenType.STRING):
            return False
        t3 = self.peek(2)
        if t3 and t3.type == TokenType.DOT:
            return True
        if t3 and t3.type == TokenType.LBRACKET:
            t4 = self.peek(3)
            t5 = self.peek(4)
            t6 = self.peek(5)
            return (
                t4 and t4.type in (TokenType.IDENTIFIER, TokenType.STRING)
                and t5 and t5.type == TokenType.RBRACKET
                and t6 and t6.type == TokenType.DOT
            )
        return False

    def parse_nominal_phrase(self):
        """Parse a nominal phrase into a PhraseStatement AST node."""
        t1 = self.current_token
        self.advance()
        t2 = self.current_token
        self.advance()

        def tok_to_text(tok):
            if tok.type == TokenType.STRING:
                v = tok.value
                if len(v) >= 2 and ((v[0] == '"' and v[-1] == '"') or (v[0] == "'" and v[-1] == "'")):
                    return v[1:-1]
                return v
            return tok.value

        a = tok_to_text(t1)
        b = tok_to_text(t2)
        relation = None
        if self.current_token and self.current_token.type == TokenType.LBRACKET:
            self.eat(TokenType.LBRACKET)
            rel_tok = self.current_token
            if rel_tok.type not in (TokenType.IDENTIFIER, TokenType.STRING):
                raise SyntaxError("Expected relation name inside [ ]")
            self.advance()
            rv = tok_to_text(rel_tok)
            self.eat(TokenType.RBRACKET)
            relation = rv
        self.eat(TokenType.DOT)
        text = f"{a} {b}"
        return PhraseStatement(text, relation)

    def is_logical_fact(self):
        """Check if the current token is a logical fact (identifier/keyword followed by parentheses and dot)"""
        if not self.current_token:
            return False

        # Allow any token that has a value (identifier or keyword) as predicate name
        # Skip tokens that are operators or punctuation
        if self.current_token.type in (TokenType.LPAREN, TokenType.RPAREN, TokenType.LBRACE,
                                       TokenType.RBRACE, TokenType.LBRACKET, TokenType.RBRACKET,
                                       TokenType.COMMA, TokenType.DOT, TokenType.COLON,
                                       TokenType.SEMICOLON, TokenType.OPERATOR, TokenType.ASSIGN,
                                       TokenType.NUMBER, TokenType.STRING, TokenType.EOF):
            return False

        # Look ahead to see if it's followed by ( and eventually )
        saved_pos = self.position
        try:
            self.advance()  # Skip identifier/keyword
            if self.current_token and self.current_token.type == TokenType.LPAREN:
                # Count parentheses to find the matching closing paren
                paren_count = 1
                self.advance()
                while self.current_token and paren_count > 0:
                    if self.current_token.type == TokenType.LPAREN:
                        paren_count += 1
                    elif self.current_token.type == TokenType.RPAREN:
                        paren_count -= 1
                    self.advance()

                # Check if followed by DOT
                result = self.current_token and self.current_token.type == TokenType.DOT
                self.position = saved_pos
                self.current_token = self.tokens[self.position] if self.position < len(self.tokens) else None
                return result
        except:
            pass

        self.position = saved_pos
        self.current_token = self.tokens[self.position] if self.position < len(self.tokens) else None
        return False

    def is_logical_rule(self):
        """Check if the current token is a logical rule (predicate followed by :- and dot)"""
        if not self.current_token:
            return False

        # Allow any token that has a value (identifier or keyword) as predicate name
        # Skip tokens that are operators or punctuation
        if self.current_token.type in (TokenType.LPAREN, TokenType.RPAREN, TokenType.LBRACE,
                                       TokenType.RBRACE, TokenType.LBRACKET, TokenType.RBRACKET,
                                       TokenType.COMMA, TokenType.DOT, TokenType.COLON,
                                       TokenType.SEMICOLON, TokenType.OPERATOR, TokenType.ASSIGN,
                                       TokenType.NUMBER, TokenType.STRING, TokenType.EOF):
            return False

        # Look ahead to see if it's followed by ( and eventually :- and )
        saved_pos = self.position
        try:
            self.advance()  # Skip identifier
            if self.current_token and self.current_token.type == TokenType.LPAREN:
                # Count parentheses to find the matching closing paren
                paren_count = 1
                self.advance()
                while self.current_token and paren_count > 0:
                    if self.current_token.type == TokenType.LPAREN:
                        paren_count += 1
                    elif self.current_token.type == TokenType.RPAREN:
                        paren_count -= 1
                    self.advance()

                # Check if followed by IMPLIES (:-) or ARROW (←)
                result = self.current_token and self.current_token.type in (TokenType.IMPLIES, TokenType.ARROW)
                self.position = saved_pos
                self.current_token = self.tokens[self.position] if self.position < len(self.tokens) else None
                return result
        except:
            pass

        self.position = saved_pos
        self.current_token = self.tokens[self.position] if self.position < len(self.tokens) else None
        return False

    def parse_function_def(self, decorators=None):
        """Parse a function definition (with optional requires/ensures)

        Also allow certain semantic programming keywords (e.g. ``similarity``, ``based_on``)
        to be used as function names, mirroring the behavior in ``parse_primary`` where
        they are allowed as callable identifiers.
        """
        if decorators is None:
            decorators = []
        def_tok = self.eat(TokenType.DEF)

        # Function name can be a normal identifier or certain semantic keywords
        if self.match(TokenType.IDENTIFIER):
            name_tok = self.eat(TokenType.IDENTIFIER)
        elif self.match(TokenType.SIMILARITY) or self.match(TokenType.BASED_ON) or \
             self.match(TokenType.DOMAIN) or self.match(TokenType.MEMORY) or \
             self.match(TokenType.KNOWLEDGE) or self.match(TokenType.PATTERN) or \
             self.match(TokenType.CONCEPT):
            name_tok = self.current_token
            self.advance()
        else:
            raise SyntaxError(f"Expected function name, got {self.current_token}")

        name = name_tok.value
        self.eat(TokenType.LPAREN)
        params = self.parse_parameter_list()
        self.eat(TokenType.RPAREN)
        self.eat(TokenType.COLON)

        # Parse optional requires/ensures clauses before body
        requires_clauses = []
        ensures_clauses = []

        while self.match(TokenType.REQUIRES) or self.match(TokenType.ENSURES):
            if self.match(TokenType.REQUIRES):
                self.advance()  # consume 'requires'
                condition = self.parse_or_expression()
                requires_clauses.append(RequiresClause(condition))
            elif self.match(TokenType.ENSURES):
                self.advance()  # consume 'ensures'
                condition = self.parse_or_expression()
                ensures_clauses.append(EnsuresClause(condition))

        body = self.parse_block()

        # Wrap body with contract checks if needed
        if requires_clauses or ensures_clauses:
            # Store contracts in function for runtime checking
            func_def = self._with_pos(FunctionDef(name, params, body, decorators), def_tok)
            func_def.requires = requires_clauses
            func_def.ensures = ensures_clauses
            return func_def

        return self._with_pos(FunctionDef(name, params, body, decorators), def_tok)

    def parse_decorator(self):
        """Parse a decorator: @name or @name(args)"""
        at_tok = self.eat(TokenType.AT)
        name = self.eat(TokenType.IDENTIFIER).value

        args = []
        if self.match(TokenType.LPAREN):
            self.eat(TokenType.LPAREN)
            if not self.match(TokenType.RPAREN):
                args.append(self.parse_expression())
                while self.match(TokenType.COMMA):
                    self.eat(TokenType.COMMA)
                    args.append(self.parse_expression())
            self.eat(TokenType.RPAREN)

        return self._with_pos(Decorator(name, args), at_tok)

    def parse_async_function_def(self, decorators=None):
        """Parse an async function definition: async def name(params): body

        Like ``parse_function_def``, allow certain semantic keywords as function names.
        """
        if decorators is None:
            decorators = []
        async_tok = self.eat(TokenType.ASYNC)
        self.eat(TokenType.DEF)

        if self.match(TokenType.IDENTIFIER):
            name_tok = self.eat(TokenType.IDENTIFIER)
        elif self.match(TokenType.SIMILARITY) or self.match(TokenType.BASED_ON):
            name_tok = self.current_token
            self.advance()
        else:
            self._error("Expected async function name", self.current_token)

        name = name_tok.value
        self.eat(TokenType.LPAREN)
        params = self.parse_parameter_list()
        self.eat(TokenType.RPAREN)
        self.eat(TokenType.COLON)
        body = self.parse_block()

        func_def = AsyncFunctionDef(name, params, body)
        func_def.decorators = decorators
        return self._with_pos(func_def, async_tok)

    def parse_parameter_list(self):
        """Parse function parameters with support for default values, *args, and **kwargs"""
        params = []

        if not self.match(TokenType.RPAREN):
            # Parse first parameter
            is_varargs = False
            is_kwargs = False

            # Check for **kwargs or *args
            if self.match(TokenType.OPERATOR):
                if self.current_token.value == '**':
                    self.advance()  # consume **
                    is_kwargs = True
                elif self.current_token.value == '*':
                    self.advance()  # consume *
                    is_varargs = True

            # Get parameter name (could be 'self' or identifier)
            if self.match(TokenType.SELF):
                param_name = self.eat(TokenType.SELF).value
            else:
                param_name = self.eat(TokenType.IDENTIFIER).value

            default_value = None

            # Check for default value (not allowed for *args/**kwargs)
            if not is_varargs and not is_kwargs and self.match(TokenType.ASSIGN):
                self.eat(TokenType.ASSIGN)
                default_value = self.parse_expression()

            params.append(Parameter(param_name, default_value, is_varargs, is_kwargs))

            # Parse remaining parameters
            while self.match(TokenType.COMMA):
                self.eat(TokenType.COMMA)

                is_varargs = False
                is_kwargs = False

                # Check for **kwargs or *args
                if self.match(TokenType.OPERATOR):
                    if self.current_token.value == '**':
                        self.advance()  # consume **
                        is_kwargs = True
                    elif self.current_token.value == '*':
                        self.advance()  # consume *
                        is_varargs = True

                # Could be 'self' or identifier or semantic keyword
                if self.match(TokenType.SELF):
                    param_name = self.eat(TokenType.SELF).value
                elif self.match(TokenType.IDENTIFIER):
                    param_name = self.eat(TokenType.IDENTIFIER).value
                else:
                    # Allow semantic keywords as parameter names
                    param_tok = self.eat_attribute_name()
                    param_name = param_tok.value

                default_value = None

                # Check for default value (not allowed for *args/**kwargs)
                if not is_varargs and not is_kwargs and self.match(TokenType.ASSIGN):
                    self.eat(TokenType.ASSIGN)
                    default_value = self.parse_expression()

                params.append(Parameter(param_name, default_value, is_varargs, is_kwargs))

        return params

    def parse_block(self):
        """Parse a block of statements"""
        self.eat(TokenType.LBRACE)
        statements = []

        while self.current_token and self.current_token.type != TokenType.RBRACE:
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)

        self.eat(TokenType.RBRACE)
        return Block(statements)

    def parse_class_def(self, decorators=None):
        """Parse a class definition"""
        if decorators is None:
            decorators = []
        class_tok = self.eat(TokenType.CLASS)
        name = self.eat(TokenType.IDENTIFIER).value

        base_class = None
        base_classes = None
        if self.match(TokenType.LPAREN):
            self.eat(TokenType.LPAREN)
            bases = []
            # Allow zero or more bases? We'll require at least one if parens present
            bases.append(self.eat(TokenType.IDENTIFIER).value)
            while self.match(TokenType.COMMA):
                self.eat(TokenType.COMMA)
                bases.append(self.eat(TokenType.IDENTIFIER).value)
            self.eat(TokenType.RPAREN)
            base_classes = bases
            base_class = bases[0] if bases else None

        self.eat(TokenType.COLON)
        body = self.parse_block()

        return self._with_pos(ClassDef(name, base_class, body, base_classes=base_classes, decorators=decorators), class_tok)

    def parse_if_statement(self):
        """Parse an if statement with optional elif chain and else"""
        if_tok = self.eat(TokenType.IF)
        condition = self.parse_expression()
        self.eat(TokenType.COLON)
        then_branch = self.parse_block()

        # Collect zero or more elif branches
        elif_branches = []
        while self.match(TokenType.ELIF):
            self.eat(TokenType.ELIF)
            elif_cond = self.parse_expression()
            self.eat(TokenType.COLON)
            elif_block = self.parse_block()
            elif_branches.append((elif_cond, elif_block))

        # Optional else branch
        else_branch = None
        if self.match(TokenType.ELSE):
            self.eat(TokenType.ELSE)
            self.eat(TokenType.COLON)
            else_branch = self.parse_block()

        # Build nested IfStatements for elif chain (right-associative)
        current_else = else_branch
        for cond, block in reversed(elif_branches):
            current_else = self._with_pos(IfStatement(cond, block, current_else), if_tok)

        return self._with_pos(IfStatement(condition, then_branch, current_else), if_tok)

    def parse_for_loop(self):
        """Parse a for loop (with optional invariants)"""
        for_tok = self.eat(TokenType.FOR)
        var_name = self.eat(TokenType.IDENTIFIER).value
        self.eat(TokenType.IN)
        iterable = self.parse_expression()
        self.eat(TokenType.COLON)

        # Parse optional invariants before body
        invariants = []
        while self.match(TokenType.INVARIANT):
            self.advance()  # consume 'invariant'
            condition = self.parse_or_expression()
            invariants.append(InvariantClause(condition))

        body = self.parse_block()

        # Store invariants in loop for runtime checking
        loop = self._with_pos(ForLoop(var_name, iterable, body), for_tok)
        if invariants:
            loop.invariants = invariants
        return loop

    def parse_while_loop(self):
        """Parse a while loop (with optional invariants)"""
        while_tok = self.eat(TokenType.WHILE)
        condition = self.parse_expression()
        self.eat(TokenType.COLON)

        # Parse optional invariants before body
        invariants = []
        while self.match(TokenType.INVARIANT):
            self.advance()  # consume 'invariant'
            inv_condition = self.parse_or_expression()
            invariants.append(InvariantClause(inv_condition))

        body = self.parse_block()

        # Store invariants in loop for runtime checking
        loop = self._with_pos(WhileLoop(condition, body), while_tok)
        if invariants:
            loop.invariants = invariants
        return loop

    def parse_return_statement(self):
        """Parse a return statement"""
        ret_tok = self.eat(TokenType.RETURN)
        value = None
        if not self.match(TokenType.SEMICOLON, TokenType.RBRACE, TokenType.EOF):
            value = self.parse_expression()
        return self._with_pos(ReturnStatement(value), ret_tok)

    def parse_yield_statement(self):
        """Parse a yield statement"""
        yield_tok = self.eat(TokenType.YIELD)
        value = None
        if not self.match(TokenType.SEMICOLON, TokenType.RBRACE, TokenType.EOF):
            value = self.parse_expression()
        return self._with_pos(YieldExpr(value), yield_tok)

    def parse_with_statement(self):
        """Parse a with statement: with expr as var: { body }"""
        with_tok = self.eat(TokenType.WITH)
        context_expr = self.parse_expression()

        target_var = None
        if self.match(TokenType.AS):
            self.eat(TokenType.AS)
            target_var = self.eat(TokenType.IDENTIFIER).value

        self.eat(TokenType.COLON)
        body = self.parse_block()

        return self._with_pos(WithStatement(context_expr, target_var, body), with_tok)

    def parse_raise_statement(self):
        """Parse a raise statement"""
        raise_tok = self.eat(TokenType.RAISE)
        value = None
        if not self.match(TokenType.SEMICOLON, TokenType.RBRACE, TokenType.EOF):
            value = self.parse_expression()
        return self._with_pos(RaiseStatement(value), raise_tok)

    def parse_try_statement(self):
        """Parse a try/except[/except...][finally] statement"""
        try_tok = self.eat(TokenType.TRY)
        self.eat(TokenType.COLON)
        try_block = self.parse_block()

        handlers = []
        finally_block = None

        # One or more except blocks
        while self.match(TokenType.EXCEPT):
            self.eat(TokenType.EXCEPT)
            type_name = None
            alias = None
            # except : (catch-all)
            if not self.match(TokenType.COLON):
                # except Type [as name] :
                type_name = self.eat(TokenType.IDENTIFIER).value
                if self.match(TokenType.AS):
                    self.eat(TokenType.AS)
                    alias = self.eat(TokenType.IDENTIFIER).value
            self.eat(TokenType.COLON)
            body = self.parse_block()
            handlers.append(self._with_pos(ExceptHandler(type_name, alias, body), try_tok))

        # Optional finally
        if self.match(TokenType.FINALLY):
            self.eat(TokenType.FINALLY)
            self.eat(TokenType.COLON)
            finally_block = self.parse_block()

        if not handlers and not finally_block:
            raise SyntaxError("'try' must be followed by at least one 'except' or a 'finally'")

        return self._with_pos(TryExceptFinally(try_block, handlers, finally_block), try_tok)

    def parse_print_statement(self):
        """Parse a print statement with support for multiple arguments"""
        pr_tok = self.eat(TokenType.PRINT)
        self.eat(TokenType.LPAREN)

        # Parse first expression
        values = [self.parse_expression()]

        # Parse additional expressions separated by commas
        while self.match(TokenType.COMMA):
            self.eat(TokenType.COMMA)
            values.append(self.parse_expression())

        self.eat(TokenType.RPAREN)

        # If single value, use old behavior
        if len(values) == 1:
            return self._with_pos(PrintStatement(values[0]), pr_tok)
        else:
            # Multiple values - return a PrintStatement with a list
            return self._with_pos(PrintStatement(values), pr_tok)

    def parse_assignment(self):
        """Parse an assignment target and value
        Supports: x = v, obj.attr = v, obj[index] = v, and chained obj.attr[index] = v
        """
        # Parse the left-hand side as a primary expression
        # This allows for simple variables like 'x'
        name_tok = self.current_token
        if not self.match(TokenType.IDENTIFIER):
            raise SyntaxError(f"Expected identifier in assignment, got {self.current_token}")

        base_name = self.eat(TokenType.IDENTIFIER).value
        target_expr = self._with_pos(Variable(base_name), name_tok)

        # Parse chained attribute/subscript access on the target
        while self.match(TokenType.DOT) or self.match(TokenType.LBRACKET):
            if self.match(TokenType.DOT):
                self.eat(TokenType.DOT)
                attr_tok = self.eat_attribute_name()
                attr_name = attr_tok.value
                target_expr = self._with_pos(AttributeAccess(target_expr, attr_name), attr_tok)
            else:
                lb_tok = self.eat(TokenType.LBRACKET)
                index_expr = self.parse_subscript_or_slice()
                self.eat(TokenType.RBRACKET)
                target_expr = self._with_pos(SubscriptAccess(target_expr, index_expr), lb_tok)

        # Now parse assignment operator and value
        if not self.match(TokenType.ASSIGN):
            raise SyntaxError(f"Expected '=' in assignment, got {self.current_token}")

        assign_tok = self.eat(TokenType.ASSIGN)
        value = self.parse_expression()

        # Build appropriate assignment node
        if isinstance(target_expr, Variable):
            return self._with_pos(Assignment(target_expr.name, value), name_tok)
        elif isinstance(target_expr, AttributeAccess):
            return self._with_pos(AttributeAssignment(target_expr.object_expr, target_expr.attribute_name, value), assign_tok)
        elif isinstance(target_expr, SubscriptAccess):
            return self._with_pos(SubscriptAssignment(target_expr.object_expr, target_expr.index_expr, value), assign_tok)
        else:
            raise SyntaxError("Invalid assignment target")

    def parse_expression_statement(self):
        """Parse an expression statement or assignment"""
        # Special handling for keywords as identifiers in assignment context
        if (self.match(TokenType.WHERE) or self.match(TokenType.FROM)) and self.peek() and self.peek().type == TokenType.ASSIGN:
            name_tok = self.current_token
            self.advance()
            self.eat(TokenType.ASSIGN)
            value = self.parse_expression()
            return Assignment(name_tok.value, value)

        expr = self.parse_expression()

        # Sample assignment sugar: <var> ~ Dist(args)
        if isinstance(expr, Variable) and self.match(TokenType.TILDE):
            tilde_tok = self.eat(TokenType.TILDE)
            name_tok = self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.LPAREN)
            args, named_args = self.parse_argument_list()
            self.eat(TokenType.RPAREN)
            dist_call = self._with_pos(FunctionCall(name_tok.value, args, named_args), name_tok)
            return self._with_pos(SampleAssign(expr.name, dist_call), tilde_tok)

        # Special sugar: Head(Key:Score, ...) -> SimilarityDecl statement
        if isinstance(expr, FunctionCall):
            if not expr.named_arguments and expr.arguments and all(isinstance(a, KeyValuePair) for a in expr.arguments):
                # Allow optional trailing '.'
                if self.match(TokenType.DOT):
                    self.eat(TokenType.DOT)
                head_name = getattr(expr, 'function_name', getattr(expr, 'name', None))
                return SimilarityDecl(head_name, expr.arguments)

        # Check if this is a logical fact or rule (ends with DOT or has IMPLIES)
        if self.match(TokenType.DOT):
            # This is a fact: predicate(args).
            self.eat(TokenType.DOT)
            # Convert FunctionCall to Predicate
            if isinstance(expr, FunctionCall):
                from .ast_nodes import Predicate, LogicalFact
                predicate = Predicate(expr.function_name, expr.arguments)
                return LogicalFact(predicate)
            return expr
        elif self.match(TokenType.IMPLIES):
            # This is a rule: head :- body.
            self.eat(TokenType.IMPLIES)
            body = self.parse_logical_body()
            if self.match(TokenType.DOT):
                self.eat(TokenType.DOT)
            # Convert FunctionCall to Predicate
            if isinstance(expr, FunctionCall):
                from .ast_nodes import Predicate, LogicalRule
                head = Predicate(expr.function_name, expr.arguments)
                return LogicalRule(head, body)
            return expr
        # Check if this is an assignment (expr = value)
        elif self.match(TokenType.ASSIGN):
            self.eat(TokenType.ASSIGN)
            value = self.parse_expression()

            # Build appropriate assignment node
            if isinstance(expr, Variable):
                return Assignment(expr.name, value)
            elif isinstance(expr, AttributeAccess):
                return AttributeAssignment(expr.object_expr, expr.attribute_name, value)
            elif isinstance(expr, SubscriptAccess):
                return SubscriptAssignment(expr.object_expr, expr.index_expr, value)
            else:
                raise SyntaxError(f"Invalid assignment target: {expr}")

        return expr

    def parse_expression(self):
        """Parse an expression (with optional where clause)"""
        expr = self.parse_pipeline_expression()

        # Check for where clause
        # Only treat 'where' as clause keyword if it's not already parsed as part of the expression
        # (e.g., if expr is Variable('where'), don't try to parse where clause)
        # Also, don't treat 'where' as clause if it's followed by '=' (it's an assignment statement)
        if self.match(TokenType.WHERE):
            # Check if this is a where clause or just 'where' used as identifier/assignment
            next_tok = self.peek()
            is_assignment = next_tok and next_tok.type == TokenType.ASSIGN
            is_variable_where = isinstance(expr, Variable) and expr.name == 'where'

            if not is_assignment and not is_variable_where:
                self.advance()  # consume 'where'
                condition = self.parse_pipeline_expression()
                expr = WhereClause(expr, condition)

        return expr

    def parse_pipeline_expression(self):
        """Parse pipeline expression: value |> function |> function2"""
        left = self.parse_composition_expression()

        while self.match(TokenType.PIPELINE):
            tok = self.current_token
            self.advance()
            right = self.parse_composition_expression()
            left = self._with_pos(PipelineOp(left, right), tok)

        return left

    def parse_composition_expression(self):
        """Parse function composition: f >> g >> h"""
        left = self.parse_or_expression()

        while self.match(TokenType.COMPOSE):
            tok = self.current_token
            self.advance()
            right = self.parse_or_expression()
            left = self._with_pos(ComposeOp(left, right), tok)

        return left

    def parse_or_expression(self):
        """Parse logical OR expression"""
        left = self.parse_and_expression()

        while self.match(TokenType.OR):
            tok = self.current_token
            self.advance()
            right = self.parse_and_expression()
            left = self._with_pos(BinaryOp('or', left, right), tok)

        return left

    def parse_and_expression(self):
        """Parse logical AND expression"""
        left = self.parse_comparison()

        while self.match(TokenType.AND):
            tok = self.current_token
            self.advance()
            right = self.parse_comparison()
            left = self._with_pos(BinaryOp('and', left, right), tok)

        return left

    def parse_comparison(self):
        """Parse comparison expression"""
        left = self.parse_additive()

        while self.match(TokenType.OPERATOR) or self.match(TokenType.IN):
            if self.match(TokenType.IN):
                tok_in = self.eat(TokenType.IN)
                right = self.parse_additive()
                left = self._with_pos(BinaryOp('in', left, right), tok_in)
            else:
                op_tok = self.eat(TokenType.OPERATOR)
                op = op_tok.value
                right = self.parse_additive()
                left = self._with_pos(BinaryOp(op, left, right), op_tok)

        return left

    def parse_additive(self):
        """Parse addition/subtraction"""
        left = self.parse_multiplicative()

        while self.match(TokenType.OPERATOR) and self.current_token.value in ['+', '-']:
            op_tok = self.eat(TokenType.OPERATOR)
            op = op_tok.value
            right = self.parse_multiplicative()
            left = self._with_pos(BinaryOp(op, left, right), op_tok)

        return left

    def parse_multiplicative(self):
        """Parse multiplication/division"""
        left = self.parse_unary()

        while self.match(TokenType.OPERATOR) and self.current_token.value in ['*', '/', '%']:
            op_tok = self.eat(TokenType.OPERATOR)
            op = op_tok.value
            right = self.parse_unary()
            left = self._with_pos(BinaryOp(op, left, right), op_tok)

        return left

    def parse_unary(self):
        """Parse unary expressions"""
        if self.match(TokenType.NOT):
            tok = self.current_token
            self.advance()
            operand = self.parse_unary()
            return self._with_pos(UnaryOp('not', operand), tok)
        elif self.match(TokenType.OPERATOR) and self.current_token.value == '-':
            tok = self.current_token
            self.advance()
            operand = self.parse_unary()
            return self._with_pos(UnaryOp('-', operand), tok)

        return self.parse_primary()

    def parse_primary(self):
        """Parse primary expressions"""
        if self.match(TokenType.AWAIT):
            await_tok = self.eat(TokenType.AWAIT)
            expr = self.parse_primary()
            return self._with_pos(AwaitExpr(expr), await_tok)

        elif self.match(TokenType.NUMBER):
            tok = self.eat(TokenType.NUMBER)
            value = tok.value
            return self._with_pos(Number(float(value) if '.' in value else int(value)), tok)

        elif self.match(TokenType.STRING):
            tok = self.eat(TokenType.STRING)
            value = tok.value
            # Remove quotes (support triple-quoted strings)
            if (value.startswith('"""') and value.endswith('"""')) or (value.startswith("'''") and value.endswith("'''")):
                inner = value[3:-3]
            else:
                inner = value[1:-1]
            inner = self._unescape_string(inner)
            return self._with_pos(String(inner), tok)

        elif self.match(TokenType.TRUE):
            tok = self.eat(TokenType.TRUE)
            return self._with_pos(Boolean(True), tok)

        elif self.match(TokenType.FALSE):
            tok = self.eat(TokenType.FALSE)
            return self._with_pos(Boolean(False), tok)

        elif self.match(TokenType.NONE):
            tok = self.eat(TokenType.NONE)
            # Treat None as a true literal, not as a variable name
            return self._with_pos(NoneLiteral(), tok)

        elif self.match(TokenType.VARIABLE):
            # Logical variable
            tok = self.eat(TokenType.VARIABLE)
            name = tok.value
            return self._with_pos(Variable(name), tok)

        elif self.match(TokenType.MATCH) or self.match(TokenType.LIMIT):
            # Allow 'match' and 'limit' as identifier/function name for backward compatibility
            if self.match(TokenType.MATCH):
                name_tok = self.eat(TokenType.MATCH)
                name = 'match'
            else:
                name_tok = self.eat(TokenType.LIMIT)
                name = 'limit'

            if self.match(TokenType.LPAREN):
                # Function call: match(...) or limit(...)
                self.eat(TokenType.LPAREN)
                args, named_args = self.parse_argument_list()
                self.eat(TokenType.RPAREN)
                expr = self._with_pos(FunctionCall(name, args, named_args), name_tok)
                return expr
            else:
                # Just the keyword as identifier
                return self._with_pos(Variable(name), name_tok)

        # Allow cognitive-semantic and semantic programming keywords as identifiers in dict context
        elif self.match(TokenType.ROLE) or self.match(TokenType.DEGREE) or \
             self.match(TokenType.STATE_CHANGES) or self.match(TokenType.ENTITIES) or \
             self.match(TokenType.RESULT) or self.match(TokenType.PARTICIPANTS) or \
             self.match(TokenType.STRENGTH) or self.match(TokenType.TRANSFORM) or \
             self.match(TokenType.REACTIONS) or self.match(TokenType.STRUCTURE) or \
             self.match(TokenType.EXPRESS) or self.match(TokenType.LINGUISTIC_FORMS) or \
             self.match(TokenType.CONTENT) or self.match(TokenType.CONTEXT) or \
             self.match(TokenType.TIME) or self.match(TokenType.PLACE) or \
             self.match(TokenType.SOURCE) or self.match(TokenType.CERTAINTY) or \
             self.match(TokenType.CURRENT_VALUE) or self.match(TokenType.HISTORY) or \
             self.match(TokenType.FUTURE_PREDICTION) or self.match(TokenType.ROOT) or \
             self.match(TokenType.TAXONOMY) or self.match(TokenType.CHARACTERS) or \
             self.match(TokenType.EVENT) or self.match(TokenType.DOMAIN) or \
             self.match(TokenType.MEMORY) or self.match(TokenType.KNOWLEDGE) or \
             self.match(TokenType.PATTERN) or self.match(TokenType.CONCEPT) or \
             self.match(TokenType.DEFAULT) or self.match(TokenType.WHERE) or \
             self.match(TokenType.FROM) or self.match(TokenType.FIRST):
            # Allow these keywords as identifiers (for dict keys)
            name_tok = self.current_token
            self.advance()
            name = name_tok.value

            if self.match(TokenType.LPAREN):
                # Function call
                self.eat(TokenType.LPAREN)
                args, named_args = self.parse_argument_list()
                self.eat(TokenType.RPAREN)
                expr = self._with_pos(FunctionCall(name, args, named_args), name_tok)

                # Check for chained access after function call
                while self.match(TokenType.DOT) or self.match(TokenType.LBRACKET):
                    if self.match(TokenType.DOT):
                        self.eat(TokenType.DOT)
                        attr_tok = self.eat_attribute_name()
                        attr_name = attr_tok.value
                        if self.match(TokenType.LPAREN):
                            self.eat(TokenType.LPAREN)
                            args, named_args = self.parse_argument_list()
                            self.eat(TokenType.RPAREN)
                            expr = self._with_pos(MethodCall(expr, attr_name, args, named_args), attr_tok)
                        else:
                            expr = self._with_pos(AttributeAccess(expr, attr_name), attr_tok)
                    else:
                        lb_tok = self.eat(TokenType.LBRACKET)
                        index_expr = self.parse_subscript_or_slice()
                        self.eat(TokenType.RBRACKET)
                        expr = self._with_pos(SubscriptAccess(expr, index_expr), lb_tok)
                return expr

            # Support chained access after these keywords as identifiers
            expr = self._with_pos(Variable(name), name_tok)

            while self.match(TokenType.DOT) or self.match(TokenType.LBRACKET):
                if self.match(TokenType.DOT):
                    self.eat(TokenType.DOT)
                    attr_tok = self.eat_attribute_name()
                    attr_name = attr_tok.value

                    if self.match(TokenType.LPAREN):
                        self.eat(TokenType.LPAREN)
                        args, named_args = self.parse_argument_list()
                        self.eat(TokenType.RPAREN)
                        expr = self._with_pos(MethodCall(expr, attr_name, args, named_args), attr_tok)
                    else:
                        expr = self._with_pos(AttributeAccess(expr, attr_name), attr_tok)
                else:
                    lb_tok = self.eat(TokenType.LBRACKET)
                    index_expr = self.parse_subscript_or_slice()
                    self.eat(TokenType.RBRACKET)
                    expr = self._with_pos(SubscriptAccess(expr, index_expr), lb_tok)

            return expr

        elif self.match(TokenType.IDENTIFIER):
            name_tok = self.eat(TokenType.IDENTIFIER)
            name = name_tok.value

            # Special handling for 'logical {' - parse as hybrid block
            if name == 'logical' and self.match(TokenType.LBRACE):
                return self.parse_logical_block_as_hybrid(name_tok)

            # Sugar: collect/topk/argmax expressions (only when next tokens match the pattern)
            lname = name.lower()
            if lname in ('collect', 'اجمع') and self.match(TokenType.VARIABLE):
                return self._parse_collect_sugar(name_tok)
            if lname == 'topk' and self.match(TokenType.NUMBER):
                return self._parse_topk_sugar(name_tok)
            if lname == 'argmax' and self.match(TokenType.VARIABLE):
                return self._parse_argmax_sugar(name_tok)
            if lname in ('choose', 'اختر') and self.match(TokenType.LBRACE):
                mapping = self.parse_dict()
                return self._with_pos(ChooseExpr(mapping), name_tok)

            if self.match(TokenType.LPAREN):
                # Function call
                self.eat(TokenType.LPAREN)
                args, named_args = self.parse_argument_list()
                self.eat(TokenType.RPAREN)
                expr = self._with_pos(FunctionCall(name, args, named_args), name_tok)

                # Check for chained access: . or [ ] after a function call result
                while self.match(TokenType.DOT) or self.match(TokenType.LBRACKET):
                    if self.match(TokenType.DOT):
                        self.eat(TokenType.DOT)
                        attr_tok = self.eat_attribute_name()
                        attr_name = attr_tok.value

                        if self.match(TokenType.LPAREN):
                            self.eat(TokenType.LPAREN)
                            args, named_args = self.parse_argument_list()
                            self.eat(TokenType.RPAREN)
                            expr = self._with_pos(MethodCall(expr, attr_name, args, named_args), attr_tok)
                        else:
                            expr = self._with_pos(AttributeAccess(expr, attr_name), attr_tok)
                    else:
                        # Subscription: expr[index] or expr[start:end:step]
                        lb_tok = self.eat(TokenType.LBRACKET)
                        index_expr = self.parse_subscript_or_slice()
                        self.eat(TokenType.RBRACKET)
                        expr = self._with_pos(SubscriptAccess(expr, index_expr), lb_tok)

                return expr
            elif self.match(TokenType.DOT) or self.match(TokenType.LBRACKET):
                # Attribute access or method call starting from a variable
                expr = self._with_pos(Variable(name), name_tok)

                while self.match(TokenType.DOT) or self.match(TokenType.LBRACKET):
                    if self.match(TokenType.DOT):
                        self.eat(TokenType.DOT)
                        attr_tok = self.eat_attribute_name()
                        attr_name = attr_tok.value

                        if self.match(TokenType.LPAREN):
                            # Method call
                            self.eat(TokenType.LPAREN)
                            args, named_args = self.parse_argument_list()
                            self.eat(TokenType.RPAREN)
                            expr = self._with_pos(MethodCall(expr, attr_name, args, named_args), attr_tok)
                        else:
                            # Attribute access
                            expr = self._with_pos(AttributeAccess(expr, attr_name), attr_tok)
                    else:
                        # Subscription: expr[index] or expr[start:end:step]
                        lb_tok = self.eat(TokenType.LBRACKET)
                        index_expr = self.parse_subscript_or_slice()
                        self.eat(TokenType.RBRACKET)
                        expr = self._with_pos(SubscriptAccess(expr, index_expr), lb_tok)

                return expr
            else:
                return self._with_pos(Variable(name), name_tok)

        elif self.match(TokenType.LBRACKET):
            return self.parse_list()

        elif self.match(TokenType.LBRACE):
            return self.parse_dict()

        elif self.match(TokenType.SELF):
            tok_self = self.current_token
            self.advance()
            expr = self._with_pos(SelfReference(), tok_self)

            # Allow chained access after self: . or [ ]
            while self.match(TokenType.DOT) or self.match(TokenType.LBRACKET):
                if self.match(TokenType.DOT):
                    self.eat(TokenType.DOT)
                    attr_tok = self.eat_attribute_name()
                    attr_name = attr_tok.value

                    if self.match(TokenType.LPAREN):
                        # Method call
                        self.eat(TokenType.LPAREN)
                        args, named_args = self.parse_argument_list()
                        self.eat(TokenType.RPAREN)
                        expr = self._with_pos(MethodCall(expr, attr_name, args, named_args), attr_tok)
                    else:
                        # Attribute access
                        expr = self._with_pos(AttributeAccess(expr, attr_name), attr_tok)
                else:
                    # Subscription: self[index] or self[start:end:step]
                    lb_tok = self.eat(TokenType.LBRACKET)
                    index_expr = self.parse_subscript_or_slice()
                    self.eat(TokenType.RBRACKET)
                    expr = self._with_pos(SubscriptAccess(expr, index_expr), lb_tok)

            return expr

        elif self.match(TokenType.SUPER):
            self.eat(TokenType.SUPER)
            self.eat(TokenType.LPAREN)
            # Support both: super(method[, args]) and super().method(args)
            if self.match(TokenType.RPAREN):
                # super().method(args)
                self.eat(TokenType.RPAREN)
                self.eat(TokenType.DOT)
                method_name = self.eat(TokenType.IDENTIFIER).value
                self.eat(TokenType.LPAREN)
                args, named_args = self.parse_argument_list()
                self.eat(TokenType.RPAREN)
                return SuperCall(method_name, args, named_args)
            else:
                # Legacy form: super(method[, args])
                method_name = self.eat(TokenType.IDENTIFIER).value
                args = []
                named_args = {}
                if self.match(TokenType.COMMA):
                    self.eat(TokenType.COMMA)
                    args, named_args = self.parse_argument_list()
                self.eat(TokenType.RPAREN)
                return SuperCall(method_name, args, named_args)

        elif self.match(TokenType.LPAREN):
            lp_tok = self.eat(TokenType.LPAREN)

            # Empty tuple: ()
            if self.match(TokenType.RPAREN):
                self.eat(TokenType.RPAREN)
                return self._with_pos(Tuple([]), lp_tok)

            # Parse first expression
            first_expr = self.parse_expression()

            # Check if this is a tuple (has comma) or just grouped expression
            if self.match(TokenType.COMMA):
                # This is a tuple
                elements = [first_expr]
                while self.match(TokenType.COMMA):
                    self.eat(TokenType.COMMA)
                    # Allow trailing comma
                    if self.match(TokenType.RPAREN):
                        break
                    elements.append(self.parse_expression())
                self.eat(TokenType.RPAREN)
                return self._with_pos(Tuple(elements), lp_tok)
            else:
                # Just a grouped expression
                self.eat(TokenType.RPAREN)
                expr = first_expr

                # Check for chained access: . or [ ] after a parenthesized expression
                while self.match(TokenType.DOT) or self.match(TokenType.LBRACKET):
                    if self.match(TokenType.DOT):
                        self.eat(TokenType.DOT)
                        attr_tok = self.eat_attribute_name()
                        attr_name = attr_tok.value

                        if self.match(TokenType.LPAREN):
                            self.eat(TokenType.LPAREN)
                            args, named_args = self.parse_argument_list()
                            self.eat(TokenType.RPAREN)
                            expr = self._with_pos(MethodCall(expr, attr_name, args, named_args), attr_tok)
                        else:
                            expr = self._with_pos(AttributeAccess(expr, attr_name), attr_tok)
                    else:
                        # Subscription: expr[index] or expr[start:end:step]
                        lb_tok = self.eat(TokenType.LBRACKET)
                        index_expr = self.parse_subscript_or_slice()
                        self.eat(TokenType.RBRACKET)
                        expr = self._with_pos(SubscriptAccess(expr, index_expr), lb_tok)

                return expr

        # Allow semantic programming keywords as function names
        elif self.match(TokenType.SIMILARITY) or self.match(TokenType.BASED_ON):
            name_tok = self.current_token
            self.advance()
            name = name_tok.value

            if self.match(TokenType.LPAREN):
                # Function call
                self.eat(TokenType.LPAREN)
                args, named_args = self.parse_argument_list()
                self.eat(TokenType.RPAREN)
                expr = self._with_pos(FunctionCall(name, args, named_args), name_tok)

                # Check for chained access after function call
                while self.match(TokenType.DOT) or self.match(TokenType.LBRACKET):
                    if self.match(TokenType.DOT):
                        self.eat(TokenType.DOT)
                        attr_tok = self.eat_attribute_name()
                        attr_name = attr_tok.value

                        if self.match(TokenType.LPAREN):
                            self.eat(TokenType.LPAREN)
                            args, named_args = self.parse_argument_list()
                            self.eat(TokenType.RPAREN)
                            expr = self._with_pos(MethodCall(expr, attr_name, args, named_args), attr_tok)
                        else:
                            expr = self._with_pos(AttributeAccess(expr, attr_name), attr_tok)
                    else:
                        # Subscription: expr[index] or expr[start:end:step]
                        lb_tok = self.eat(TokenType.LBRACKET)
                        index_expr = self.parse_subscript_or_slice()
                        self.eat(TokenType.RBRACKET)
                        expr = self._with_pos(SubscriptAccess(expr, index_expr), lb_tok)

                return expr
            else:
                # Just a variable reference
                return self._with_pos(Variable(name), name_tok)

        # Existential query as expression
        elif self.match(TokenType.EXISTENTIAL_QUERY):
            tok = self.eat(TokenType.EXISTENTIAL_QUERY)
            self.eat(TokenType.COLON)
            config = self.parse_entity_body()
            return self._with_pos(ExistentialQuery(config), tok)

        else:
            raise SyntaxError(f"Unexpected token: {self.current_token}")
    def _parse_collect_sugar(self, start_tok):
        # Expect VARIABLE then FROM/"from"/"من" then logical predicate
        if not self.match(TokenType.VARIABLE):
            raise SyntaxError("collect expects a logical variable, e.g., collect ?X from ...")
        var_tok = self.eat(TokenType.VARIABLE)
        var_name = var_tok.value[1:]  # strip leading '?'

        # FROM token or identifier 'from' / Arabic 'من'
        if self.match(TokenType.FROM):
            self.eat(TokenType.FROM)
        else:
            if not (self.match(TokenType.IDENTIFIER) and self.current_token.value in ('from', 'من')):
                raise SyntaxError("collect syntax: collect ?X from predicate(...)")
            self.eat(TokenType.IDENTIFIER)

        goal = self.parse_logical_predicate()

        # Optional: limit N
        limit = None
        unique = False
        # Check for both LIMIT token and 'limit' identifier for backward compatibility
        if self.match(TokenType.LIMIT) or (self.match(TokenType.IDENTIFIER) and self.current_token.value.lower() in ('limit', 'حد')):
            if self.match(TokenType.LIMIT):
                self.eat(TokenType.LIMIT)
            else:
                self.eat(TokenType.IDENTIFIER)
            if not self.match(TokenType.NUMBER):
                raise SyntaxError("limit expects a number")
            n_tok = self.eat(TokenType.NUMBER)
            limit = int(n_tok.value)
        # Optional: unique
        if self.match(TokenType.IDENTIFIER) and self.current_token.value.lower() == 'unique':
            self.eat(TokenType.IDENTIFIER)
            unique = True

        from .ast_nodes import CollectExpr
        return self._with_pos(CollectExpr(var_name, goal, limit=limit, unique=unique), start_tok)

    def _parse_topk_sugar(self, start_tok):
        # topk K of ?Var by ?Score where predicate(...)
        if not self.match(TokenType.NUMBER):
            raise SyntaxError("topk expects a number: topk 3 of ?Y by ?S where ...")
        k_tok = self.eat(TokenType.NUMBER)
        k = int(k_tok.value)
        # 'of'
        if not (self.match(TokenType.IDENTIFIER) and self.current_token.value.lower() == 'of'):
            raise SyntaxError("topk syntax: topk K of ?Var by ?Score where predicate(...)")
        self.eat(TokenType.IDENTIFIER)
        # ?Var
        if not self.match(TokenType.VARIABLE):
            raise SyntaxError("topk expects a logical variable after 'of'")
        var_tok = self.eat(TokenType.VARIABLE)
        var_name = var_tok.value[1:]
        # 'by'
        if not (self.match(TokenType.IDENTIFIER) and self.current_token.value.lower() == 'by'):
            raise SyntaxError("topk expects 'by ?Score'")
        self.eat(TokenType.IDENTIFIER)
        # ?Score
        if not self.match(TokenType.VARIABLE):
            raise SyntaxError("topk expects a logical variable score after 'by'")
        sc_tok = self.eat(TokenType.VARIABLE)
        score_name = sc_tok.value[1:]
        # 'where'
        # Accept both WHERE token and 'where' as identifier
        if not (self.match(TokenType.WHERE) or (self.match(TokenType.IDENTIFIER) and self.current_token.value.lower() == 'where')):
            raise SyntaxError("topk expects 'where predicate(...)'")
        self.advance()  # consume WHERE or 'where'
        goal = self.parse_logical_predicate()
        from .ast_nodes import TopkExpr
        return self._with_pos(TopkExpr(k, var_name, score_name, goal), start_tok)

    def _parse_argmax_sugar(self, start_tok):
        # argmax ?Var by ?Score where predicate(...)
        if not self.match(TokenType.VARIABLE):
            raise SyntaxError("argmax expects '?Var by ?Score where ...'")
        var_tok = self.eat(TokenType.VARIABLE)
        var_name = var_tok.value[1:]
        if not (self.match(TokenType.IDENTIFIER) and self.current_token.value.lower() == 'by'):
            raise SyntaxError("argmax expects 'by ?Score'")
        self.eat(TokenType.IDENTIFIER)
        if not self.match(TokenType.VARIABLE):
            raise SyntaxError("argmax expects a logical variable score after 'by'")
        sc_tok = self.eat(TokenType.VARIABLE)
        score_name = sc_tok.value[1:]
        # Accept both WHERE token and 'where' as identifier
        if not (self.match(TokenType.WHERE) or (self.match(TokenType.IDENTIFIER) and self.current_token.value.lower() == 'where')):
            raise SyntaxError("argmax expects 'where predicate(...)'")
        self.advance()  # consume WHERE or 'where'
        goal = self.parse_logical_predicate()
        from .ast_nodes import ArgmaxExpr
        return self._with_pos(ArgmaxExpr(var_name, score_name, goal), start_tok)


    def parse_argument_list(self):
        """Parse function arguments with support for:
        - named arguments: func(name=value)
        - pair sugar inside calls: head(key: value, ...)


        """
        args = []
        named_args = {}

        def is_keyword_or_identifier():
            """Check if current token can be used as argument name"""
            return (self.match(TokenType.IDENTIFIER) or
                    self.match(TokenType.DEFAULT, TokenType.MATCH, TokenType.LIMIT,
                               TokenType.DOMAIN, TokenType.MEMORY, TokenType.KNOWLEDGE,
                               TokenType.PATTERN, TokenType.CONCEPT, TokenType.SIMILARITY,
                               TokenType.BASED_ON, TokenType.REACTIONS,
                               TokenType.ROLE, TokenType.DEGREE, TokenType.STATE_CHANGES,
                               TokenType.ENTITIES, TokenType.RESULT, TokenType.PARTICIPANTS,
                               TokenType.STRENGTH, TokenType.TRANSFORM, TokenType.STRUCTURE,
                               TokenType.EXPRESS, TokenType.LINGUISTIC_FORMS, TokenType.CONTENT,
                               TokenType.CONTEXT, TokenType.TIME, TokenType.PLACE, TokenType.SOURCE,
                               TokenType.CERTAINTY, TokenType.CURRENT_VALUE, TokenType.HISTORY,
                               TokenType.FUTURE_PREDICTION, TokenType.ROOT, TokenType.TAXONOMY,
                               TokenType.CHARACTERS, TokenType.EVENT))

        def parse_pair_if_any():
            # Lookahead for IDENTIFIER|KEYWORD|STRING followed by ':'
            if (is_keyword_or_identifier() and self.peek() and self.peek().type == TokenType.COLON) or \
               (self.match(TokenType.STRING) and self.peek() and self.peek().type == TokenType.COLON):
                # Key
                if self.match(TokenType.STRING):
                    s_tok = self.eat(TokenType.STRING)
                    raw = s_tok.value
                    inner = raw[1:-1] if len(raw) >= 2 else raw
                    inner = self._unescape_string(inner)
                    key_node = self._with_pos(String(inner), s_tok)
                else:
                    # IDENTIFIER or keyword
                    if self.match(TokenType.IDENTIFIER):
                        key_tok = self.eat(TokenType.IDENTIFIER)
                    else:
                        key_tok = self.eat_attribute_name()
                    key_node = self._with_pos(String(key_tok.value), key_tok)
                # ':' and value expression
                self.eat(TokenType.COLON)
                value = self.parse_expression()
                return KeyValuePair(key_node, value)
            return None

        if not self.match(TokenType.RPAREN):
            # Parse first argument
            # Check if it's a named argument (identifier/keyword followed by '=')
            if is_keyword_or_identifier() and self.peek() and self.peek().type == TokenType.ASSIGN:
                if self.match(TokenType.IDENTIFIER):
                    name = self.eat(TokenType.IDENTIFIER).value
                else:
                    name = self.eat_attribute_name().value
                self.eat(TokenType.ASSIGN)
                value = self.parse_expression()
                named_args[name] = value
            else:
                pair = parse_pair_if_any()
                if pair is not None:
                    args.append(pair)
                else:
                    args.append(self.parse_expression())

            # Parse remaining arguments
            while self.match(TokenType.COMMA):
                self.eat(TokenType.COMMA)

                # Check if it's a named argument
                if is_keyword_or_identifier() and self.peek() and self.peek().type == TokenType.ASSIGN:
                    if self.match(TokenType.IDENTIFIER):
                        name = self.eat(TokenType.IDENTIFIER).value
                    else:
                        name = self.eat_attribute_name().value
                    self.eat(TokenType.ASSIGN)
                    value = self.parse_expression()
                    named_args[name] = value
                else:
                    pair = parse_pair_if_any()
                    if pair is not None:
                        args.append(pair)
                    else:
                        args.append(self.parse_expression())

        return args, named_args

    def parse_dotted_name(self):
        """Parse dotted module name like 'a.b.c'"""
        # Allow semantic keywords as module names
        if self.match(TokenType.IDENTIFIER):
            parts = [self.eat(TokenType.IDENTIFIER).value]
        else:
            # Allow semantic keywords as module names
            first_tok = self.eat_attribute_name()
            parts = [first_tok.value]
        while self.match(TokenType.DOT):
            self.eat(TokenType.DOT)
            if self.match(TokenType.IDENTIFIER):
                parts.append(self.eat(TokenType.IDENTIFIER).value)
            else:
                # Allow semantic keywords as module names
                tok = self.eat_attribute_name()
                parts.append(tok.value)
        return '.'.join(parts)

    def parse_import_statement(self):
        """Parse 'import module [as alias]'"""
        imp_tok = self.eat(TokenType.IMPORT)
        module_name = self.parse_dotted_name()
        alias = None
        if self.match(TokenType.AS):
            self.eat(TokenType.AS)
            alias = self.eat(TokenType.IDENTIFIER).value
        return self._with_pos(ImportStatement(module_name, alias), imp_tok)

    def parse_from_import_statement(self):
        """Parse 'from module import name[, name]*'"""
        from_tok = self.eat(TokenType.FROM)
        module_name = self.parse_dotted_name()
        self.eat(TokenType.IMPORT)
        names = [self.eat(TokenType.IDENTIFIER).value]
        while self.match(TokenType.COMMA):
            self.eat(TokenType.COMMA)
            names.append(self.eat(TokenType.IDENTIFIER).value)
        return self._with_pos(FromImportStatement(module_name, names), from_tok)

        return args

    def parse_list(self):
        """Parse a list literal, list comprehension, or list pattern [H|T]"""
        lb_tok = self.eat(TokenType.LBRACKET)
        elements = []

        if not self.match(TokenType.RBRACKET):
            first_expr = self.parse_expression()

            # Check for list pattern [H|T] or [H1, H2, ...|T]
            if self.match(TokenType.PIPE):
                self.eat(TokenType.PIPE)
                tail = self.parse_expression()
                self.eat(TokenType.RBRACKET)
                # Create a ListPattern node with head elements and tail
                return self._with_pos(ListPattern([first_expr], tail), lb_tok)

            # Check for list comprehension: [expr for var in iterable (if cond)?]
            elif self.match(TokenType.FOR):
                self.eat(TokenType.FOR)
                var_name = self.eat(TokenType.IDENTIFIER).value
                self.eat(TokenType.IN)
                iterable = self.parse_expression()
                condition = None
                if self.match(TokenType.IF):
                    self.eat(TokenType.IF)
                    condition = self.parse_expression()
                self.eat(TokenType.RBRACKET)
                return self._with_pos(ListComprehension(first_expr, var_name, iterable, condition), lb_tok)
            else:
                elements.append(first_expr)
                while self.match(TokenType.COMMA):
                    self.eat(TokenType.COMMA)
                    # Check if this is [H1, H2, ...|T] pattern (after comma)
                    if self.match(TokenType.PIPE):
                        self.eat(TokenType.PIPE)
                        tail = self.parse_expression()
                        self.eat(TokenType.RBRACKET)
                        return self._with_pos(ListPattern(elements, tail), lb_tok)
                    # Otherwise, parse next element
                    next_expr = self.parse_expression()
                    elements.append(next_expr)
                    # Check if pipe comes after this element
                    if self.match(TokenType.PIPE):
                        self.eat(TokenType.PIPE)
                        tail = self.parse_expression()
                        self.eat(TokenType.RBRACKET)
                        return self._with_pos(ListPattern(elements, tail), lb_tok)

        self.eat(TokenType.RBRACKET)
        return self._with_pos(List(elements), lb_tok)

    def parse_dict(self):
        """Parse a dictionary literal or set literal"""
        lb_tok = self.eat(TokenType.LBRACE)

        # Empty dict: {}
        if self.match(TokenType.RBRACE):
            self.eat(TokenType.RBRACE)
            return self._with_pos(Dict([]), lb_tok)

        # Parse first expression
        first_expr = self.parse_expression()

        # Check if this is a dict (has colon) or set (has comma or just one element)
        if self.match(TokenType.COLON):
            # This is a dictionary
            pairs = []
            self.eat(TokenType.COLON)
            value = self.parse_expression()
            pairs.append((first_expr, value))

            while self.match(TokenType.COMMA):
                self.eat(TokenType.COMMA)
                # Allow trailing comma
                if self.match(TokenType.RBRACE):
                    break
                key = self.parse_expression()
                self.eat(TokenType.COLON)
                value = self.parse_expression()
                pairs.append((key, value))

            self.eat(TokenType.RBRACE)
            return self._with_pos(Dict(pairs), lb_tok)
        else:
            # This is a set
            elements = [first_expr]
            while self.match(TokenType.COMMA):
                self.eat(TokenType.COMMA)
                # Allow trailing comma
                if self.match(TokenType.RBRACE):
                    break
                elements.append(self.parse_expression())

            self.eat(TokenType.RBRACE)
            return self._with_pos(Set(elements), lb_tok)

    def parse_query(self):
        """Parse a logical query"""
        self.eat(TokenType.QUERY)
        goal = self.parse_logical_predicate()
        if self.current_token and self.current_token.type == TokenType.DOT:
            self.eat(TokenType.DOT)
        return LogicalQuery(goal)

    def parse_fact(self):
        """Parse a logical fact or sugar statement inside hybrid blocks.
        Supports optional probability: fact[0.8] p(args)."""
        prob_expr = None
        if self.match(TokenType.FACT):
            self.eat(TokenType.FACT)
            # Optional probability in brackets: fact[prob]
            if self.current_token and self.current_token.type == TokenType.LBRACKET:
                self.eat(TokenType.LBRACKET)
                prob_expr = self.parse_expression()
                self.eat(TokenType.RBRACKET)

        pred_or_sugar = self.parse_logical_predicate()
        # Consume trailing dot if present/required
        if self.current_token and self.current_token.type == TokenType.DOT:
            self.eat(TokenType.DOT)

        # If sugar returned, pass it through directly (probability not applicable)
        if isinstance(pred_or_sugar, SimilarityDecl):
            return pred_or_sugar

        return LogicalFact(pred_or_sugar, probability=prob_expr)

    def parse_rule(self):
        """Parse a logical rule"""
        if self.match(TokenType.RULE):
            self.eat(TokenType.RULE)

        head = self.parse_logical_predicate()

        # Handle both :- and ←
        if self.match(TokenType.IMPLIES):
            self.eat(TokenType.IMPLIES)
        elif self.match(TokenType.ARROW):
            self.eat(TokenType.ARROW)
        else:
            raise SyntaxError(f"Expected :- or ← in rule, got {self.current_token}")

        body = self.parse_logical_body()

        # Handle optional dot at the end
        if self.current_token and self.current_token.type == TokenType.DOT:
            self.eat(TokenType.DOT)

        return LogicalRule(head, body)

    def parse_entity_body(self):
        """Parse entity body: allows both quoted strings and bare identifiers as keys

        Supports both old syntax:
            entity Ahmed { "states": {...}, "properties": {...} }

        And new syntax:
            entity Ahmed { states: {...}, properties: {...} }
        """
        lb_tok = self.eat(TokenType.LBRACE)

        # Empty dict: {}
        if self.match(TokenType.RBRACE):
            self.eat(TokenType.RBRACE)
            return self._with_pos(Dict([]), lb_tok)

        pairs = []

        while True:
            # Skip newlines
            while self.match(TokenType.NEWLINE):
                self.eat(TokenType.NEWLINE)

            # Check for end of dict
            if self.match(TokenType.RBRACE):
                break

            # Parse key: can be a string literal OR an identifier OR a keyword
            if self.match(TokenType.STRING):
                # Old syntax: "states": {...}
                key = self.parse_primary()
            elif self.match(TokenType.IDENTIFIER):
                # New syntax: states: {...}
                # Convert identifier to string literal for backward compatibility
                key_tok = self.eat(TokenType.IDENTIFIER)
                key = self._with_pos(String(key_tok.value), key_tok)
            elif self.current_token and self.current_token.type != TokenType.RBRACE:
                # Allow keywords as keys (e.g., حالة, نتيجة, etc.)
                key_tok = self.current_token
                self.advance()
                key = self._with_pos(String(key_tok.value), key_tok)
            else:
                raise SyntaxError(f"Expected string or identifier as entity body key, got {self.current_token}")

            self.eat(TokenType.COLON)

            # Value can be any expression (usually a dict)
            value = self.parse_expression()
            pairs.append((key, value))

            # Skip newlines after value
            while self.match(TokenType.NEWLINE):
                self.eat(TokenType.NEWLINE)

            # Check for comma or end
            if self.match(TokenType.COMMA):
                self.eat(TokenType.COMMA)
                # Skip newlines after comma
                while self.match(TokenType.NEWLINE):
                    self.eat(TokenType.NEWLINE)
                # Allow trailing comma
                if self.match(TokenType.RBRACE):
                    break
            elif self.match(TokenType.RBRACE):
                break
            # Allow newline as separator (no comma required)
            # Continue to next iteration

        self.eat(TokenType.RBRACE)
        return self._with_pos(Dict(pairs), lb_tok)

    def parse_entity_def(self):
        """Parse an entity definition: entity <name> { ... } or entity <name>: { ... }"""
        ent_tok = self.eat(TokenType.ENTITY)
        name = self.eat(TokenType.IDENTIFIER).value
        # Colon is optional
        if self.match(TokenType.COLON):
            self.eat(TokenType.COLON)
        # Entity body is a dict-like structure (supports both quoted and unquoted keys)
        body = self.parse_entity_body()
        return self._with_pos(EntityDef(name, body), ent_tok)

    def parse_apply_action(self):
        """Parse apply statement: apply <actor>.<action>(<target>, [name=expr, ...])"""
        app_tok = self.eat(TokenType.APPLY)
        actor_name = self.eat(TokenType.IDENTIFIER).value
        self.eat(TokenType.DOT)
        action_name = self.eat(TokenType.IDENTIFIER).value
        self.eat(TokenType.LPAREN)
        args, named_args = self.parse_argument_list()
        self.eat(TokenType.RPAREN)
        if not args:
            raise SyntaxError("apply requires at least a target argument")
        target_expr = args[0]
        return self._with_pos(ApplyActionStmt(actor_name, action_name, target_expr, named_args), app_tok)


    def parse_concept_def(self):
        """Parse a concept definition:
        Old syntax: concept <Name> = { ... } (set literal)
        New syntax: concept "<name>": {...} (semantic concept)
        """
        c_tok = self.eat(TokenType.CONCEPT)

        # Check if this is new syntax (string or identifier followed by colon)
        if self.match(TokenType.STRING):
            name = self.eat(TokenType.STRING).value
            self.eat(TokenType.COLON)
            properties = self.parse_entity_body()
            return self._with_pos(Concept(name, properties), c_tok)
        elif self.match(TokenType.IDENTIFIER):
            name = self.eat(TokenType.IDENTIFIER).value
            # Check if followed by colon (new syntax) or assign (old syntax)
            if self.match(TokenType.COLON):
                self.eat(TokenType.COLON)
                properties = self.parse_entity_body()
                return self._with_pos(Concept(name, properties), c_tok)
            elif self.match(TokenType.ASSIGN):
                # Old syntax: concept Name = {a, b, c}
                self.eat(TokenType.ASSIGN)
                set_node = self.parse_dict()  # parse_dict also handles set literals
                if not isinstance(set_node, Set):
                    # If the dict parser returned a Dict, it's a user error
                    raise SyntaxError("concept expects a set literal: {a, b, c}")
                return self._with_pos(ConceptDef(name, set_node), c_tok)
            else:
                raise SyntaxError(f"Expected ':' or '=' after concept name, got {self.current_token.type}")
        else:
            raise SyntaxError(f"Expected identifier or string after 'concept', got {self.current_token.type}")

    def parse_once_statement(self):
        """Parse once statement: once goal. or once { block }"""
        once_tok = self.eat(TokenType.ONCE)

        # Check if it's a block or a single goal
        if self.match(TokenType.LBRACE):
            # once { block } - execute block with max_solutions=1
            body = self.parse_block()
            from .ast_nodes import OnceStatement
            return self._with_pos(OnceStatement(body), once_tok)
        else:
            # once goal. - single logical goal with limit 1
            goal = self.parse_logical_predicate()
            self.eat(TokenType.DOT)
            from .ast_nodes import OnceGoal
            return self._with_pos(OnceGoal(goal), once_tok)

    def parse_limit_statement(self):
        """Parse limit statement: limit N { block } or limit N goal."""
        limit_tok = self.eat(TokenType.LIMIT)

        # Parse the limit number
        if not self.match(TokenType.NUMBER):
            raise SyntaxError("limit expects a number: limit 3 { ... }")
        n_tok = self.eat(TokenType.NUMBER)
        n = int(n_tok.value)

        # Check if it's a block or a single goal
        if self.match(TokenType.LBRACE):
            # limit N { block }
            body = self.parse_block()
            from .ast_nodes import LimitStatement
            return self._with_pos(LimitStatement(n, body), limit_tok)
        else:
            # limit N goal.
            goal = self.parse_logical_predicate()
            self.eat(TokenType.DOT)
            from .ast_nodes import LimitGoal
            return self._with_pos(LimitGoal(n, goal), limit_tok)

    def _parse_keyword_as_identifier(self, keyword_tok, keyword_name):
        """Parse a keyword token as an identifier (for backward compatibility)"""
        name = keyword_name

        # Handle assignment: keyword = value
        if self.match(TokenType.ASSIGN):
            self.eat(TokenType.ASSIGN)
            value = self.parse_expression()
            from .ast_nodes import Assignment
            return self._with_pos(Assignment(name, value), keyword_tok)

        # Handle subscript assignment: keyword[index] = value
        elif self.match(TokenType.LBRACKET):
            lb_tok = self.eat(TokenType.LBRACKET)
            index_expr = self.parse_subscript_or_slice()
            self.eat(TokenType.RBRACKET)
            self.eat(TokenType.ASSIGN)
            value = self.parse_expression()
            from .ast_nodes import SubscriptAssignment, Variable, SubscriptAccess
            target = self._with_pos(SubscriptAccess(Variable(name), index_expr), lb_tok)
            return self._with_pos(SubscriptAssignment(target, value), keyword_tok)

        # Handle attribute assignment: keyword.attr = value
        elif self.match(TokenType.DOT):
            self.eat(TokenType.DOT)
            attr_name = self.eat_attribute_name().value
            self.eat(TokenType.ASSIGN)
            value = self.parse_expression()
            from .ast_nodes import AttributeAssignment, Variable
            return self._with_pos(AttributeAssignment(Variable(name), attr_name, value), keyword_tok)

        # Handle function call: keyword(...)
        elif self.match(TokenType.LPAREN):
            self.eat(TokenType.LPAREN)
            args, named_args = self.parse_argument_list()
            self.eat(TokenType.RPAREN)
            from .ast_nodes import FunctionCall
            return self._with_pos(FunctionCall(name, args, named_args), keyword_tok)

        else:
            raise SyntaxError(f"Unexpected token after '{keyword_name}': {self.current_token}")

    def _parse_match_as_identifier(self):
        """Parse 'match' as an identifier (for backward compatibility with match = ...)"""
        match_tok = self.eat(TokenType.MATCH)
        return self._parse_keyword_as_identifier(match_tok, 'match')

    def _parse_limit_as_identifier(self):
        """Parse 'limit' as an identifier (for backward compatibility with limit = ...)"""
        limit_tok = self.eat(TokenType.LIMIT)
        return self._parse_keyword_as_identifier(limit_tok, 'limit')

    def parse_match_in_as(self):
        """Parse match statement: match pattern in text as var_name
        Syntactic sugar for: var_name = match(pattern, text)
        """
        match_tok = self.eat(TokenType.MATCH)

        # Parse pattern expression (use parse_additive to avoid consuming 'in')
        pattern = self.parse_additive()

        # Expect 'in' keyword
        if not (self.match(TokenType.IN) or (self.match(TokenType.IDENTIFIER) and self.current_token.value in ('in', 'في'))):
            raise SyntaxError("match syntax: match pattern in text as var_name")
        if self.match(TokenType.IN):
            self.eat(TokenType.IN)
        else:
            self.eat(TokenType.IDENTIFIER)

        # Parse text expression (use parse_additive to avoid consuming 'as')
        text = self.parse_additive()

        # Expect 'as' keyword
        if not (self.match(TokenType.AS) or (self.match(TokenType.IDENTIFIER) and self.current_token.value in ('as', 'كـ'))):
            raise SyntaxError("match syntax: match pattern in text as var_name")
        if self.match(TokenType.AS):
            self.eat(TokenType.AS)
        else:
            self.eat(TokenType.IDENTIFIER)

        # Parse variable name (allow keywords as identifiers)
        if self.match(TokenType.IDENTIFIER):
            var_name = self.eat(TokenType.IDENTIFIER).value
        elif self.current_token and hasattr(self.current_token, 'value') and self.current_token.value:
            # Allow any token with a value as variable name
            var_name = self.current_token.value
            self.advance()
        else:
            raise SyntaxError("match expects a variable name after 'as'")

        from .ast_nodes import MatchInAs
        return self._with_pos(MatchInAs(pattern, text, var_name), match_tok)


    def parse_logical_predicate(self):
        """Parse a logical predicate or similarity sugar inside hybrid logic."""
        # Allow any token with a value as predicate name (identifier or keyword)
        if not self.current_token or self.current_token.type in (TokenType.LPAREN, TokenType.RPAREN,
                                                                  TokenType.LBRACE, TokenType.RBRACE,
                                                                  TokenType.LBRACKET, TokenType.RBRACKET,
                                                                  TokenType.COMMA, TokenType.DOT,
                                                                  TokenType.COLON, TokenType.SEMICOLON,
                                                                  TokenType.OPERATOR, TokenType.ASSIGN,
                                                                  TokenType.NUMBER, TokenType.STRING,
                                                                  TokenType.EOF):
            raise SyntaxError(f"Expected predicate name, got {self.current_token}")

        name_tok = self.current_token
        name = name_tok.value
        self.advance()
        self.eat(TokenType.LPAREN)

        # Try to parse similarity sugar: key:value pairs
        def _parse_pair_in_logic():
            if (self.match(TokenType.IDENTIFIER) and self.peek() and self.peek().type == TokenType.COLON) or \
               (self.match(TokenType.STRING) and self.peek() and self.peek().type == TokenType.COLON):
                # Key as string node
                if self.match(TokenType.IDENTIFIER):
                    k_tok = self.eat(TokenType.IDENTIFIER)
                    k_node = self._with_pos(String(k_tok.value), k_tok)
                else:
                    s_tok = self.eat(TokenType.STRING)
                    raw = s_tok.value
                    inner = raw[1:-1] if len(raw) >= 2 else raw
                    inner = self._unescape_string(inner)
                    k_node = self._with_pos(String(inner), s_tok)
                self.eat(TokenType.COLON)
                # Score/value as general expression (allow numbers/expressions)
                v_expr = self.parse_expression()
                return KeyValuePair(k_node, v_expr)
            return None

        pairs = []
        # Detect first pair
        pair0 = None
        if not self.match(TokenType.RPAREN):
            pair0 = _parse_pair_in_logic()
        if pair0 is not None:
            pairs.append(pair0)
            # parse additional pairs separated by commas
            while self.match(TokenType.COMMA):
                self.eat(TokenType.COMMA)
                # Allow trailing close
                if self.match(TokenType.RPAREN):
                    break
                p = _parse_pair_in_logic()
                if p is None:
                    raise SyntaxError("Expected key:value pair in similarity sugar")
                pairs.append(p)
            self.eat(TokenType.RPAREN)
            return SimilarityDecl(name, pairs)

        # Fallback: normal logical predicate
        args = self.parse_logical_arguments()
        self.eat(TokenType.RPAREN)
        return Predicate(name, args)

    def parse_logical_arguments(self):
        """Parse logical predicate arguments"""
        args = []

        if not self.match(TokenType.RPAREN):
            args.append(self.parse_logical_term())

            while self.match(TokenType.COMMA):
                self.eat(TokenType.COMMA)
                args.append(self.parse_logical_term())

        return args

    def parse_logical_term(self):
        """Parse a logical term (including list patterns)"""
        if self.match(TokenType.VARIABLE):
            var_name = self.eat(TokenType.VARIABLE).value[1:]  # Remove ?
            return Term(var_name, is_variable=True)

        elif self.match(TokenType.STRING):
            raw = self.eat(TokenType.STRING).value
            if (raw.startswith('"""') and raw.endswith('"""')) or (raw.startswith("'''") and raw.endswith("'''")):
                value = raw[3:-3]
            else:
                value = raw[1:-1]
            value = self._unescape_string(value)
            return Term(value, is_variable=False)

        elif self.match(TokenType.NUMBER):
            value = self.eat(TokenType.NUMBER).value
            return Term(value, is_variable=False)

        elif self.match(TokenType.IDENTIFIER):
            value = self.eat(TokenType.IDENTIFIER).value
            return Term(value, is_variable=False)

        elif self.match(TokenType.LBRACKET):
            # Parse list or list pattern
            return self.parse_list()

        else:
            raise SyntaxError(f"Unexpected token in logical term: {self.current_token}")

    def parse_logical_body(self):
        """Parse the body of a logical rule (predicates, comparisons, is expressions)"""
        goals = [self.parse_logical_goal()]

        while self.match(TokenType.COMMA):
            self.eat(TokenType.COMMA)
            goals.append(self.parse_logical_goal())

        return goals

    def parse_logical_goal(self):
        """Parse a single goal in logical body (predicate, comparison, is expression, or cut)"""
        # Check for cut operator: !
        if self.match(TokenType.CUT):
            self.eat(TokenType.CUT)
            return Cut()

        # Check if this is an 'is' expression or comparison: ?X is Expression or ?X > ?Y
        if self.match(TokenType.VARIABLE):
            # Peek ahead to see if 'is' or comparison operator follows
            saved_pos = self.position
            var_token = self.eat(TokenType.VARIABLE)

            if self.match(TokenType.IS):
                # This is an 'is' expression
                self.eat(TokenType.IS)
                expr = self.parse_additive()  # Parse arithmetic expression
                var_name = var_token.value[1:]  # Remove ?
                return IsExpression(Term(var_name, is_variable=True), expr)
            elif self.match(TokenType.OPERATOR):
                # This might be a comparison: ?X > ?Y
                op_tok = self.eat(TokenType.OPERATOR)
                op = op_tok.value
                if op in ['>', '<', '>=', '<=', '=<', '==', '!=', '=:=', '=\\=']:
                    # Restore and parse as comparison
                    self.position = saved_pos
                    self.current_token = self.tokens[self.position] if self.position < len(self.tokens) else None
                    left = self.parse_logical_term()
                    op_tok = self.eat(TokenType.OPERATOR)
                    right = self.parse_logical_term()
                    # Represent comparisons as special predicates handled by the logical engine
                    return Predicate(f'_compare_{op_tok.value}', [left, right])
                else:
                    # Not a comparison, restore and parse as predicate
                    self.position = saved_pos
                    self.current_token = self.tokens[self.position] if self.position < len(self.tokens) else None
                    return self.parse_logical_predicate()
            else:
                # Not an 'is' expression or comparison, restore position and parse as predicate
                self.position = saved_pos
                self.current_token = self.tokens[self.position] if self.position < len(self.tokens) else None
                return self.parse_logical_predicate()

        # Check for comparison expressions: ?X > 5, ?Y < 10, etc.
        elif self.match(TokenType.IDENTIFIER):
            # Check if this is a predicate (followed by '(') or a comparison
            saved_pos = self.position
            if self.peek_ahead(1) and self.peek_ahead(1).type == TokenType.LPAREN:
                # This is a predicate call
                return self.parse_logical_predicate()
            else:
                # Try to parse as comparison
                left = self.parse_logical_term()

                # Check for comparison operators
                if self.match(TokenType.OPERATOR):
                    op_tok = self.eat(TokenType.OPERATOR)
                    op = op_tok.value
                    if op in ['>', '<', '>=', '<=', '=<', '==', '!=', '=:=', '=\\=']:
                        right = self.parse_logical_term()
                        # Return a comparison as a special predicate
                        return Predicate(f'_compare_{op}', [left, right])

                # If no comparison, this should be a predicate - error
                raise SyntaxError(f"Expected predicate or comparison, got: {left}")

        elif self.match(TokenType.NUMBER):
            # Must be a comparison
            left = self.parse_logical_term()
            if self.match(TokenType.OPERATOR):
                op_tok = self.eat(TokenType.OPERATOR)
                op = op_tok.value
                if op in ['>', '<', '>=', '<=', '=<', '==', '!=', '=:=', '=\\=']:
                    right = self.parse_logical_term()
                    return Predicate(f'_compare_{op}', [left, right])
            raise SyntaxError(f"Expected comparison operator after number")

        # Otherwise, parse as predicate
        else:
            return self.parse_logical_predicate()

    def parse_subscript_or_slice(self):
        """Parse subscript or slice expression: [index] or [start:end:step]"""
        # Check if this is a slice by looking ahead for colons
        # We need to parse the first expression, then check for colon

        # Save position to potentially backtrack
        start_pos = self.position

        # Try to parse first expression (could be start of slice or just index)
        first_expr = None
        if not self.match(TokenType.COLON):
            first_expr = self.parse_expression()

        # Check if we have a colon (indicating slice)
        if self.match(TokenType.COLON):
            # This is a slice: [start:end:step]
            start = first_expr
            self.eat(TokenType.COLON)

            # Parse end (optional)
            end = None
            if not self.match(TokenType.COLON) and not self.match(TokenType.RBRACKET):
                end = self.parse_expression()

            # Parse step (optional)
            step = None
            if self.match(TokenType.COLON):
                self.eat(TokenType.COLON)
                if not self.match(TokenType.RBRACKET):
                    step = self.parse_expression()

            return Slice(start, end, step)
        else:
            # This is just a regular index
            return first_expr

    # ============ Temporal Constructs Parsing ============

    def parse_temporal_block(self):
        """Parse temporal block: temporal { first: stmt, then: stmt, lastly: stmt }

        Supports both English and Arabic keywords:
        - first/أولا, then/ثم, lastly/أخيرا
        """
        temporal_tok = self.eat(TokenType.TEMPORAL)
        self.eat(TokenType.LBRACE)

        steps = []

        while not self.match(TokenType.RBRACE):
            # Parse label (first, then, lastly, or Arabic equivalents)
            if self.match(TokenType.FIRST):
                label_tok = self.eat(TokenType.FIRST)
                label = 'first'
            elif self.match(TokenType.THEN):
                label_tok = self.eat(TokenType.THEN)
                label = 'then'
            elif self.match(TokenType.LASTLY):
                label_tok = self.eat(TokenType.LASTLY)
                label = 'lastly'
            else:
                raise SyntaxError(f"Expected temporal label (first/أولا, then/ثم, lastly/أخيرا), got {self.current_token}")

            self.eat(TokenType.COLON)

            # Parse statement
            stmt = self.parse_statement()
            steps.append((label, stmt))

            # Optional comma
            if self.match(TokenType.COMMA):
                self.eat(TokenType.COMMA)

        self.eat(TokenType.RBRACE)
        return self._with_pos(TemporalBlock(steps), temporal_tok)

    def parse_within_block(self):
        """Parse within block: within 5.0 seconds { ... }

        Supports time units: seconds/ثانية, minutes/دقيقة, hours/ساعة
        """
        within_tok = self.eat(TokenType.WITHIN)

        # Parse duration (number)
        if not self.match(TokenType.NUMBER):
            raise SyntaxError(f"Expected number after 'within', got {self.current_token}")
        duration_tok = self.eat(TokenType.NUMBER)
        duration = duration_tok.value

        # Parse unit (seconds, minutes, hours)
        if self.match(TokenType.SECONDS):
            unit_tok = self.eat(TokenType.SECONDS)
            unit = 'seconds'
        elif self.match(TokenType.MINUTES):
            unit_tok = self.eat(TokenType.MINUTES)
            unit = 'minutes'
        elif self.match(TokenType.HOURS):
            unit_tok = self.eat(TokenType.HOURS)
            unit = 'hours'
        else:
            raise SyntaxError(f"Expected time unit (seconds/ثانية, minutes/دقيقة, hours/ساعة), got {self.current_token}")

        # Parse body (block or statement)
        if self.match(TokenType.LBRACE):
            body = self.parse_block()
        else:
            body = self.parse_statement()

        return self._with_pos(WithinBlock(duration, unit, body), within_tok)

    def parse_schedule_block(self):
        """Parse schedule block: schedule every 2.0 seconds { ... }

        Supports time units: seconds/ثانية, minutes/دقيقة, hours/ساعة
        """
        schedule_tok = self.eat(TokenType.SCHEDULE)

        # Parse 'every' keyword
        if not self.match(TokenType.EVERY):
            raise SyntaxError(f"Expected 'every' after 'schedule', got {self.current_token}")
        self.eat(TokenType.EVERY)

        # Parse interval (number)
        if not self.match(TokenType.NUMBER):
            raise SyntaxError(f"Expected number after 'every', got {self.current_token}")
        interval_tok = self.eat(TokenType.NUMBER)
        interval = interval_tok.value

        # Parse unit (seconds, minutes, hours)
        if self.match(TokenType.SECONDS):
            unit_tok = self.eat(TokenType.SECONDS)
            unit = 'seconds'
        elif self.match(TokenType.MINUTES):
            unit_tok = self.eat(TokenType.MINUTES)
            unit = 'minutes'
        elif self.match(TokenType.HOURS):
            unit_tok = self.eat(TokenType.HOURS)
            unit = 'hours'
        else:
            raise SyntaxError(f"Expected time unit (seconds/ثانية, minutes/دقيقة, hours/ساعة), got {self.current_token}")

        # Parse body (block or statement)
        if self.match(TokenType.LBRACE):
            body = self.parse_block()
        else:
            body = self.parse_statement()

        return self._with_pos(ScheduleBlock(interval, unit, body), schedule_tok)

    def parse_delay_statement(self):
        """Parse delay statement: delay 1.5 seconds

        Supports time units: seconds/ثانية, minutes/دقيقة, hours/ساعة
        """
        delay_tok = self.eat(TokenType.DELAY)

        # Parse duration (number)
        if not self.match(TokenType.NUMBER):
            raise SyntaxError(f"Expected number after 'delay', got {self.current_token}")
        duration_tok = self.eat(TokenType.NUMBER)
        duration = duration_tok.value

        # Parse unit (seconds, minutes, hours)
        if self.match(TokenType.SECONDS):
            unit_tok = self.eat(TokenType.SECONDS)
            unit = 'seconds'
        elif self.match(TokenType.MINUTES):
            unit_tok = self.eat(TokenType.MINUTES)
            unit = 'minutes'
        elif self.match(TokenType.HOURS):
            unit_tok = self.eat(TokenType.HOURS)
            unit = 'hours'
        else:
            raise SyntaxError(f"Expected time unit (seconds/ثانية, minutes/دقيقة, hours/ساعة), got {self.current_token}")

        return self._with_pos(DelayStatement(duration, unit), delay_tok)

    def parse_match_statement(self):
        """Parse match statement for pattern matching

        Syntax:
            match value:
            {
                case pattern1: { body1 }
                case pattern2 when guard: { body2 }
                default: { default_body }
            }

        Arabic:
            طابق قيمة:
            {
                حالة نمط1: { جسم1 }
                حالة نمط2 عندما شرط: { جسم2 }
                افتراضي: { جسم_افتراضي }
            }
        """
        match_tok = self.eat(TokenType.MATCH)

        # Parse value to match
        value = self.parse_expression()

        # Expect colon
        self.eat(TokenType.COLON)

        # Expect opening brace
        self.eat(TokenType.LBRACE)

        # Parse cases
        cases = []
        while self.current_token and not self.match(TokenType.RBRACE):
            if self.match(TokenType.CASE):
                cases.append(self.parse_case_clause())
            elif self.match(TokenType.DEFAULT):
                cases.append(self.parse_default_clause())
            else:
                raise SyntaxError(f"Expected 'case' or 'default' in match statement, got {self.current_token}")

        # Expect closing brace
        self.eat(TokenType.RBRACE)

        return self._with_pos(MatchStatement(value, cases), match_tok)

    def parse_case_clause(self):
        """Parse case clause in match statement

        Syntax:
            case pattern: { body }
            case pattern when guard: { body }
        """
        self.eat(TokenType.CASE)

        # Parse pattern
        pattern = self.parse_pattern()

        # Check for guard (when clause)
        guard = None
        if self.match(TokenType.WHEN):
            self.advance()
            guard = self.parse_expression()

        # Expect colon
        self.eat(TokenType.COLON)

        # Parse body
        body = self.parse_block()

        return CaseClause(pattern, body, guard)

    def parse_default_clause(self):
        """Parse default clause in match statement

        Syntax:
            default: { body }
        """
        self.eat(TokenType.DEFAULT)

        # Expect colon
        self.eat(TokenType.COLON)

        # Parse body
        body = self.parse_block()

        return DefaultClause(body)

    def parse_pattern(self):
        """Parse a pattern for pattern matching

        Patterns can be:
        - Literals: 1, "hello", True
        - Variables: x, name
        - Lists: [x, y, z]
        - Dicts: {"name": n, "age": a}
        """
        if self.match(TokenType.LBRACKET):
            # List pattern
            return self.parse_list_pattern()
        elif self.match(TokenType.LBRACE):
            # Dict pattern
            return self.parse_dict_pattern()
        else:
            # Literal or variable
            return self.parse_expression()

    def parse_list_pattern(self):
        """Parse list pattern for destructuring

        Syntax:
            [x, y, z]
            [first, second]
        """
        self.eat(TokenType.LBRACKET)

        elements = []
        while self.current_token and not self.match(TokenType.RBRACKET):
            elements.append(self.parse_pattern())

            if self.match(TokenType.COMMA):
                self.advance()
            elif not self.match(TokenType.RBRACKET):
                raise SyntaxError(f"Expected ',' or ']' in list pattern, got {self.current_token}")

        self.eat(TokenType.RBRACKET)

        return ListPattern(elements)

    def parse_dict_pattern(self):
        """Parse dictionary pattern for destructuring

        Syntax:
            {"name": n, "age": a}
        """
        self.eat(TokenType.LBRACE)

        keys = []
        patterns = []

        while self.current_token and not self.match(TokenType.RBRACE):
            # Parse key (must be string or identifier)
            if self.match(TokenType.STRING):
                key = self.current_token.value
                # Remove quotes from string
                if key.startswith('"') and key.endswith('"'):
                    key = key[1:-1]
                elif key.startswith("'") and key.endswith("'"):
                    key = key[1:-1]
                self.advance()
            elif self.match(TokenType.IDENTIFIER):
                key = self.current_token.value
                self.advance()
            else:
                raise SyntaxError(f"Expected string or identifier as dict key in pattern, got {self.current_token}")

            keys.append(key)

            # Expect colon
            self.eat(TokenType.COLON)

            # Parse pattern for this key
            patterns.append(self.parse_pattern())

            if self.match(TokenType.COMMA):
                self.advance()
            elif not self.match(TokenType.RBRACE):
                raise SyntaxError(f"Expected ',' or '}}' in dict pattern, got {self.current_token}")

        self.eat(TokenType.RBRACE)

        return DictPattern(keys, patterns)

    # ========================================================================
    # Reactive Programming Parsing - تحليل البرمجة التفاعلية
    # ========================================================================

    def parse_reactive_declaration(self):
        """Parse reactive variable declaration

        Syntax:
            reactive x = 10
            تفاعلي س = 10
        """
        self.eat(TokenType.REACTIVE)

        # Parse variable name
        if not self.match(TokenType.IDENTIFIER):
            raise SyntaxError(f"Expected identifier after 'reactive', got {self.current_token}")

        variable = self.current_token.value
        self.advance()

        # Expect assignment
        self.eat(TokenType.ASSIGN)

        # Parse initial value
        value = self.parse_expression()

        return ReactiveDeclaration(variable, value)

    def parse_watch_block(self):
        """Parse watch block for monitoring variable changes

        Syntax:
            watch x, y: { body }
            راقب س, ص: { جسم }
        """
        self.eat(TokenType.WATCH)

        # Parse list of variables to watch
        variables = []

        if not self.match(TokenType.IDENTIFIER):
            raise SyntaxError(f"Expected identifier after 'watch', got {self.current_token}")

        variables.append(self.current_token.value)
        self.advance()

        # Parse additional variables
        while self.match(TokenType.COMMA):
            self.advance()
            if not self.match(TokenType.IDENTIFIER):
                raise SyntaxError(f"Expected identifier after ',', got {self.current_token}")
            variables.append(self.current_token.value)
            self.advance()

        # Expect colon
        self.eat(TokenType.COLON)

        # Parse body block
        body = self.parse_block()

        return WatchBlock(variables, body)

    def parse_computed_property(self):
        """Parse computed property

        Syntax:
            computed sum = x + y
            محسوب مجموع = س + ص
        """
        self.eat(TokenType.COMPUTED)

        # Parse property name - allow cognitive-semantic keywords as identifiers
        if not self.match(TokenType.IDENTIFIER):
            # Allow cognitive-semantic keywords as identifiers in this context
            if self.current_token.type in [
                TokenType.RESULT, TokenType.EVENT, TokenType.PATTERN,
                TokenType.IDEA, TokenType.PARTICIPANTS, TokenType.STRENGTH,
                TokenType.TRANSFORM, TokenType.REACTIONS, TokenType.STRUCTURE,
                TokenType.EXPRESS, TokenType.ENTITIES, TokenType.STATE_CHANGES,
                TokenType.LINGUISTIC_FORMS, TokenType.DEGREE, TokenType.ROLE
            ]:
                variable = self.current_token.value
                self.advance()
            else:
                raise SyntaxError(f"Expected identifier after 'computed', got {self.current_token}")
        else:
            variable = self.current_token.value
            self.advance()

        # Expect assignment
        self.eat(TokenType.ASSIGN)

        # Parse expression
        expression = self.parse_expression()

        # Extract dependencies from expression (variables used)
        dependencies = self._extract_dependencies(expression)

        return ComputedProperty(variable, expression, dependencies)

    def _extract_dependencies(self, expr):
        """Extract variable dependencies from an expression

        Returns a list of variable names that the expression depends on.
        """
        dependencies = []

        if isinstance(expr, Variable):
            dependencies.append(expr.name)
        elif isinstance(expr, BinaryOp):
            dependencies.extend(self._extract_dependencies(expr.left))
            dependencies.extend(self._extract_dependencies(expr.right))
        elif isinstance(expr, UnaryOp):
            dependencies.extend(self._extract_dependencies(expr.operand))
        elif isinstance(expr, FunctionCall):
            for arg in expr.arguments:
                dependencies.extend(self._extract_dependencies(arg))
        elif isinstance(expr, List):
            for elem in expr.elements:
                dependencies.extend(self._extract_dependencies(elem))
        elif isinstance(expr, Dict):
            for value in expr.values:
                dependencies.extend(self._extract_dependencies(value))
        elif isinstance(expr, AttributeAccess):
            dependencies.extend(self._extract_dependencies(expr.object))
        elif isinstance(expr, SubscriptAccess):
            dependencies.extend(self._extract_dependencies(expr.object))
            dependencies.extend(self._extract_dependencies(expr.index))
        # For literals (Number, String, etc.), no dependencies

        # Remove duplicates
        return list(set(dependencies))

    # ============ Cognitive-Semantic Model Parsing ============

    def parse_cognitive_entity(self):
        """Parse cognitive entity definition

        Syntax:
            cognitive_entity <name>:
            {
                property1: value1
                property2: value2
            }

            OR (without colon):
            cognitive_entity <name> { ... }
        """
        tok = self.eat(TokenType.COGNITIVE_ENTITY)
        name = self.eat(TokenType.IDENTIFIER).value
        # Colon is optional
        if self.match(TokenType.COLON):
            self.eat(TokenType.COLON)
        properties = self.parse_entity_body()  # Reuse entity body parser
        return self._with_pos(CognitiveEntity(name, properties), tok)

    def parse_cognitive_event(self):
        """Parse cognitive event definition

        Syntax:
            cognitive_event <name>:
            {
                participants: {...},
                strength: 0.9,
                transform: {...},
                reactions: [...]
            }

            OR (without colon):
            cognitive_event <name> { ... }
        """
        tok = self.eat(TokenType.COGNITIVE_EVENT)
        # Allow keywords as names
        if self.match(TokenType.IDENTIFIER):
            name = self.eat(TokenType.IDENTIFIER).value
        elif self.current_token and hasattr(self.current_token, 'value') and self.current_token.value:
            name = self.current_token.value
            self.advance()
        else:
            raise SyntaxError(f"Expected name after cognitive_event, got {self.current_token}")
        # Colon is optional
        if self.match(TokenType.COLON):
            self.eat(TokenType.COLON)
        config = self.parse_entity_body()  # Reuse entity body parser
        return self._with_pos(CognitiveEvent(name, config), tok)

    def parse_conceptual_blueprint(self):
        """Parse conceptual blueprint definition

        Syntax:
            conceptual_blueprint <name> {
                ... blueprint config as dict ...
            }

        Arabic:
            تصور_عام <name> {
                ... blueprint config as dict ...
            }
        """
        tok = self.eat(TokenType.CONCEPTUAL_BLUEPRINT)
        name = self.eat(TokenType.IDENTIFIER).value
        config = self.parse_entity_body()  # Reuse entity body parser
        return self._with_pos(ConceptualBlueprint(name, config), tok)

    def parse_trigger_event(self):
        """Parse trigger event statement

        Syntax:
            trigger <event_name>
            trigger <event_name> with {param: value}
        """
        tok = self.eat(TokenType.TRIGGER)
        event_name = self.eat(TokenType.IDENTIFIER).value

        params = None
        if self.match(TokenType.WITH):
            self.eat(TokenType.WITH)
            params = self.parse_entity_body()  # Parse params as dict

        return self._with_pos(TriggerEvent(event_name, params), tok)

    def parse_concurrent_events(self):
        """Parse concurrent events block

        Syntax 1 (dict-based):
            concurrent name:
            {
                events: [("event1", 0.8), ("event2", 0.6)]
            }

        Syntax 2 (statement-based):
            concurrent:
            {
                event event1 with strength 0.8
                event event2 with strength 0.6
            }
            => {
                # Combined effects
            }
        """
        tok = self.eat(TokenType.CONCURRENT)

        # Check if there's a name (identifier)
        name = None
        if self.match(TokenType.IDENTIFIER):
            name = self.eat(TokenType.IDENTIFIER).value

        self.eat(TokenType.COLON)

        # Parse as dict (Syntax 1)
        if name:
            config = self.parse_entity_body()
            # Extract events from config
            # For now, just return a simple node
            return self._with_pos(ConcurrentEvents([], config), tok)

        # Parse as statement block (Syntax 2)
        self.eat(TokenType.LBRACE)

        # Parse list of events with strengths
        events = []
        while not self.match(TokenType.RBRACE):
            # Expect: event <name> with strength <value>
            if self.match(TokenType.COGNITIVE_EVENT):
                self.eat(TokenType.COGNITIVE_EVENT)
            elif self.match(TokenType.EVENT):
                self.eat(TokenType.EVENT)
            else:
                # Try to continue without 'event' keyword
                pass

            event_name = self.eat(TokenType.IDENTIFIER).value

            # Optional: with strength <value>
            strength = 1.0  # Default
            if self.match(TokenType.WITH):
                self.eat(TokenType.WITH)
                if self.match(TokenType.STRENGTH):
                    self.eat(TokenType.STRENGTH)
                strength_expr = self.parse_expression()
                # For now, assume it's a number
                if isinstance(strength_expr, Number):
                    strength = strength_expr.value

            events.append((event_name, strength))

            # Optional newline or semicolon
            if self.match(TokenType.NEWLINE):
                self.eat(TokenType.NEWLINE)
            elif self.match(TokenType.SEMICOLON):
                self.eat(TokenType.SEMICOLON)

        self.eat(TokenType.RBRACE)

        # Parse effects block
        effects = None
        if self.match(TokenType.ARROW):
            self.eat(TokenType.ARROW)
            effects = self.parse_block()

        return self._with_pos(ConcurrentEvents(events, effects), tok)

    def parse_linguistic_pattern(self):
        """Parse linguistic pattern definition

        Syntax:
            pattern <name>:
            {
                structure: [component1, component2],
                express: function(idea) { ... }
            }
        """
        tok = self.eat(TokenType.PATTERN)
        name = self.eat(TokenType.IDENTIFIER).value
        self.eat(TokenType.COLON)
        config = self.parse_entity_body()  # Reuse entity body parser
        return self._with_pos(LinguisticPattern(name, config), tok)

    def parse_idea_def(self):
        """Parse idea definition

        Syntax:
            idea "<name>":
            {
                entities: {...},
                event: "event_name",
                result: {...}
            }
        """
        tok = self.eat(TokenType.IDEA)

        # Name can be string or identifier
        if self.match(TokenType.STRING):
            name = self.eat(TokenType.STRING).value
        else:
            name = self.eat(TokenType.IDENTIFIER).value

        self.eat(TokenType.COLON)
        config = self.parse_entity_body()  # Reuse entity body parser
        return self._with_pos(IdeaDef(name, config), tok)

    # ========================================================================
    # Semantic Programming & Knowledge Management Parsing Methods
    # ========================================================================

    def parse_semantic_meaning(self):
        """Parse semantic meaning definition

        Syntax:
            meaning <name>:
            {
                relationship1: value1,
                relationship2: value2
            }
        """
        tok = self.eat(TokenType.MEANING)
        name = self.eat(TokenType.IDENTIFIER).value
        self.eat(TokenType.COLON)
        relationships = self.parse_entity_body()
        return self._with_pos(SemanticMeaning(name, relationships), tok)

    def parse_semantic_query(self):
        """Parse semantic query

        Syntax:
            query: function_call()
            استعلام: دالة()
        """
        tok = self.eat(TokenType.QUERY)
        self.eat(TokenType.COLON)
        query_expr = self.parse_expression()
        return self._with_pos(SemanticQuery(query_expr), tok)

    def parse_knowledge_info(self):
        """Parse knowledge information with context

        Syntax:
            information "<name>":
            {
                content: {...},
                context: {...}
            }
        """
        tok = self.eat(TokenType.INFORMATION)

        if self.match(TokenType.STRING):
            name = self.eat(TokenType.STRING).value
        else:
            name = self.eat(TokenType.IDENTIFIER).value

        self.eat(TokenType.COLON)
        config = self.parse_entity_body()
        return self._with_pos(KnowledgeInfo(name, config), tok)

    def parse_inference_rule(self):
        """Parse inference rule

        Syntax:
            inference_rule "<name>":
            {
                if: [...],
                then: {...}
            }
        """
        tok = self.eat(TokenType.INFERENCE_RULE)

        if self.match(TokenType.STRING):
            name = self.eat(TokenType.STRING).value
        else:
            name = self.eat(TokenType.IDENTIFIER).value

        self.eat(TokenType.COLON)
        config = self.parse_entity_body()
        return self._with_pos(InferenceRule(name, config), tok)

    def parse_infer_from(self):
        """Parse infer from statement

        Syntax:
            infer_from: "statement"
            استنتج من: "عبارة"
        """
        tok = self.eat(TokenType.INFER_FROM)

        # Handle optional "من" after "استنتج"
        if self.match(TokenType.IDENTIFIER) and self.current_token.value == "من":
            self.advance()

        self.eat(TokenType.COLON)
        statement = self.parse_expression()
        return self._with_pos(InferFrom(statement), tok)

    def parse_contradiction(self):
        """Parse contradiction detection

        Syntax:
            contradiction between: [item1, item2]
            resolve: "strategy"
        """
        tok = self.eat(TokenType.CONTRADICTION)
        self.eat(TokenType.BETWEEN)
        self.eat(TokenType.COLON)

        items = self.parse_expression()  # Should be a list

        resolution = None
        if self.match(TokenType.NEWLINE):
            self.advance()
        if self.match(TokenType.RESOLVE):
            self.eat(TokenType.RESOLVE)
            self.eat(TokenType.COLON)
            resolution = self.parse_expression()

        return self._with_pos(Contradiction(items, resolution), tok)

    def parse_evolving_knowledge(self):
        """Parse evolving knowledge

        Syntax:
            knowledge "<name>":
            {
                current_value: ...,
                history: [...],
                future_prediction: {...}
            }
        """
        tok = self.eat(TokenType.KNOWLEDGE)

        if self.match(TokenType.STRING):
            name = self.eat(TokenType.STRING).value
        else:
            name = self.eat(TokenType.IDENTIFIER).value

        self.eat(TokenType.COLON)
        config = self.parse_entity_body()
        return self._with_pos(EvolvingKnowledge(name, config), tok)

    def parse_ontology(self):
        """Parse ontology definition

        Syntax:
            ontology "<name>":
            {
                root: "concept",
                taxonomy: {...}
            }
        """
        tok = self.eat(TokenType.ONTOLOGY)

        if self.match(TokenType.STRING):
            name = self.eat(TokenType.STRING).value
        else:
            name = self.eat(TokenType.IDENTIFIER).value

        self.eat(TokenType.COLON)
        config = self.parse_entity_body()
        return self._with_pos(Ontology(name, config), tok)

    def parse_concept_definition(self):
        """Parse concept definition

        Syntax:
            concept "<name>": {...}
            مفهوم "<اسم>": {...}
        """
        tok = self.eat(TokenType.CONCEPT)

        if self.match(TokenType.STRING):
            name = self.eat(TokenType.STRING).value
        else:
            name = self.eat(TokenType.IDENTIFIER).value

        self.eat(TokenType.COLON)
        properties = self.parse_entity_body()
        return self._with_pos(Concept(name, properties), tok)

    def parse_narrative(self):
        """Parse narrative definition

        Syntax:
            narrative "<name>":
            {
                characters: {...},
                events: [...],
                structure: "..."
            }
        """
        tok = self.eat(TokenType.NARRATIVE)

        if self.match(TokenType.STRING):
            name = self.eat(TokenType.STRING).value
        else:
            name = self.eat(TokenType.IDENTIFIER).value

        self.eat(TokenType.COLON)
        config = self.parse_entity_body()
        return self._with_pos(Narrative(name, config), tok)

    def parse_generate_narrative(self):
        """Parse generate narrative statement

        Syntax:
            generate_narrative: based_on("template")
            ولّد_سرد: بناءً_على("قالب")
        """
        tok = self.eat(TokenType.GENERATE_NARRATIVE)
        self.eat(TokenType.COLON)
        template = self.parse_expression()
        return self._with_pos(GenerateNarrative(template), tok)

    def parse_current_context(self):
        """Parse current context definition

        Syntax:
            current_context: {...}
            سياق_حالي: {...}
        """
        tok = self.eat(TokenType.CURRENT_CONTEXT)
        self.eat(TokenType.COLON)
        context_data = self.parse_entity_body()
        return self._with_pos(CurrentContext(context_data), tok)

    # ========================================================================
    # EXISTENTIAL MODEL PARSING (النموذج الوجودي)
    # ========================================================================

    def parse_domain(self):
        """Parse domain definition

        Syntax:
            domain "name": {...}
            مجال "اسم": {...}
        """
        tok = self.eat(TokenType.DOMAIN)
        name = self.eat(TokenType.STRING).value
        self.eat(TokenType.COLON)
        config = self.parse_entity_body()
        return self._with_pos(Domain(name, config), tok)

    def parse_generic_environment(self):
        """Parse generic environment definition

        Syntax:
            environment "name" in_domain "domain": {...}
            بيئة "اسم" في_مجال "مجال": {...}
        """
        tok = self.eat(TokenType.ENVIRONMENT)
        name = self.eat(TokenType.STRING).value
        self.eat(TokenType.IN_DOMAIN)
        domain = self.eat(TokenType.STRING).value
        self.eat(TokenType.COLON)
        config = self.parse_entity_body()
        return self._with_pos(GenericEnvironment(name, domain, config), tok)

    def parse_existential_being(self):
        """Parse existential being definition

        Syntax:
            existential_being "name" of_type "type" in_domain "domain": {...}
            كائن_وجودي "اسم" من_نوع "نوع" في_مجال "مجال": {...}
        """
        tok = self.eat(TokenType.EXISTENTIAL_BEING)
        name = self.eat(TokenType.STRING).value
        self.eat(TokenType.OF_TYPE)
        entity_type = self.eat(TokenType.STRING).value
        self.eat(TokenType.IN_DOMAIN)
        domain = self.eat(TokenType.STRING).value
        self.eat(TokenType.COLON)
        config = self.parse_entity_body()
        return self._with_pos(ExistentialBeing(name, entity_type, domain, config), tok)

    def parse_domain_relation(self):
        """Parse domain relation definition

        Syntax:
            domain_relation "name" in_domain "domain": {...}
            علاقة_مجالية "اسم" في_مجال "مجال": {...}
        """
        tok = self.eat(TokenType.DOMAIN_RELATION)
        name = self.eat(TokenType.STRING).value
        self.eat(TokenType.IN_DOMAIN)
        domain = self.eat(TokenType.STRING).value
        self.eat(TokenType.COLON)
        config = self.parse_entity_body()
        return self._with_pos(DomainRelation(name, domain, config), tok)

    def parse_domain_action(self):
        """Parse domain action definition

        Syntax:
            domain_action "name" in_domain "domain": {...}
            فعل_مجالي "اسم" في_مجال "مجال": {...}
        """
        tok = self.eat(TokenType.DOMAIN_ACTION)
        name = self.eat(TokenType.STRING).value
        self.eat(TokenType.IN_DOMAIN)
        domain = self.eat(TokenType.STRING).value
        self.eat(TokenType.COLON)
        config = self.parse_entity_body()
        return self._with_pos(DomainAction(name, domain, config), tok)

    def parse_metaphorical_meaning(self):
        """Parse metaphorical meaning definition

        Syntax:
            metaphorical_meaning "name" in_domain "domain": {...}
            معنى_مجازي "اسم" في_مجال "مجال": {...}
        """
        tok = self.eat(TokenType.METAPHORICAL_MEANING)
        name = self.eat(TokenType.STRING).value
        self.eat(TokenType.IN_DOMAIN)
        domain = self.eat(TokenType.STRING).value
        self.eat(TokenType.COLON)
        config = self.parse_entity_body()
        return self._with_pos(MetaphoricalMeaning(name, domain, config), tok)

    def parse_domain_law(self):
        """Parse domain law definition

        Syntax:
            domain_law "name" in_domain "domain": {...}
            قانون_مجالي "اسم" في_مجال "مجال": {...}
        """
        tok = self.eat(TokenType.DOMAIN_LAW)
        name = self.eat(TokenType.STRING).value
        self.eat(TokenType.IN_DOMAIN)
        domain = self.eat(TokenType.STRING).value
        self.eat(TokenType.COLON)
        config = self.parse_entity_body()
        return self._with_pos(DomainLaw(name, domain, config), tok)

    def parse_existential_query(self):
        """Parse existential query

        Syntax:
            existential_query: {...}
            استعلام_وجودي: {...}
        """
        tok = self.eat(TokenType.EXISTENTIAL_QUERY)
        self.eat(TokenType.COLON)
        config = self.parse_entity_body()
        return self._with_pos(ExistentialQuery(config), tok)


