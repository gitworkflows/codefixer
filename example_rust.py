"""
Example usage of Rust compilation.
"""
from code_fixer.compilers import compile_rust

def main():
    # Example Rust code
    rust_code = '''
fn main() {
    println!("Hello from Rust!");
}
'''
    
    try:
        success, message = compile_rust(rust_code, "hello")
        if success:
            print("Compilation successful!")
        else:
            print(f"Compilation failed: {message}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()