#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📝 مصنف النصوص الثوري
Revolutionary Text Classifier

مبني على نظام بصيرة الثوري - بدون معالجة لغة طبيعية تقليدية
Built on Basera Revolutionary System - No traditional NLP

المطور: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداعه الشخصي
"""

import numpy as np
import json
import re
from datetime import datetime
from typing import Dict, List, Tuple, Any
from collections import defaultdict
import math

class RevolutionaryTextClassifier:
    """
    📝 مصنف النصوص الثوري
    يستخدم النظريات الثلاث الثورية لتصنيف النصوص وتحليل المشاعر
    """
    
    def __init__(self, classifier_name: str = "RevolutionaryTextClassifier"):
        """تهيئة المصنف"""
        self.classifier_name = classifier_name
        self.categories = {}
        self.sentiment_patterns = {}
        self.classification_history = []
        
        print(f"📝 تهيئة {self.classifier_name}")
        print("🧬 مصنف نصوص ثوري بدون معالجة لغة تقليدية")
    
    def train_category(self, category_name: str, training_texts: List[str]):
        """
        📚 تدريب فئة جديدة باستخدام النظريات الثورية
        """
        print(f"📚 تدريب فئة: {category_name} بـ {len(training_texts)} نص")
        
        # تطبيق النظريات الثلاث على النصوص التدريبية
        category_profile = self._create_category_profile(training_texts)
        
        # حفظ ملف الفئة
        self.categories[category_name] = {
            "profile": category_profile,
            "training_count": len(training_texts),
            "trained_at": datetime.now().isoformat()
        }
        
        print(f"✅ تم تدريب فئة {category_name} بنجاح")
    
    def classify_text(self, text: str) -> Dict:
        """
        🎯 تصنيف نص باستخدام النظريات الثورية
        """
        print(f"\n🎯 تصنيف النص: '{text[:50]}...'")
        
        if not self.categories:
            return {
                "predicted_category": "unknown",
                "confidence": 0.0,
                "reason": "لا توجد فئات مدربة"
            }
        
        # تحليل النص باستخدام النظريات الثلاث
        text_analysis = self._analyze_text(text)
        
        # حساب التطابق مع كل فئة
        category_scores = {}
        for category_name, category_data in self.categories.items():
            score = self._calculate_category_match(
                text_analysis, category_data["profile"]
            )
            category_scores[category_name] = score
        
        # اختيار أفضل فئة
        best_category = max(category_scores, key=category_scores.get)
        confidence = category_scores[best_category]
        
        # توليد التفسير
        explanation = self._generate_classification_explanation(
            text_analysis, best_category, confidence
        )
        
        # حفظ نتيجة التصنيف
        classification_result = {
            "text": text,
            "predicted_category": best_category,
            "confidence": confidence,
            "all_scores": category_scores,
            "explanation": explanation,
            "classified_at": datetime.now().isoformat()
        }
        
        self.classification_history.append(classification_result)
        
        return classification_result
    
    def analyze_sentiment(self, text: str) -> Dict:
        """
        😊 تحليل المشاعر باستخدام ثنائية الصفر
        """
        print(f"\n😊 تحليل مشاعر النص: '{text[:50]}...'")
        
        # تطبيق ثنائية الصفر على المشاعر
        sentiment_duality = self.apply_zero_duality_to_sentiment(text)
        
        # تحديد المشاعر الإجمالية
        overall_sentiment = self._determine_overall_sentiment(sentiment_duality)
        
        return {
            "text": text,
            "sentiment_analysis": sentiment_duality,
            "overall_sentiment": overall_sentiment,
            "analyzed_at": datetime.now().isoformat()
        }
    
    def apply_zero_duality_to_sentiment(self, text: str) -> Dict:
        """
        🔄 تطبيق نظرية ثنائية الصفر على المشاعر
        تحليل التوازن بين المشاعر الإيجابية والسلبية
        """
        words = self._extract_words(text)
        
        positive_words = []
        negative_words = []
        neutral_words = []
        
        for word in words:
            sentiment_energy = self._calculate_sentiment_energy(word)
            
            if sentiment_energy > 0.6:
                positive_words.append(word)
            elif sentiment_energy < 0.4:
                negative_words.append(word)
            else:
                neutral_words.append(word)
        
        # حساب التوازن العاطفي
        total_emotional_words = len(positive_words) + len(negative_words)
        if total_emotional_words > 0:
            positivity_ratio = len(positive_words) / total_emotional_words
        else:
            positivity_ratio = 0.5  # محايد
        
        return {
            "positive_words": positive_words,
            "negative_words": negative_words,
            "neutral_words": neutral_words,
            "positivity_ratio": positivity_ratio,
            "emotional_balance": self._interpret_emotional_balance(positivity_ratio)
        }
    
    def _create_category_profile(self, training_texts: List[str]) -> Dict:
        """إنشاء ملف شخصي للفئة"""
        all_analyses = []
        
        for text in training_texts:
            analysis = self._analyze_text(text)
            all_analyses.append(analysis)
        
        # دمج التحليلات لإنشاء ملف الفئة
        category_profile = self._merge_text_analyses(all_analyses)
        
        return category_profile
    
    def _analyze_text(self, text: str) -> Dict:
        """تحليل نص باستخدام النظريات الثلاث"""
        # ثنائية الصفر
        zero_duality = self.apply_zero_duality_to_text(text)
        
        # الأضداد المتعامدة
        perpendicular = self.apply_perpendicular_opposites_to_text(text)
        
        # الخيوط
        filaments = self.apply_filament_theory_to_text(text)
        
        return {
            "zero_duality": zero_duality,
            "perpendicular_opposites": perpendicular,
            "filament_connections": filaments,
            "word_count": len(self._extract_words(text)),
            "character_count": len(text)
        }
    
    def apply_zero_duality_to_text(self, text: str) -> Dict:
        """تطبيق ثنائية الصفر على النص"""
        words = self._extract_words(text)
        
        formal_words = []
        informal_words = []
        
        for word in words:
            formality_score = self._calculate_formality_score(word)
            
            if formality_score > 0.5:
                formal_words.append(word)
            else:
                informal_words.append(word)
        
        # حساب التوازن الأسلوبي
        total_words = len(formal_words) + len(informal_words)
        if total_words > 0:
            formality_ratio = len(formal_words) / total_words
        else:
            formality_ratio = 0.5
        
        return {
            "formal_words": formal_words,
            "informal_words": informal_words,
            "formality_ratio": formality_ratio,
            "style_insight": self._interpret_style(formality_ratio)
        }
    
    def apply_perpendicular_opposites_to_text(self, text: str) -> Dict:
        """تطبيق الأضداد المتعامدة على النص"""
        words = self._extract_words(text)
        
        # البحث عن أزواج الكلمات المتضادة
        opposite_pairs = self._find_word_opposites(words)
        
        # إنشاء أبعاد دلالية
        semantic_dimensions = []
        for pair in opposite_pairs:
            dimension = self._create_word_dimension(pair)
            semantic_dimensions.append(dimension)
        
        return {
            "opposite_pairs": opposite_pairs,
            "semantic_dimensions": semantic_dimensions,
            "conceptual_complexity": len(semantic_dimensions) * 0.1
        }
    
    def apply_filament_theory_to_text(self, text: str) -> Dict:
        """تطبيق نظرية الخيوط على النص"""
        words = self._extract_words(text)
        
        # ربط الكلمات بخيوط دلالية
        word_connections = {}
        for word in words:
            connected_words = self._find_word_connections(word, words)
            word_connections[word] = connected_words
        
        # اكتشاف الموضوعات
        topics = self._discover_topics(word_connections)
        
        return {
            "word_connections": word_connections,
            "discovered_topics": topics,
            "coherence_score": self._calculate_text_coherence(word_connections)
        }
    
    def _extract_words(self, text: str) -> List[str]:
        """استخراج الكلمات من النص"""
        # تنظيف النص
        cleaned_text = re.sub(r'[^\w\s]', ' ', text.lower())
        words = [word for word in cleaned_text.split() if len(word) > 2]
        return words
    
    def _calculate_sentiment_energy(self, word: str) -> float:
        """حساب الطاقة العاطفية للكلمة"""
        # قاموس بسيط للمشاعر
        positive_indicators = ['جميل', 'رائع', 'ممتاز', 'سعيد', 'حب', 'نجح', 'فرح']
        negative_indicators = ['سيء', 'فظيع', 'حزين', 'غضب', 'فشل', 'ألم', 'خوف']
        
        if any(indicator in word for indicator in positive_indicators):
            return 0.8
        elif any(indicator in word for indicator in negative_indicators):
            return 0.2
        else:
            # حساب بناءً على خصائص الكلمة
            word_hash = hash(word) % 100
            return word_hash / 100
    
    def _interpret_emotional_balance(self, positivity_ratio: float) -> str:
        """تفسير التوازن العاطفي"""
        if positivity_ratio > 0.7:
            return "إيجابي جداً"
        elif positivity_ratio > 0.6:
            return "إيجابي"
        elif positivity_ratio > 0.4:
            return "محايد"
        elif positivity_ratio > 0.3:
            return "سلبي"
        else:
            return "سلبي جداً"
    
    def _calculate_formality_score(self, word: str) -> float:
        """حساب درجة الرسمية للكلمة"""
        # مؤشرات الرسمية
        formal_indicators = ['يرجى', 'نتشرف', 'نحيطكم', 'المحترم', 'التقدير']
        informal_indicators = ['هاي', 'مرحبا', 'شلونك', 'كيفك', 'يلا']
        
        if any(indicator in word for indicator in formal_indicators):
            return 0.9
        elif any(indicator in word for indicator in informal_indicators):
            return 0.1
        else:
            # حساب بناءً على طول الكلمة (الكلمات الطويلة أكثر رسمية)
            length_score = min(len(word) / 10, 1.0)
            return length_score
    
    def _interpret_style(self, formality_ratio: float) -> str:
        """تفسير الأسلوب"""
        if formality_ratio > 0.7:
            return "رسمي جداً"
        elif formality_ratio > 0.6:
            return "رسمي"
        elif formality_ratio > 0.4:
            return "متوسط"
        elif formality_ratio > 0.3:
            return "غير رسمي"
        else:
            return "عامي"
    
    def _find_word_opposites(self, words: List[str]) -> List[Tuple]:
        """البحث عن الكلمات المتضادة"""
        opposites = []
        
        # قاموس بسيط للأضداد
        opposite_pairs = [
            ('جميل', 'قبيح'), ('كبير', 'صغير'), ('سريع', 'بطيء'),
            ('ساخن', 'بارد'), ('نور', 'ظلام'), ('فرح', 'حزن')
        ]
        
        for word1 in words:
            for word2 in words:
                if word1 != word2:
                    for pair in opposite_pairs:
                        if (word1 in pair[0] and word2 in pair[1]) or \
                           (word1 in pair[1] and word2 in pair[0]):
                            opposites.append((word1, word2))
        
        return opposites
    
    def _create_word_dimension(self, word_pair: Tuple) -> Dict:
        """إنشاء بُعد من زوج كلمات"""
        word1, word2 = word_pair
        
        dimension = {
            "axis_name": f"{word1}_vs_{word2}",
            "semantic_distance": self._calculate_semantic_distance(word1, word2),
            "conceptual_bridge": self._find_conceptual_bridge(word1, word2)
        }
        
        return dimension
    
    def _calculate_semantic_distance(self, word1: str, word2: str) -> float:
        """حساب المسافة الدلالية"""
        # حساب بسيط بناءً على الاختلاف في الخصائص
        len_diff = abs(len(word1) - len(word2)) / max(len(word1), len(word2))
        hash_diff = abs(hash(word1) - hash(word2)) % 100 / 100
        
        return (len_diff + hash_diff) / 2
    
    def _find_conceptual_bridge(self, word1: str, word2: str) -> str:
        """إيجاد الجسر المفاهيمي"""
        # مفهوم بسيط للجسر
        combined_hash = (hash(word1) + hash(word2)) % 3
        
        bridges = ["تدرج", "تكامل", "توازن"]
        return bridges[combined_hash]
    
    def _find_word_connections(self, word: str, all_words: List[str]) -> List[str]:
        """البحث عن اتصالات الكلمة"""
        connections = []
        
        for other_word in all_words:
            if other_word != word:
                connection_strength = self._calculate_word_connection(word, other_word)
                
                if connection_strength > 0.6:
                    connections.append(other_word)
        
        return connections
    
    def _calculate_word_connection(self, word1: str, word2: str) -> float:
        """حساب قوة الاتصال بين كلمتين"""
        # التشابه في الطول
        length_similarity = 1.0 - abs(len(word1) - len(word2)) / max(len(word1), len(word2))
        
        # التشابه في الأحرف الأولى
        first_char_similarity = 1.0 if word1[0] == word2[0] else 0.0
        
        # قوة الاتصال الإجمالية
        connection_strength = (length_similarity + first_char_similarity) / 2
        
        return connection_strength
    
    def _discover_topics(self, word_connections: Dict) -> List[str]:
        """اكتشاف الموضوعات"""
        topics = []
        
        # البحث عن مجموعات الكلمات المترابطة
        for word, connections in word_connections.items():
            if len(connections) >= 2:
                topic = f"موضوع: {word} ({len(connections)} كلمات مرتبطة)"
                topics.append(topic)
        
        return topics
    
    def _calculate_text_coherence(self, word_connections: Dict) -> float:
        """حساب تماسك النص"""
        total_connections = sum(len(connections) for connections in word_connections.values())
        total_words = len(word_connections)
        
        if total_words == 0:
            return 0.0
        
        coherence = total_connections / total_words
        return min(coherence, 1.0)
    
    def _merge_text_analyses(self, analyses: List[Dict]) -> Dict:
        """دمج تحليلات النصوص لإنشاء ملف الفئة"""
        if not analyses:
            return {}
        
        # حساب المتوسطات
        avg_formality = np.mean([a["zero_duality"]["formality_ratio"] for a in analyses])
        avg_complexity = np.mean([a["perpendicular_opposites"]["conceptual_complexity"] for a in analyses])
        avg_coherence = np.mean([a["filament_connections"]["coherence_score"] for a in analyses])
        avg_word_count = np.mean([a["word_count"] for a in analyses])
        
        return {
            "average_formality": avg_formality,
            "average_complexity": avg_complexity,
            "average_coherence": avg_coherence,
            "average_word_count": avg_word_count,
            "profile_created_at": datetime.now().isoformat()
        }
    
    def _calculate_category_match(self, text_analysis: Dict, category_profile: Dict) -> float:
        """حساب التطابق مع فئة"""
        # مقارنة الخصائص
        formality_match = 1.0 - abs(
            text_analysis["zero_duality"]["formality_ratio"] - 
            category_profile["average_formality"]
        )
        
        complexity_match = 1.0 - abs(
            text_analysis["perpendicular_opposites"]["conceptual_complexity"] - 
            category_profile["average_complexity"]
        )
        
        coherence_match = 1.0 - abs(
            text_analysis["filament_connections"]["coherence_score"] - 
            category_profile["average_coherence"]
        )
        
        # النتيجة الإجمالية
        overall_match = (formality_match + complexity_match + coherence_match) / 3
        
        return overall_match
    
    def _generate_classification_explanation(self, text_analysis: Dict, category: str, confidence: float) -> str:
        """توليد تفسير للتصنيف"""
        style = text_analysis["zero_duality"]["style_insight"]
        complexity = text_analysis["perpendicular_opposites"]["conceptual_complexity"]
        
        explanation = f"تم تصنيف النص كـ '{category}' بناءً على الأسلوب ({style})"
        
        if complexity > 0.5:
            explanation += " والتعقيد المفاهيمي العالي"
        
        return explanation
    
    def _determine_overall_sentiment(self, sentiment_duality: Dict) -> str:
        """تحديد المشاعر الإجمالية"""
        return sentiment_duality["emotional_balance"]

def main():
    """مثال على الاستخدام"""
    print("📝 مصنف النصوص الثوري - مثال تطبيقي")
    print("=" * 50)
    
    # إنشاء المصنف
    classifier = RevolutionaryTextClassifier("NewsClassifier")
    
    # نصوص تدريبية للفئات
    sports_texts = [
        "الفريق فاز في المباراة بنتيجة رائعة",
        "اللاعب سجل هدف جميل في الدقيقة الأخيرة",
        "البطولة كانت مثيرة ومليئة بالمفاجآت"
    ]
    
    technology_texts = [
        "الذكاء الاصطناعي يطور تقنيات جديدة",
        "الشركة أطلقت منتج تقني متقدم",
        "البرمجة تتطور بسرعة كبيرة"
    ]
    
    # تدريب الفئات
    classifier.train_category("رياضة", sports_texts)
    classifier.train_category("تكنولوجيا", technology_texts)
    
    # نصوص للاختبار
    test_texts = [
        "الفريق الجديد يستخدم تقنيات متطورة في التدريب",
        "المباراة كانت مثيرة جداً والجمهور استمتع",
        "الشركة طورت تطبيق جديد للهواتف الذكية",
        "هذا المنتج سيء جداً ولا أنصح بشرائه"
    ]
    
    # اختبار التصنيف
    for i, text in enumerate(test_texts, 1):
        # تصنيف النص
        classification = classifier.classify_text(text)
        
        # تحليل المشاعر
        sentiment = classifier.analyze_sentiment(text)
        
        print(f"\n📝 النص {i}: '{text}'")
        print(f"   🎯 الفئة: {classification['predicted_category']}")
        print(f"   📊 الثقة: {classification['confidence']:.3f}")
        print(f"   💡 السبب: {classification['explanation']}")
        print(f"   😊 المشاعر: {sentiment['overall_sentiment']}")
        print(f"   📈 الإيجابية: {sentiment['sentiment_analysis']['positivity_ratio']:.3f}")
    
    print("\n✅ تم إنجاز التصنيف وتحليل المشاعر بنجاح!")

if __name__ == "__main__":
    main()
