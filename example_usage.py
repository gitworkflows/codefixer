"""
Example usage of the code fixing system.
"""
from code_fixer import fix_code

def main():
    # Example code with issues
    code = '''
def process_items(items=[]):    
    for Item in items:     
        print(Item)   


    return items
'''
    
    try:
        fixed_code, issues = fix_code(code)
        
        if issues:
            print("Found issues:")
            for issue in issues:
                print(issue.format())
            print("\nFixed code:")
            print(fixed_code)
        else:
            print("No issues found!")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()