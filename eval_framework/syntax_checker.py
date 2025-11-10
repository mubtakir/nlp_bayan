#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Syntax checker for Bayan code snippets.
Uses Bayan's HybridLexer/HybridParser to parse code without executing it.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

# Local import of Bayan language components
from bayan.bayan import HybridLexer, HybridParser


@dataclass
class SyntaxResult:
    ok: bool
    error: Optional[str] = None


import re

_SEMI = re.compile(r";+")
_PLUS_EQ = re.compile(r"(?P<lhs>[\w\u0600-\u06FF\.]+)\s*\+=\s*(?P<rhs>[^;\n]+)")
_MINUS_EQ = re.compile(r"(?P<lhs>[\w\u0600-\u06FF\.]+)\s*-_=\s*(?P<rhs>[^;\n]+)")  # placeholder, will fix next line
_MINUS_EQ = re.compile(r"(?P<lhs>[\w\u0600-\u06FF\.]+)\s*-==?\s*(?P<rhs>[^;\n]+)")  # safety
_MINUS_EQ = re.compile(r"(?P<lhs>[\w\u0600-\u06FF\.]+)\s*-\=\s*(?P<rhs>[^;\n]+)")


def _normalize(code: str) -> str:
    # Split statements by semicolons into newlines
    text = _SEMI.sub("\n", code or "")
    # Normalize augmented assignment to simple assignment
    text = _PLUS_EQ.sub(lambda m: f"{m.group('lhs')} = {m.group('lhs')} + {m.group('rhs')}", text)
    text = _MINUS_EQ.sub(lambda m: f"{m.group('lhs')} = {m.group('lhs')} - {m.group('rhs')}", text)
    return text


def check_syntax(code: str, filename: str = "<mem>") -> SyntaxResult:
    """Parse Bayan code and return SyntaxResult without running it."""
    try:
        code_norm = _normalize(code or "")
        lexer = HybridLexer(code_norm)
        tokens = lexer.tokenize()
        parser = HybridParser(tokens, filename=filename)
        _ = parser.parse()
        return SyntaxResult(ok=True, error=None)
    except Exception as e:
        return SyntaxResult(ok=False, error=str(e))


__all__ = ["SyntaxResult", "check_syntax"]

