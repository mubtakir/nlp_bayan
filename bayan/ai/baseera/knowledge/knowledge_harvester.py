#!/usr/bin/env python3
"""
🌾 حاصد المعرفة الثوري - نظام بصيرة
📚 استخراج المعرفة من مصادر متعددة مع تطبيق النظريات الثلاث
🧬 بناء مكتبة معرفية ذاتية تدريجياً

الاستراتيجية: استخراج → تحليل → حفظ → استقلالية
المصادر: ملفات محلية، APIs مفتوحة، نصوص جاهزة

المطور: باسل يحيى عبدالله
"""

import json
import sqlite3
import hashlib
import os
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime
import re

@dataclass
class KnowledgeItem:
    """عنصر معرفي مع النظريات الثورية"""
    content: str
    source: str
    category: str
    language: str
    zero_duality_score: float
    perpendicularity_factor: float
    filament_connections: List[str]
    revolutionary_id: str

class KnowledgeHarvester:
    """
    🌾 حاصد المعرفة الثوري
    يستخرج المعرفة من مصادر متعددة ويطبق النظريات الثلاث
    """
    
    def __init__(self, db_path: str = "databases/harvested_knowledge.db"):
        """تهيئة حاصد المعرفة"""
        self.db_path = db_path
        self.setup_database()
        
        # النظريات الثورية
        self.zero_duality_factor = 0.618
        self.perpendicularity_angle = 90.0
        self.filament_strength = 0.85
        
        print("🌾⚡ تم إنشاء حاصد المعرفة الثوري")
        print("   📚 جاهز لاستخراج المعرفة من مصادر متعددة")
        print("   🧬 النظريات الثلاث: نشطة")
    
    def setup_database(self):
        """إعداد قاعدة بيانات المعرفة"""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS knowledge_base (
                id INTEGER PRIMARY KEY,
                content TEXT NOT NULL,
                source TEXT NOT NULL,
                category TEXT,
                language TEXT DEFAULT 'ar',
                zero_duality_score REAL,
                perpendicularity_factor REAL,
                filament_connections TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                revolutionary_id TEXT UNIQUE,
                content_hash TEXT UNIQUE
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS word_embeddings (
                id INTEGER PRIMARY KEY,
                word TEXT NOT NULL,
                embedding_vector TEXT,
                frequency INTEGER DEFAULT 1,
                zero_duality_embedding REAL,
                perpendicularity_embedding REAL,
                filament_embedding TEXT,
                revolutionary_word_id TEXT UNIQUE
            )
        """)
        
        conn.commit()
        conn.close()
    
    def harvest_from_text_file(self, file_path: str, category: str = "text_file") -> int:
        """استخراج المعرفة من ملف نصي"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # تقسيم النص إلى فقرات
            paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
            
            harvested_count = 0
            for paragraph in paragraphs:
                if len(paragraph) > 50:  # تجاهل الفقرات القصيرة
                    knowledge_item = self._create_knowledge_item(
                        content=paragraph,
                        source=f"file_{os.path.basename(file_path)}",
                        category=category,
                        language="ar"
                    )
                    
                    if self._save_knowledge_item(knowledge_item):
                        harvested_count += 1
            
            print(f"✅ تم استخراج {harvested_count} فقرة من {file_path}")
            return harvested_count
            
        except Exception as e:
            print(f"❌ خطأ في استخراج المعرفة من الملف: {e}")
            return 0
    
    def harvest_sample_knowledge(self) -> int:
        """استخراج معرفة تجريبية مدمجة"""
        
        sample_knowledge = [
            {
                "content": "الذكاء الاصطناعي هو محاكاة الذكاء البشري في الآلات المبرمجة للتفكير والتعلم مثل البشر. يشمل التعلم الآلي ومعالجة اللغة الطبيعية والرؤية الحاسوبية.",
                "category": "technology",
                "source": "sample_ai_knowledge"
            },
            {
                "content": "الرياضيات هي علم الأرقام والأشكال والأنماط. تشمل الجبر والهندسة والتفاضل والتكامل والإحصاء. الرياضيات أساس جميع العلوم والتكنولوجيا الحديثة.",
                "category": "mathematics",
                "source": "sample_math_knowledge"
            },
            {
                "content": "اللغة العربية هي إحدى أكثر اللغات انتشاراً في العالم. تتميز بنظام صرفي معقد يعتمد على الجذور الثلاثية والأوزان الصرفية. كل كلمة لها جذر وزن ومعنى.",
                "category": "linguistics",
                "source": "sample_arabic_knowledge"
            },
            {
                "content": "الفيزياء هي علم دراسة المادة والطاقة والحركة. تشمل الميكانيكا والكهرومغناطيسية والديناميكا الحرارية وفيزياء الكم. الفيزياء تفسر كيف يعمل الكون.",
                "category": "physics",
                "source": "sample_physics_knowledge"
            },
            {
                "content": "التعلم الآلي هو فرع من الذكاء الاصطناعي يمكن الآلات من التعلم من البيانات دون برمجة صريحة. يشمل التعلم المراقب وغير المراقب والتعلم المعزز.",
                "category": "machine_learning",
                "source": "sample_ml_knowledge"
            },
            {
                "content": "معالجة اللغة الطبيعية هي مجال يجمع بين علوم الحاسوب واللسانيات لتمكين الحاسوب من فهم ومعالجة اللغة البشرية. يشمل التحليل النحوي والدلالي والترجمة الآلية.",
                "category": "nlp",
                "source": "sample_nlp_knowledge"
            }
        ]
        
        harvested_count = 0
        for item in sample_knowledge:
            knowledge_item = self._create_knowledge_item(
                content=item["content"],
                source=item["source"],
                category=item["category"],
                language="ar"
            )
            
            if self._save_knowledge_item(knowledge_item):
                harvested_count += 1
        
        print(f"✅ تم استخراج {harvested_count} عنصر معرفي تجريبي")
        return harvested_count
    
    def harvest_arabic_words(self) -> int:
        """استخراج كلمات عربية مع تحليل صرفي"""
        
        arabic_words = [
            {"word": "كتاب", "root": "كتب", "pattern": "فعال", "meaning": "مجموعة أوراق مكتوبة"},
            {"word": "مكتبة", "root": "كتب", "pattern": "مفعلة", "meaning": "مكان الكتب"},
            {"word": "كاتب", "root": "كتب", "pattern": "فاعل", "meaning": "من يكتب"},
            {"word": "مكتوب", "root": "كتب", "pattern": "مفعول", "meaning": "ما تم كتابته"},
            {"word": "مدرسة", "root": "درس", "pattern": "مفعلة", "meaning": "مكان التعليم"},
            {"word": "طالب", "root": "طلب", "pattern": "فاعل", "meaning": "من يطلب العلم"},
            {"word": "معلم", "root": "علم", "pattern": "مفعل", "meaning": "من يعلم"},
            {"word": "حاسوب", "root": "حسب", "pattern": "فاعول", "meaning": "آلة حاسبة"},
            {"word": "برنامج", "root": "برمج", "pattern": "فعلال", "meaning": "مجموعة تعليمات"},
            {"word": "شبكة", "root": "شبك", "pattern": "فعلة", "meaning": "نظام متصل"}
        ]
        
        harvested_count = 0
        for word_data in arabic_words:
            # إنشاء محتوى وصفي للكلمة
            content = f"الكلمة: {word_data['word']} | الجذر: {word_data['root']} | الوزن: {word_data['pattern']} | المعنى: {word_data['meaning']}"
            
            knowledge_item = self._create_knowledge_item(
                content=content,
                source="arabic_morphology",
                category="arabic_words",
                language="ar"
            )
            
            if self._save_knowledge_item(knowledge_item):
                harvested_count += 1
                
                # حفظ الكلمة في جدول المتجهات
                self._save_word_embedding(word_data['word'], word_data)
        
        print(f"✅ تم استخراج {harvested_count} كلمة عربية مع تحليل صرفي")
        return harvested_count
    
    def _create_knowledge_item(self, content: str, source: str, 
                              category: str, language: str) -> KnowledgeItem:
        """إنشاء عنصر معرفي مع تطبيق النظريات الثورية"""
        
        # تطبيق النظريات الثلاث
        zero_duality_score = self._calculate_zero_duality(content)
        perpendicularity_factor = self._calculate_perpendicularity(content)
        filament_connections = self._calculate_filament_connections(content)
        
        # إنشاء معرف ثوري
        content_hash = hashlib.sha256(content.encode()).hexdigest()[:12]
        revolutionary_id = f"rev_{category}_{content_hash}"
        
        return KnowledgeItem(
            content=content,
            source=source,
            category=category,
            language=language,
            zero_duality_score=zero_duality_score,
            perpendicularity_factor=perpendicularity_factor,
            filament_connections=filament_connections,
            revolutionary_id=revolutionary_id
        )
    
    def _calculate_zero_duality(self, content: str) -> float:
        """حساب نقاط ثنائية الصفر"""
        words = content.split()
        if not words:
            return 0.0
        
        total_chars = sum(len(word) for word in words)
        avg_word_length = total_chars / len(words)
        
        # تطبيق النسبة الذهبية
        balance_score = (avg_word_length * self.zero_duality_factor) % 1.0
        return round(balance_score, 4)
    
    def _calculate_perpendicularity(self, content: str) -> float:
        """حساب عامل التعامد"""
        sentences = re.split(r'[.!?]', content)
        sentence_count = len([s for s in sentences if s.strip()])
        
        if sentence_count == 0:
            return 0.0
        
        # تطبيق زاوية التعامد
        perpendicularity = (sentence_count * self.perpendicularity_angle) % 180.0 / 180.0
        return round(perpendicularity, 4)
    
    def _calculate_filament_connections(self, content: str) -> List[str]:
        """حساب اتصالات الفتائل"""
        words = content.split()
        connections = []
        
        # أهم الكلمات كاتصالات
        important_words = [w for w in words if len(w) > 3 and w.isalpha()][:5]
        
        for word in important_words:
            connections.append(f"{word}:{len(word)}")
        
        return connections
    
    def _save_knowledge_item(self, item: KnowledgeItem) -> bool:
        """حفظ العنصر المعرفي"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            content_hash = hashlib.sha256(item.content.encode()).hexdigest()
            
            cursor.execute("""
                INSERT OR IGNORE INTO knowledge_base 
                (content, source, category, language, zero_duality_score, 
                 perpendicularity_factor, filament_connections, revolutionary_id, content_hash)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                item.content,
                item.source,
                item.category,
                item.language,
                item.zero_duality_score,
                item.perpendicularity_factor,
                json.dumps(item.filament_connections),
                item.revolutionary_id,
                content_hash
            ))
            
            success = cursor.rowcount > 0
            conn.commit()
            conn.close()
            return success
            
        except Exception as e:
            print(f"❌ خطأ في حفظ المعرفة: {e}")
            return False
    
    def _save_word_embedding(self, word: str, word_data: Dict[str, str]):
        """حفظ متجه الكلمة"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # إنشاء متجه بسيط للكلمة
            embedding = {
                "word_length": len(word),
                "root_length": len(word_data.get("root", "")),
                "pattern_complexity": len(word_data.get("pattern", "")),
                "meaning_words": len(word_data.get("meaning", "").split())
            }
            
            revolutionary_word_id = f"word_{hashlib.sha256(word.encode()).hexdigest()[:8]}"
            
            cursor.execute("""
                INSERT OR REPLACE INTO word_embeddings 
                (word, embedding_vector, zero_duality_embedding, 
                 perpendicularity_embedding, filament_embedding, revolutionary_word_id)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                word,
                json.dumps(embedding),
                self._calculate_zero_duality(word),
                self._calculate_perpendicularity(word_data.get("meaning", "")),
                json.dumps([f"{word}:{len(word)}"]),
                revolutionary_word_id
            ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(f"❌ خطأ في حفظ متجه الكلمة: {e}")
    
    def get_knowledge_stats(self) -> Dict[str, Any]:
        """إحصائيات المعرفة المحصودة"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute("SELECT COUNT(*) FROM knowledge_base")
            total_knowledge = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM word_embeddings")
            total_words = cursor.fetchone()[0]
            
            cursor.execute("""
                SELECT category, COUNT(*) 
                FROM knowledge_base 
                GROUP BY category
            """)
            by_category = dict(cursor.fetchall())
            
            conn.close()
            
            return {
                'total_knowledge': total_knowledge,
                'total_words': total_words,
                'by_category': by_category
            }
            
        except Exception as e:
            print(f"❌ خطأ في الإحصائيات: {e}")
            return {}
    
    def search_knowledge(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """البحث في المعرفة"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT content, source, category, zero_duality_score
                FROM knowledge_base 
                WHERE content LIKE ? 
                ORDER BY zero_duality_score DESC
                LIMIT ?
            """, (f"%{query}%", limit))
            
            results = []
            for row in cursor.fetchall():
                results.append({
                    'content': row[0][:150] + "..." if len(row[0]) > 150 else row[0],
                    'source': row[1],
                    'category': row[2],
                    'score': row[3]
                })
            
            conn.close()
            return results
            
        except Exception as e:
            print(f"❌ خطأ في البحث: {e}")
            return []

def main():
    """الدالة الرئيسية لحاصد المعرفة"""
    
    print("🌾⚡ حاصد المعرفة الثوري - نظام بصيرة")
    print("=" * 60)
    
    # إنشاء الحاصد
    harvester = KnowledgeHarvester()
    
    # استخراج المعرفة التجريبية
    print("\n📚 استخراج المعرفة التجريبية:")
    knowledge_count = harvester.harvest_sample_knowledge()
    
    # استخراج الكلمات العربية
    print("\n🔤 استخراج الكلمات العربية:")
    words_count = harvester.harvest_arabic_words()
    
    # عرض الإحصائيات
    print("\n📊 إحصائيات المعرفة المحصودة:")
    stats = harvester.get_knowledge_stats()
    print(f"   📈 إجمالي المعرفة: {stats.get('total_knowledge', 0)}")
    print(f"   🔤 إجمالي الكلمات: {stats.get('total_words', 0)}")
    print(f"   📂 الفئات: {list(stats.get('by_category', {}).keys())}")
    
    # اختبار البحث
    print("\n🔍 اختبار البحث:")
    search_terms = ["ذكاء", "رياضيات", "عربية"]
    for term in search_terms:
        results = harvester.search_knowledge(term, limit=2)
        print(f"   🔎 '{term}': {len(results)} نتيجة")
        for result in results:
            print(f"      📄 {result['content'][:80]}...")
    
    print(f"\n🎉 تم حصاد {knowledge_count + words_count} عنصر معرفي!")
    print("🧬 مكتبة المعرفة الثورية جاهزة للنمو!")

if __name__ == "__main__":
    main()
