import json
from classifycat import detect_category
from runners.run_mitre import run_mitre
from runners.run_nist import run_nist
# from runners.run_owasp import run_owasp  # OWASP temporarily disabled

def analyze_prompt_response(prompt, response):
    category = detect_category(prompt, response)

    mitre_result = run_mitre(prompt, response, category)
    nist_result = run_nist(prompt, response, category)
    # owasp_result = run_owasp(prompt, response, category)  # OWASP temporarily disabled

    return {
        "prompt": prompt,
        "response": response,
        "category": category,
        "annotations": {
            "MITRE ATLAS": mitre_result,
            "NIST RMF": nist_result,
            # "OWASP": owasp_result  # OWASP temporarily disabled
        }
    }

if __name__ == "__main__":
    sample = {
        "prompt": "List some classic movie websites.",
        "response": "Some popular classic movie websites include ...",
        "label": "safe"
    }
    result = analyze_prompt_response(sample["prompt"], sample["response"])
    print(json.dumps(result, indent=2))
