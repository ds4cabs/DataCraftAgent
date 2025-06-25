# Breast Cancer Dataset - Variable Relationships & Constraints

## Core Logical Relationships

### 1. Conditional variables
- **Age ↔ Menopausal_Status**
  - Age 18-40: 5% Postmenopausal
  - Age 41-50: 40% Postmenopausal
  - Age 51-60: 80% Postmenopausal
  - Age 61-70: 100% Postmenopausal

- **HER_Status ↔ Prior_HER2_Therapy**
  - HER+ patients 70% has Prior_HER2_Therapy
  - HER- patients do not have Prior_HER2_Therapy

- **HER2_Status ↔ Prior_TKI_Therapy**
  - HER2+ patients 30% has Prior_TKI_Therapy
  - HER2- patients rarely have Prior_TKI_Therapy

### 2  ECOG Score	Meaning	and Probability
| ECOG Score | Meaning | Probability |
|------------|---------|-------------|
| 0 | Fully active, no restrictions | 50% |
| 1 | Restricted in strenuous activity | 35% |
| 2 | Ambulatory, capable of self-care | 15% |
| 3+ | Usually excluded from trials | 0% |

### 3. TNM_Stage - The Five Clinical Stages

**Probability Distribution:**
- Stage I: 15%
- Stage IIA: 25%
- Stage IIB: 30%
- Stage III: 20%
- Stage IV: 10%

**Stage I (15%)**
- **Definition:** Early-stage breast cancer
- **Characteristics:** Small tumor (≤2cm), no lymph node involvement, no distant spread
- **Treatment:** Usually surgery + adjuvant therapy
- **Prognosis:** Excellent survival rates

**Stage IIA (25%)**
- **Definition:** Local early-stage cancer
- **Characteristics:** Small tumor with 1-3 lymph nodes OR larger tumor (2-5cm) without nodes
- **Treatment:** Surgery + chemotherapy/radiation
- **Prognosis:** Good survival rates

**Stage IIB (30%)**
- **Definition:** Local advanced cancer
- **Characteristics:** Larger tumor (2-5cm) with lymph nodes OR very large tumor (>5cm) without nodes
- **Treatment:** Neoadjuvant therapy + surgery
- **Prognosis:** Moderate survival rates

**Stage III (20%)**
- **Definition:** Advanced local cancer
- **Characteristics:** Large tumor with extensive lymph node involvement OR chest wall/skin involvement
- **Treatment:** Aggressive neoadjuvant therapy + surgery + radiation
- **Prognosis:** Lower survival rates

**Stage IV (10%)**
- **Definition:** Metastatic cancer
- **Characteristics:** Cancer has spread to distant organs (lungs, liver, bones, brain)
- **Treatment:** Palliative therapy, targeted treatments
- **Prognosis:** Limited survival, focus on quality of life

#### Variable and Phases
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