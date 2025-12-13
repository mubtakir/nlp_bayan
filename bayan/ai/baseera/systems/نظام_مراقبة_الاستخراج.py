#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
نظام مراقبة الاستخراج - Extraction Monitoring System
نظام بصيرة الثوري المتكامل

المطور: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله

نظام متقدم لمراقبة والتحكم في عملية استخراج المعرفة من Ollama
"""

import json
import time
import os
import threading
import psutil
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import matplotlib.pyplot as plt
import pandas as pd

class ExtractionMonitor:
    """
    مراقب الاستخراج - يراقب ويتحكم في عملية استخراج المعرفة
    """
    
    def __init__(self):
        self.monitor_name = "نظام مراقبة الاستخراج"
        self.creator = "باسل يحيى عبدالله"
        self.version = "v1.0 - مراقبة ذكية"
        
        # إعدادات المراقبة
        self.monitoring_settings = {
            "update_interval": 5,  # ثواني
            "log_file": "سجل_الاستخراج.log",
            "stats_file": "إحصائيات_الاستخراج.json",
            "alerts_enabled": True,
            "auto_backup": True,
            "backup_interval": 300  # 5 دقائق
        }
        
        # حالة النظام
        self.system_status = {
            "is_running": False,
            "start_time": None,
            "current_batch": 0,
            "total_batches": 0,
            "questions_processed": 0,
            "successful_extractions": 0,
            "failed_extractions": 0,
            "current_speed": 0,  # أسئلة في الدقيقة
            "estimated_completion": None,
            "system_resources": {}
        }
        
        # تحذيرات النظام
        self.alerts = {
            "high_failure_rate": False,
            "low_speed": False,
            "high_memory_usage": False,
            "disk_space_low": False,
            "ollama_disconnected": False
        }
        
        # إحصائيات مفصلة
        self.detailed_stats = {
            "hourly_progress": [],
            "category_distribution": {},
            "quality_trends": [],
            "speed_history": [],
            "error_log": []
        }
        
        print(f"🔍 تم تهيئة {self.monitor_name}")
    
    def start_monitoring(self, extraction_process):
        """بدء مراقبة عملية الاستخراج"""
        
        print("🔍 بدء مراقبة عملية الاستخراج...")
        
        self.system_status["is_running"] = True
        self.system_status["start_time"] = datetime.now()
        
        # بدء خيط المراقبة
        monitor_thread = threading.Thread(target=self._monitor_loop)
        monitor_thread.daemon = True
        monitor_thread.start()
        
        # بدء خيط النسخ الاحتياطي
        if self.monitoring_settings["auto_backup"]:
            backup_thread = threading.Thread(target=self._backup_loop)
            backup_thread.daemon = True
            backup_thread.start()
        
        print("✅ تم بدء المراقبة")
    
    def _monitor_loop(self):
        """حلقة المراقبة الرئيسية"""
        
        while self.system_status["is_running"]:
            try:
                # تحديث الإحصائيات
                self._update_system_stats()
                
                # فحص التحذيرات
                self._check_alerts()
                
                # تسجيل الحالة
                self._log_status()
                
                # حفظ الإحصائيات
                self._save_stats()
                
                # انتظار
                time.sleep(self.monitoring_settings["update_interval"])
                
            except Exception as e:
                self._log_error(f"خطأ في المراقبة: {e}")
    
    def _update_system_stats(self):
        """تحديث إحصائيات النظام"""
        
        # موارد النظام
        self.system_status["system_resources"] = {
            "cpu_percent": psutil.cpu_percent(),
            "memory_percent": psutil.virtual_memory().percent,
            "disk_percent": psutil.disk_usage('/').percent,
            "network_io": psutil.net_io_counters()._asdict()
        }
        
        # حساب السرعة
        if self.system_status["start_time"]:
            elapsed = datetime.now() - self.system_status["start_time"]
            if elapsed.total_seconds() > 0:
                self.system_status["current_speed"] = (
                    self.system_status["questions_processed"] / 
                    (elapsed.total_seconds() / 60)
                )
        
        # تقدير وقت الإنجاز
        if (self.system_status["current_speed"] > 0 and 
            self.system_status["total_batches"] > 0):
            
            remaining_questions = (
                self.system_status["total_batches"] - 
                self.system_status["current_batch"]
            ) * 10  # افتراض 10 أسئلة لكل دفعة
            
            remaining_minutes = remaining_questions / self.system_status["current_speed"]
            self.system_status["estimated_completion"] = (
                datetime.now() + timedelta(minutes=remaining_minutes)
            ).isoformat()
    
    def _check_alerts(self):
        """فحص التحذيرات"""
        
        # معدل الفشل العالي
        total_attempts = (self.system_status["successful_extractions"] + 
                         self.system_status["failed_extractions"])
        
        if total_attempts > 10:
            failure_rate = self.system_status["failed_extractions"] / total_attempts
            self.alerts["high_failure_rate"] = failure_rate > 0.3
        
        # السرعة المنخفضة
        self.alerts["low_speed"] = self.system_status["current_speed"] < 1
        
        # استخدام الذاكرة العالي
        memory_percent = self.system_status["system_resources"].get("memory_percent", 0)
        self.alerts["high_memory_usage"] = memory_percent > 85
        
        # مساحة القرص المنخفضة
        disk_percent = self.system_status["system_resources"].get("disk_percent", 0)
        self.alerts["disk_space_low"] = disk_percent > 90
        
        # إرسال التحذيرات
        if self.monitoring_settings["alerts_enabled"]:
            self._send_alerts()
    
    def _send_alerts(self):
        """إرسال التحذيرات"""
        
        active_alerts = [alert for alert, active in self.alerts.items() if active]
        
        if active_alerts:
            alert_message = f"⚠️ تحذيرات النظام: {', '.join(active_alerts)}"
            print(alert_message)
            self._log_error(alert_message)
    
    def _log_status(self):
        """تسجيل حالة النظام"""
        
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "status": self.system_status.copy(),
            "alerts": self.alerts.copy()
        }
        
        # كتابة في ملف السجل
        with open(self.monitoring_settings["log_file"], 'a', encoding='utf-8') as f:
            f.write(f"{json.dumps(log_entry, ensure_ascii=False)}\n")
    
    def _log_error(self, error_message: str):
        """تسجيل الأخطاء"""
        
        error_entry = {
            "timestamp": datetime.now().isoformat(),
            "error": error_message,
            "system_status": self.system_status.copy()
        }
        
        self.detailed_stats["error_log"].append(error_entry)
        
        # كتابة في ملف الأخطاء
        with open("أخطاء_الاستخراج.log", 'a', encoding='utf-8') as f:
            f.write(f"{json.dumps(error_entry, ensure_ascii=False)}\n")
    
    def _save_stats(self):
        """حفظ الإحصائيات"""
        
        stats_data = {
            "last_update": datetime.now().isoformat(),
            "system_status": self.system_status,
            "alerts": self.alerts,
            "detailed_stats": self.detailed_stats
        }
        
        with open(self.monitoring_settings["stats_file"], 'w', encoding='utf-8') as f:
            json.dump(stats_data, f, ensure_ascii=False, indent=2)
    
    def _backup_loop(self):
        """حلقة النسخ الاحتياطي"""
        
        while self.system_status["is_running"]:
            try:
                time.sleep(self.monitoring_settings["backup_interval"])
                self._create_backup()
            except Exception as e:
                self._log_error(f"خطأ في النسخ الاحتياطي: {e}")
    
    def _create_backup(self):
        """إنشاء نسخة احتياطية"""
        
        backup_dir = f"نسخ_احتياطية/{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        os.makedirs(backup_dir, exist_ok=True)
        
        # نسخ قواعد البيانات
        database_files = [
            "قاعدة_المعرفة_الرياضية.json",
            "قاعدة_المعرفة_العلمية.json",
            "قاعدة_المعرفة_الفلسفية.json",
            "قاعدة_المعرفة_الإبداعية.json",
            "قاعدة_المعرفة_التقنية.json",
            "قاعدة_المعرفة_اللغوية.json",
            "قاعدة_المعرفة_التاريخية.json",
            "قاعدة_المعرفة_العامة.json"
        ]
        
        for db_file in database_files:
            if os.path.exists(db_file):
                import shutil
                shutil.copy2(db_file, backup_dir)
        
        print(f"💾 تم إنشاء نسخة احتياطية: {backup_dir}")
    
    def generate_progress_report(self) -> Dict:
        """توليد تقرير التقدم"""
        
        if not self.system_status["start_time"]:
            return {"error": "لم تبدأ العملية بعد"}
        
        elapsed = datetime.now() - self.system_status["start_time"]
        
        report = {
            "تاريخ_التقرير": datetime.now().isoformat(),
            "مدة_التشغيل": str(elapsed),
            "الحالة_الحالية": "يعمل" if self.system_status["is_running"] else "متوقف",
            "التقدم": {
                "الدفعة_الحالية": self.system_status["current_batch"],
                "إجمالي_الدفعات": self.system_status["total_batches"],
                "الأسئلة_المعالجة": self.system_status["questions_processed"],
                "الاستخراج_الناجح": self.system_status["successful_extractions"],
                "الاستخراج_الفاشل": self.system_status["failed_extractions"]
            },
            "الأداء": {
                "السرعة_الحالية": f"{self.system_status['current_speed']:.2f} سؤال/دقيقة",
                "وقت_الإنجاز_المتوقع": self.system_status["estimated_completion"]
            },
            "موارد_النظام": self.system_status["system_resources"],
            "التحذيرات_النشطة": [alert for alert, active in self.alerts.items() if active]
        }
        
        return report
    
    def create_visual_dashboard(self):
        """إنشاء لوحة تحكم بصرية"""
        
        try:
            import matplotlib.pyplot as plt
            import matplotlib.dates as mdates
            from matplotlib.animation import FuncAnimation
            
            # إعداد الرسم البياني
            fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
            fig.suptitle('لوحة تحكم استخراج المعرفة - نظام بصيرة الثوري', fontsize=16)
            
            # الرسم البياني 1: التقدم العام
            ax1.set_title('التقدم العام')
            ax1.set_xlabel('الوقت')
            ax1.set_ylabel('عدد الأسئلة')
            
            # الرسم البياني 2: معدل النجاح
            ax2.set_title('معدل النجاح')
            ax2.set_xlabel('الوقت')
            ax2.set_ylabel('النسبة المئوية')
            
            # الرسم البياني 3: موارد النظام
            ax3.set_title('موارد النظام')
            ax3.set_xlabel('المورد')
            ax3.set_ylabel('الاستخدام (%)')
            
            # الرسم البياني 4: توزيع الفئات
            ax4.set_title('توزيع فئات المعرفة')
            
            plt.tight_layout()
            plt.savefig('لوحة_تحكم_الاستخراج.png', dpi=300, bbox_inches='tight')
            print("📊 تم إنشاء لوحة التحكم البصرية")
            
        except ImportError:
            print("⚠️ matplotlib غير متوفر - تم تخطي لوحة التحكم البصرية")
    
    def export_detailed_report(self):
        """تصدير تقرير مفصل"""
        
        report = {
            "معلومات_التقرير": {
                "تاريخ_الإنشاء": datetime.now().isoformat(),
                "النظام": self.monitor_name,
                "المطور": self.creator,
                "الإصدار": self.version
            },
            "ملخص_العملية": self.generate_progress_report(),
            "الإحصائيات_المفصلة": self.detailed_stats,
            "سجل_الأخطاء": self.detailed_stats["error_log"][-10:],  # آخر 10 أخطاء
            "توصيات_التحسين": self._generate_recommendations()
        }
        
        # حفظ التقرير
        report_filename = f"تقرير_الاستخراج_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(report_filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        print(f"📄 تم تصدير التقرير المفصل: {report_filename}")
        return report_filename
    
    def _generate_recommendations(self) -> List[str]:
        """توليد توصيات لتحسين الأداء"""
        
        recommendations = []
        
        # توصيات بناءً على معدل الفشل
        total_attempts = (self.system_status["successful_extractions"] + 
                         self.system_status["failed_extractions"])
        
        if total_attempts > 0:
            failure_rate = self.system_status["failed_extractions"] / total_attempts
            
            if failure_rate > 0.2:
                recommendations.append("معدل الفشل مرتفع - تحقق من اتصال Ollama")
            
            if failure_rate > 0.5:
                recommendations.append("معدل الفشل عالي جداً - أعد تشغيل Ollama")
        
        # توصيات بناءً على السرعة
        if self.system_status["current_speed"] < 0.5:
            recommendations.append("السرعة منخفضة - قلل من تأخير الطلبات")
        
        # توصيات بناءً على الموارد
        memory_percent = self.system_status["system_resources"].get("memory_percent", 0)
        if memory_percent > 80:
            recommendations.append("استخدام الذاكرة مرتفع - أغلق التطبيقات الأخرى")
        
        disk_percent = self.system_status["system_resources"].get("disk_percent", 0)
        if disk_percent > 85:
            recommendations.append("مساحة القرص منخفضة - احذف الملفات غير الضرورية")
        
        if not recommendations:
            recommendations.append("الأداء جيد - استمر في العملية")
        
        return recommendations
    
    def stop_monitoring(self):
        """إيقاف المراقبة"""
        
        print("⏹️ إيقاف مراقبة الاستخراج...")
        
        self.system_status["is_running"] = False
        
        # إنشاء تقرير نهائي
        final_report = self.export_detailed_report()
        
        # إنشاء نسخة احتياطية نهائية
        self._create_backup()
        
        print("✅ تم إيقاف المراقبة وحفظ التقرير النهائي")
        return final_report

def main():
    """الدالة الرئيسية لاختبار النظام"""
    
    print("🔍 نظام مراقبة الاستخراج")
    print("👨‍💻 المطور: باسل يحيى عبدالله")
    print("=" * 50)
    
    # إنشاء مراقب
    monitor = ExtractionMonitor()
    
    # محاكاة عملية استخراج
    print("🧪 محاكاة عملية الاستخراج...")
    
    monitor.start_monitoring(None)
    
    # محاكاة بعض الإحصائيات
    monitor.system_status["total_batches"] = 100
    monitor.system_status["current_batch"] = 25
    monitor.system_status["questions_processed"] = 250
    monitor.system_status["successful_extractions"] = 200
    monitor.system_status["failed_extractions"] = 50
    
    # انتظار قليل
    time.sleep(10)
    
    # توليد تقرير
    report = monitor.generate_progress_report()
    print("📊 تقرير التقدم:")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    
    # إيقاف المراقبة
    monitor.stop_monitoring()

if __name__ == "__main__":
    main()
