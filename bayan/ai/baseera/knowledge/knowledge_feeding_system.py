#!/usr/bin/env python3
"""
knowledge_feeding_system.py - نظام تغذية المعرفة لنموذج بصيرة الثوري

🧠 نظام شامل لتغذية النموذج بالمعرفة والبيانات
📁 يدعم أنواع ملفات متعددة ومصادر معرفة مختلفة
🔄 تحويل تلقائي للبيانات إلى تنسيق النموذج

🧬 جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله
"""

import os
import json
import csv
import xml.etree.ElementTree as ET
import sqlite3
import pandas as pd
from pathlib import Path
from typing import Dict, List, Any, Optional, Union
from datetime import datetime
from enum import Enum
import uuid
import re

# استيراد مكونات النظام
try:
    from complete_specialized_databases import CompleteSpecializedDatabases, ThinkingLayerType, LearningSource
    DATABASES_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ تحذير: قواعد البيانات غير متوفرة: {e}")
    DATABASES_AVAILABLE = False

try:
    from specialized_knowledge_systems import SpecializedKnowledgeSystem, KnowledgeItem, KnowledgeType, KnowledgeLevel
    KNOWLEDGE_SYSTEM_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ تحذير: نظام المعرفة غير متوفر: {e}")
    KNOWLEDGE_SYSTEM_AVAILABLE = False
    # تعريف بديل للفئات
    class KnowledgeType:
        MATHEMATICAL = "mathematical"
        SCIENTIFIC = "scientific"
        TECHNICAL = "technical"
        PHILOSOPHICAL = "philosophical"
        GENERAL = "general"

    class KnowledgeLevel:
        BASIC = "basic"
        INTERMEDIATE = "intermediate"
        ADVANCED = "advanced"

class FileType(Enum):
    """أنواع الملفات المدعومة"""
    JSON = "json"
    CSV = "csv"
    TXT = "txt"
    XML = "xml"
    XLSX = "xlsx"
    SQL = "sql"
    MD = "md"
    PDF = "pdf"
    DOCX = "docx"

class KnowledgeCategory(Enum):
    """فئات المعرفة"""
    MATHEMATICAL = "mathematical"
    SCIENTIFIC = "scientific"
    LINGUISTIC = "linguistic"
    HISTORICAL = "historical"
    TECHNICAL = "technical"
    PHILOSOPHICAL = "philosophical"
    CULTURAL = "cultural"
    GENERAL = "general"

class DataSource(Enum):
    """مصادر البيانات"""
    FILE_IMPORT = "file_import"
    DATABASE_IMPORT = "database_import"
    WEB_SCRAPING = "web_scraping"
    MANUAL_INPUT = "manual_input"
    API_IMPORT = "api_import"
    BULK_UPLOAD = "bulk_upload"

class KnowledgeFeedingSystem:
    """
    نظام تغذية المعرفة الشامل
    
    🧠 يحول البيانات من مصادر مختلفة إلى معرفة منظمة
    📊 يدعم أنواع ملفات متعددة
    🔄 يوزع المعرفة على الطبقات المناسبة
    """
    
    def __init__(self, knowledge_base_path: str = "knowledge_base"):
        self.knowledge_base_path = knowledge_base_path
        self.creation_time = datetime.now()
        
        # إنشاء مجلد قاعدة المعرفة
        os.makedirs(knowledge_base_path, exist_ok=True)
        
        # إحصائيات النظام
        self.total_files_processed = 0
        self.total_knowledge_items = 0
        self.processing_errors = 0
        self.supported_formats = list(FileType)
        
        # تهيئة المكونات
        self._initialize_components()
        
        # سجل المعالجة
        self.processing_log = []
        
        print(f"🧠📚 تم إنشاء نظام تغذية المعرفة")
        print(f"   📁 مسار قاعدة المعرفة: {knowledge_base_path}")
        print(f"   📋 الصيغ المدعومة: {len(self.supported_formats)}")
    
    def _initialize_components(self):
        """تهيئة مكونات النظام"""
        if DATABASES_AVAILABLE:
            try:
                self.specialized_databases = CompleteSpecializedDatabases()
                print("✅ تم تحميل قواعد البيانات المتخصصة")
            except:
                self.specialized_databases = None
                print("❌ فشل تحميل قواعد البيانات المتخصصة")
        else:
            self.specialized_databases = None
            print("❌ قواعد البيانات المتخصصة غير متوفرة")

        if KNOWLEDGE_SYSTEM_AVAILABLE:
            try:
                self.knowledge_system = SpecializedKnowledgeSystem()
                print("✅ تم تحميل نظام المعرفة المتخصص")
            except:
                self.knowledge_system = None
                print("❌ فشل تحميل نظام المعرفة المتخصص")
        else:
            self.knowledge_system = None
            print("❌ نظام المعرفة المتخصص غير متوفر")
    
    def detect_file_type(self, file_path: str) -> Optional[FileType]:
        """كشف نوع الملف"""
        extension = Path(file_path).suffix.lower()
        
        type_mapping = {
            '.json': FileType.JSON,
            '.csv': FileType.CSV,
            '.txt': FileType.TXT,
            '.xml': FileType.XML,
            '.xlsx': FileType.XLSX,
            '.xls': FileType.XLSX,
            '.sql': FileType.SQL,
            '.md': FileType.MD,
            '.pdf': FileType.PDF,
            '.docx': FileType.DOCX
        }
        
        return type_mapping.get(extension)
    
    def process_file(self, file_path: str, category: KnowledgeCategory = KnowledgeCategory.GENERAL,
                    custom_metadata: Dict[str, Any] = None) -> Dict[str, Any]:
        """معالجة ملف واستخراج المعرفة منه"""
        
        if not os.path.exists(file_path):
            return {"success": False, "error": "الملف غير موجود"}
        
        file_type = self.detect_file_type(file_path)
        if not file_type:
            return {"success": False, "error": "نوع ملف غير مدعوم"}
        
        print(f"\n📁 معالجة الملف: {Path(file_path).name}")
        print(f"   📋 النوع: {file_type.value}")
        print(f"   🏷️ الفئة: {category.value}")
        
        try:
            # استخراج البيانات حسب نوع الملف
            if file_type == FileType.JSON:
                data = self._process_json_file(file_path)
            elif file_type == FileType.CSV:
                data = self._process_csv_file(file_path)
            elif file_type == FileType.TXT:
                data = self._process_txt_file(file_path)
            elif file_type == FileType.XML:
                data = self._process_xml_file(file_path)
            elif file_type == FileType.XLSX:
                data = self._process_excel_file(file_path)
            elif file_type == FileType.MD:
                data = self._process_markdown_file(file_path)
            else:
                return {"success": False, "error": f"معالج {file_type.value} غير مطبق بعد"}
            
            # تحويل البيانات إلى معرفة منظمة
            knowledge_items = self._convert_to_knowledge(data, category, file_path, custom_metadata)
            
            # حفظ المعرفة في النظام
            saved_items = self._save_knowledge_items(knowledge_items)
            
            # تسجيل النتائج
            result = {
                "success": True,
                "file_path": file_path,
                "file_type": file_type.value,
                "category": category.value,
                "items_extracted": len(knowledge_items),
                "items_saved": len(saved_items),
                "processing_time": datetime.now()
            }
            
            self.processing_log.append(result)
            self.total_files_processed += 1
            self.total_knowledge_items += len(saved_items)
            
            print(f"   ✅ تم استخراج {len(knowledge_items)} عنصر معرفي")
            print(f"   💾 تم حفظ {len(saved_items)} عنصر")
            
            return result
            
        except Exception as e:
            self.processing_errors += 1
            error_result = {
                "success": False,
                "file_path": file_path,
                "error": str(e),
                "processing_time": datetime.now()
            }
            self.processing_log.append(error_result)
            print(f"   ❌ خطأ في المعالجة: {e}")
            return error_result
    
    def _process_json_file(self, file_path: str) -> Dict[str, Any]:
        """معالجة ملف JSON"""
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _process_csv_file(self, file_path: str) -> List[Dict[str, Any]]:
        """معالجة ملف CSV"""
        data = []
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(dict(row))
        return data
    
    def _process_txt_file(self, file_path: str) -> Dict[str, Any]:
        """معالجة ملف نصي"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # تحليل النص إلى فقرات
        paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
        
        return {
            "content": content,
            "paragraphs": paragraphs,
            "word_count": len(content.split()),
            "line_count": len(content.split('\n'))
        }
    
    def _process_xml_file(self, file_path: str) -> Dict[str, Any]:
        """معالجة ملف XML"""
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        def xml_to_dict(element):
            result = {}
            if element.text and element.text.strip():
                result['text'] = element.text.strip()
            
            for child in element:
                child_data = xml_to_dict(child)
                if child.tag in result:
                    if not isinstance(result[child.tag], list):
                        result[child.tag] = [result[child.tag]]
                    result[child.tag].append(child_data)
                else:
                    result[child.tag] = child_data
            
            result.update(element.attrib)
            return result
        
        return {root.tag: xml_to_dict(root)}
    
    def _process_excel_file(self, file_path: str) -> Dict[str, Any]:
        """معالجة ملف Excel"""
        try:
            # قراءة جميع الأوراق
            excel_data = pd.read_excel(file_path, sheet_name=None)
            
            result = {}
            for sheet_name, df in excel_data.items():
                result[sheet_name] = df.to_dict('records')
            
            return result
        except Exception as e:
            print(f"⚠️ تحذير: فشل في قراءة Excel، محاولة CSV: {e}")
            # محاولة قراءة كـ CSV
            df = pd.read_csv(file_path)
            return {"data": df.to_dict('records')}
    
    def _process_markdown_file(self, file_path: str) -> Dict[str, Any]:
        """معالجة ملف Markdown"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # استخراج العناوين
        headers = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
        
        # استخراج الروابط
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
        
        # تقسيم إلى أقسام
        sections = re.split(r'^#+\s+', content, flags=re.MULTILINE)[1:]
        
        return {
            "content": content,
            "headers": headers,
            "links": links,
            "sections": sections,
            "word_count": len(content.split())
        }
    
    def _convert_to_knowledge(self, data: Any, category: KnowledgeCategory,
                            source_file: str, metadata: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """تحويل البيانات إلى عناصر معرفية"""
        knowledge_items = []
        
        if isinstance(data, dict):
            knowledge_items.extend(self._process_dict_data(data, category, source_file, metadata))
        elif isinstance(data, list):
            knowledge_items.extend(self._process_list_data(data, category, source_file, metadata))
        else:
            # بيانات نصية بسيطة
            item = self._create_knowledge_item(
                title=f"محتوى من {Path(source_file).name}",
                content=str(data),
                category=category,
                source_file=source_file,
                metadata=metadata
            )
            knowledge_items.append(item)
        
        return knowledge_items
    
    def _process_dict_data(self, data: Dict[str, Any], category: KnowledgeCategory,
                          source_file: str, metadata: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """معالجة البيانات من نوع Dictionary"""
        items = []
        
        # إذا كان القاموس يحتوي على عناصر معرفية منظمة
        if 'title' in data and 'content' in data:
            item = self._create_knowledge_item(
                title=data['title'],
                content=data['content'],
                category=category,
                source_file=source_file,
                metadata={**(metadata or {}), **data}
            )
            items.append(item)
        else:
            # تحويل كل مفتاح-قيمة إلى عنصر معرفي
            for key, value in data.items():
                if isinstance(value, (str, int, float)):
                    item = self._create_knowledge_item(
                        title=key,
                        content=str(value),
                        category=category,
                        source_file=source_file,
                        metadata=metadata
                    )
                    items.append(item)
                elif isinstance(value, dict):
                    item = self._create_knowledge_item(
                        title=key,
                        content=json.dumps(value, ensure_ascii=False, indent=2),
                        category=category,
                        source_file=source_file,
                        metadata=metadata
                    )
                    items.append(item)
        
        return items
    
    def _process_list_data(self, data: List[Any], category: KnowledgeCategory,
                          source_file: str, metadata: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """معالجة البيانات من نوع List"""
        items = []
        
        for i, item_data in enumerate(data):
            if isinstance(item_data, dict):
                items.extend(self._process_dict_data(item_data, category, source_file, metadata))
            else:
                item = self._create_knowledge_item(
                    title=f"عنصر {i+1} من {Path(source_file).name}",
                    content=str(item_data),
                    category=category,
                    source_file=source_file,
                    metadata=metadata
                )
                items.append(item)
        
        return items
    
    def _create_knowledge_item(self, title: str, content: str, category: KnowledgeCategory,
                              source_file: str, metadata: Dict[str, Any] = None) -> Dict[str, Any]:
        """إنشاء عنصر معرفي"""
        
        # تحديد نوع المعرفة ومستواها
        knowledge_type = self._determine_knowledge_type(category, content)
        knowledge_level = self._determine_knowledge_level(content)
        
        # استخراج العلامات
        tags = self._extract_tags(title, content, category)
        
        # إنشاء العنصر المعرفي
        if KNOWLEDGE_SYSTEM_AVAILABLE:
            try:
                item = KnowledgeItem(
                    title=title[:200],  # تحديد طول العنوان
                    content=content,
                    knowledge_type=knowledge_type,
                    knowledge_level=knowledge_level,
                    tags=tags,
                    related_equations=[]
                )
                return item
            except:
                pass

        # إنشاء عنصر بسيط في حالة عدم توفر النظام المتقدم
        return {
            "title": title[:200],
            "content": content,
            "category": category.value if hasattr(category, 'value') else str(category),
            "source_file": source_file,
            "metadata": metadata or {},
            "creation_time": datetime.now().isoformat(),
            "knowledge_type": knowledge_type,
            "knowledge_level": knowledge_level,
            "tags": tags
        }
    
    def _determine_knowledge_type(self, category: KnowledgeCategory, content: str) -> KnowledgeType:
        """تحديد نوع المعرفة"""
        try:
            if category == KnowledgeCategory.MATHEMATICAL:
                return KnowledgeType.MATHEMATICAL
            elif category == KnowledgeCategory.SCIENTIFIC:
                return KnowledgeType.SCIENTIFIC
            elif category == KnowledgeCategory.TECHNICAL:
                return KnowledgeType.TECHNICAL
            elif category == KnowledgeCategory.PHILOSOPHICAL:
                return KnowledgeType.PHILOSOPHICAL
            else:
                return KnowledgeType.GENERAL
        except:
            return "general"
    
    def _determine_knowledge_level(self, content: str) -> KnowledgeLevel:
        """تحديد مستوى المعرفة"""
        try:
            content_length = len(content)
            if content_length > 1000:
                return KnowledgeLevel.ADVANCED
            elif content_length > 300:
                return KnowledgeLevel.INTERMEDIATE
            else:
                return KnowledgeLevel.BASIC
        except:
            return "basic"
    
    def _extract_tags(self, title: str, content: str, category: KnowledgeCategory) -> List[str]:
        """استخراج العلامات"""
        tags = [category.value]
        
        # كلمات مفتاحية شائعة
        keywords = {
            'رياضيات': ['معادلة', 'حساب', 'رقم', 'دالة'],
            'علوم': ['تجربة', 'نظرية', 'قانون', 'ظاهرة'],
            'تقنية': ['برمجة', 'نظام', 'تطبيق', 'خوارزمية'],
            'فلسفة': ['فكر', 'مفهوم', 'نظرية', 'تأمل']
        }
        
        text = (title + " " + content).lower()
        for tag, words in keywords.items():
            if any(word in text for word in words):
                tags.append(tag)
        
        return list(set(tags))
    
    def _save_knowledge_items(self, knowledge_items: List[Any]) -> List[str]:
        """حفظ العناصر المعرفية في النظام"""
        saved_ids = []
        
        for item in knowledge_items:
            try:
                if self.knowledge_system and hasattr(item, 'title'):
                    # حفظ في نظام المعرفة المتخصص
                    item_id = self.knowledge_system.add_knowledge_item(item)
                    saved_ids.append(item_id)
                
                # حفظ في قواعد البيانات المتخصصة
                if self.specialized_databases:
                    self._distribute_to_specialized_databases(item)
                
            except Exception as e:
                print(f"   ⚠️ خطأ في حفظ العنصر: {e}")
        
        return saved_ids
    
    def _distribute_to_specialized_databases(self, item: Any):
        """توزيع المعرفة على قواعد البيانات المتخصصة"""
        try:
            # تحديد الطبقة المناسبة
            if hasattr(item, 'knowledge_type'):
                if 'mathematical' in str(item.knowledge_type).lower():
                    self.specialized_databases.store_learning_for_layer(
                        ThinkingLayerType.MATHEMATICAL, 
                        {"knowledge_item": item.__dict__ if hasattr(item, '__dict__') else item},
                        LearningSource.USER_INTERACTION
                    )
                elif 'linguistic' in str(item.knowledge_type).lower():
                    self.specialized_databases.store_learning_for_layer(
                        ThinkingLayerType.LINGUISTIC,
                        {"knowledge_item": item.__dict__ if hasattr(item, '__dict__') else item},
                        LearningSource.USER_INTERACTION
                    )
        except Exception as e:
            print(f"   ⚠️ خطأ في التوزيع: {e}")
    
    def process_directory(self, directory_path: str, category: KnowledgeCategory = KnowledgeCategory.GENERAL) -> Dict[str, Any]:
        """معالجة جميع الملفات في مجلد"""
        if not os.path.exists(directory_path):
            return {"success": False, "error": "المجلد غير موجود"}
        
        results = []
        total_files = 0
        successful_files = 0
        
        print(f"\n📁 معالجة المجلد: {directory_path}")
        
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                if self.detect_file_type(file_path):
                    total_files += 1
                    result = self.process_file(file_path, category)
                    results.append(result)
                    if result["success"]:
                        successful_files += 1
        
        summary = {
            "success": True,
            "directory": directory_path,
            "total_files": total_files,
            "successful_files": successful_files,
            "failed_files": total_files - successful_files,
            "results": results,
            "processing_time": datetime.now()
        }
        
        print(f"   📊 ملخص المعالجة:")
        print(f"   📁 إجمالي الملفات: {total_files}")
        print(f"   ✅ نجح: {successful_files}")
        print(f"   ❌ فشل: {total_files - successful_files}")
        
        return summary
    
    def get_statistics(self) -> Dict[str, Any]:
        """إحصائيات النظام"""
        return {
            "total_files_processed": self.total_files_processed,
            "total_knowledge_items": self.total_knowledge_items,
            "processing_errors": self.processing_errors,
            "supported_formats": [f.value for f in self.supported_formats],
            "success_rate": (self.total_files_processed - self.processing_errors) / max(self.total_files_processed, 1) * 100,
            "creation_time": self.creation_time.isoformat(),
            "last_processing": self.processing_log[-1] if self.processing_log else None
        }


# مثال على الاستخدام
if __name__ == "__main__":
    print("🧠📚 اختبار نظام تغذية المعرفة")
    print("=" * 60)
    
    # إنشاء النظام
    feeding_system = KnowledgeFeedingSystem()
    
    # عرض الإحصائيات
    stats = feeding_system.get_statistics()
    print(f"\n📊 إحصائيات النظام:")
    for key, value in stats.items():
        print(f"   {key}: {value}")
    
    print(f"\n🎯 النظام جاهز لتغذية المعرفة!")
    print(f"   📋 الصيغ المدعومة: {', '.join([f.value for f in FileType])}")
    print(f"   🏷️ الفئات المتاحة: {', '.join([c.value for c in KnowledgeCategory])}")
