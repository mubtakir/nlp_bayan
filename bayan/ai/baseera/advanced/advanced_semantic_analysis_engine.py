#!/usr/bin/env python3
"""
محرك التحليل الدلالي المتقدم - Advanced Semantic Analysis Engine
نظام بصيرة الثوري

🧠 تحليل دلالي عميق للنصوص العربية والإنجليزية
🔍 استخراج المعاني والمفاهيم والعلاقات
🎯 تحليل المشاعر والسياق والنوايا
⚡ يعتمد على النظريات الثلاث الثورية

المطور: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله
"""

import numpy as np
import re
import json
import math
from typing import Dict, List, Tuple, Any, Optional, Union
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import uuid

# استيراد المكونات الأساسية
from core_interfaces import BaseComponent
from advanced_linguistic_vector_system import AdvancedLinguisticVectorSystem, LinguisticVector

class AnalysisType(Enum):
    """أنواع التحليل الدلالي"""
    SENTIMENT_ANALYSIS = "sentiment_analysis"
    CONCEPT_EXTRACTION = "concept_extraction"
    RELATIONSHIP_ANALYSIS = "relationship_analysis"
    CONTEXT_ANALYSIS = "context_analysis"
    INTENT_ANALYSIS = "intent_analysis"
    SEMANTIC_SIMILARITY = "semantic_similarity"

class SentimentType(Enum):
    """أنواع المشاعر"""
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
    MIXED = "mixed"

class ConceptType(Enum):
    """أنواع المفاهيم"""
    ENTITY = "entity"
    ACTION = "action"
    ATTRIBUTE = "attribute"
    RELATION = "relation"
    ABSTRACT = "abstract"

@dataclass
class SemanticAnalysisResult:
    """نتيجة التحليل الدلالي"""
    text: str
    analysis_type: AnalysisType
    sentiment: SentimentType
    confidence: float
    concepts: List[Dict[str, Any]] = field(default_factory=list)
    relationships: List[Dict[str, Any]] = field(default_factory=list)
    context_info: Dict[str, Any] = field(default_factory=dict)
    semantic_vector: Optional[np.ndarray] = None
    analysis_time: float = 0.0
    analysis_id: str = field(default_factory=lambda: str(uuid.uuid4()))

@dataclass
class ExtractedConcept:
    """مفهوم مستخرج"""
    concept: str
    concept_type: ConceptType
    importance: float
    context: str
    related_words: List[str] = field(default_factory=list)

class ArabicSemanticRules:
    """قواعد الدلالة العربية"""
    
    def __init__(self):
        # قواعد المشاعر العربية
        self.sentiment_rules = {
            'positive_words': [
                'خير', 'نور', 'حب', 'سلام', 'فرح', 'أمل', 'نجاح', 'جمال',
                'بركة', 'رحمة', 'هداية', 'توفيق', 'سعادة', 'راحة', 'طمأنينة'
            ],
            'negative_words': [
                'شر', 'ظلام', 'كره', 'حرب', 'حزن', 'يأس', 'فشل', 'قبح',
                'لعنة', 'عذاب', 'ضلال', 'خذلان', 'تعاسة', 'قلق', 'خوف'
            ],
            'intensifiers': ['جداً', 'كثيراً', 'للغاية', 'أشد', 'أكثر', 'أعظم'],
            'negators': ['لا', 'ليس', 'غير', 'بدون', 'ما', 'لم', 'لن']
        }
        
        # قواعد المفاهيم
        self.concept_patterns = {
            'religious': ['الله', 'رسول', 'قرآن', 'صلاة', 'صوم', 'حج', 'زكاة'],
            'family': ['أب', 'أم', 'ابن', 'بنت', 'أخ', 'أخت', 'زوج', 'زوجة'],
            'nature': ['شمس', 'قمر', 'نجم', 'بحر', 'جبل', 'شجر', 'زهر'],
            'time': ['يوم', 'ليل', 'صباح', 'مساء', 'أمس', 'اليوم', 'غد'],
            'place': ['بيت', 'مدينة', 'قرية', 'شارع', 'حديقة', 'مسجد']
        }
        
        # قواعد العلاقات
        self.relationship_patterns = {
            'causality': ['لأن', 'بسبب', 'نتيجة', 'يؤدي إلى', 'ينتج عن'],
            'comparison': ['أكثر من', 'أقل من', 'مثل', 'كما', 'يشبه'],
            'temporal': ['قبل', 'بعد', 'أثناء', 'عند', 'حين', 'لما'],
            'spatial': ['في', 'على', 'تحت', 'فوق', 'بجانب', 'أمام', 'خلف']
        }

class AdvancedSemanticAnalysisEngine(BaseComponent):
    """محرك التحليل الدلالي المتقدم"""
    
    def __init__(self, name: str = "AdvancedSemanticAnalysisEngine"):
        super().__init__(name)
        
        # المكونات الأساسية
        self.linguistic_vector_system = AdvancedLinguisticVectorSystem()
        self.arabic_rules = ArabicSemanticRules()
        
        # قواعد التحليل
        self.analysis_rules = self._initialize_analysis_rules()
        self.context_patterns = self._initialize_context_patterns()
        
        # ذاكرة التحليل
        self.analysis_history: List[SemanticAnalysisResult] = []
        self.concept_database: Dict[str, ExtractedConcept] = {}
        
        # إحصائيات
        self.stats = {
            'total_analyses': 0,
            'sentiment_analyses': 0,
            'concept_extractions': 0,
            'relationship_analyses': 0,
            'average_confidence': 0.0,
            'processing_time': 0.0
        }
    
    def initialize(self) -> bool:
        """تهيئة المحرك"""
        try:
            # تهيئة نظام المتجهات اللغوية
            self.linguistic_vector_system.initialize()
            
            print(f"🧠⚡ تم إنشاء محرك التحليل الدلالي المتقدم: {self.name}")
            print(f"   🔍 قواعد التحليل: {len(self.analysis_rules)}")
            print(f"   📊 أنماط السياق: {len(self.context_patterns)}")
            print(f"   🔤 نظام المتجهات اللغوية: نشط")
            
            self.is_initialized = True
            return True
        except Exception as e:
            print(f"❌ فشل تهيئة محرك التحليل الدلالي: {e}")
            return False
    
    def _initialize_analysis_rules(self) -> Dict[str, Any]:
        """تهيئة قواعد التحليل"""
        return {
            'sentiment_threshold': 0.6,
            'concept_importance_threshold': 0.5,
            'relationship_strength_threshold': 0.4,
            'context_relevance_threshold': 0.3,
            'similarity_threshold': 0.7
        }
    
    def _initialize_context_patterns(self) -> Dict[str, List[str]]:
        """تهيئة أنماط السياق"""
        return {
            'quranic': ['قال الله', 'في القرآن', 'آية', 'سورة', 'تفسير'],
            'hadith': ['قال الرسول', 'روى', 'حديث', 'سنة', 'رواية'],
            'literary': ['قصيدة', 'شعر', 'أدب', 'رواية', 'قصة'],
            'scientific': ['بحث', 'دراسة', 'تجربة', 'نظرية', 'علم'],
            'daily': ['يومي', 'عادي', 'حياة', 'مجتمع', 'أسرة']
        }
    
    def process(self, input_data: Any) -> Any:
        """معالجة النص للتحليل الدلالي"""
        if isinstance(input_data, str):
            return self.analyze_text(input_data)
        elif isinstance(input_data, dict) and 'text' in input_data:
            analysis_type = input_data.get('analysis_type', AnalysisType.SENTIMENT_ANALYSIS)
            return self.analyze_text(input_data['text'], analysis_type)
        else:
            return None
    
    def analyze_text(self, text: str, analysis_type: AnalysisType = AnalysisType.SENTIMENT_ANALYSIS) -> SemanticAnalysisResult:
        """تحليل النص دلالياً"""
        start_time = datetime.now()
        
        # تنظيف النص
        cleaned_text = self._clean_text(text)
        
        # تحليل المشاعر
        sentiment, sentiment_confidence = self._analyze_sentiment(cleaned_text)
        
        # استخراج المفاهيم
        concepts = self._extract_concepts(cleaned_text)
        
        # تحليل العلاقات
        relationships = self._analyze_relationships(cleaned_text)
        
        # تحليل السياق
        context_info = self._analyze_context(cleaned_text)
        
        # إنشاء المتجه الدلالي
        semantic_vector = self._create_semantic_vector(cleaned_text, concepts)
        
        # حساب الثقة الإجمالية
        overall_confidence = self._calculate_overall_confidence(
            sentiment_confidence, concepts, relationships
        )
        
        # إنشاء النتيجة
        result = SemanticAnalysisResult(
            text=text,
            analysis_type=analysis_type,
            sentiment=sentiment,
            confidence=overall_confidence,
            concepts=[concept.__dict__ for concept in concepts],
            relationships=relationships,
            context_info=context_info,
            semantic_vector=semantic_vector,
            analysis_time=(datetime.now() - start_time).total_seconds()
        )
        
        # حفظ النتيجة
        self.analysis_history.append(result)
        self._update_concept_database(concepts)
        self._update_stats(result)
        
        return result
    
    def _clean_text(self, text: str) -> str:
        """تنظيف النص"""
        # إزالة الرموز غير المرغوبة
        cleaned = re.sub(r'[^\w\s\u0600-\u06FF]', ' ', text)
        # إزالة المسافات الزائدة
        cleaned = re.sub(r'\s+', ' ', cleaned).strip()
        return cleaned
    
    def _analyze_sentiment(self, text: str) -> Tuple[SentimentType, float]:
        """تحليل المشاعر"""
        words = text.split()
        positive_score = 0
        negative_score = 0
        total_words = len(words)
        
        if total_words == 0:
            return SentimentType.NEUTRAL, 0.5
        
        # تحليل الكلمات
        for word in words:
            # كلمات إيجابية
            if word in self.arabic_rules.sentiment_rules['positive_words']:
                positive_score += 1
            # كلمات سلبية
            elif word in self.arabic_rules.sentiment_rules['negative_words']:
                negative_score += 1
            
            # تحقق من المكثفات
            if word in self.arabic_rules.sentiment_rules['intensifiers']:
                # زيادة النتيجة للكلمة السابقة
                if positive_score > negative_score:
                    positive_score += 0.5
                else:
                    negative_score += 0.5
            
            # تحقق من النفي
            if word in self.arabic_rules.sentiment_rules['negators']:
                # عكس النتيجة
                positive_score, negative_score = negative_score, positive_score
        
        # حساب النتيجة النهائية
        if positive_score > negative_score:
            sentiment = SentimentType.POSITIVE
            confidence = positive_score / (positive_score + negative_score + 1)
        elif negative_score > positive_score:
            sentiment = SentimentType.NEGATIVE
            confidence = negative_score / (positive_score + negative_score + 1)
        else:
            sentiment = SentimentType.NEUTRAL
            confidence = 0.5
        
        # تحقق من المشاعر المختلطة
        if abs(positive_score - negative_score) < 2 and (positive_score + negative_score) > 2:
            sentiment = SentimentType.MIXED
            confidence = 0.6
        
        return sentiment, confidence
    
    def _extract_concepts(self, text: str) -> List[ExtractedConcept]:
        """استخراج المفاهيم"""
        concepts = []
        words = text.split()
        
        # البحث في أنماط المفاهيم
        for category, concept_words in self.arabic_rules.concept_patterns.items():
            for word in words:
                if word in concept_words:
                    # حساب الأهمية
                    importance = self._calculate_concept_importance(word, text, category)
                    
                    if importance >= self.analysis_rules['concept_importance_threshold']:
                        concept = ExtractedConcept(
                            concept=word,
                            concept_type=self._map_category_to_type(category),
                            importance=importance,
                            context=category,
                            related_words=self._find_related_words(word, words)
                        )
                        concepts.append(concept)
        
        return concepts
    
    def _analyze_relationships(self, text: str) -> List[Dict[str, Any]]:
        """تحليل العلاقات"""
        relationships = []
        
        # البحث في أنماط العلاقات
        for rel_type, patterns in self.arabic_rules.relationship_patterns.items():
            for pattern in patterns:
                if pattern in text:
                    # استخراج الكلمات المرتبطة
                    before, after = text.split(pattern, 1)
                    before_words = before.split()[-3:] if before else []
                    after_words = after.split()[:3] if after else []
                    
                    relationship = {
                        'type': rel_type,
                        'pattern': pattern,
                        'before_context': ' '.join(before_words),
                        'after_context': ' '.join(after_words),
                        'strength': self._calculate_relationship_strength(pattern, text)
                    }
                    relationships.append(relationship)
        
        return relationships
    
    def _analyze_context(self, text: str) -> Dict[str, Any]:
        """تحليل السياق"""
        context_info = {
            'detected_contexts': [],
            'primary_context': 'general',
            'context_confidence': 0.0,
            'text_length': len(text),
            'word_count': len(text.split())
        }
        
        # كشف السياق
        context_scores = {}
        for context_type, patterns in self.context_patterns.items():
            score = 0
            for pattern in patterns:
                if pattern in text:
                    score += 1
            
            if score > 0:
                context_scores[context_type] = score / len(patterns)
                context_info['detected_contexts'].append({
                    'type': context_type,
                    'confidence': context_scores[context_type]
                })
        
        # تحديد السياق الأساسي
        if context_scores:
            primary_context = max(context_scores, key=context_scores.get)
            context_info['primary_context'] = primary_context
            context_info['context_confidence'] = context_scores[primary_context]
        
        return context_info
    
    def _create_semantic_vector(self, text: str, concepts: List[ExtractedConcept]) -> np.ndarray:
        """إنشاء المتجه الدلالي"""
        # إنشاء متجهات للكلمات الرئيسية
        words = text.split()[:10]  # أول 10 كلمات
        word_vectors = []
        
        for word in words:
            vector = self.linguistic_vector_system.create_word_vector(word)
            word_vectors.append(vector.vector)
        
        if word_vectors:
            # متوسط المتجهات
            semantic_vector = np.mean(word_vectors, axis=0)
            
            # إضافة وزن المفاهيم
            for concept in concepts:
                concept_weight = concept.importance * 0.1
                semantic_vector += concept_weight
            
            return semantic_vector
        else:
            return np.zeros(100)  # متجه فارغ
    
    def _calculate_concept_importance(self, word: str, text: str, category: str) -> float:
        """حساب أهمية المفهوم"""
        # تكرار الكلمة
        frequency = text.count(word) / len(text.split())
        
        # أهمية الفئة
        category_weights = {
            'religious': 1.0,
            'family': 0.8,
            'nature': 0.6,
            'time': 0.5,
            'place': 0.7
        }
        category_weight = category_weights.get(category, 0.5)
        
        # موقع الكلمة (الكلمات في البداية أهم)
        words = text.split()
        if word in words:
            position_weight = 1.0 - (words.index(word) / len(words)) * 0.5
        else:
            position_weight = 0.5
        
        return (frequency + category_weight + position_weight) / 3
    
    def _map_category_to_type(self, category: str) -> ConceptType:
        """تحويل الفئة إلى نوع المفهوم"""
        mapping = {
            'religious': ConceptType.ABSTRACT,
            'family': ConceptType.ENTITY,
            'nature': ConceptType.ENTITY,
            'time': ConceptType.ATTRIBUTE,
            'place': ConceptType.ENTITY
        }
        return mapping.get(category, ConceptType.ENTITY)
    
    def _find_related_words(self, word: str, words: List[str]) -> List[str]:
        """البحث عن الكلمات المرتبطة"""
        related = []
        word_index = words.index(word) if word in words else -1
        
        if word_index >= 0:
            # الكلمات المجاورة
            start = max(0, word_index - 2)
            end = min(len(words), word_index + 3)
            related = words[start:end]
            related.remove(word)  # إزالة الكلمة نفسها
        
        return related[:3]  # أول 3 كلمات مرتبطة
    
    def _calculate_relationship_strength(self, pattern: str, text: str) -> float:
        """حساب قوة العلاقة"""
        # تكرار النمط
        frequency = text.count(pattern)
        
        # طول النمط (الأنماط الأطول أقوى)
        length_factor = len(pattern.split()) / 5.0
        
        # موقع النمط
        position = text.find(pattern) / len(text)
        position_factor = 1.0 - position * 0.3
        
        return min((frequency + length_factor + position_factor) / 3, 1.0)
    
    def _calculate_overall_confidence(self, sentiment_confidence: float, 
                                    concepts: List[ExtractedConcept], 
                                    relationships: List[Dict[str, Any]]) -> float:
        """حساب الثقة الإجمالية"""
        # ثقة المشاعر
        sentiment_weight = sentiment_confidence * 0.4
        
        # ثقة المفاهيم
        if concepts:
            concept_weight = np.mean([c.importance for c in concepts]) * 0.4
        else:
            concept_weight = 0.0
        
        # ثقة العلاقات
        if relationships:
            relationship_weight = np.mean([r['strength'] for r in relationships]) * 0.2
        else:
            relationship_weight = 0.0
        
        return sentiment_weight + concept_weight + relationship_weight
    
    def _update_concept_database(self, concepts: List[ExtractedConcept]):
        """تحديث قاعدة بيانات المفاهيم"""
        for concept in concepts:
            if concept.concept in self.concept_database:
                # تحديث الأهمية
                existing = self.concept_database[concept.concept]
                existing.importance = (existing.importance + concept.importance) / 2
                existing.related_words.extend(concept.related_words)
                existing.related_words = list(set(existing.related_words))  # إزالة التكرار
            else:
                self.concept_database[concept.concept] = concept
    
    def _update_stats(self, result: SemanticAnalysisResult):
        """تحديث الإحصائيات"""
        self.stats['total_analyses'] += 1
        
        if result.analysis_type == AnalysisType.SENTIMENT_ANALYSIS:
            self.stats['sentiment_analyses'] += 1
        elif result.analysis_type == AnalysisType.CONCEPT_EXTRACTION:
            self.stats['concept_extractions'] += 1
        elif result.analysis_type == AnalysisType.RELATIONSHIP_ANALYSIS:
            self.stats['relationship_analyses'] += 1
        
        # تحديث متوسط الثقة
        total_confidence = self.stats['average_confidence'] * (self.stats['total_analyses'] - 1)
        self.stats['average_confidence'] = (total_confidence + result.confidence) / self.stats['total_analyses']
        
        # تحديث وقت المعالجة
        self.stats['processing_time'] += result.analysis_time

# اختبار المحرك
def test_semantic_analysis_engine():
    """اختبار محرك التحليل الدلالي"""
    print("🧪 اختبار محرك التحليل الدلالي المتقدم")
    print("=" * 50)
    
    # إنشاء المحرك
    engine = AdvancedSemanticAnalysisEngine()
    engine.initialize()
    
    # نصوص تجريبية
    test_texts = [
        "الله نور السماوات والأرض",
        "الحب والسلام يجلبان السعادة للناس",
        "الحرب والكراهية تدمر المجتمعات",
        "العلم نور والجهل ظلام"
    ]
    
    print(f"\n🔍 اختبار التحليل الدلالي:")
    for i, text in enumerate(test_texts, 1):
        print(f"\n📝 النص {i}: {text}")
        
        result = engine.analyze_text(text)
        
        print(f"   🎭 المشاعر: {result.sentiment.value}")
        print(f"   🎯 الثقة: {result.confidence:.3f}")
        print(f"   💡 المفاهيم: {len(result.concepts)}")
        print(f"   🔗 العلاقات: {len(result.relationships)}")
        print(f"   📊 السياق: {result.context_info['primary_context']}")
        print(f"   ⏱️ وقت التحليل: {result.analysis_time:.3f}s")
    
    # عرض الإحصائيات
    print(f"\n📈 إحصائيات المحرك:")
    print(f"   📊 إجمالي التحليلات: {engine.stats['total_analyses']}")
    print(f"   🎭 تحليلات المشاعر: {engine.stats['sentiment_analyses']}")
    print(f"   🎯 متوسط الثقة: {engine.stats['average_confidence']:.3f}")
    print(f"   💡 قاعدة المفاهيم: {len(engine.concept_database)} مفهوم")
    print(f"   ⏱️ إجمالي وقت المعالجة: {engine.stats['processing_time']:.3f}s")
    
    print(f"\n✅ انتهى اختبار محرك التحليل الدلالي!")
    return engine

if __name__ == "__main__":
    test_semantic_analysis_engine()
