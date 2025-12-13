#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📊 مراقب نمو النظام - نظام بصيرة الثوري
==========================================

هذا السكريبت يراقب نمو النظام المعرفي ويُنتج تقارير مفصلة
عن حالة المعرفة والتقدم نحو الاستقلالية.

الاستخدام:
    python3 monitor_growth.py

المطور: باسل يحيى عبدالله
"""

from revolutionary_knowledge_system import RevolutionaryKnowledgeSystem
import sqlite3
from datetime import datetime, timedelta
import json
import os

class SystemGrowthMonitor:
    """مراقب نمو النظام المعرفي"""
    
    def __init__(self):
        """تهيئة المراقب"""
        self.system = RevolutionaryKnowledgeSystem()
        self.db_path = 'databases/revolutionary_knowledge_system.db'
        self.reports_dir = 'reports'
        self._ensure_reports_directory()
    
    def _ensure_reports_directory(self):
        """التأكد من وجود مجلد التقارير"""
        if not os.path.exists(self.reports_dir):
            os.makedirs(self.reports_dir)
    
    def get_basic_statistics(self):
        """الحصول على الإحصائيات الأساسية"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # إجمالي المعرفة
            cursor.execute("SELECT COUNT(*) FROM unified_knowledge")
            total_knowledge = cursor.fetchone()[0]
            
            # توزيع المصادر
            cursor.execute("SELECT source_type, COUNT(*) FROM unified_knowledge GROUP BY source_type")
            sources_stats = dict(cursor.fetchall())
            
            # توزيع الفئات
            cursor.execute("SELECT category, COUNT(*) FROM unified_knowledge GROUP BY category")
            categories_stats = dict(cursor.fetchall())
            
            # متوسط النظريات الثورية
            cursor.execute("""
                SELECT 
                    AVG(zero_duality_score), 
                    AVG(perpendicularity_factor),
                    AVG(confidence_score)
                FROM unified_knowledge
            """)
            avg_scores = cursor.fetchone()
            
            # أحدث إضافات
            cursor.execute("""
                SELECT content, source_type, created_at 
                FROM unified_knowledge 
                ORDER BY rowid DESC 
                LIMIT 5
            """)
            recent_additions = cursor.fetchall()
            
            conn.close()
            
            return {
                'total_knowledge': total_knowledge,
                'sources_stats': sources_stats,
                'categories_stats': categories_stats,
                'avg_zero_duality': avg_scores[0] or 0,
                'avg_perpendicularity': avg_scores[1] or 0,
                'avg_confidence': avg_scores[2] or 0,
                'recent_additions': recent_additions
            }
            
        except Exception as e:
            print(f"❌ خطأ في الحصول على الإحصائيات: {e}")
            return None
    
    def calculate_independence_level(self, stats):
        """حساب مستوى الاستقلالية"""
        if not stats or stats['total_knowledge'] == 0:
            return 0
        
        external_count = sum(
            count for source, count in stats['sources_stats'].items() 
            if source != 'internal'
        )
        
        return (external_count / stats['total_knowledge']) * 100
    
    def assess_quality_metrics(self, stats):
        """تقييم مقاييس الجودة"""
        if not stats:
            return {}
        
        # تقييم ثنائية الصفر
        zero_duality_rating = "ممتاز" if stats['avg_zero_duality'] > 0.7 else \
                             "جيد" if stats['avg_zero_duality'] > 0.5 else \
                             "متوسط" if stats['avg_zero_duality'] > 0.3 else "ضعيف"
        
        # تقييم العمودية
        perpendicularity_rating = "ممتاز" if stats['avg_perpendicularity'] > 0.7 else \
                                  "جيد" if stats['avg_perpendicularity'] > 0.5 else \
                                  "متوسط" if stats['avg_perpendicularity'] > 0.3 else "ضعيف"
        
        # تقييم الثقة
        confidence_rating = "ممتاز" if stats['avg_confidence'] > 0.8 else \
                           "جيد" if stats['avg_confidence'] > 0.6 else \
                           "متوسط" if stats['avg_confidence'] > 0.4 else "ضعيف"
        
        return {
            'zero_duality_rating': zero_duality_rating,
            'perpendicularity_rating': perpendicularity_rating,
            'confidence_rating': confidence_rating
        }
    
    def generate_growth_recommendations(self, stats, independence_level):
        """إنتاج توصيات النمو"""
        recommendations = []
        
        if stats['total_knowledge'] < 100:
            recommendations.append("🎯 ركز على إضافة المزيد من المعرفة الأساسية (الهدف: 100 عنصر)")
        elif stats['total_knowledge'] < 500:
            recommendations.append("📈 وسع المجالات المعرفية (الهدف: 500 عنصر)")
        elif stats['total_knowledge'] < 2000:
            recommendations.append("🚀 اعمل على التخصص والعمق (الهدف: 2000 عنصر)")
        else:
            recommendations.append("🎉 ممتاز! ركز على الجودة والاستقلالية")
        
        if independence_level < 20:
            recommendations.append("🔴 أضف المزيد من المصادر الخارجية لزيادة التنوع")
        elif independence_level < 50:
            recommendations.append("🟡 استمر في التوازن بين المصادر الداخلية والخارجية")
        else:
            recommendations.append("🟢 ممتاز! مستوى استقلالية عالي")
        
        # توصيات حسب الفئات
        if len(stats['categories_stats']) < 5:
            recommendations.append("📚 أضف فئات معرفية جديدة لزيادة التنوع")
        
        # توصيات حسب الجودة
        if stats['avg_confidence'] < 0.5:
            recommendations.append("⚡ حسن جودة المعرفة المستخرجة")
        
        return recommendations
    
    def print_detailed_report(self):
        """طباعة تقرير مفصل"""
        print("📊 تقرير نمو النظام المعرفي الشامل")
        print("=" * 60)
        print(f"📅 التاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # الحصول على الإحصائيات
        stats = self.get_basic_statistics()
        if not stats:
            print("❌ فشل في الحصول على الإحصائيات")
            return
        
        # الإحصائيات الأساسية
        print(f"📚 إجمالي المعرفة: {stats['total_knowledge']:,}")
        
        # مستوى الاستقلالية
        independence_level = self.calculate_independence_level(stats)
        print(f"🎯 مستوى الاستقلالية: {independence_level:.1f}%")
        
        # تقييم المستوى
        if independence_level < 20:
            status = "🔴 مبتدئ"
        elif independence_level < 50:
            status = "🟡 متوسط"
        elif independence_level < 80:
            status = "🟢 متقدم"
        else:
            status = "🏆 خبير"
        print(f"📊 التقييم: {status}")
        
        print("\n🔗 توزيع المصادر:")
        for source, count in stats['sources_stats'].items():
            percentage = (count / stats['total_knowledge']) * 100
            print(f"  📖 {source}: {count:,} ({percentage:.1f}%)")
        
        print("\n📂 توزيع الفئات:")
        sorted_categories = sorted(stats['categories_stats'].items(), key=lambda x: x[1], reverse=True)
        for category, count in sorted_categories:
            percentage = (count / stats['total_knowledge']) * 100
            print(f"  🏷️ {category}: {count:,} ({percentage:.1f}%)")
        
        # النظريات الثورية
        print("\n🧬 النظريات الثورية:")
        quality_metrics = self.assess_quality_metrics(stats)
        print(f"  🔄 ثنائية الصفر: {stats['avg_zero_duality']:.3f} ({quality_metrics['zero_duality_rating']})")
        print(f"  ⚖️ العمودية: {stats['avg_perpendicularity']:.3f} ({quality_metrics['perpendicularity_rating']})")
        print(f"  🎯 الثقة: {stats['avg_confidence']:.3f} ({quality_metrics['confidence_rating']})")
        
        # أحدث الإضافات
        if stats['recent_additions']:
            print("\n📝 أحدث الإضافات:")
            for i, (content, source, created_at) in enumerate(stats['recent_additions'], 1):
                preview = content[:80] + "..." if len(content) > 80 else content
                print(f"  {i}. {preview}")
                print(f"     المصدر: {source}")
        
        # التوصيات
        recommendations = self.generate_growth_recommendations(stats, independence_level)
        if recommendations:
            print("\n💡 التوصيات:")
            for rec in recommendations:
                print(f"  {rec}")
        
        # خطة النمو
        print("\n🗺️ خطة النمو المقترحة:")
        current = stats['total_knowledge']
        if current < 100:
            next_target = 100
            timeframe = "1-2 أسبوع"
        elif current < 500:
            next_target = 500
            timeframe = "1-2 شهر"
        elif current < 2000:
            next_target = 2000
            timeframe = "2-4 شهر"
        else:
            next_target = current + 1000
            timeframe = "حسب الحاجة"
        
        remaining = max(0, next_target - current)
        print(f"  🎯 الهدف التالي: {next_target:,} عنصر")
        print(f"  📈 المطلوب إضافة: {remaining:,} عنصر")
        print(f"  ⏰ الإطار الزمني المقترح: {timeframe}")
        
        if remaining > 0:
            daily_target = max(1, remaining // 30)  # توزيع على شهر
            print(f"  📅 الهدف اليومي المقترح: {daily_target} عنصر")
    
    def save_report_to_file(self):
        """حفظ التقرير في ملف"""
        stats = self.get_basic_statistics()
        if not stats:
            return False
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{self.reports_dir}/growth_report_{timestamp}.json"
        
        # إعداد البيانات للحفظ
        report_data = {
            'timestamp': datetime.now().isoformat(),
            'statistics': stats,
            'independence_level': self.calculate_independence_level(stats),
            'quality_metrics': self.assess_quality_metrics(stats),
            'recommendations': self.generate_growth_recommendations(stats, self.calculate_independence_level(stats))
        }
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(report_data, f, ensure_ascii=False, indent=2)
            
            print(f"\n💾 تم حفظ التقرير في: {filename}")
            return True
            
        except Exception as e:
            print(f"❌ خطأ في حفظ التقرير: {e}")
            return False

def main():
    """الدالة الرئيسية"""
    print("📊 مرحباً بك في مراقب نمو النظام!")
    print()
    
    monitor = SystemGrowthMonitor()
    
    # طباعة التقرير
    monitor.print_detailed_report()
    
    # حفظ التقرير
    print("\n" + "="*60)
    save_response = input("هل تريد حفظ التقرير في ملف؟ (y/n): ").lower().strip()
    if save_response in ['y', 'yes', 'نعم', 'ن']:
        monitor.save_report_to_file()
    
    print("\n🎉 انتهى التقرير!")

if __name__ == "__main__":
    main()
