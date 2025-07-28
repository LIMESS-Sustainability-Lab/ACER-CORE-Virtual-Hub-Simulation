import json
import re

def add_warning_suppression_to_notebook(notebook_path):
    """Add warning suppression to all cells in a Jupyter notebook."""
    
    # Read the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Process each cell
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            
            # Check if warnings import is already present
            if 'import warnings' not in source:
                # Add warnings import at the beginning
                cell['source'] = ['import warnings\n'] + cell['source']
            
            # Check if warning suppression is already present
            if 'warnings.filterwarnings' not in source:
                # Add warning suppression after imports
                new_source = []
                imports_done = False
                
                for line in cell['source']:
                    new_source.append(line)
                    
                    # After the last import, add warning suppression
                    if not imports_done and line.strip() and not line.strip().startswith('import') and not line.strip().startswith('from'):
                        new_source.insert(-1, '\n# Suppress Cartopy download warnings\n')
                        new_source.insert(-1, 'warnings.filterwarnings(\'ignore\', category=UserWarning, module=\'cartopy.io\')\n')
                        imports_done = True
                
                cell['source'] = new_source
    
    # Write the modified notebook back
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)

if __name__ == "__main__":
    notebook_path = "paper-figures/reference-market.ipynb"
    add_warning_suppression_to_notebook(notebook_path)
    print(f"Warning suppression added to {notebook_path}") 