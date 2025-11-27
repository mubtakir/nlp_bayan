-- ============================================================================
-- قاعدة بيانات طبية للتكامل مع Bayan
-- Medical Database for Bayan Integration
-- ============================================================================
-- PostgreSQL Schema
-- ============================================================================

-- جدول الأعراض
CREATE TABLE symptoms (
    id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    name_en VARCHAR(100),
    type VARCHAR(50) NOT NULL,
    severity VARCHAR(20) CHECK (severity IN ('low', 'medium', 'high', 'critical')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- جدول الأمراض
CREATE TABLE diseases (
    id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    name_en VARCHAR(100),
    severity VARCHAR(20) CHECK (severity IN ('low', 'moderate', 'high', 'critical')),
    category VARCHAR(50),
    contagious BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- جدول الشبكة السببية (العلاقات بين الأمراض والأعراض)
CREATE TABLE disease_symptom_relations (
    id SERIAL PRIMARY KEY,
    disease_id VARCHAR(10) REFERENCES diseases(id) ON DELETE CASCADE,
    symptom_id VARCHAR(10) REFERENCES symptoms(id) ON DELETE CASCADE,
    probability DECIMAL(5,2) CHECK (probability >= 0 AND probability <= 100),
    onset_days INTEGER,
    duration_days INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(disease_id, symptom_id)
);

-- جدول العلاجات
CREATE TABLE treatments (
    id SERIAL PRIMARY KEY,
    disease_id VARCHAR(10) REFERENCES diseases(id) ON DELETE CASCADE,
    treatment TEXT NOT NULL,
    treatment_en TEXT,
    duration_days INTEGER,
    effectiveness DECIMAL(5,2) CHECK (effectiveness >= 0 AND effectiveness <= 100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- جدول المرضى
CREATE TABLE patients (
    id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INTEGER,
    gender VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- جدول أعراض المرضى
CREATE TABLE patient_symptoms (
    id SERIAL PRIMARY KEY,
    patient_id VARCHAR(10) REFERENCES patients(id) ON DELETE CASCADE,
    symptom_id VARCHAR(10) REFERENCES symptoms(id) ON DELETE CASCADE,
    onset_date DATE,
    severity VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(patient_id, symptom_id)
);

-- ============================================================================
-- إدخال البيانات التجريبية
-- Sample Data Insertion
-- ============================================================================

-- إدخال الأعراض
INSERT INTO symptoms (id, name, name_en, type, severity) VALUES
('S001', 'حمى_عالية', 'high_fever', 'temperature', 'high'),
('S002', 'سعال_جاف', 'dry_cough', 'respiratory', 'medium'),
('S003', 'صداع', 'headache', 'neurological', 'low'),
('S004', 'ألم_صدر', 'chest_pain', 'cardiac', 'high'),
('S005', 'ضيق_تنفس', 'shortness_of_breath', 'respiratory', 'critical'),
('S006', 'إرهاق', 'fatigue', 'general', 'low');

-- إدخال الأمراض
INSERT INTO diseases (id, name, name_en, severity, category, contagious) VALUES
('D001', 'كوفيد-19', 'COVID-19', 'critical', 'viral_infection', TRUE),
('D002', 'إنفلونزا', 'Influenza', 'moderate', 'viral_infection', TRUE),
('D003', 'التهاب_رئوي', 'Pneumonia', 'high', 'bacterial_infection', FALSE),
('D004', 'نزلة_برد', 'Common_Cold', 'low', 'viral_infection', TRUE);

-- إدخال الشبكة السببية
INSERT INTO disease_symptom_relations (disease_id, symptom_id, probability, onset_days, duration_days) VALUES
-- كوفيد-19
('D001', 'S001', 85.00, 2, 7),
('D001', 'S002', 90.00, 3, 14),
('D001', 'S005', 80.00, 5, 10),
('D001', 'S006', 95.00, 1, 21),
-- إنفلونزا
('D002', 'S001', 75.00, 1, 5),
('D002', 'S002', 60.00, 2, 7),
('D002', 'S003', 70.00, 1, 5),
('D002', 'S006', 80.00, 1, 7),
-- التهاب رئوي
('D003', 'S001', 80.00, 2, 10),
('D003', 'S004', 85.00, 3, 7),
('D003', 'S005', 90.00, 2, 14),
-- نزلة برد
('D004', 'S002', 50.00, 1, 5),
('D004', 'S003', 60.00, 1, 3),
('D004', 'S006', 70.00, 1, 5);

-- إدخال العلاجات
INSERT INTO treatments (disease_id, treatment, treatment_en, duration_days, effectiveness) VALUES
('D001', 'عزل_منزلي_وأدوية_داعمة', 'Home_isolation_and_supportive_medication', 14, 85.00),
('D002', 'راحة_ومضادات_فيروسات', 'Rest_and_antivirals', 7, 80.00),
('D003', 'مضادات_حيوية_قوية_ومراقبة', 'Strong_antibiotics_and_monitoring', 10, 90.00),
('D004', 'راحة_وسوائل', 'Rest_and_fluids', 5, 95.00);

-- إدخال مرضى تجريبيين
INSERT INTO patients (id, name, age, gender) VALUES
('P001', 'أحمد_محمد', 45, 'male'),
('P002', 'فاطمة_علي', 32, 'female'),
('P003', 'خالد_سعيد', 28, 'male');

-- إدخال أعراض المرضى
INSERT INTO patient_symptoms (patient_id, symptom_id, onset_date, severity) VALUES
('P001', 'S001', '2025-11-25', 'high'),
('P001', 'S002', '2025-11-26', 'medium'),
('P001', 'S005', '2025-11-27', 'high'),
('P002', 'S003', '2025-11-26', 'low'),
('P002', 'S006', '2025-11-26', 'medium'),
('P003', 'S001', '2025-11-27', 'high'),
('P003', 'S004', '2025-11-27', 'critical');

-- ============================================================================
-- استعلامات مفيدة للتكامل مع Bayan
-- Useful Queries for Bayan Integration
-- ============================================================================

-- 1. الحصول على جميع الأعراض
SELECT id, name, type, severity FROM symptoms;

-- 2. الحصول على جميع الأمراض
SELECT id, name, severity, category FROM diseases;

-- 3. الحصول على الشبكة السببية (احتمالية > 70%)
SELECT disease_id, symptom_id, probability 
FROM disease_symptom_relations 
WHERE probability > 70
ORDER BY probability DESC;

-- 4. الحصول على أعراض مريض معين
SELECT p.id, p.name, s.id as symptom_id, s.name as symptom_name
FROM patients p
JOIN patient_symptoms ps ON p.id = ps.patient_id
JOIN symptoms s ON ps.symptom_id = s.id
WHERE p.id = 'P001';

-- 5. تشخيص محتمل لمريض بناءً على أعراضه
SELECT 
    d.id as disease_id,
    d.name as disease_name,
    AVG(dsr.probability) as avg_probability,
    COUNT(dsr.symptom_id) as matching_symptoms
FROM patients p
JOIN patient_symptoms ps ON p.id = ps.patient_id
JOIN disease_symptom_relations dsr ON ps.symptom_id = dsr.symptom_id
JOIN diseases d ON dsr.disease_id = d.id
WHERE p.id = 'P001'
GROUP BY d.id, d.name
ORDER BY avg_probability DESC;

-- 6. الحصول على العلاج الموصى به لمرض
SELECT disease_id, treatment, duration_days, effectiveness
FROM treatments
WHERE disease_id = 'D001';

-- ============================================================================
-- فهارس لتحسين الأداء
-- Indexes for Performance
-- ============================================================================

CREATE INDEX idx_disease_symptom_probability ON disease_symptom_relations(probability);
CREATE INDEX idx_patient_symptoms_patient ON patient_symptoms(patient_id);
CREATE INDEX idx_disease_severity ON diseases(severity);
CREATE INDEX idx_symptom_type ON symptoms(type);

-- ============================================================================
-- Views مفيدة
-- Useful Views
-- ============================================================================

-- عرض للشبكة السببية الكاملة مع الأسماء
CREATE VIEW causal_network_view AS
SELECT 
    d.id as disease_id,
    d.name as disease_name,
    s.id as symptom_id,
    s.name as symptom_name,
    dsr.probability,
    dsr.onset_days,
    dsr.duration_days
FROM disease_symptom_relations dsr
JOIN diseases d ON dsr.disease_id = d.id
JOIN symptoms s ON dsr.symptom_id = s.id
ORDER BY dsr.probability DESC;

-- عرض لحالة المرضى
CREATE VIEW patient_status_view AS
SELECT 
    p.id as patient_id,
    p.name as patient_name,
    p.age,
    COUNT(ps.symptom_id) as symptom_count,
    STRING_AGG(s.name, ', ') as symptoms
FROM patients p
LEFT JOIN patient_symptoms ps ON p.id = ps.patient_id
LEFT JOIN symptoms s ON ps.symptom_id = s.id
GROUP BY p.id, p.name, p.age;

-- ============================================================================
-- ملاحظات
-- Notes
-- ============================================================================

-- للاتصال من Python:
-- pip install psycopg2-binary
-- 
-- import psycopg2
-- conn = psycopg2.connect(
--     host="localhost",
--     database="medical_kb",
--     user="your_username",
--     password="your_password"
-- )

-- للاتصال من Node.js:
-- npm install pg
-- 
-- const { Client } = require('pg')
-- const client = new Client({
--   host: 'localhost',
--   database: 'medical_kb',
--   user: 'your_username',
--   password: 'your_password'
-- })
