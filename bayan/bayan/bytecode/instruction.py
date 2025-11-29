"""
Bytecode Instruction Class
===========================

Represents a single bytecode instruction with opcode and optional argument.
"""

from .opcodes import Opcode, opcode_name, has_arg


class Instruction:
    """
    A single bytecode instruction.
    
    Attributes:
        opcode (Opcode): The operation code
        arg: The argument (None if opcode takes no argument)
        offset (int): Position in bytecode sequence
    """
    
    __slots__ = ('opcode', 'arg', 'offset', 'line_number')
    
    def __init__(self, opcode, arg=None, offset=0, line_number=None):
        """
        Initialize instruction.
        
        Args:
            opcode (Opcode or int): Operation code
            arg: Argument value (int, str, or None)
            offset (int): Byte offset in code
            line_number (int): Source line number
        """
        if isinstance(opcode, int):
            self.opcode = Opcode(opcode)
        else:
            self.opcode = opcode
            
        self.arg = arg
        self.offset = offset
        self.line_number = line_number
    
    def __repr__(self):
        if self.arg is not None:
            return f"Instruction({opcode_name(self.opcode)}, {self.arg!r})"
        return f"Instruction({opcode_name(self.opcode)})"
    
    def __str__(self):
        """Human-readable format for disassembly"""
        name = opcode_name(self.opcode)
        if self.arg is not None:
            return f"{self.offset:4d}  {name:15s} {self.arg}"
        return f"{self.offset:4d}  {name}"
    
    def __eq__(self, other):
        if not isinstance(other, Instruction):
            return False
        return (self.opcode == other.opcode and 
                self.arg == other.arg)
    
    def size(self):
        """Return the size of this instruction in bytes"""
        size = 1  # Opcode itself
        
        if has_arg(self.opcode):
            # For PoC, arguments are variable length
            # In full implementation, this would be more sophisticated
            if isinstance(self.arg, int):
                if self.arg < 256:
                    size += 1
                else:
                    size += 2
            elif isinstance(self.arg, str):
                # String indices into constant pool
                size += 2
            else:
                size += 2  # Default
        
        return size
    
    def encode(self):
        """
        Encode instruction to bytes.
        
        Returns:
            bytes: Encoded instruction
        """
        result = bytes([self.opcode])
        
        if self.arg is not None:
            if isinstance(self.arg, int):
                # Encode integer argument
                if self.arg < 256:
                    result += bytes([self.arg])
                else:
                    # 2-byte encoding for larger numbers
                    result += self.arg.to_bytes(2, 'big')
            else:
                # For strings and other types, store as 2-byte index
                # (will be resolved during code generation)
                result += bytes([0, 0])  # Placeholder
        
        return result
    
    @staticmethod
    def decode(bytecode, offset=0):
        """
        Decode instruction from bytecode.
        
        Args:
            bytecode (bytes): Bytecode sequence
            offset (int): Starting offset
        
        Returns:
            Instruction: Decoded instruction
        """
        opcode = Opcode(bytecode[offset])
        arg = None
        
        if has_arg(opcode):
            # Simple decoding for PoC
            if offset + 1 < len(bytecode):
                arg = bytecode[offset + 1]
                # Check if 2-byte argument
                if offset + 2 < len(bytecode) and bytecode[offset + 1] != 0:
                    arg = int.from_bytes(bytecode[offset+1:offset+3], 'big')
        
        return Instruction(opcode, arg, offset)


class CodeObject:
    """
    Represents a compiled code object (function, module, etc.)
    
    Similar to Python's code objects.
    """
    
    def __init__(self, name, instructions, constants=None, names=None):
        """
        Initialize code object.
        
        Args:
            name (str): Code object name (function name, '<module>', etc.)
            instructions (list[Instruction]): List of instructions
            constants (list): Constant pool
            names (list[str]): Variable/function names
        """
        self.name = name
        self.instructions = instructions
        self.constants = constants or []
        self.names = names or []
        
        # Calculate offsets
        offset = 0
        for instr in self.instructions:
            instr.offset = offset
            offset += instr.size()
    
    def __repr__(self):
        return f"CodeObject({self.name!r}, {len(self.instructions)} instructions)"
    
    def disassemble(self):
        """Return disassembled code as string"""
        lines = [f"Code object <{self.name}>:"]
        lines.append(f"  Constants: {self.constants}")
        lines.append(f"  Names: {self.names}")
        lines.append("")
        
        for instr in self.instructions:
            lines.append(f"  {instr}")
        
        return "\n".join(lines)
    
    def encode(self):
        """Encode entire code object to bytes"""
        return b''.join(instr.encode() for instr in self.instructions)
