#!/usr/bin/env python3
"""
Test Bytecode Logic Programming
===============================

Tests integration of LogicalEngine with Bytecode VM.
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bayan.bayan.bytecode.instruction import Instruction, CodeObject
from bayan.bayan.bytecode.vm import BytecodeVM
from bayan.bayan.bytecode.opcodes import Opcode
from bayan.bayan.logical_engine import Fact, Predicate, Term, Substitution


class TestBytecodeLogic(unittest.TestCase):
    def setUp(self):
        self.vm = BytecodeVM()

    def test_assert_fact(self):
        """Test ASSERT_FACT opcode"""
        # Fact: parent(john, mary).
        fact = Fact(Predicate('parent', [
            Term('john'),
            Term('mary')
        ]))
        
        code = CodeObject(
            name='test_fact',
            instructions=[
                Instruction(Opcode.LOAD_CONST, 0),
                Instruction(Opcode.ASSERT_FACT),
            ],
            constants=[fact],
            names=[]
        )
        
        self.vm.execute(code)
        
        # Verify fact is in KB
        self.assertIn('parent', self.vm.logical_engine.knowledge_base)
        kb_facts = self.vm.logical_engine.knowledge_base['parent']
        self.assertEqual(len(kb_facts), 1)
        self.assertEqual(kb_facts[0].predicate.name, 'parent')
        self.assertEqual(kb_facts[0].predicate.args[0].value, 'john')

    def test_query(self):
        """Test QUERY opcode"""
        # 1. Assert parent(john, mary)
        fact = Fact(Predicate('parent', [
            Term('john'),
            Term('mary')
        ]))
        self.vm.logical_engine.add_fact(fact)
        
        # 2. Query: ?- parent(john, ?X).
        query_goal = Predicate('parent', [
            Term('john'),
            Term('X', is_variable=True)
        ])
        
        code = CodeObject(
            name='test_query',
            instructions=[
                Instruction(Opcode.LOAD_CONST, 0),
                Instruction(Opcode.QUERY),
                # Result is on stack, will be returned by execute()
            ],
            constants=[query_goal],
            names=[]
        )
        
        results = self.vm.execute(code)
        
        # Verify results
        self.assertEqual(len(results), 1)
        self.assertIsInstance(results[0], Substitution)
        # Lookup returns a Term object, check its value
        self.assertEqual(results[0].lookup('X').value, 'mary')

    def test_codegen_logic(self):
        """Test compilation of logic AST nodes"""
        from bayan.bayan.bytecode.codegen import CodeGenerator
        from bayan.bayan.ast_nodes import LogicalFact, LogicalPredicate, LogicalConstant, LogicalVariable, LogicalQuery
        
        # AST: parent(alice, bob).
        fact_node = LogicalFact(
            predicate=LogicalPredicate('parent', [
                LogicalConstant('alice'),
                LogicalConstant('bob')
            ])
        )
        
        # AST: ?- parent(alice, ?Who).
        query_node = LogicalQuery(
            goal=LogicalPredicate('parent', [
                LogicalConstant('alice'),
                LogicalVariable('Who')
            ])
        )
        
        gen = CodeGenerator()
        code = gen.generate([fact_node, query_node])
        
        # Execute
        self.vm.execute(code)
        
        # Verify
        # 1. Fact asserted
        self.assertIn('parent', self.vm.logical_engine.knowledge_base)
        
        # 2. Query executed (result is on stack, but we didn't store it)
        # To verify query, we can check the VM stack if we didn't pop it, 
        # but codegen for expression statement pops it.
        # Let's trust the previous test for QUERY opcode and this test for compilation.
        
        # Check instructions
        # LOAD_CONST (fact), ASSERT_FACT, LOAD_CONST (goal), QUERY, POP
        instrs = code.instructions
        self.assertEqual(instrs[1].opcode, Opcode.ASSERT_FACT)
        self.assertEqual(instrs[3].opcode, Opcode.QUERY)

    def test_rule(self):
        """Test logical rule execution"""
        from bayan.bayan.logical_engine import Rule
        
        # Rule: grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
        # Facts: parent(a, b), parent(b, c)
        
        # 1. Assert Facts
        p_ab = Fact(Predicate('parent', [Term('a'), Term('b')]))
        p_bc = Fact(Predicate('parent', [Term('b'), Term('c')]))
        self.vm.logical_engine.add_fact(p_ab)
        self.vm.logical_engine.add_fact(p_bc)
        
        # 2. Assert Rule
        rule = Rule(
            head=Predicate('grandparent', [Term('X', True), Term('Z', True)]),
            body=[
                Predicate('parent', [Term('X', True), Term('Y', True)]),
                Predicate('parent', [Term('Y', True), Term('Z', True)])
            ]
        )
        
        code_rule = CodeObject(
            name='rule',
            instructions=[
                Instruction(Opcode.LOAD_CONST, 0),
                Instruction(Opcode.ASSERT_FACT),
            ],
            constants=[rule],
            names=[]
        )
        self.vm.execute(code_rule)
        
        # 3. Query: ?- grandparent(a, ?Who).
        query = Predicate('grandparent', [Term('a'), Term('Who', True)])
        code_query = CodeObject(
            name='query',
            instructions=[
                Instruction(Opcode.LOAD_CONST, 0),
                Instruction(Opcode.QUERY),
            ],
            constants=[query],
            names=[]
        )
        
        results = self.vm.execute(code_query)
        
        self.assertEqual(len(results), 1)
        
        # Helper to dereference
        def deref(val, sub):
            from bayan.bayan.logical_engine import Term
            if isinstance(val, Term) and val.is_variable:
                next_val = sub.lookup(val.value)
                if next_val is not None:
                    return deref(next_val, sub)
            return val

        val = results[0].lookup('Who')
        resolved = deref(val, results[0])
        
        # Check value (resolved might be Term('c') or 'c')
        final_val = resolved.value if hasattr(resolved, 'value') else resolved
        self.assertEqual(final_val, 'c')


if __name__ == '__main__':
    unittest.main()
