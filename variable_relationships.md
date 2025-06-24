# Breast Cancer Dataset - Variable Relationships & Constraints

## Core Logical Relationships

### 1. DEMOGRAPHIC RELATIONSHIPS
- **Age ↔ Menopausal_Status**
  - Age < 40: Pre-menopausal (90%), Peri-menopausal (10%)
  - Age 40-55: Peri-menopausal (60%), Post-menopausal (40%)
  - Age > 55: Post-menopausal (95%), Peri-menopausal (5%)

- **Age ↔ Height/Weight**
  - Height: 140-180 cm (realistic adult range)
  - Weight: 40-120 kg (BMI considerations)
  - BMI = Weight(kg) / (Height(m))² should be 16-45

### 2. CLINICAL DIAGNOSIS RELATIONSHIPS
- **Tumor_Size ↔ TNM_Stage**
  - T1: ≤ 2 cm
  - T2: 2-5 cm  
  - T3: > 5 cm
  - T4: Any size with chest wall/skin involvement

- **CNS_Lesion_Count ↔ CNS_Lesion_Status**
  - Count = 0 → Status = "Absent"
  - Count > 0 → Status = "Present"

- **ECOG ↔ Life_Expectancy_Weeks**
  - ECOG 0-1: Life_Expectancy 52-156 weeks
  - ECOG 2: Life_Expectancy 26-78 weeks
  - ECOG 3-4: Life_Expectancy 12-52 weeks

### 3. BIOMARKER RELATIONSHIPS
- **ER_Status ↔ PR_Status**
  - ER+ patients are more likely to be PR+ (70% correlation)
  - ER- patients are more likely to be PR- (80% correlation)

- **HER2_Status ↔ Prior_HER2_Therapy**
  - HER2+ patients more likely to have prior HER2 therapy
  - HER2- patients rarely have HER2 therapy

### 4. LABORATORY VALUE RELATIONSHIPS
- **WBC ↔ ANC**
  - ANC typically 50-70% of WBC
  - ANC = WBC × (Neutrophil % / 100)

- **Toxicity_Grade ↔ Lab Values**
  - Grade 3-4 toxicity often correlates with low ANC, PLT, Hemoglobin
  - Grade 1-2 toxicity: mild lab abnormalities

### 5. TREATMENT RELATIONSHIPS
- **Prior_HER2_Therapy ↔ Last_Treatment_Interval_Weeks**
  - If Prior_HER2_Therapy = "Yes": Interval 1-52 weeks
  - If Prior_HER2_Therapy = "No": Interval 0-4 weeks (new diagnosis)

- **Prior_TKI_Therapy ↔ Last_Treatment_Interval_Weeks**
  - Similar logic to HER2 therapy

## Value Ranges & Constraints

### Demographics
- **PatientID**: Unique sequential or UUID
- **Age**: 25-85 years (breast cancer age range)
- **Height**: 140-180 cm
- **Weight**: 40-120 kg
- **Ethnicity**: ["Caucasian", "African American", "Hispanic", "Asian", "Other"]

### Clinical Variables
- **Diagnosis**: ["Invasive Ductal Carcinoma", "Invasive Lobular Carcinoma", "Ductal Carcinoma In Situ", "Triple Negative", "HER2+"]
- **ECOG**: 0-4 (performance status)
- **CNS_Lesion_Count**: 0-10
- **CNS_Lesion_Status**: ["Present", "Absent"]
- **Tumor_Size**: 0.1-15.0 cm
- **TNM_Stage**: ["I", "IIA", "IIB", "IIIA", "IIIB", "IIIC", "IV"]

### Biomarkers
- **HER2_Status**: ["Positive", "Negative", "Equivocal"]
- **ER_Status**: ["Positive", "Negative"]
- **PR_Status**: ["Positive", "Negative"]

### Patient Characteristics
- **Menopausal_Status**: ["Pre-menopausal", "Peri-menopausal", "Post-menopausal"]
- **Comorbidity_Indicator**: ["None", "Diabetes", "Hypertension", "Cardiovascular", "Multiple"]

### Treatment History
- **Prior_HER2_Therapy**: ["Yes", "No"]
- **Prior_TKI_Therapy**: ["Yes", "No"]
- **Last_Treatment_Interval_Weeks**: 0-156 weeks
- **Toxicity_Grade**: 0-4

### Lab Values (Realistic Ranges)
- **WBC**: 2.0-20.0 K/μL
- **ANC**: 1.0-15.0 K/μL
- **PLT**: 50-500 K/μL
- **Hemoglobin**: 8.0-16.0 g/dL
- **TBIL**: 0.1-2.0 mg/dL
- **ALT**: 5-100 U/L
- **AST**: 5-80 U/L
- **Creatinine_Clearance**: 30-150 mL/min

### Outcomes
- **Life_Expectancy_Weeks**: 12-156 weeks

## Data Generation Strategy

### Phase 1: Core Variables (Independent)
1. PatientID, Age, Height, Weight, Ethnicity
2. Diagnosis, Tumor_Size, CNS_Lesion_Count

### Phase 2: Dependent Variables
1. Menopausal_Status (based on Age)
2. TNM_Stage (based on Tumor_Size + other factors)
3. Biomarker status (with correlations)
4. Lab values (with realistic correlations)

### Phase 3: Treatment & Outcomes
1. Treatment history (based on biomarkers)
2. Toxicity and outcomes (based on treatment + lab values)
3. Life expectancy (based on stage + performance status) 