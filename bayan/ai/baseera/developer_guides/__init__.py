"""
📚 أدلة المطورين - نظام بصيرة الثوري
Developer Guides - Basera Revolutionary System

هذا المجلد يحتوي على أدلة تقنية شاملة لفهم وتطوير نظام بصيرة الثوري.
This folder contains comprehensive technical guides for understanding and developing the Basera Revolutionary System.

المطور: باسل يحيى عبدالله
Developer: Basel Yahya Abdullah

جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله
All ideas and theories are the creation of Basel Yahya Abdullah
"""

# معلومات المجلد
__version__ = "1.0.0"
__author__ = "Basel Yahya Abdullah"
__description__ = "Developer guides for Basera Revolutionary System"

# الأدلة المتاحة
AVAILABLE_GUIDES = {
    "basera_system_overview": {
        "file": "basera_system_overview.md",
        "title": "دليل نظام بصيرة العام",
        "description": "نظرة عامة شاملة للنظام الكامل - ابدأ من هنا!",
        "status": "complete",
        "level": "beginner",
        "priority": "high"
    },
    "expert_explorer_system": {
        "file": "expert_explorer_system_guide.md",
        "title": "دليل نظام الخبير/المستكشف",
        "description": "الدليل الشامل لفهم دماغ النظام",
        "status": "complete",
        "level": "advanced"
    },
    "general_shape_equation": {
        "file": "general_shape_equation_guide.md",
        "title": "دليل معادلة الشكل العام",
        "description": "الدليل الشامل لقلب النظام الرياضي",
        "status": "complete",
        "level": "advanced"
    },
    "adaptive_equations": {
        "file": "adaptive_equations_guide.md",
        "title": "دليل المعادلات المتكيفة",
        "description": "الدليل الشامل للنظام التطوري في بصيرة",
        "status": "complete",
        "level": "advanced"
    },
    "mother_equation": {
        "file": "mother_equation_guide.md",
        "title": "دليل المعادلة الأم",
        "description": "شرح المعادلة الأساسية التي يقوم عليها النظام",
        "status": "planned",
        "level": "advanced"
    },
    "artistic_unit": {
        "file": "artistic_unit_guide.md",
        "title": "دليل الوحدة الفنية",
        "description": "شرح نظام تحويل المعادلات إلى صور والعكس",
        "status": "planned",
        "level": "intermediate"
    },
    "thinking_core": {
        "file": "thinking_core_guide.md",
        "title": "دليل النواة التفكيرية",
        "description": "شرح النظام متعدد الطبقات للتفكير",
        "status": "planned",
        "level": "advanced"
    }
}

def get_guide_info(guide_name: str) -> dict:
    """
    الحصول على معلومات دليل معين
    Get information about a specific guide
    """
    return AVAILABLE_GUIDES.get(guide_name, {})

def list_available_guides() -> list:
    """
    قائمة بجميع الأدلة المتاحة
    List of all available guides
    """
    return list(AVAILABLE_GUIDES.keys())

def get_completed_guides() -> list:
    """
    قائمة بالأدلة المكتملة
    List of completed guides
    """
    return [name for name, info in AVAILABLE_GUIDES.items() if info.get("status") == "complete"]

def get_planned_guides() -> list:
    """
    قائمة بالأدلة المخططة
    List of planned guides
    """
    return [name for name, info in AVAILABLE_GUIDES.items() if info.get("status") == "planned"]

# رسالة ترحيب
WELCOME_MESSAGE = """
🌟 مرحباً بك في أدلة المطورين لنظام بصيرة الثوري!

📚 الأدلة المتاحة:
"""

for name, info in AVAILABLE_GUIDES.items():
    status_emoji = "✅" if info["status"] == "complete" else "📋"
    WELCOME_MESSAGE += f"   {status_emoji} {info['title']}\n"

WELCOME_MESSAGE += """
🚀 ابدأ بدليل نظام بصيرة العام للحصول على نظرة شاملة!

📝 المطور: باسل يحيى عبدالله
🧬 جميع الأفكار والنظريات من إبداعه الشخصي
"""

if __name__ == "__main__":
    print(WELCOME_MESSAGE)
