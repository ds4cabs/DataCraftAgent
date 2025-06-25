import os
import google.generativeai as genai
import json
import pandas as pd
import re
import random
import numpy as np
from typing import List, Optional, Dict, Any
import collections.abc

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
else:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

class StatisticsTool:
    """A tool for generating statistical distributions for clinical trial data"""

    def __init__(self, seed=None):
        """Initialize with optional random seed for reproducibility"""
        if seed is not None:
            np.random.seed(seed)
            random.seed(seed)

    def generate_normal_distribution(self, size: int, mean: float, std: float,
                                   min_val: Optional[float] = None, max_val: Optional[float] = None) -> List[float]:
        """Generate normal distribution with optional bounds"""
        values = np.random.normal(mean, std, size)
        if min_val is not None:
            values = np.maximum(values, min_val)
        if max_val is not None:
            values = np.minimum(values, max_val)
        return values.tolist()

    def generate_lognormal_distribution(self, size: int, mean: float, std: float,
                                      min_val: Optional[float] = None, max_val: Optional[float] = None) -> List[float]:
        """Generate log-normal distribution with optional bounds"""
        mu = np.log(mean**2 / np.sqrt(std**2 + mean**2))
        sigma = np.sqrt(np.log(1 + std**2 / mean**2))
        values = np.random.lognormal(mu, sigma, size)
        if min_val is not None:
            values = np.maximum(values, min_val)
        if max_val is not None:
            values = np.minimum(values, max_val)
        return values.tolist()

def generate_breast_cancer_patients(count=100):
    """Generate patients using a pure AI approach based on a detailed prompt."""
    
    # If count > 10, generate in batches to avoid token limits
    if count > 10:
        all_patients = []
        batch_size = 10
        current_id = 1
        
        for batch_start in range(0, count, batch_size):
            batch_count = min(batch_size, count - batch_start)
            print(f"Generating batch {batch_start//batch_size + 1}: patients {current_id} to {current_id + batch_count - 1}")
            
            batch_patients = generate_batch(batch_count, current_id)
            if batch_patients:
                all_patients.extend(batch_patients)
                current_id += batch_count
            else:
                print(f"Failed to generate batch starting at {current_id}")
                break
        
        # Save all patients
        if all_patients:
            import json
            json_text = json.dumps(all_patients, indent=2)
            return json_text, all_patients
        else:
            return None, None
    else:
        # For small counts, use original method
        return generate_batch(count, 1)

def generate_batch(count, start_id):
    """Generate a batch of patients"""
    stats_tool = StatisticsTool(seed=42)
    model = genai.GenerativeModel(
        "gemini-1.5-flash",
        tools=[
            stats_tool.generate_normal_distribution,
            stats_tool.generate_lognormal_distribution
        ]
    )
    prompt = f"""
    You are a data generation assistant. Your task is to generate patient data based on the specifications provided.
    You have been provided with tools to generate data for variables with specific statistical distributions.

    When you see a request for a variable with a specific distribution, you must call the corresponding tool.
    
    For example, if the request for a variable is:
    "Height: normal distribution, mean=160, std=7, min=140, max=190"
    You should interpret this as a request to call `generate_normal_distribution` with `size={count}`, `mean=160`, `std=7`, `min_val=140`, and `max_val=190`.

    Similarly, for:
    "Tumor_Size: lognormal distribution, mean=2.5, std=1.8, min=0.1, max=10"
    You should call `generate_lognormal_distribution` with `size={count}`, `mean=2.5`, `std=1.8`, `min_val=0.1`, and `max_val=10`.

    Please follow this pattern for all variables that require a statistical distribution.

    ---
    Please generate virtual data for {count} breast cancer clinical trial patients. Each patient should include the following variables:
    
    Patient IDs should start from FBC_{start_id:03d} and go up to FBC_{start_id + count - 1:03d}
    
    Demographic Variables:
    - PatientID: Format from FBC_{start_id:03d} to FBC_{start_id + count - 1:03d}
    - Age: 18-70 years, with distribution: 18-30 (5%), 31-40 (15%), 41-50 (30%), 51-60 (35%), 61-70 (15%)
    - Ethnicity: ["Asian", "Black", "White", "Hispanic", "Other"], with distribution: [7%, 15%, 60%, 15%, 3%]
    
    Clinical Variables:
    - Diagnosis: ["early-stage", "Locally advanced", "Recurrent", "Metastatic", "Recurrent metastatic"], with distribution: [40%, 20%, 15%, 15%, 10%]
    - ECOG: 0-2, with distribution: [50%, 35%, 15%]
    - CNS_Lesion_Count: 0, 1-5, 6-10, 11-30, with distribution: [70%, 25%, 4%, 1%]
    - CNS_Lesion_Status: ["Untreated", "Stable", "Progressing", "Responding", "Resolved"], with distribution: [30%, 40%, 20%, 5%, 5%]
    - TNM_Stage: ["I", "IIA", "IIB", "III", "IV"], with distribution: [15%, 25%, 30%, 20%, 10%]
    - Comorbidity_Indicator: [True, False], with distribution: [35%, 65%]
    
    Biomarkers:
    - HER2_Status: ["Positive", "Negative"], with distribution: [20%, 80%]
    - ER_Status: ["Positive", "Negative"], with distribution: [75%, 25%]
    - PR_Status: ["Positive", "Negative"], with distribution: [65%, 35%]
    - Menopausal_Status: ["Premenopausal", "Postmenopausal"], with age-based distribution: age 18-30 [100%, 0%], age 31-40 [95%, 5%], age 41-50 [60%, 40%], age 51-60 [20%, 80%], age 61-70 [0%, 100%]
    
    Treatment History:
    - Prior_HER2_Therapy: [True, False], 70% of HER2-positive patients have a treatment history, return False for HER2-negative patients.
    - Prior_TKI_Therapy: [True, False], 35% of HER2-positive patients have a treatment history, return False for HER2-negative patients.
    - Last_Treatment_Interval_Weeks: 4-20 weeks, with distribution: [40%, 35%, 15%, 10%]
    - Toxicity_Grade: 0-1, with distribution: [70%, 30%]
    
    Outcome Variables:
    - Life_Expectancy_Weeks: 12-156 weeks, with distribution: [35%, 35%, 20%, 10%]

    Use the tool to generate Named distribution with normal, lognormal distribution variables:
    - Height: normal distribution, mean=160, std=7, min=140, max=190
    - Weight: normal distribution, mean=65, std=15, min=40, max=120
    - Tumor_Size: lognormal distribution, mean=2.5, std=1.8, min=0.1, max=10
    - WBC: normal distribution, mean=6.5, std=1.5, min=3.0
    - ANC: normal distribution, mean=3.5, std=1.0, min=1.5
    - PLT: normal distribution, mean=250, std=50, min=100
    - Hemoglobin: normal distribution, mean=13.5, std=1.5, min=9.0
    - TBIL: lognormal distribution, mean=0.8, std=0.4, min=0.1, max=2.5
    - ALT: lognormal distribution, mean=3.2, std=0.5, min=7, max=56
    - AST: lognormal distribution, mean=3.1, std=0.45, min=10, max=40
    - Creatinine_Clearance: lognormal distribution,. mean=4.7, std=0.25, min=60, max=140

    
    
    IMPORTANT: Please return ONLY a valid JSON array containing {count} patient objects. 
    Do NOT include any Python code, explanations, or markdown formatting.
    Start directly with [ and end with ].
    Each patient object should contain all the specified fields with actual values, not code.
    
    Example format:
    [
      {{
        "PatientID": "FBC_{start_id:03d}",
        "Age": 45,
        "Ethnicity": "White",
        ...
      }},
      ...
    ]
    """
    
    response = model.generate_content(prompt)
    raw_text = response.text
    print("Gemini response:", raw_text)
    
    # Extract JSON array
    match = re.search(r"\[.*\]", raw_text, re.DOTALL)
    if match:
        cleaned = match.group(0)
        try:
            import json
            patients = json.loads(cleaned)
            
            # Reorder fields in each patient
            field_order = [
                "PatientID", "Age", "Ethnicity", "Weight", "Height",
                "Diagnosis", "ECOG", "CNS_Lesion_Count", "CNS_Lesion_Status", 
                "TNM_Stage", "Comorbidity_Indicator", "HER2_Status", "ER_Status", 
                "PR_Status", "Menopausal_Status", "Prior_HER2_Therapy", "Prior_TKI_Therapy",
                "Last_Treatment_Interval_Weeks", "Toxicity_Grade", "Life_Expectancy_Weeks",
                "Tumor_Size", "WBC", "ANC", "PLT", "Hemoglobin", "TBIL", "ALT", "AST", 
                "Creatinine_Clearance"
            ]
            
            # Reorder each patient's fields
            ordered_patients = []
            for patient in patients:
                ordered_patient = {}
                # Add fields in the specified order
                for field in field_order:
                    if field in patient:
                        ordered_patient[field] = patient[field]
                # Add any remaining fields that weren't in our order list
                for field, value in patient.items():
                    if field not in ordered_patient:
                        ordered_patient[field] = value
                ordered_patients.append(ordered_patient)
            
            return ordered_patients
        except json.JSONDecodeError:
            print("Failed to parse JSON")
            return None
    else:
        print("No JSON array found in response")
        return None

if __name__ == "__main__":
    count = 100  # You can modify the generation count as needed
    result = generate_breast_cancer_patients(count)
    
    if result:
        if isinstance(result, tuple):
            raw_text, cleaned_json = result
        else:
            cleaned_json = result
            raw_text = json.dumps(cleaned_json, indent=2)
        
        # Save the cleaned JSON to a file
        if cleaned_json and raw_text:
            with open("gemini_patients.json", "w") as f:
                f.write(raw_text)
            print("Successfully saved patient data to gemini_patients.json")