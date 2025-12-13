/**
 * Bayan Visual Editor - JavaScript
 * محرر بيان البصري - جافاسكريبت
 */

// Block definitions with colors and templates
const BLOCKS = {
    variables: {
        icon: '📦',
        color: 'variable',
        items: [
            { id: 'var_assign', name: 'متغير = قيمة', template: '{var} = {value}', inputs: ['var', 'value'] },
            { id: 'var_print', name: 'طباعة', template: 'print({value})', inputs: ['value'] },
            { id: 'var_input', name: 'إدخال', template: '{var} = input("{prompt}")', inputs: ['var', 'prompt'] },
        ]
    },
    math: {
        icon: '🔢',
        color: 'math',
        items: [
            { id: 'math_add', name: 'جمع (+)', template: '{a} + {b}', inputs: ['a', 'b'] },
            { id: 'math_sub', name: 'طرح (-)', template: '{a} - {b}', inputs: ['a', 'b'] },
            { id: 'math_mul', name: 'ضرب (×)', template: '{a} * {b}', inputs: ['a', 'b'] },
            { id: 'math_div', name: 'قسمة (÷)', template: '{a} / {b}', inputs: ['a', 'b'] },
        ]
    },
    control: {
        icon: '🔄',
        color: 'control',
        items: [
            { id: 'if_block', name: 'إذا (شرط)', template: 'if ({cond}) {\n    {body}\n}', inputs: ['cond', 'body'], multiline: true },
            { id: 'if_else', name: 'إذا / وإلا', template: 'if ({cond}) {\n    {if_body}\n} else {\n    {else_body}\n}', inputs: ['cond', 'if_body', 'else_body'], multiline: true },
            { id: 'while_loop', name: 'طالما (حلقة)', template: 'while ({cond}) {\n    {body}\n}', inputs: ['cond', 'body'], multiline: true },
            { id: 'for_loop', name: 'كرر (عدد)', template: 'for {i} in range({n}) {\n    {body}\n}', inputs: ['i', 'n', 'body'], multiline: true },
        ]
    },
    functions: {
        icon: '⚡',
        color: 'function',
        items: [
            { id: 'func_def', name: 'تعريف دالة', template: 'def {name}({params}): {\n    {body}\n}', inputs: ['name', 'params', 'body'], multiline: true },
            { id: 'func_call', name: 'استدعاء دالة', template: '{name}({args})', inputs: ['name', 'args'] },
            { id: 'func_return', name: 'إرجاع قيمة', template: 'return {value}', inputs: ['value'] },
        ]
    },
    logic: {
        icon: '🧠',
        color: 'logic',
        items: [
            { id: 'fact', name: 'حقيقة منطقية', template: '{pred}({args}).', inputs: ['pred', 'args'] },
            { id: 'rule', name: 'قاعدة منطقية', template: '{head}({hargs}) :- {body}.', inputs: ['head', 'hargs', 'body'] },
            { id: 'query', name: 'استعلام', template: 'query {pred}({args})?', inputs: ['pred', 'args'] },
        ]
    },
    comparison: {
        icon: '⚖️',
        color: 'comparison',
        items: [
            { id: 'cmp_eq', name: 'يساوي (==)', template: '{a} == {b}', inputs: ['a', 'b'] },
            { id: 'cmp_neq', name: 'لا يساوي (!=)', template: '{a} != {b}', inputs: ['a', 'b'] },
            { id: 'cmp_gt', name: 'أكبر من (>)', template: '{a} > {b}', inputs: ['a', 'b'] },
            { id: 'cmp_lt', name: 'أصغر من (<)', template: '{a} < {b}', inputs: ['a', 'b'] },
        ]
    }
};

// State
let droppedBlocks = [];
let blockCounter = 0;
let currentTab = 'code';

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    initToolbox();
    initWorkspace();
    initTabs();
});

// Initialize toolbox with blocks
function initToolbox() {
    const toolbox = document.getElementById('toolbox');

    for (const [category, data] of Object.entries(BLOCKS)) {
        const section = document.createElement('div');
        section.className = 'toolbox-section';

        const title = document.createElement('div');
        title.className = 'toolbox-title';
        title.innerHTML = `<span>${data.icon}</span> ${getCategoryName(category)}`;
        section.appendChild(title);

        data.items.forEach(block => {
            const blockEl = createBlockElement(block, data.color);
            section.appendChild(blockEl);
        });

        toolbox.appendChild(section);
    }
}

// Get Arabic category name
function getCategoryName(category) {
    const names = {
        variables: 'المتغيرات',
        math: 'العمليات الحسابية',
        control: 'التحكم',
        functions: 'الدوال',
        logic: 'المنطق',
        comparison: 'المقارنة'
    };
    return names[category] || category;
}

// Create a draggable block element
function createBlockElement(block, color) {
    const el = document.createElement('div');
    el.className = `block ${color}`;
    el.draggable = true;
    el.dataset.blockId = block.id;
    el.dataset.template = block.template;
    el.dataset.inputs = JSON.stringify(block.inputs);
    el.dataset.multiline = block.multiline || false;

    el.innerHTML = `<span class="block-icon">⬛</span> ${block.name}`;

    el.addEventListener('dragstart', handleDragStart);

    return el;
}

// Initialize workspace
function initWorkspace() {
    const canvas = document.getElementById('canvas');
    const workspace = document.getElementById('workspace');

    workspace.addEventListener('dragover', (e) => {
        e.preventDefault();
        workspace.style.background = 'rgba(37, 99, 235, 0.1)';
    });

    workspace.addEventListener('dragleave', () => {
        workspace.style.background = '';
    });

    workspace.addEventListener('drop', handleDrop);
}

// Handle drag start
function handleDragStart(e) {
    e.dataTransfer.setData('blockId', e.target.dataset.blockId);
    e.dataTransfer.setData('template', e.target.dataset.template);
    e.dataTransfer.setData('inputs', e.target.dataset.inputs);
    e.dataTransfer.setData('multiline', e.target.dataset.multiline);
    e.dataTransfer.setData('color', getBlockColor(e.target));
    e.target.style.opacity = '0.5';

    setTimeout(() => {
        e.target.style.opacity = '1';
    }, 100);
}

// Get block color class
function getBlockColor(el) {
    const colors = ['variable', 'math', 'control', 'function', 'logic', 'comparison'];
    for (const c of colors) {
        if (el.classList.contains(c)) return c;
    }
    return 'variable';
}

// Handle drop
function handleDrop(e) {
    e.preventDefault();
    document.getElementById('workspace').style.background = '';

    const blockId = e.dataTransfer.getData('blockId');
    const template = e.dataTransfer.getData('template');
    const inputs = JSON.parse(e.dataTransfer.getData('inputs'));
    const multiline = e.dataTransfer.getData('multiline') === 'true';
    const color = e.dataTransfer.getData('color');

    // Hide hint
    document.getElementById('workspace-hint').style.display = 'none';

    // Create dropped block
    const droppedBlock = createDroppedBlock(blockId, template, inputs, color, multiline);
    document.getElementById('canvas').appendChild(droppedBlock);

    // Store in state
    droppedBlocks.push({
        id: blockCounter++,
        blockId,
        template,
        inputs,
        values: {}
    });

    updateCode();
}

// Create a dropped block with inputs
function createDroppedBlock(blockId, template, inputs, color, multiline) {
    const id = blockCounter;

    const el = document.createElement('div');
    el.className = `dropped-block ${color}`;
    el.dataset.id = id;

    // Delete button
    const deleteBtn = document.createElement('button');
    deleteBtn.className = 'delete-btn';
    deleteBtn.innerHTML = '×';
    deleteBtn.onclick = () => removeBlock(id);
    el.appendChild(deleteBtn);

    // Build block content with inputs
    let html = template;
    inputs.forEach(input => {
        const inputEl = multiline && input.includes('body')
            ? `<textarea class="block-input" data-input="${input}" placeholder="${input}" rows="2"></textarea>`
            : `<input type="text" class="block-input" data-input="${input}" placeholder="${input}">`;
        html = html.replace(`{${input}}`, inputEl);
    });

    const content = document.createElement('div');
    content.className = 'block-content';
    content.innerHTML = html;
    content.style.fontFamily = 'monospace';
    content.style.direction = 'ltr';
    content.style.textAlign = 'left';
    content.style.whiteSpace = 'pre';
    el.appendChild(content);

    // Add input event listeners
    el.querySelectorAll('.block-input').forEach(input => {
        input.addEventListener('input', () => {
            updateBlockValue(id, input.dataset.input, input.value);
            updateCode();
        });
    });

    return el;
}

// Update block value
function updateBlockValue(blockId, inputName, value) {
    const block = droppedBlocks.find(b => b.id === blockId);
    if (block) {
        block.values[inputName] = value;
    }
}

// Remove block
function removeBlock(id) {
    droppedBlocks = droppedBlocks.filter(b => b.id !== id);
    const el = document.querySelector(`.dropped-block[data-id="${id}"]`);
    if (el) {
        el.remove();
    }

    if (droppedBlocks.length === 0) {
        document.getElementById('workspace-hint').style.display = 'block';
    }

    updateCode();
}

// Generate Bayan code from blocks
function generateCode() {
    if (droppedBlocks.length === 0) return '';

    let code = 'hybrid {\n';

    droppedBlocks.forEach(block => {
        let line = block.template;
        block.inputs.forEach(input => {
            const value = block.values[input] || input;
            line = line.replace(`{${input}}`, value);
        });

        // Indent each line
        const lines = line.split('\n').map(l => '    ' + l).join('\n');
        code += lines + '\n';
    });

    code += '}';
    return code;
}

// Update code display
function updateCode() {
    const code = generateCode();
    document.getElementById('code-output').textContent = code || '// اسحب الكتل هنا لبناء البرنامج';
}

// Run the code
async function runCode() {
    const code = generateCode();

    if (!code) {
        showOutput('⚠️ لا يوجد كود للتشغيل', 'error');
        return;
    }

    showOutput('⏳ جاري التشغيل...', '');

    try {
        const response = await fetch('/run', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ code })
        });

        const result = await response.json();

        if (result.success) {
            let output = result.output || '';
            if (result.result) {
                output += '\n➤ النتيجة: ' + result.result;
            }
            showOutput(output || '✅ تم التنفيذ بنجاح', 'success');
        } else {
            showOutput('❌ خطأ: ' + result.error, 'error');
        }
    } catch (error) {
        showOutput('❌ خطأ في الاتصال: ' + error.message, 'error');
    }

    // Switch to output tab
    switchTab('output');
}

// Show output
function showOutput(text, type) {
    const output = document.getElementById('run-output');
    output.textContent = text;
    output.className = 'run-output ' + type;
}

// Clear all blocks
function clearBlocks() {
    droppedBlocks = [];
    blockCounter = 0;
    document.getElementById('canvas').innerHTML = '';
    document.getElementById('workspace-hint').style.display = 'block';
    updateCode();
    showOutput('', '');
}

// Initialize tabs
function initTabs() {
    document.querySelectorAll('.tab').forEach(tab => {
        tab.addEventListener('click', () => {
            switchTab(tab.dataset.tab);
        });
    });
}

// Switch tab
function switchTab(tabName) {
    currentTab = tabName;

    document.querySelectorAll('.tab').forEach(tab => {
        tab.classList.toggle('active', tab.dataset.tab === tabName);
    });

    document.getElementById('code-panel').style.display = tabName === 'code' ? 'block' : 'none';
    document.getElementById('output-panel').style.display = tabName === 'output' ? 'block' : 'none';
}

// Copy code to clipboard
function copyCode() {
    const code = generateCode();
    navigator.clipboard.writeText(code).then(() => {
        alert('✅ تم نسخ الكود!');
    });
}
