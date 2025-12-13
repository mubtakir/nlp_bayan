#!/usr/bin/env python3
"""
knowledge_feeding_interface.py - واجهة تغذية المعرفة التفاعلية

🖥️ واجهة سهلة الاستخدام لتغذية النموذج بالمعرفة
📁 رفع ومعالجة الملفات بسهولة
🎯 توجيه المعرفة للطبقات المناسبة

🧬 جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله
"""

import os
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Any
import json

try:
    import gradio as gr
    GRADIO_AVAILABLE = True
except ImportError:
    GRADIO_AVAILABLE = False
    print("⚠️ Gradio غير متوفر - سيتم استخدام واجهة CLI فقط")

from .knowledge_feeding_system import KnowledgeFeedingSystem, KnowledgeCategory, FileType

class KnowledgeFeedingInterface:
    """
    واجهة تغذية المعرفة التفاعلية
    
    🖥️ واجهة شاملة لتغذية النموذج بالمعرفة
    📊 عرض الإحصائيات والنتائج
    🔄 معالجة متعددة الملفات
    """
    
    def __init__(self):
        self.feeding_system = KnowledgeFeedingSystem()
        self.processing_history = []
        
        print(f"🖥️📚 تم إنشاء واجهة تغذية المعرفة")
        print(f"   🧠 النظام جاهز لاستقبال المعرفة")
    
    def process_single_file(self, file_path: str, category: str = "general", 
                           metadata: str = "{}") -> Dict[str, Any]:
        """معالجة ملف واحد"""
        try:
            # تحويل الفئة
            knowledge_category = KnowledgeCategory(category)
            
            # تحويل البيانات الإضافية
            try:
                custom_metadata = json.loads(metadata) if metadata.strip() else {}
            except:
                custom_metadata = {}
            
            # معالجة الملف
            result = self.feeding_system.process_file(file_path, knowledge_category, custom_metadata)
            
            # حفظ في التاريخ
            self.processing_history.append(result)
            
            return result
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def process_multiple_files(self, file_paths: List[str], category: str = "general") -> Dict[str, Any]:
        """معالجة ملفات متعددة"""
        results = []
        successful = 0
        failed = 0
        
        knowledge_category = KnowledgeCategory(category)
        
        for file_path in file_paths:
            if os.path.exists(file_path):
                result = self.feeding_system.process_file(file_path, knowledge_category)
                results.append(result)
                if result["success"]:
                    successful += 1
                else:
                    failed += 1
            else:
                results.append({"success": False, "error": f"الملف غير موجود: {file_path}"})
                failed += 1
        
        summary = {
            "success": True,
            "total_files": len(file_paths),
            "successful": successful,
            "failed": failed,
            "results": results
        }
        
        self.processing_history.append(summary)
        return summary
    
    def process_directory(self, directory_path: str, category: str = "general") -> Dict[str, Any]:
        """معالجة مجلد كامل"""
        try:
            knowledge_category = KnowledgeCategory(category)
            result = self.feeding_system.process_directory(directory_path, knowledge_category)
            self.processing_history.append(result)
            return result
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_system_statistics(self) -> str:
        """إحصائيات النظام"""
        stats = self.feeding_system.get_statistics()
        
        report = f"""
📊 إحصائيات نظام تغذية المعرفة:

🔢 الأرقام الأساسية:
   📁 الملفات المعالجة: {stats['total_files_processed']}
   📚 العناصر المعرفية: {stats['total_knowledge_items']}
   ❌ الأخطاء: {stats['processing_errors']}
   ✅ معدل النجاح: {stats['success_rate']:.1f}%

📋 الصيغ المدعومة:
   {', '.join(stats['supported_formats'])}

🕐 معلومات النظام:
   📅 تاريخ الإنشاء: {stats['creation_time']}
   🔄 آخر معالجة: {stats['last_processing']['processing_time'] if stats['last_processing'] else 'لا توجد'}
        """
        
        return report.strip()
    
    def run_cli_interface(self):
        """تشغيل واجهة سطر الأوامر"""
        print("\n🖥️ واجهة تغذية المعرفة - سطر الأوامر")
        print("=" * 50)
        print("الأوامر المتاحة:")
        print("  file <path> [category] - معالجة ملف واحد")
        print("  dir <path> [category] - معالجة مجلد")
        print("  stats - عرض الإحصائيات")
        print("  history - عرض تاريخ المعالجة")
        print("  help - عرض المساعدة")
        print("  exit - الخروج")
        print("-" * 50)
        
        while True:
            try:
                command = input("\n📚> ").strip()
                
                if not command:
                    continue
                
                parts = command.split()
                cmd = parts[0].lower()
                
                if cmd == "exit":
                    print("👋 شكراً لاستخدام نظام تغذية المعرفة!")
                    break
                
                elif cmd == "help":
                    self._show_help()
                
                elif cmd == "stats":
                    print(self.get_system_statistics())
                
                elif cmd == "history":
                    self._show_history()
                
                elif cmd == "file":
                    if len(parts) < 2:
                        print("❌ يرجى تحديد مسار الملف")
                        continue
                    
                    file_path = parts[1]
                    category = parts[2] if len(parts) > 2 else "general"
                    
                    result = self.process_single_file(file_path, category)
                    self._display_result(result)
                
                elif cmd == "dir":
                    if len(parts) < 2:
                        print("❌ يرجى تحديد مسار المجلد")
                        continue
                    
                    dir_path = parts[1]
                    category = parts[2] if len(parts) > 2 else "general"
                    
                    result = self.process_directory(dir_path, category)
                    self._display_result(result)
                
                else:
                    print(f"❌ أمر غير معروف: {cmd}")
                    print("استخدم 'help' لعرض الأوامر المتاحة")
            
            except KeyboardInterrupt:
                print("\n👋 تم إيقاف النظام")
                break
            except Exception as e:
                print(f"❌ خطأ: {e}")
    
    def _show_help(self):
        """عرض المساعدة"""
        help_text = """
🆘 مساعدة نظام تغذية المعرفة:

📋 الأوامر المتاحة:
  file <path> [category]     - معالجة ملف واحد
  dir <path> [category]      - معالجة جميع ملفات المجلد
  stats                      - عرض إحصائيات النظام
  history                    - عرض تاريخ المعالجة
  help                       - عرض هذه المساعدة
  exit                       - الخروج من النظام

🏷️ الفئات المتاحة:
  mathematical    - معرفة رياضية
  scientific      - معرفة علمية
  linguistic      - معرفة لغوية
  historical      - معرفة تاريخية
  technical       - معرفة تقنية
  philosophical   - معرفة فلسفية
  cultural        - معرفة ثقافية
  general         - معرفة عامة (افتراضي)

📁 الصيغ المدعومة:
  JSON, CSV, TXT, XML, XLSX, MD, SQL

💡 أمثلة:
  file data.json mathematical
  dir /path/to/knowledge scientific
  stats
        """
        print(help_text.strip())
    
    def _show_history(self):
        """عرض تاريخ المعالجة"""
        if not self.processing_history:
            print("📝 لا يوجد تاريخ معالجة بعد")
            return
        
        print(f"\n📝 تاريخ المعالجة ({len(self.processing_history)} عملية):")
        print("-" * 50)
        
        for i, entry in enumerate(self.processing_history[-10:], 1):  # آخر 10 عمليات
            status = "✅" if entry.get("success", False) else "❌"
            if "file_path" in entry:
                print(f"{i}. {status} ملف: {Path(entry['file_path']).name}")
            elif "directory" in entry:
                print(f"{i}. {status} مجلد: {Path(entry['directory']).name}")
            else:
                print(f"{i}. {status} عملية متعددة")
    
    def _display_result(self, result: Dict[str, Any]):
        """عرض نتيجة المعالجة"""
        if result["success"]:
            print("✅ تمت المعالجة بنجاح!")
            if "items_extracted" in result:
                print(f"   📚 العناصر المستخرجة: {result['items_extracted']}")
            if "items_saved" in result:
                print(f"   💾 العناصر المحفوظة: {result['items_saved']}")
            if "successful_files" in result:
                print(f"   📁 الملفات الناجحة: {result['successful_files']}/{result['total_files']}")
        else:
            print(f"❌ فشلت المعالجة: {result.get('error', 'خطأ غير معروف')}")
    
    def run_gradio_interface(self):
        """تشغيل واجهة Gradio"""
        if not GRADIO_AVAILABLE:
            print("❌ Gradio غير متوفر - يرجى تثبيته أولاً")
            return
        
        def process_file_gradio(file, category, metadata):
            if file is None:
                return "❌ يرجى اختيار ملف"
            
            result = self.process_single_file(file.name, category, metadata)
            
            if result["success"]:
                return f"""✅ تمت معالجة الملف بنجاح!

📁 الملف: {Path(file.name).name}
🏷️ الفئة: {category}
📚 العناصر المستخرجة: {result.get('items_extracted', 0)}
💾 العناصر المحفوظة: {result.get('items_saved', 0)}
⏰ وقت المعالجة: {result.get('processing_time', 'غير محدد')}"""
            else:
                return f"❌ فشلت المعالجة: {result.get('error', 'خطأ غير معروف')}"
        
        def get_stats_gradio():
            return self.get_system_statistics()
        
        # إنشاء الواجهة
        with gr.Blocks(title="نظام تغذية المعرفة - بصيرة الثوري") as interface:
            gr.Markdown("# 🧠📚 نظام تغذية المعرفة - بصيرة الثوري")
            gr.Markdown("### 🧬 جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله")
            
            with gr.Tab("رفع الملفات"):
                with gr.Row():
                    with gr.Column():
                        file_input = gr.File(label="اختر الملف")
                        category_input = gr.Dropdown(
                            choices=[c.value for c in KnowledgeCategory],
                            value="general",
                            label="فئة المعرفة"
                        )
                        metadata_input = gr.Textbox(
                            label="بيانات إضافية (JSON)",
                            placeholder='{"author": "المؤلف", "source": "المصدر"}',
                            value="{}"
                        )
                        process_btn = gr.Button("معالجة الملف", variant="primary")
                    
                    with gr.Column():
                        result_output = gr.Textbox(
                            label="نتيجة المعالجة",
                            interactive=False,
                            lines=10
                        )
                
                process_btn.click(
                    process_file_gradio,
                    inputs=[file_input, category_input, metadata_input],
                    outputs=result_output
                )
            
            with gr.Tab("الإحصائيات"):
                stats_btn = gr.Button("تحديث الإحصائيات")
                stats_output = gr.Textbox(
                    label="إحصائيات النظام",
                    interactive=False,
                    lines=15
                )
                
                stats_btn.click(get_stats_gradio, outputs=stats_output)
            
            with gr.Tab("المساعدة"):
                gr.Markdown("""
## 📚 دليل استخدام نظام تغذية المعرفة

### 🎯 الهدف:
تغذية نموذج بصيرة الثوري بالمعرفة والبيانات من مصادر مختلفة

### 📁 الصيغ المدعومة:
- **JSON** - ملفات البيانات المنظمة
- **CSV** - جداول البيانات
- **TXT** - النصوص العادية
- **XML** - البيانات المهيكلة
- **XLSX** - ملفات Excel
- **MD** - ملفات Markdown
- **SQL** - قواعد البيانات

### 🏷️ فئات المعرفة:
- **mathematical** - المعرفة الرياضية
- **scientific** - المعرفة العلمية
- **linguistic** - المعرفة اللغوية
- **technical** - المعرفة التقنية
- **philosophical** - المعرفة الفلسفية
- **cultural** - المعرفة الثقافية
- **general** - المعرفة العامة

### 🔄 كيفية العمل:
1. اختر الملف المراد معالجته
2. حدد فئة المعرفة المناسبة
3. أضف بيانات إضافية إن أردت
4. اضغط "معالجة الملف"
5. راجع النتائج والإحصائيات

### 🧠 التوزيع الذكي:
النظام يوزع المعرفة تلقائياً على الطبقات المناسبة:
- الطبقة الرياضية للمعادلات والحسابات
- الطبقة اللغوية للنصوص والكلمات
- الطبقة المنطقية للقواعد والأنماط
- وباقي الطبقات حسب نوع المحتوى
                """)
        
        print("🌐 تشغيل واجهة Gradio...")
        interface.launch(server_port=7862, share=False)


def main():
    """الدالة الرئيسية"""
    parser = argparse.ArgumentParser(description="واجهة تغذية المعرفة لنظام بصيرة الثوري")
    parser.add_argument("--interface", "-i", choices=["cli", "gradio"], default="cli",
                       help="نوع الواجهة")
    parser.add_argument("--file", "-f", help="معالجة ملف واحد")
    parser.add_argument("--directory", "-d", help="معالجة مجلد")
    parser.add_argument("--category", "-c", choices=[c.value for c in KnowledgeCategory],
                       default="general", help="فئة المعرفة")
    
    args = parser.parse_args()
    
    # إنشاء الواجهة
    interface = KnowledgeFeedingInterface()
    
    # معالجة مباشرة إذا تم تحديد ملف أو مجلد
    if args.file:
        result = interface.process_single_file(args.file, args.category)
        interface._display_result(result)
        return
    
    if args.directory:
        result = interface.process_directory(args.directory, args.category)
        interface._display_result(result)
        return
    
    # تشغيل الواجهة المطلوبة
    if args.interface == "gradio":
        interface.run_gradio_interface()
    else:
        interface.run_cli_interface()


if __name__ == "__main__":
    main()
