"""
Top-level Bayan package initializer.
Re-exports symbols from the implementation subpackage `bayan.bayan` for convenience,
AND provides compatibility aliases so `import bayan.lexer` etc. keep working.
"""

from .bayan import *  # noqa: F401,F403

# Compat: expose submodules under top-level package, e.g. `bayan.lexer`
import importlib as _importlib
import sys as _sys

_submods = [
    'lexer', 'parser', 'logical_engine', 'hybrid_interpreter', 'traditional_interpreter',
    'ast_nodes', 'object_system', 'import_system', 'entity_engine'
    # Removed 'builtins' and 'visualization' - they import heavy dependencies (matplotlib)
    # and cause ~10s startup delay. Import them explicitly when needed.
]
for _name in _submods:
    try:
        _mod = _importlib.import_module(f'.bayan.{_name}', __name__)
        _sys.modules[f'{__name__}.{_name}'] = _mod
    except Exception:
        # Be permissive; some tools may import only a subset
        pass

