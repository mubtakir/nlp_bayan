#!/usr/bin/env python3
"""
🌉 جسر المعرفة الخارجية - نظام بصيرة الثوري
🔗 ربط مؤقت بالمصادر الخارجية مع استخراج وحفظ المعرفة
🧬 تطبيق النظريات الثلاث على المعرفة المستخرجة

الهدف: بناء مكتبة معرفية ذاتية تدريجياً
الاستراتيجية: استخراج → تحليل → حفظ → استقلالية

المطور: باسل يحيى عبدالله
"""

import requests
import json
import sqlite3
import numpy as np
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
import hashlib
import time
from datetime import datetime
import os

@dataclass
class KnowledgeEntry:
    """مدخل معرفي مع تطبيق النظريات الثورية"""
    content: str
    source: str
    category: str
    language: str
    zero_duality_score: float
    perpendicularity_factor: float
    filament_connections: List[str]
    extraction_date: str
    revolutionary_id: str

class ExternalKnowledgeBridge:
    """
    🌉 جسر المعرفة الخارجية
    يربط نظام بصيرة بالمصادر الخارجية مؤقتاً
    """
    
    def __init__(self, db_path: str = "databases/external_knowledge.db"):
        """تهيئة جسر المعرفة"""
        self.db_path = db_path
        self.setup_database()
        
        # إعدادات الاتصال الخارجي
        self.wikipedia_api = "https://ar.wikipedia.org/api/rest_v1"
        
        # النظريات الثورية
        self.zero_duality_factor = 0.618
        self.perpendicularity_angle = 90.0
        self.filament_strength = 0.85
        
        print("🌉⚡ تم إنشاء جسر المعرفة الخارجية")
        print("   🔗 جاهز للربط مع المصادر الخارجية")
        print("   🧬 النظريات الثلاث: نشطة")
        print("   💾 استخراج وحفظ المعرفة: مفعل")
    
    def extract_from_wikipedia(self, topic: str, language: str = "ar") -> Optional[str]:
        """استخراج معرفة من ويكيبيديا"""
        try:
            # البحث عن المقال
            search_url = f"https://{language}.wikipedia.org/api/rest_v1/page/summary/{topic}"
            
            response = requests.get(search_url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                content = data.get('extract', '')
                
                if content:
                    # حفظ المعرفة المستخرجة
                    knowledge_entry = self._create_knowledge_entry(
                        content=content,
                        source=f"wikipedia_{language}",
                        category="encyclopedia",
                        language=language
                    )
                    
                    self._save_knowledge_entry(knowledge_entry)
                    print(f"✅ تم استخراج معرفة من ويكيبيديا: {topic}")
                    return content
                else:
                    print(f"❌ لم يتم العثور على محتوى للموضوع: {topic}")
                    return None
            else:
                print(f"❌ خطأ في ويكيبيديا: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"❌ خطأ في استخراج المعرفة من ويكيبيديا: {e}")
            return None
    
    def _create_knowledge_entry(self, content: str, source: str, 
                               category: str, language: str) -> KnowledgeEntry:
        """إنشاء مدخل معرفي مع تطبيق النظريات الثورية"""
        
        # تطبيق نظرية ثنائية الصفر
        zero_duality_score = self._calculate_zero_duality(content)
        
        # تطبيق نظرية تعامد الأضداد
        perpendicularity_factor = self._calculate_perpendicularity(content)
        
        # تطبيق نظرية الفتائل
        filament_connections = self._calculate_filament_connections(content)
        
        # إنشاء معرف ثوري
        content_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
        revolutionary_id = f"rev_{source}_{content_hash}"
        
        return KnowledgeEntry(
            content=content,
            source=source,
            category=category,
            language=language,
            zero_duality_score=zero_duality_score,
            perpendicularity_factor=perpendicularity_factor,
            filament_connections=filament_connections,
            extraction_date=datetime.now().isoformat(),
            revolutionary_id=revolutionary_id
        )
    
    def _calculate_zero_duality(self, content: str) -> float:
        """حساب نقاط ثنائية الصفر للمحتوى"""
        # تطبيق مبسط لنظرية ثنائية الصفر
        char_count = len(content)
        word_count = len(content.split())
        
        if word_count == 0:
            return 0.0
        
        balance_ratio = char_count / word_count
        zero_duality_score = (balance_ratio * self.zero_duality_factor) % 1.0
        
        return round(zero_duality_score, 4)
    
    def _calculate_perpendicularity(self, content: str) -> float:
        """حساب عامل التعامد للمحتوى"""
        # تطبيق مبسط لنظرية تعامد الأضداد
        sentences = content.split('.')
        sentence_count = len([s for s in sentences if s.strip()])
        
        if sentence_count == 0:
            return 0.0
        
        perpendicularity = (sentence_count * self.perpendicularity_angle) % 180.0 / 180.0
        return round(perpendicularity, 4)
    
    def _calculate_filament_connections(self, content: str) -> List[str]:
        """حساب اتصالات الفتائل للمحتوى"""
        # تطبيق مبسط لنظرية الفتائل
        words = content.split()
        connections = []
        
        # أول 5 كلمات كاتصالات فتائل
        for i, word in enumerate(words[:5]):
            if len(word) > 2:  # تجاهل الكلمات القصيرة
                connections.append(f"{word}:{len(word)}")
        
        return connections
    
    def _save_knowledge_entry(self, entry: KnowledgeEntry):
        """حفظ المدخل المعرفي في قاعدة البيانات"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            content_hash = hashlib.sha256(entry.content.encode()).hexdigest()
            
            cursor.execute("""
                INSERT OR IGNORE INTO extracted_knowledge 
                (content, source, category, language, zero_duality_score, 
                 perpendicularity_factor, filament_connections, extraction_date, 
                 revolutionary_id, content_hash)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                entry.content,
                entry.source,
                entry.category,
                entry.language,
                entry.zero_duality_score,
                entry.perpendicularity_factor,
                json.dumps(entry.filament_connections),
                entry.extraction_date,
                entry.revolutionary_id,
                content_hash
            ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(f"❌ خطأ في حفظ المعرفة: {e}")
    
    def get_knowledge_stats(self) -> Dict[str, Any]:
        """الحصول على إحصائيات المعرفة المستخرجة"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # إجمالي المعرفة المستخرجة
            cursor.execute("SELECT COUNT(*) FROM extracted_knowledge")
            total_knowledge = cursor.fetchone()[0]
            
            # المعرفة حسب المصدر
            cursor.execute("""
                SELECT source, COUNT(*) 
                FROM extracted_knowledge 
                GROUP BY source
            """)
            by_source = dict(cursor.fetchall())
            
            # المعرفة حسب الفئة
            cursor.execute("""
                SELECT category, COUNT(*) 
                FROM extracted_knowledge 
                GROUP BY category
            """)
            by_category = dict(cursor.fetchall())
            
            conn.close()
            
            return {
                'total_knowledge': total_knowledge,
                'by_source': by_source,
                'by_category': by_category,
                'database_path': self.db_path
            }
            
        except Exception as e:
            print(f"❌ خطأ في الحصول على الإحصائيات: {e}")
            return {}
    
    def search_knowledge(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """البحث في المعرفة المستخرجة"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT content, source, category, zero_duality_score, 
                       perpendicularity_factor, filament_connections
                FROM extracted_knowledge 
                WHERE content LIKE ? 
                ORDER BY zero_duality_score DESC
                LIMIT ?
            """, (f"%{query}%", limit))
            
            results = []
            for row in cursor.fetchall():
                results.append({
                    'content': row[0][:200] + "..." if len(row[0]) > 200 else row[0],
                    'source': row[1],
                    'category': row[2],
                    'zero_duality_score': row[3],
                    'perpendicularity_factor': row[4],
                    'filament_connections': json.loads(row[5]) if row[5] else []
                })
            
            conn.close()
            return results
            
        except Exception as e:
            print(f"❌ خطأ في البحث: {e}")
            return []

def demo_external_knowledge_bridge():
    """عرض توضيحي لجسر المعرفة الخارجية"""
    
    print("🌉⚡ عرض توضيحي لجسر المعرفة الخارجية")
    print("=" * 60)
    
    # إنشاء الجسر
    bridge = ExternalKnowledgeBridge()
    
    # اختبار الاتصال مع Ollama
    print("\n🔗 اختبار الاتصال مع Ollama:")
    ollama_available = bridge.check_ollama_connection()
    
    # استخراج من ويكيبيديا
    print("\n📚 استخراج معرفة من ويكيبيديا:")
    topics = ["الذكاء_الاصطناعي", "الرياضيات", "الفيزياء"]
    
    for topic in topics:
        content = bridge.extract_from_wikipedia(topic)
        if content:
            print(f"   ✅ {topic}: {len(content)} حرف")
        else:
            print(f"   ❌ فشل في استخراج: {topic}")
    
    # عرض الإحصائيات
    print("\n📊 إحصائيات المعرفة المستخرجة:")
    stats = bridge.get_knowledge_stats()
    print(f"   📈 إجمالي المعرفة: {stats.get('total_knowledge', 0)}")
    print(f"   🔗 المصادر: {list(stats.get('by_source', {}).keys())}")
    print(f"   📂 الفئات: {list(stats.get('by_category', {}).keys())}")
    
    # اختبار البحث
    print("\n🔍 اختبار البحث في المعرفة:")
    results = bridge.search_knowledge("ذكاء", limit=3)
    for i, result in enumerate(results, 1):
        print(f"   {i}. {result['content'][:100]}...")
        print(f"      المصدر: {result['source']} | ثنائية الصفر: {result['zero_duality_score']}")
    
    print("\n🎉 انتهى العرض التوضيحي!")
    print("🧬 جسر المعرفة الخارجية جاهز للاستخدام!")

if __name__ == "__main__":
    demo_external_knowledge_bridge()
