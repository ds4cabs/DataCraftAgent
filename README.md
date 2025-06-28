# DataCraft AI Agent - Breast Cancer Dataset Generator

This project is an advanced virtual breast cancer patient data generator powered by Google Gemini LLM. It generates comprehensive clinical datasets with 30 carefully designed variables for research and development purposes.

## Features

- Generate realistic breast cancer patient datasets with 30 clinical variables
- Comprehensive medical data including demographics, diagnosis, biomarkers, and lab values
- Support for various breast cancer subtypes and treatment scenarios
- Advanced data validation and consistency checks
- Visualize and download datasets in CSV format
- Backend built with Flask, using Gemini API for intelligent data generation
- One-click startup scripts with automatic frontend launch

## Dataset Variables

The generator creates datasets with the following 30 variables:

### Patient Information
- **PatientID**: Unique patient identifier
- **Age**: Patient age in years
- **Height**: Patient height in cm
- **Weight**: Patient weight in kg
- **Ethnicity**: Patient ethnic background

### Clinical Diagnosis
- **Diagnosis**: Breast cancer diagnosis type
- **ECOG**: Eastern Cooperative Oncology Group performance status
- **CNS_Lesion_Count**: Number of central nervous system lesions
- **CNS_Lesion_Status**: Status of CNS lesions (present/absent)
- **Tumor_Size**: Primary tumor size in cm
- **TNM_Stage**: Tumor-Node-Metastasis staging

### Biomarker Status
- **HER2_Status**: Human Epidermal Growth Factor Receptor 2 status
- **ER_Status**: Estrogen Receptor status
- **PR_Status**: Progesterone Receptor status

### Patient Characteristics
- **Menopausal_Status**: Menopausal status of the patient
- **Comorbidity_Indicator**: Presence of comorbid conditions

### Treatment History
- **Prior_HER2_Therapy**: Previous HER2-targeted therapy
- **Prior_TKI_Therapy**: Previous Tyrosine Kinase Inhibitor therapy
- **Last_Treatment_Interval_Weeks**: Time since last treatment

### Clinical Outcomes
- **Toxicity_Grade**: Treatment-related toxicity grade
- **Life_Expectancy_Weeks**: Estimated life expectancy

### Laboratory Values
- **WBC**: White Blood Cell count
- **ANC**: Absolute Neutrophil Count
- **PLT**: Platelet count
- **Hemoglobin**: Hemoglobin level
- **TBIL**: Total Bilirubin
- **ALT**: Alanine Aminotransferase
- **AST**: Aspartate Aminotransferase
- **Creatinine_Clearance**: Creatinine clearance rate

## Project Structure

```
DataCraftAgent/
├── app.py                        # Flask backend main program
├── generate_breast_cancer_data.py # Gemini data generation logic
├── frontend/index.html           # Frontend web interface
├── start.sh                      # One-click shell startup script
├── start_app.py                  # One-click Python startup script
├── breast_cancer_dataset.csv     # Generated dataset (CSV)
├── breast_cancer_raw.txt         # Raw Gemini API output
├── sample_dataset.json           # Example dataset
├── ...
```

## Quick Start

1. **Install dependencies** (recommended: use a virtual environment)
   ```bash
   pip3 install flask flask-cors google-generativeai pandas numpy
   ```

2. **Set your Google Gemini API Key**
   ```bash
   export GOOGLE_API_KEY=your_api_key_here
   ```

3. **Start the system**
   ```bash
   ./start.sh
   # or
   python3 start_app.py
   ```

4. **How to use**
   - The frontend page will open automatically in your browser
   - Enter the number of patient records to generate
   - Click "Generate Dataset" to create breast cancer patient data
   - View the results and download as CSV

## API

- `GET /generate_breast_cancer_data?count=100`
  - Parameter: `count` (number of patient records to generate, default 100)
  - Returns: JSON array of breast cancer patient records with all 30 variables

## Data Quality Features

- **Realistic Value Ranges**: All variables are generated within clinically appropriate ranges
- **Logical Consistency**: Related variables maintain medical logic (e.g., age and menopausal status)
- **Missing Data Handling**: Optional realistic missing data patterns
- **Data Validation**: Built-in checks for data integrity and consistency

## Use Cases

- Clinical research and development
- Machine learning model training
- Healthcare analytics testing
- Medical software development
- Educational purposes in oncology

## Contact

For questions, suggestions, or collaboration opportunities, please open an [issue on GitHub](https://github.com/yourusername/DataCraftAgent/issues).

---

**Important Notice**: This tool generates synthetic data for research and development purposes only. The generated data does not represent real patients and should not be used for clinical decision-making or patient care. 
