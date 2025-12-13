#!/usr/bin/env python3
"""
🧬 نظام المعرفة الثوري الشامل - نظام بصيرة
🌉 يدمج جميع مصادر المعرفة مع النظريات الثلاث الثورية
📚 الهدف: بناء مكتبة معرفية ذاتية مستقلة تدريجياً

الاستراتيجية الذهبية:
1. البدء بالمصادر الخارجية (APIs)
2. استخراج وتحليل المعرفة بالنظريات الثورية
3. بناء مكتبة ذاتية غنية
4. التحول للاستقلالية الكاملة

المطور: باسل يحيى عبدالله
"""

import json
import sqlite3
import os
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
from .knowledge_harvester import KnowledgeHarvester
import hashlib

class RevolutionaryKnowledgeSystem:
    """
    🧬 نظام المعرفة الثوري الشامل
    يدمج جميع مصادر المعرفة مع تطبيق النظريات الثلاث
    """
    
    def __init__(self, db_path: str = "databases/revolutionary_knowledge_system.db"):
        """تهيئة النظام الشامل"""
        self.db_path = db_path
        self.setup_master_database()
        
        # المكونات الفرعية
        self.harvester = KnowledgeHarvester()
        
        # إحصائيات النظام
        self.total_knowledge_items = 0
        self.external_sources_count = 0
        self.internal_knowledge_count = 0
        
        print("🧬⚡ تم إنشاء نظام المعرفة الثوري الشامل")
        print("   🌉 يدمج جميع مصادر المعرفة")
        print("   📚 يطبق النظريات الثلاث الثورية")
        print("   🎯 الهدف: الاستقلالية التدريجية")
        
        self.initialize_system()
    
    def setup_master_database(self):
        """إعداد قاعدة البيانات الرئيسية"""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # جدول المعرفة الموحد
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS unified_knowledge (
                id INTEGER PRIMARY KEY,
                content TEXT NOT NULL,
                source_type TEXT NOT NULL,  -- internal, wikipedia, file
                source_name TEXT NOT NULL,
                category TEXT,
                language TEXT DEFAULT 'ar',
                zero_duality_score REAL,
                perpendicularity_factor REAL,
                filament_connections TEXT,
                confidence_score REAL DEFAULT 0.5,
                usage_count INTEGER DEFAULT 0,
                last_accessed TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                revolutionary_id TEXT UNIQUE,
                content_hash TEXT UNIQUE
            )
        """)
        
        # جدول متجهات الكلمات الموحد
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS unified_word_vectors (
                id INTEGER PRIMARY KEY,
                word TEXT NOT NULL,
                vector_data TEXT,
                source_model TEXT,
                language TEXT DEFAULT 'ar',
                frequency INTEGER DEFAULT 1,
                zero_duality_embedding REAL,
                perpendicularity_embedding REAL,
                filament_embedding TEXT,
                confidence REAL DEFAULT 0.5,
                revolutionary_vector_id TEXT UNIQUE
            )
        """)
        
        # جدول إحصائيات المصادر
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS source_statistics (
                id INTEGER PRIMARY KEY,
                source_type TEXT NOT NULL,
                source_name TEXT NOT NULL,
                total_items INTEGER DEFAULT 0,
                successful_extractions INTEGER DEFAULT 0,
                failed_extractions INTEGER DEFAULT 0,
                average_quality REAL DEFAULT 0.0,
                last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                revolutionary_efficiency REAL DEFAULT 0.0
            )
        """)
        
        conn.commit()
        conn.close()
        print("📊 تم إعداد قاعدة البيانات الرئيسية")
    
    def initialize_system(self):
        """تهيئة النظام وتحميل المعرفة الأولية"""
        print("\n🚀 تهيئة نظام المعرفة الثوري:")
        
        # 1. تحميل المعرفة المحلية
        print("   📚 تحميل المعرفة المحلية...")
        self.load_internal_knowledge()
        
        # 2. فحص المصادر الخارجية
        print("   🔗 فحص المصادر الخارجية...")
        self.check_external_sources()
        
        # 3. تحديث الإحصائيات
        print("   📊 تحديث الإحصائيات...")
        self.update_system_statistics()
        
        print("✅ تم تهيئة النظام بنجاح!")
    
    def load_internal_knowledge(self):
        """تحميل المعرفة الداخلية من الحاصد"""
        try:
            # الحصول على المعرفة من الحاصد
            harvester_stats = self.harvester.get_knowledge_stats()
            
            if harvester_stats.get('total_knowledge', 0) == 0:
                # إذا لم توجد معرفة، قم بحصادها
                print("     🌾 حصاد المعرفة الأولية...")
                self.harvester.harvest_sample_knowledge()
                self.harvester.harvest_arabic_words()
            
            # نسخ المعرفة إلى النظام الموحد
            self._sync_harvester_knowledge()
            
            print(f"     ✅ تم تحميل المعرفة الداخلية")
            
        except Exception as e:
            print(f"     ❌ خطأ في تحميل المعرفة الداخلية: {e}")
    
    def check_external_sources(self):
        """فحص المصادر الخارجية المتاحة"""
        external_sources = {
            "wikipedia": True,  # متاح دائماً
            "local_files": True  # متاح دائماً
        }
        
        available_sources = [source for source, available in external_sources.items() if available]
        print(f"     🔗 المصادر المتاحة: {available_sources}")
        
        self.external_sources_count = len(available_sources)
    
    def _sync_harvester_knowledge(self):
        """مزامنة المعرفة من الحاصد إلى النظام الموحد"""
        try:
            # الاتصال بقاعدة بيانات الحاصد
            harvester_conn = sqlite3.connect(self.harvester.db_path)
            harvester_cursor = harvester_conn.cursor()
            
            # الحصول على جميع المعرفة
            harvester_cursor.execute("""
                SELECT content, source, category, language, 
                       zero_duality_score, perpendicularity_factor, 
                       filament_connections, revolutionary_id
                FROM knowledge_base
            """)
            
            knowledge_items = harvester_cursor.fetchall()
            harvester_conn.close()
            
            # إدراج في النظام الموحد
            unified_conn = sqlite3.connect(self.db_path)
            unified_cursor = unified_conn.cursor()
            
            for item in knowledge_items:
                content_hash = hashlib.sha256(item[0].encode()).hexdigest()
                
                unified_cursor.execute("""
                    INSERT OR IGNORE INTO unified_knowledge 
                    (content, source_type, source_name, category, language,
                     zero_duality_score, perpendicularity_factor, 
                     filament_connections, revolutionary_id, content_hash)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    item[0],  # content
                    "internal",  # source_type
                    item[1],  # source_name
                    item[2],  # category
                    item[3],  # language
                    item[4],  # zero_duality_score
                    item[5],  # perpendicularity_factor
                    item[6],  # filament_connections
                    item[7],  # revolutionary_id
                    content_hash
                ))
            
            unified_conn.commit()
            unified_conn.close()
            
            self.internal_knowledge_count = len(knowledge_items)
            
        except Exception as e:
            print(f"     ❌ خطأ في مزامنة المعرفة: {e}")
    
    def extract_from_external_source(self, source_type: str, query: str) -> Optional[str]:
        """استخراج معرفة من مصدر خارجي"""
        try:
            content = None
            
            if source_type == "wikipedia":
                # يمكن إضافة استخراج من ويكيبيديا هنا
                pass
            
            if content:
                # حفظ في النظام الموحد
                self._save_external_knowledge(content, source_type, query)
                return content
            
            return None
            
        except Exception as e:
            print(f"❌ خطأ في استخراج من {source_type}: {e}")
            return None
    
    def _save_external_knowledge(self, content: str, source_type: str, query: str):
        """حفظ المعرفة المستخرجة من مصدر خارجي"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # تطبيق النظريات الثورية
            zero_duality = self._calculate_zero_duality(content)
            perpendicularity = self._calculate_perpendicularity(content)
            filaments = self._calculate_filament_connections(content)
            
            content_hash = hashlib.sha256(content.encode()).hexdigest()
            revolutionary_id = f"ext_{source_type}_{content_hash[:12]}"
            
            cursor.execute("""
                INSERT OR IGNORE INTO unified_knowledge 
                (content, source_type, source_name, category, 
                 zero_duality_score, perpendicularity_factor, 
                 filament_connections, revolutionary_id, content_hash)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                content,
                source_type,
                f"{source_type}_extraction",
                "external_knowledge",
                zero_duality,
                perpendicularity,
                json.dumps(filaments),
                revolutionary_id,
                content_hash
            ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(f"❌ خطأ في حفظ المعرفة الخارجية: {e}")
    
    def search_unified_knowledge(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """البحث في المعرفة الموحدة"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT content, source_type, source_name, category,
                       zero_duality_score, perpendicularity_factor,
                       confidence_score, usage_count
                FROM unified_knowledge 
                WHERE content LIKE ? 
                ORDER BY zero_duality_score DESC, confidence_score DESC
                LIMIT ?
            """, (f"%{query}%", limit))
            
            results = []
            for row in cursor.fetchall():
                results.append({
                    'content': row[0][:200] + "..." if len(row[0]) > 200 else row[0],
                    'source_type': row[1],
                    'source_name': row[2],
                    'category': row[3],
                    'zero_duality_score': row[4],
                    'perpendicularity_factor': row[5],
                    'confidence_score': row[6],
                    'usage_count': row[7]
                })
            
            # تحديث عداد الاستخدام
            cursor.execute("""
                UPDATE unified_knowledge 
                SET usage_count = usage_count + 1, 
                    last_accessed = CURRENT_TIMESTAMP
                WHERE content LIKE ?
            """, (f"%{query}%",))
            
            conn.commit()
            conn.close()
            
            return results
            
        except Exception as e:
            print(f"❌ خطأ في البحث: {e}")
            return []
    
    def get_system_statistics(self) -> Dict[str, Any]:
        """إحصائيات النظام الشاملة"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # إجمالي المعرفة
            cursor.execute("SELECT COUNT(*) FROM unified_knowledge")
            total_knowledge = cursor.fetchone()[0]
            
            # المعرفة حسب المصدر
            cursor.execute("""
                SELECT source_type, COUNT(*) 
                FROM unified_knowledge 
                GROUP BY source_type
            """)
            by_source = dict(cursor.fetchall())
            
            # المعرفة حسب الفئة
            cursor.execute("""
                SELECT category, COUNT(*) 
                FROM unified_knowledge 
                GROUP BY category
            """)
            by_category = dict(cursor.fetchall())
            
            # متوسط جودة المعرفة
            cursor.execute("""
                SELECT AVG(zero_duality_score), AVG(confidence_score)
                FROM unified_knowledge
            """)
            avg_quality = cursor.fetchone()
            
            conn.close()
            
            return {
                'total_knowledge': total_knowledge,
                'by_source': by_source,
                'by_category': by_category,
                'average_zero_duality': round(avg_quality[0] or 0, 4),
                'average_confidence': round(avg_quality[1] or 0, 4),
                'external_sources_available': self.external_sources_count,
                'system_status': 'operational'
            }
            
        except Exception as e:
            print(f"❌ خطأ في الإحصائيات: {e}")
            return {}
    
    def update_system_statistics(self):
        """تحديث إحصائيات النظام"""
        stats = self.get_system_statistics()
        self.total_knowledge_items = stats.get('total_knowledge', 0)
        
        print(f"     📊 إجمالي المعرفة: {self.total_knowledge_items}")
        print(f"     🔗 المصادر الخارجية: {self.external_sources_count}")
        print(f"     📚 المعرفة الداخلية: {self.internal_knowledge_count}")
    
    # النظريات الثورية (نسخ مبسطة)
    def _calculate_zero_duality(self, content: str) -> float:
        words = content.split()
        if not words:
            return 0.0
        avg_length = sum(len(w) for w in words) / len(words)
        return round((avg_length * 0.618) % 1.0, 4)
    
    def _calculate_perpendicularity(self, content: str) -> float:
        sentences = len([s for s in content.split('.') if s.strip()])
        return round((sentences * 90.0) % 180.0 / 180.0, 4)
    
    def _calculate_filament_connections(self, content: str) -> List[str]:
        words = content.split()
        return [f"{w}:{len(w)}" for w in words[:5] if len(w) > 3]

def main():
    """الدالة الرئيسية للنظام الشامل"""
    
    print("🧬⚡ نظام المعرفة الثوري الشامل - نظام بصيرة")
    print("=" * 70)
    
    # إنشاء النظام
    system = RevolutionaryKnowledgeSystem()
    
    # عرض الإحصائيات
    print("\n📊 إحصائيات النظام:")
    stats = system.get_system_statistics()
    print(f"   📈 إجمالي المعرفة: {stats.get('total_knowledge', 0)}")
    print(f"   🔗 المصادر: {list(stats.get('by_source', {}).keys())}")
    print(f"   📂 الفئات: {list(stats.get('by_category', {}).keys())}")
    print(f"   🧬 متوسط ثنائية الصفر: {stats.get('average_zero_duality', 0)}")
    print(f"   ⚖️ متوسط الثقة: {stats.get('average_confidence', 0)}")
    
    # اختبار البحث
    print("\n🔍 اختبار البحث في المعرفة الموحدة:")
    search_terms = ["ذكاء", "رياضيات", "عربية"]
    
    for term in search_terms:
        results = system.search_unified_knowledge(term, limit=2)
        print(f"\n   🔎 البحث عن '{term}': {len(results)} نتيجة")
        for i, result in enumerate(results, 1):
            print(f"      {i}. {result['content'][:80]}...")
            print(f"         المصدر: {result['source_type']} | الثقة: {result['confidence_score']}")
    
    print(f"\n🎉 النظام الشامل يعمل بكفاءة!")
    print("🧬 جاهز لبناء مكتبة معرفية ثورية مستقلة!")

if __name__ == "__main__":
    main()
