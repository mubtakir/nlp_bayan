"""
🎨 Bayan Visual Programming Editor
محرر البرمجة البصرية لبيان

A drag-and-drop block-based programming interface for Bayan language.
"""

from flask import Flask, render_template, request, jsonify
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bayan.bayan import run_code

app = Flask(__name__, 
            template_folder='templates',
            static_folder='static')

@app.route('/')
def index():
    """Main visual editor page"""
    return render_template('visual_editor.html')

@app.route('/run', methods=['POST'])
def run_bayan_code():
    """Execute Bayan code and return result"""
    try:
        data = request.get_json()
        code = data.get('code', '')
        
        # Capture output
        import io
        from contextlib import redirect_stdout
        
        f = io.StringIO()
        with redirect_stdout(f):
            result = run_code(code)
        
        output = f.getvalue()
        
        return jsonify({
            'success': True,
            'output': output,
            'result': str(result) if result else None
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/blocks')
def get_blocks():
    """Get available block definitions"""
    blocks = {
        'variables': [
            {'id': 'var_assign', 'name': 'متغير = قيمة', 'name_en': 'Variable Assignment', 'template': '{var} = {value}'},
            {'id': 'var_print', 'name': 'طباعة', 'name_en': 'Print', 'template': 'print({value})'},
        ],
        'math': [
            {'id': 'math_add', 'name': 'جمع', 'name_en': 'Add', 'template': '{a} + {b}'},
            {'id': 'math_sub', 'name': 'طرح', 'name_en': 'Subtract', 'template': '{a} - {b}'},
            {'id': 'math_mul', 'name': 'ضرب', 'name_en': 'Multiply', 'template': '{a} * {b}'},
            {'id': 'math_div', 'name': 'قسمة', 'name_en': 'Divide', 'template': '{a} / {b}'},
        ],
        'control': [
            {'id': 'if_block', 'name': 'إذا', 'name_en': 'If', 'template': 'if ({condition}) {\n    {body}\n}'},
            {'id': 'if_else', 'name': 'إذا / وإلا', 'name_en': 'If/Else', 'template': 'if ({condition}) {\n    {if_body}\n} else {\n    {else_body}\n}'},
            {'id': 'while_loop', 'name': 'طالما', 'name_en': 'While', 'template': 'while ({condition}) {\n    {body}\n}'},
            {'id': 'for_loop', 'name': 'لكل', 'name_en': 'For', 'template': 'for {var} in range({count}) {\n    {body}\n}'},
        ],
        'functions': [
            {'id': 'func_def', 'name': 'تعريف دالة', 'name_en': 'Define Function', 'template': 'def {name}({params}): {\n    {body}\n}'},
            {'id': 'func_call', 'name': 'استدعاء دالة', 'name_en': 'Call Function', 'template': '{name}({args})'},
            {'id': 'func_return', 'name': 'إرجاع', 'name_en': 'Return', 'template': 'return {value}'},
        ],
        'logic': [
            {'id': 'fact', 'name': 'حقيقة', 'name_en': 'Fact', 'template': '{predicate}({args}).'},
            {'id': 'rule', 'name': 'قاعدة', 'name_en': 'Rule', 'template': '{head}({args}) :- {body}.'},
            {'id': 'query', 'name': 'استعلام', 'name_en': 'Query', 'template': 'query {predicate}({args})?'},
        ],
        'comparison': [
            {'id': 'cmp_eq', 'name': 'يساوي', 'name_en': 'Equals', 'template': '{a} == {b}'},
            {'id': 'cmp_neq', 'name': 'لا يساوي', 'name_en': 'Not Equals', 'template': '{a} != {b}'},
            {'id': 'cmp_gt', 'name': 'أكبر من', 'name_en': 'Greater Than', 'template': '{a} > {b}'},
            {'id': 'cmp_lt', 'name': 'أصغر من', 'name_en': 'Less Than', 'template': '{a} < {b}'},
        ],
    }
    return jsonify(blocks)

if __name__ == '__main__':
    print("🎨 Bayan Visual Programming Editor")
    print("محرر البرمجة البصرية لبيان")
    print("=" * 50)
    print("افتح المتصفح على: http://127.0.0.1:5003")
    print("=" * 50)
    app.run(debug=True, port=5003)
