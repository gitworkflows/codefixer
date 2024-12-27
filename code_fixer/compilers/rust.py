"""
Rust compilation and error handling.
"""
import subprocess
from typing import Tuple, Optional
from ..core.errors import CompilationError
from ..core.logging import log_error

def compile_rust(source_code: str, output_path: Optional[str] = None) -> Tuple[bool, str]:
    """
    Compile Rust source code using rustc.
    
    Args:
        source_code: Rust source code to compile
        output_path: Optional path for compiled binary
        
    Returns:
        Tuple of (success: bool, message: str)
    """
    try:
        # Write source to temporary file
        with open('temp.rs', 'w') as f:
            f.write(source_code)
        
        # Build command
        cmd = ['rustc', 'temp.rs']
        if output_path:
            cmd.extend(['-o', output_path])
            
        # Run compiler
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            return True, "Compilation successful"
        else:
            return False, result.stderr
            
    except Exception as e:
        log_error(e, "Rust compilation failed")
        raise CompilationError(f"Failed to compile Rust code: {str(e)}")