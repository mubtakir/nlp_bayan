#!/usr/bin/env python3
"""
أنظمة المعرفة المتخصصة - Specialized Knowledge Systems
نظام بصيرة المتكامل

📚 أنظمة معرفة متقدمة للمعلومات المتخصصة
🧠 إدارة المعرفة الذكية بالنظريات الثورية
🔗 ربط المعرفة بالمعادلات والأنماط

المطور: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله
"""

import numpy as np
import sqlite3
import json
import uuid
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional, Union
from dataclasses import dataclass, field
from enum import Enum
import pickle
import hashlib

class KnowledgeType(Enum):
    """أنواع المعرفة"""
    MATHEMATICAL = "mathematical"
    SCIENTIFIC = "scientific"
    LINGUISTIC = "linguistic"
    PHILOSOPHICAL = "philosophical"
    TECHNICAL = "technical"
    HISTORICAL = "historical"
    CULTURAL = "cultural"
    REVOLUTIONARY = "revolutionary"

class KnowledgeLevel(Enum):
    """مستويات المعرفة"""
    BASIC = "basic"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"
    REVOLUTIONARY = "revolutionary"

@dataclass
class KnowledgeItem:
    """عنصر معرفي"""
    item_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str = ""
    content: str = ""
    knowledge_type: KnowledgeType = KnowledgeType.TECHNICAL
    knowledge_level: KnowledgeLevel = KnowledgeLevel.INTERMEDIATE
    tags: List[str] = field(default_factory=list)
    related_equations: List[str] = field(default_factory=list)
    confidence_score: float = 0.8
    creation_time: datetime = field(default_factory=datetime.now)
    last_updated: datetime = field(default_factory=datetime.now)
    usage_count: int = 0
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class KnowledgeRelation:
    """علاقة معرفية"""
    relation_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    source_id: str = ""
    target_id: str = ""
    relation_type: str = "related"  # related, depends_on, contradicts, extends
    strength: float = 0.5  # 0-1
    description: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)

class SpecializedKnowledgeSystem:
    """
    نظام المعرفة المتخصص
    
    📚 نظام متكامل لإدارة المعرفة:
    - تخزين واسترجاع المعرفة المتخصصة
    - ربط المعرفة بالمعادلات والأنماط
    - تطبيق النظريات الثورية في التنظيم
    - تعلم وتطوير المعرفة تلقائياً
    """
    
    def __init__(self, name: str = "BaserahKnowledge", db_path: str = "knowledge_systems.db"):
        self.name = name
        self.db_path = db_path
        self.creation_time = datetime.now()
        
        # معاملات المعرفة الثورية
        self.alpha_knowledge = [1.3, 0.9, 0.6]  # معاملات الفهم
        self.k_knowledge = [2.8, 3.2, 3.6]      # معاملات العمق المعرفي
        self.beta_knowledge = [0.18, 0.12, 0.08] # معاملات الترابط
        
        # إحصائيات النظام
        self.total_knowledge_items = 0
        self.total_relations = 0
        self.knowledge_quality_average = 0.0
        self.retrieval_efficiency = 0.0
        
        # ذاكرة المعرفة
        self.knowledge_cache = {}
        self.relation_cache = {}
        
        # إنشاء قاعدة البيانات
        self._initialize_database()
        
        print(f"📚⚡ تم إنشاء نظام المعرفة المتخصص: {name}")
        print(f"   🧠 معاملات المعرفة: α={self.alpha_knowledge}, k={self.k_knowledge}, β={self.beta_knowledge}")
        print(f"   💾 قاعدة البيانات: {db_path}")
    
    def _initialize_database(self):
        """إنشاء قاعدة البيانات وجداولها"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # جدول عناصر المعرفة
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS knowledge_items (
                item_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                knowledge_type TEXT NOT NULL,
                knowledge_level TEXT NOT NULL,
                tags TEXT,
                related_equations TEXT,
                confidence_score REAL,
                creation_time TEXT,
                last_updated TEXT,
                usage_count INTEGER,
                metadata TEXT
            )
        ''')
        
        # جدول العلاقات المعرفية
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS knowledge_relations (
                relation_id TEXT PRIMARY KEY,
                source_id TEXT NOT NULL,
                target_id TEXT NOT NULL,
                relation_type TEXT NOT NULL,
                strength REAL,
                description TEXT,
                metadata TEXT,
                FOREIGN KEY (source_id) REFERENCES knowledge_items (item_id),
                FOREIGN KEY (target_id) REFERENCES knowledge_items (item_id)
            )
        ''')
        
        # جدول إحصائيات الاستخدام
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usage_statistics (
                stat_id TEXT PRIMARY KEY,
                item_id TEXT NOT NULL,
                access_time TEXT,
                context TEXT,
                success_rate REAL,
                FOREIGN KEY (item_id) REFERENCES knowledge_items (item_id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def compute_knowledge_understanding_function(self, complexity: float, depth: float) -> float:
        """حساب دالة الفهم المعرفي الثورية"""
        understanding_score = 0.0
        
        # تطبيق معادلة الفهم: U(x) = Σ(αᵢ·σ(complexity;kᵢ) + βᵢ·depth)
        for i in range(min(len(self.alpha_knowledge), len(self.k_knowledge), len(self.beta_knowledge))):
            # دالة السيجمويد للتعقيد المعرفي
            sigmoid_part = self.alpha_knowledge[i] / (1 + np.exp(-self.k_knowledge[i] * complexity))
            
            # الجزء الخطي للعمق
            linear_part = self.beta_knowledge[i] * depth
            
            understanding_score += sigmoid_part + linear_part
        
        return min(understanding_score, 1.0)  # تطبيع النتيجة
    
    def add_knowledge_item(self, item: KnowledgeItem) -> str:
        """إضافة عنصر معرفي جديد"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # تحليل المعرفة
        analysis = self._analyze_knowledge_item(item)
        
        # تحديث نقاط الثقة بناءً على التحليل
        item.confidence_score = analysis["understanding_score"]
        
        try:
            cursor.execute('''
                INSERT INTO knowledge_items 
                (item_id, title, content, knowledge_type, knowledge_level, tags, 
                 related_equations, confidence_score, creation_time, last_updated, 
                 usage_count, metadata)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                item.item_id, item.title, item.content, 
                item.knowledge_type.value, item.knowledge_level.value,
                json.dumps(item.tags), json.dumps(item.related_equations),
                item.confidence_score, item.creation_time.isoformat(),
                item.last_updated.isoformat(), item.usage_count,
                json.dumps(item.metadata)
            ))
            
            conn.commit()
            self.total_knowledge_items += 1
            
            # تحديث الذاكرة المؤقتة
            self.knowledge_cache[item.item_id] = item
            
            # البحث عن علاقات تلقائية
            self._discover_automatic_relations(item)
            
            print(f"📚 تم إضافة عنصر معرفي: {item.title}")
            print(f"   🎯 الثقة: {item.confidence_score:.3f}")
            print(f"   🧠 الفهم: {analysis['understanding_score']:.3f}")
            
        except Exception as e:
            print(f"❌ خطأ في إضافة المعرفة: {e}")
            return ""
        finally:
            conn.close()
        
        return item.item_id
    
    def _analyze_knowledge_item(self, item: KnowledgeItem) -> Dict[str, Any]:
        """تحليل عنصر المعرفة"""
        # تحليل التعقيد
        content_words = len(item.content.split())
        complexity_score = min(content_words / 200.0, 1.0)  # تطبيع التعقيد
        
        # تحليل العمق
        depth_indicators = len(item.tags) + len(item.related_equations)
        depth_score = min(depth_indicators / 10.0, 1.0)  # تطبيع العمق
        
        # حساب الفهم المطلوب
        understanding_score = self.compute_knowledge_understanding_function(complexity_score, depth_score)
        
        # تطبيق النظريات الثورية
        zero_duality_balance = self._apply_zero_duality_knowledge(item)
        perpendicular_diversity = self._apply_perpendicular_knowledge(item)
        filament_connections = self._apply_filament_knowledge_theory(item)
        
        return {
            "complexity_score": complexity_score,
            "depth_score": depth_score,
            "understanding_score": understanding_score,
            "zero_duality_balance": zero_duality_balance,
            "perpendicular_diversity": perpendicular_diversity,
            "filament_connections": filament_connections,
            "content_words": content_words,
            "depth_indicators": depth_indicators
        }
    
    def _apply_zero_duality_knowledge(self, item: KnowledgeItem) -> float:
        """تطبيق نظرية ثنائية الصفر في المعرفة"""
        # تحليل التوازن في المحتوى المعرفي
        content_words = item.content.lower().split()
        
        # كلمات إيجابية ومعرفية
        positive_knowledge = ['صحيح', 'دقيق', 'مؤكد', 'ثابت', 'موثوق', 'علمي']
        negative_knowledge = ['خطأ', 'غير دقيق', 'مشكوك', 'غير مؤكد', 'ضعيف']
        
        positive_count = sum(1 for word in content_words if any(pos in word for pos in positive_knowledge))
        negative_count = sum(1 for word in content_words if any(neg in word for neg in negative_knowledge))
        
        total_indicators = positive_count + negative_count
        if total_indicators == 0:
            return 0.8  # توازن محايد جيد
        
        balance = 1.0 - abs(positive_count - negative_count) / total_indicators
        return balance
    
    def _apply_perpendicular_knowledge(self, item: KnowledgeItem) -> float:
        """تطبيق نظرية تعامد الأضداد في المعرفة"""
        # تحليل التنوع في العلامات والمعادلات
        total_elements = len(item.tags) + len(item.related_equations)
        if total_elements < 2:
            return 0.6
        
        # حساب التنوع
        unique_elements = set(item.tags + item.related_equations)
        diversity = len(unique_elements) / total_elements if total_elements > 0 else 0
        
        return min(diversity * 1.5, 1.0)  # تعزيز التنوع
    
    def _apply_filament_knowledge_theory(self, item: KnowledgeItem) -> float:
        """تطبيق نظرية الفتائل في المعرفة"""
        # تحليل الترابط في المعرفة
        title_words = set(item.title.lower().split())
        content_words = set(item.content.lower().split())
        tag_words = set(' '.join(item.tags).lower().split())
        
        # حساب الترابط
        title_content_intersection = len(title_words & content_words)
        title_tag_intersection = len(title_words & tag_words)
        content_tag_intersection = len(content_words & tag_words)
        
        total_connections = title_content_intersection + title_tag_intersection + content_tag_intersection
        max_possible_connections = len(title_words) + len(tag_words)
        
        if max_possible_connections == 0:
            return 0.5
        
        connection_strength = min(total_connections / max_possible_connections, 1.0)
        return connection_strength
    
    def _discover_automatic_relations(self, new_item: KnowledgeItem):
        """اكتشاف العلاقات التلقائية"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # البحث عن عناصر مشابهة
        cursor.execute('SELECT * FROM knowledge_items WHERE item_id != ?', (new_item.item_id,))
        existing_items = cursor.fetchall()
        
        for row in existing_items:
            existing_item = self._row_to_knowledge_item(row)
            
            # حساب التشابه
            similarity = self._calculate_similarity(new_item, existing_item)
            
            if similarity > 0.3:  # عتبة التشابه
                # إنشاء علاقة
                relation = KnowledgeRelation(
                    source_id=new_item.item_id,
                    target_id=existing_item.item_id,
                    relation_type="related",
                    strength=similarity,
                    description=f"علاقة تلقائية بقوة {similarity:.3f}"
                )
                
                self.add_knowledge_relation(relation)
        
        conn.close()
    
    def _calculate_similarity(self, item1: KnowledgeItem, item2: KnowledgeItem) -> float:
        """حساب التشابه بين عنصرين معرفيين"""
        # تشابه النوع
        type_similarity = 1.0 if item1.knowledge_type == item2.knowledge_type else 0.0
        
        # تشابه العلامات
        tags1 = set(item1.tags)
        tags2 = set(item2.tags)
        tag_intersection = len(tags1 & tags2)
        tag_union = len(tags1 | tags2)
        tag_similarity = tag_intersection / tag_union if tag_union > 0 else 0
        
        # تشابه المحتوى (مبسط)
        words1 = set(item1.content.lower().split())
        words2 = set(item2.content.lower().split())
        content_intersection = len(words1 & words2)
        content_union = len(words1 | words2)
        content_similarity = content_intersection / content_union if content_union > 0 else 0
        
        # المتوسط المرجح
        total_similarity = (type_similarity * 0.3 + tag_similarity * 0.4 + content_similarity * 0.3)
        return total_similarity
    
    def add_knowledge_relation(self, relation: KnowledgeRelation) -> str:
        """إضافة علاقة معرفية"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO knowledge_relations 
                (relation_id, source_id, target_id, relation_type, strength, description, metadata)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                relation.relation_id, relation.source_id, relation.target_id,
                relation.relation_type, relation.strength, relation.description,
                json.dumps(relation.metadata)
            ))
            
            conn.commit()
            self.total_relations += 1
            
            # تحديث الذاكرة المؤقتة
            self.relation_cache[relation.relation_id] = relation
            
        except Exception as e:
            print(f"❌ خطأ في إضافة العلاقة: {e}")
            return ""
        finally:
            conn.close()
        
        return relation.relation_id
    
    def search_knowledge(self, query: str, knowledge_type: KnowledgeType = None, 
                        limit: int = 10) -> List[KnowledgeItem]:
        """البحث في المعرفة"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # بناء استعلام البحث
        base_query = '''
            SELECT * FROM knowledge_items 
            WHERE (title LIKE ? OR content LIKE ? OR tags LIKE ?)
        '''
        params = [f'%{query}%', f'%{query}%', f'%{query}%']
        
        if knowledge_type:
            base_query += ' AND knowledge_type = ?'
            params.append(knowledge_type.value)
        
        base_query += ' ORDER BY confidence_score DESC, usage_count DESC LIMIT ?'
        params.append(limit)
        
        cursor.execute(base_query, params)
        rows = cursor.fetchall()
        
        results = []
        for row in rows:
            item = self._row_to_knowledge_item(row)
            results.append(item)
            
            # تحديث عداد الاستخدام
            self._update_usage_count(item.item_id)
        
        conn.close()
        return results
    
    def get_related_knowledge(self, item_id: str, relation_types: List[str] = None) -> List[Tuple[KnowledgeItem, KnowledgeRelation]]:
        """الحصول على المعرفة المرتبطة"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # بناء استعلام العلاقات
        base_query = '''
            SELECT kr.*, ki.* FROM knowledge_relations kr
            JOIN knowledge_items ki ON (kr.target_id = ki.item_id OR kr.source_id = ki.item_id)
            WHERE (kr.source_id = ? OR kr.target_id = ?) AND ki.item_id != ?
        '''
        params = [item_id, item_id, item_id]
        
        if relation_types:
            placeholders = ','.join(['?' for _ in relation_types])
            base_query += f' AND kr.relation_type IN ({placeholders})'
            params.extend(relation_types)
        
        base_query += ' ORDER BY kr.strength DESC'
        
        cursor.execute(base_query, params)
        rows = cursor.fetchall()
        
        results = []
        for row in rows:
            # تقسيم البيانات (العلاقة + العنصر المعرفي)
            relation_data = row[:7]  # أول 7 أعمدة للعلاقة
            item_data = row[7:]      # باقي الأعمدة للعنصر المعرفي
            
            relation = self._row_to_knowledge_relation(relation_data)
            item = self._row_to_knowledge_item(item_data)
            
            results.append((item, relation))
        
        conn.close()
        return results
    
    def _row_to_knowledge_item(self, row) -> KnowledgeItem:
        """تحويل صف قاعدة البيانات إلى عنصر معرفي"""
        return KnowledgeItem(
            item_id=row[0],
            title=row[1],
            content=row[2],
            knowledge_type=KnowledgeType(row[3]),
            knowledge_level=KnowledgeLevel(row[4]),
            tags=json.loads(row[5]) if row[5] else [],
            related_equations=json.loads(row[6]) if row[6] else [],
            confidence_score=row[7],
            creation_time=datetime.fromisoformat(row[8]),
            last_updated=datetime.fromisoformat(row[9]),
            usage_count=row[10],
            metadata=json.loads(row[11]) if row[11] else {}
        )
    
    def _row_to_knowledge_relation(self, row) -> KnowledgeRelation:
        """تحويل صف قاعدة البيانات إلى علاقة معرفية"""
        return KnowledgeRelation(
            relation_id=row[0],
            source_id=row[1],
            target_id=row[2],
            relation_type=row[3],
            strength=row[4],
            description=row[5],
            metadata=json.loads(row[6]) if row[6] else {}
        )
    
    def _update_usage_count(self, item_id: str):
        """تحديث عداد الاستخدام"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE knowledge_items 
            SET usage_count = usage_count + 1, last_updated = ?
            WHERE item_id = ?
        ''', (datetime.now().isoformat(), item_id))
        
        conn.commit()
        conn.close()
    
    def get_knowledge_statistics(self) -> Dict[str, Any]:
        """الحصول على إحصائيات المعرفة"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # إحصائيات عامة
        cursor.execute('SELECT COUNT(*) FROM knowledge_items')
        total_items = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM knowledge_relations')
        total_relations = cursor.fetchone()[0]
        
        cursor.execute('SELECT AVG(confidence_score) FROM knowledge_items')
        avg_confidence = cursor.fetchone()[0] or 0
        
        # إحصائيات حسب النوع
        cursor.execute('''
            SELECT knowledge_type, COUNT(*) 
            FROM knowledge_items 
            GROUP BY knowledge_type
        ''')
        type_distribution = dict(cursor.fetchall())
        
        # إحصائيات حسب المستوى
        cursor.execute('''
            SELECT knowledge_level, COUNT(*) 
            FROM knowledge_items 
            GROUP BY knowledge_level
        ''')
        level_distribution = dict(cursor.fetchall())
        
        conn.close()
        
        return {
            "total_items": total_items,
            "total_relations": total_relations,
            "average_confidence": avg_confidence,
            "type_distribution": type_distribution,
            "level_distribution": level_distribution,
            "knowledge_parameters": {
                "alpha": self.alpha_knowledge,
                "k": self.k_knowledge,
                "beta": self.beta_knowledge
            },
            "creation_time": self.creation_time.isoformat()
        }

# ==================== اختبار أنظمة المعرفة ====================

def test_specialized_knowledge_systems():
    """اختبار شامل لأنظمة المعرفة المتخصصة"""
    print("📚 اختبار أنظمة المعرفة المتخصصة")
    print("="*60)
    
    # إنشاء نظام المعرفة
    knowledge_system = SpecializedKnowledgeSystem("TestKnowledge", "test_knowledge.db")
    
    # إنشاء عناصر معرفية اختبارية
    test_items = [
        KnowledgeItem(
            title="نظرية ثنائية الصفر",
            content="نظرية ثورية تحقق التوازن المثالي في الأنظمة الرياضية من خلال تطبيق مبدأ الثنائية الصفرية التي تضمن الاستقرار والدقة في الحسابات المعقدة.",
            knowledge_type=KnowledgeType.MATHEMATICAL,
            knowledge_level=KnowledgeLevel.REVOLUTIONARY,
            tags=["ثنائية الصفر", "توازن", "رياضيات", "نظرية ثورية"],
            related_equations=["f(x) = α·σ(x) + β·x", "balance = |pos - neg| / total"]
        ),
        KnowledgeItem(
            title="نظرية تعامد الأضداد",
            content="نظرية تطبق مبدأ التعامد الرياضي على الأضداد لتحقيق التنوع والشمولية في التحليل، مما يضمن تغطية جميع الجوانب المختلفة للمشكلة.",
            knowledge_type=KnowledgeType.MATHEMATICAL,
            knowledge_level=KnowledgeLevel.REVOLUTIONARY,
            tags=["تعامد الأضداد", "تنوع", "شمولية", "تحليل"],
            related_equations=["perpendicular = 1 - similarity", "diversity = unique / total"]
        ),
        KnowledgeItem(
            title="نظرية الفتائل",
            content="نظرية تصف الترابط المعقد بين العناصر المختلفة في النظام، مشبهة بالفتائل المتداخلة التي تقوي البنية الكلية للنظام.",
            knowledge_type=KnowledgeType.MATHEMATICAL,
            knowledge_level=KnowledgeLevel.REVOLUTIONARY,
            tags=["فتائل", "ترابط", "تعقيد", "بنية"],
            related_equations=["filament = connections / max_connections", "strength = Σ(weights)"]
        ),
        KnowledgeItem(
            title="الذكاء الاصطناعي النقي",
            content="منهجية ثورية لتطوير أنظمة ذكية بدون الاعتماد على مكتبات الذكاء الاصطناعي التقليدية، باستخدام الرياضيات النقية فقط.",
            knowledge_type=KnowledgeType.TECHNICAL,
            knowledge_level=KnowledgeLevel.ADVANCED,
            tags=["ذكاء اصطناعي", "رياضيات نقية", "شفافية", "ابتكار"],
            related_equations=["AI(x) = sigmoid(x) + linear(x)", "transparency = 100%"]
        )
    ]
    
    print(f"\n📝 إضافة {len(test_items)} عناصر معرفية:")
    
    # إضافة العناصر المعرفية
    item_ids = []
    for i, item in enumerate(test_items, 1):
        print(f"\n📚 العنصر {i}: {item.title}")
        item_id = knowledge_system.add_knowledge_item(item)
        item_ids.append(item_id)
        print(f"   🆔 المعرف: {item_id[:8]}...")
        print(f"   🏷️ العلامات: {', '.join(item.tags)}")
    
    # اختبار البحث
    print(f"\n🔍 اختبار البحث في المعرفة:")
    
    search_queries = ["نظرية", "ثوري", "رياضيات", "ذكاء"]
    for query in search_queries:
        results = knowledge_system.search_knowledge(query, limit=3)
        print(f"\n   🔎 البحث عن '{query}': {len(results)} نتيجة")
        for result in results:
            print(f"      • {result.title} (ثقة: {result.confidence_score:.3f})")
    
    # اختبار العلاقات المرتبطة
    if item_ids:
        print(f"\n🔗 اختبار العلاقات المرتبطة:")
        first_item_id = item_ids[0]
        related = knowledge_system.get_related_knowledge(first_item_id)
        print(f"   📊 العلاقات للعنصر الأول: {len(related)} علاقة")
        for item, relation in related:
            print(f"      • {item.title} (قوة: {relation.strength:.3f})")
    
    # عرض الإحصائيات
    print(f"\n📊 إحصائيات نظام المعرفة:")
    stats = knowledge_system.get_knowledge_statistics()
    print(f"   📈 إجمالي العناصر: {stats['total_items']}")
    print(f"   🔗 إجمالي العلاقات: {stats['total_relations']}")
    print(f"   🎯 متوسط الثقة: {stats['average_confidence']:.3f}")
    print(f"   📊 توزيع الأنواع: {stats['type_distribution']}")
    print(f"   📊 توزيع المستويات: {stats['level_distribution']}")
    
    print(f"\n✅ انتهى اختبار أنظمة المعرفة المتخصصة!")
    return knowledge_system

if __name__ == "__main__":
    test_specialized_knowledge_systems()

