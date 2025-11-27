#!/usr/bin/env python3
"""
مثال على التكامل بين Bayan وقاعدة بيانات PostgreSQL
Example of integrating Bayan with PostgreSQL database

هذا السكريبت يوضح كيفية:
1. الاتصال بقاعدة بيانات PostgreSQL
2. تحميل الشبكات السببية من قاعدة البيانات
3. تحويل البيانات إلى حقائق Bayan
4. تنفيذ الاستعلامات المنطقية

This script demonstrates how to:
1. Connect to PostgreSQL database
2. Load causal networks from database
3. Convert data to Bayan facts
4. Execute logical queries
"""

import psycopg2
import json
from typing import List, Dict, Any

class BayanDatabaseIntegration:
    """فئة للتكامل بين Bayan وقاعدة البيانات"""
    
    def __init__(self, db_config: Dict[str, str]):
        """
        تهيئة الاتصال بقاعدة البيانات
        
        Args:
            db_config: معلومات الاتصال بقاعدة البيانات
        """
        self.conn = psycopg2.connect(**db_config)
        self.cursor = self.conn.cursor()
        self.facts = []
        
    def load_symptoms(self) -> List[str]:
        """تحميل الأعراض من قاعدة البيانات"""
        query = "SELECT id, name, type, severity FROM symptoms"
        self.cursor.execute(query)
        
        facts = []
        for row in self.cursor.fetchall():
            fact = f'fact: symptom("{row[0]}", "{row[1]}", "{row[2]}", "{row[3]}").'
            facts.append(fact)
            
        return facts
    
    def load_diseases(self) -> List[str]:
        """تحميل الأمراض من قاعدة البيانات"""
        query = "SELECT id, name, severity, category FROM diseases"
        self.cursor.execute(query)
        
        facts = []
        for row in self.cursor.fetchall():
            fact = f'fact: disease("{row[0]}", "{row[1]}", "{row[2]}", "{row[3]}").'
            facts.append(fact)
            
        return facts
    
    def load_causal_network(self, min_probability: float = 50.0) -> List[str]:
        """
        تحميل الشبكة السببية من قاعدة البيانات
        
        Args:
            min_probability: الحد الأدنى للاحتمالية (افتراضي 50%)
        """
        query = """
            SELECT disease_id, symptom_id, probability, onset_days, duration_days
            FROM disease_symptom_relations
            WHERE probability >= %s
            ORDER BY probability DESC
        """
        self.cursor.execute(query, (min_probability,))
        
        facts = []
        for row in self.cursor.fetchall():
            fact = f'fact: disease_causes_symptom("{row[0]}", "{row[1]}", {row[2]}, {row[3]}, {row[4]}).'
            facts.append(fact)
            
        return facts
    
    def load_treatments(self) -> List[str]:
        """تحميل العلاجات من قاعدة البيانات"""
        query = "SELECT disease_id, treatment, duration_days, effectiveness FROM treatments"
        self.cursor.execute(query)
        
        facts = []
        for row in self.cursor.fetchall():
            fact = f'fact: treatment_for_disease("{row[0]}", "{row[1]}", {row[2]}, {row[3]}).'
            facts.append(fact)
            
        return facts
    
    def load_patient_data(self, patient_id: str) -> List[str]:
        """تحميل بيانات مريض معين"""
        # معلومات المريض
        query = "SELECT id, name, age, gender FROM patients WHERE id = %s"
        self.cursor.execute(query, (patient_id,))
        patient = self.cursor.fetchone()
        
        facts = []
        if patient:
            facts.append(f'fact: patient("{patient[0]}", "{patient[1]}", {patient[2]}, "{patient[3]}").')
            
            # أعراض المريض
            query = """
                SELECT symptom_id 
                FROM patient_symptoms 
                WHERE patient_id = %s
            """
            self.cursor.execute(query, (patient_id,))
            symptoms = [row[0] for row in self.cursor.fetchall()]
            
            if symptoms:
                symptoms_str = '", "'.join(symptoms)
                facts.append(f'fact: patient_symptoms("{patient_id}", ["{symptoms_str}"]).')
        
        return facts
    
    def get_diagnosis_from_db(self, patient_id: str) -> List[Dict[str, Any]]:
        """الحصول على تشخيص محتمل من قاعدة البيانات مباشرة"""
        query = """
            SELECT 
                d.id as disease_id,
                d.name as disease_name,
                d.severity,
                AVG(dsr.probability) as avg_probability,
                COUNT(dsr.symptom_id) as matching_symptoms
            FROM patients p
            JOIN patient_symptoms ps ON p.id = ps.patient_id
            JOIN disease_symptom_relations dsr ON ps.symptom_id = dsr.symptom_id
            JOIN diseases d ON dsr.disease_id = d.id
            WHERE p.id = %s
            GROUP BY d.id, d.name, d.severity
            ORDER BY avg_probability DESC
        """
        self.cursor.execute(query, (patient_id,))
        
        results = []
        for row in self.cursor.fetchall():
            results.append({
                'disease_id': row[0],
                'disease_name': row[1],
                'severity': row[2],
                'confidence': float(row[3]),
                'matching_symptoms': row[4]
            })
        
        return results
    
    def export_to_bayan_file(self, output_file: str):
        """تصدير جميع البيانات إلى ملف Bayan"""
        all_facts = []
        
        # تحميل جميع البيانات
        all_facts.extend(self.load_symptoms())
        all_facts.extend(self.load_diseases())
        all_facts.extend(self.load_causal_network())
        all_facts.extend(self.load_treatments())
        
        # كتابة إلى ملف
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("#!/usr/bin/env bayan\n")
            f.write("# تم التوليد تلقائياً من قاعدة البيانات\n")
            f.write("# Auto-generated from database\n\n")
            
            f.write("# ============================================================================\n")
            f.write("# الأعراض - Symptoms\n")
            f.write("# ============================================================================\n\n")
            for fact in self.load_symptoms():
                f.write(fact + "\n")
            
            f.write("\n# ============================================================================\n")
            f.write("# الأمراض - Diseases\n")
            f.write("# ============================================================================\n\n")
            for fact in self.load_diseases():
                f.write(fact + "\n")
            
            f.write("\n# ============================================================================\n")
            f.write("# الشبكة السببية - Causal Network\n")
            f.write("# ============================================================================\n\n")
            for fact in self.load_causal_network():
                f.write(fact + "\n")
            
            f.write("\n# ============================================================================\n")
            f.write("# العلاجات - Treatments\n")
            f.write("# ============================================================================\n\n")
            for fact in self.load_treatments():
                f.write(fact + "\n")
    
    def close(self):
        """إغلاق الاتصال بقاعدة البيانات"""
        self.cursor.close()
        self.conn.close()


def main():
    """الدالة الرئيسية"""
    
    # معلومات الاتصال بقاعدة البيانات
    db_config = {
        'host': 'localhost',
        'database': 'medical_kb',
        'user': 'postgres',
        'password': 'your_password'
    }
    
    # إنشاء كائن التكامل
    integration = BayanDatabaseIntegration(db_config)
    
    print("🔗 الاتصال بقاعدة البيانات...")
    print()
    
    # تحميل الأعراض
    print("📋 تحميل الأعراض...")
    symptoms = integration.load_symptoms()
    print(f"   تم تحميل {len(symptoms)} عَرَض")
    print()
    
    # تحميل الأمراض
    print("🦠 تحميل الأمراض...")
    diseases = integration.load_diseases()
    print(f"   تم تحميل {len(diseases)} مرض")
    print()
    
    # تحميل الشبكة السببية
    print("🔗 تحميل الشبكة السببية...")
    causal_network = integration.load_causal_network(min_probability=70.0)
    print(f"   تم تحميل {len(causal_network)} علاقة سببية")
    print()
    
    # تحميل العلاجات
    print("💊 تحميل العلاجات...")
    treatments = integration.load_treatments()
    print(f"   تم تحميل {len(treatments)} علاج")
    print()
    
    # تحميل بيانات مريض
    print("👤 تحميل بيانات المريض P001...")
    patient_data = integration.load_patient_data("P001")
    for fact in patient_data:
        print(f"   {fact}")
    print()
    
    # الحصول على تشخيص
    print("🔍 التشخيص المحتمل للمريض P001:")
    diagnosis = integration.get_diagnosis_from_db("P001")
    for d in diagnosis:
        print(f"   - {d['disease_name']}: {d['confidence']:.1f}% ثقة ({d['matching_symptoms']} أعراض متطابقة)")
    print()
    
    # تصدير إلى ملف Bayan
    print("💾 تصدير البيانات إلى ملف Bayan...")
    integration.export_to_bayan_file("generated_medical_kb.by")
    print("   ✅ تم التصدير إلى: generated_medical_kb.by")
    print()
    
    # إغلاق الاتصال
    integration.close()
    print("✅ تم بنجاح!")


if __name__ == "__main__":
    main()
