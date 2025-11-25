"""
Bytecode Opcode Definitions
============================

Defines all bytecode instructions for the Bayan VM.

Opcode Format:
- Each opcode is 1 byte (0x00 - 0xFF)
- Arguments follow the opcode (variable length)
- Total of 40+ opcodes across 7 categories
"""

from enum import IntEnum


class Opcode(IntEnum):
    """Bytecode operation codes"""
    
    # ===== Stack Operations (0x00 - 0x0F) =====
    NOP = 0x00          # No operation
    LOAD_CONST = 0x01   # Push constant from pool: arg=const_index
    LOAD_VAR = 0x02     # Push variable value: arg=var_name
    STORE_VAR = 0x03    # Pop and store to variable: arg=var_name
    LOAD_ATTR = 0x04    # Load attribute from TOS: arg=attr_name
    STORE_ATTR = 0x05   # Store to attribute: arg=attr_name
    POP = 0x06          # Pop top of stack
    DUP = 0x07          # Duplicate TOS
    
    # ===== Arithmetic Operations (0x10 - 0x1F) =====
    ADD = 0x10          # TOS = TOS1 + TOS
    SUB = 0x11          # TOS = TOS1 - TOS
    MUL = 0x12          # TOS = TOS1 * TOS
    DIV = 0x13          # TOS = TOS1 / TOS
    FLOOR_DIV = 0x14    # TOS = TOS1 // TOS
    MOD = 0x15          # TOS = TOS1 % TOS
    POW = 0x16          # TOS = TOS1 ** TOS
    NEG = 0x17          # TOS = -TOS
    NOT = 0x18          # TOS = not TOS
    AND = 0x19          # TOS = TOS1 and TOS
    OR = 0x1A           # TOS = TOS1 or TOS
    
    # ===== Comparison Operations (0x20 - 0x2F) =====
    EQ = 0x20           # TOS = (TOS1 == TOS)
    NE = 0x21           # TOS = (TOS1 != TOS)
    LT = 0x22           # TOS = (TOS1 < TOS)
    LE = 0x23           # TOS = (TOS1 <= TOS)
    GT = 0x24           # TOS = (TOS1 > TOS)
    GE = 0x25           # TOS = (TOS1 >= TOS)
    IN = 0x26           # TOS = (TOS1 in TOS)
    IS = 0x27           # TOS = (TOS1 is TOS)
    
    # ===== Control Flow (0x30 - 0x3F) =====
    JUMP = 0x30         # Unconditional jump: arg=target_offset
    JUMP_IF_TRUE = 0x31   # Jump if TOS is true: arg=target_offset
    JUMP_IF_FALSE = 0x32  # Jump if TOS is false: arg=target_offset
    JUMP_IF_NONE = 0x33   # Jump if TOS is None: arg=target_offset
    LOOP_START = 0x34   # Mark loop start
    LOOP_END = 0x35     # Mark loop end
    BREAK = 0x36        # Break from loop
    CONTINUE = 0x37     # Continue loop
    
    # ===== Function Operations (0x40 - 0x4F) =====
    CALL_FUNC = 0x40    # Call function: arg=nargs
    RETURN = 0x41       # Return from function (TOS = return value)
    MAKE_FUNC = 0x42    # Create function object: arg=code_index
    LOAD_FUNC = 0x43    # Load function by name: arg=func_name
    CALL_METHOD = 0x44  # Call method: arg1=method_name, arg2=nargs
    MAKE_CLASS = 0x45   # Create class: arg=class_name
    LOAD_GLOBAL = 0x46  # Load global variable: arg=var_name
    STORE_GLOBAL = 0x47 # Store global variable: arg=var_name
    
    # ===== Data Structures (0x50 - 0x5F) =====
    MAKE_LIST = 0x50    # Create list from top N items: arg=count
    MAKE_DICT = 0x51    # Create dict from top 2N items: arg=count
    MAKE_TUPLE = 0x52   # Create tuple from top N items: arg=count
    LIST_APPEND = 0x53  # Append TOS to TOS1 (list)
    DICT_SET = 0x54     # Set TOS1[TOS2] = TOS
    INDEX = 0x55        # TOS = TOS1[TOS]
    SLICE = 0x56        # TOS = TOS1[TOS2:TOS]
    
    # ===== Logic Programming (0x60 - 0x6F) =====
    ASSERT_FACT = 0x60  # Assert fact from TOS
    RETRACT_FACT = 0x61 # Retract fact
    QUERY = 0x62        # Execute logical query: arg=nargs
    UNIFY = 0x63        # Unify TOS1 with TOS
    BACKTRACK = 0x64    # Trigger backtracking
    CUT = 0x65          # Prolog cut operation
    MAKE_RULE = 0x66    # Create rule: arg=code_index
    CHECK_CONDITION = 0x67  # Check rule condition
    
    # ===== Special (0x70 - 0x7F) =====
    PRINT = 0x70        # Print TOS (for debugging)
    IMPORT = 0x71       # Import module: arg=module_name
    BUILD_SLICE = 0x72  # Build slice object from TOS2:TOS1:TOS
    UNPACK_SEQ = 0x73   # Unpack sequence: arg=count
    BUILD_STRING = 0x74 # Build formatted string
    
    # Sentinel
    MAX_OPCODE = 0x7F


# Opcode name lookup (for disassembly)
OpcodeName = {opcode: name for name, opcode in Opcode.__members__.items()}


# Opcodes that take arguments
OPCODES_WITH_ARGS = {
    Opcode.LOAD_CONST,
    Opcode.LOAD_VAR,
    Opcode.STORE_VAR,
    Opcode.LOAD_ATTR,
    Opcode.STORE_ATTR,
    Opcode.JUMP,
    Opcode.JUMP_IF_TRUE,
    Opcode.JUMP_IF_FALSE,
    Opcode.JUMP_IF_NONE,
    Opcode.CALL_FUNC,
    Opcode.MAKE_FUNC,
    Opcode.LOAD_FUNC,
    Opcode.CALL_METHOD,
    Opcode.MAKE_CLASS,
    Opcode.LOAD_GLOBAL,
    Opcode.STORE_GLOBAL,
    Opcode.MAKE_LIST,
    Opcode.MAKE_DICT,
    Opcode.MAKE_TUPLE,
    Opcode.QUERY,
    Opcode.MAKE_RULE,
    Opcode.IMPORT,
    Opcode.UNPACK_SEQ,
}


def has_arg(opcode):
    """Check if opcode takes an argument"""
    return opcode in OPCODES_WITH_ARGS


def opcode_name(opcode):
    """Get opcode name for disassembly"""
    return OpcodeName.get(opcode, f"UNKNOWN_{opcode:#04x}")


# Opcode argument sizes (in bytes)
OPCODE_ARG_SIZE = {
    Opcode.LOAD_CONST: 2,      # 2 bytes for constant pool index
    Opcode.JUMP: 2,             # 2 bytes for jump offset
    Opcode.JUMP_IF_TRUE: 2,
    Opcode.JUMP_IF_FALSE: 2,
    Opcode.JUMP_IF_NONE: 2,
    # Most others: variable length (for now, assume 0 for simple PoC)
}


def get_arg_size(opcode):
    """Get argument size for opcode (0 if no arg)"""
    if not has_arg(opcode):
        return 0
    return OPCODE_ARG_SIZE.get(opcode, 0)
