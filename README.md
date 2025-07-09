# aiXamine Frameworks Mappings

A tool to automatically classify and annotate user prompt/response pairs against major AI risk frameworks:

- **MITRE ATLAS** (Adversarial Tactics, Techniques & Common Knowledge for LLMs)  
- **NIST AI RMF** (Risk Management Framework for AI)  
<!-- - **OWASP LLM Top 10** (Top 10 Risks for LLM‑Driven Applications) -->  
*OWASP support is currently disabled.*

## 🚀 Features

1. **Category Detection**  
   Automatically detect which of 8 high‑level risk categories a prompt/response pair belongs to  
   (e.g. Hallucination, Fairness & Bias, Code Security, etc.)

2. **Framework Mapping**  
   For each pair, generate annotations under:  
   - MITRE ATLAS  
   - NIST AI RMF  

3. **Modular Runners**  
   Separate runner modules (`run_mitre.py`, `run_nist.py`) each load the appropriate schema + system prompt to get structured JSON annotations from your Azure OpenAI instance.

## 📦 Project Structure

```
aiXamine-Frameworks-Mappings/
├── classifycat.py           # detect_category(prompt, response)
├── openai_client.py         # AzureOpenAI client wrapper
├── systemprompts/
│   ├── hallucination_mitre.txt
│   ├── fairness_mitre.txt
│   ├── code_security_mitre.txt
│   └── ...                  # one per high‑level category & framework
├── schemas/
│   ├── mitre_atlas.json
│   ├── nist_ai_rmf_playbook.json
├── runners/
│   ├── run_mitre.py
│   └── run_nist.py
├── main.py                  # glue everything: analyze_prompt_response()
├── requirements.txt
└── README.md
```

## 💿 Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/05nuha/aiXamine-Frameworks-Mappings.git
   cd aiXamine-Frameworks-Mappings
   ```

2. **Create & activate a virtual environment**
   ```bash
   python -m venv .venv
   # macOS/Linux
   source .venv/bin/activate
   # Windows
   .\.venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Azure OpenAI credentials**  
   Create a `.env` file or export environment variables:
   ```
   AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com/
   AZURE_OPENAI_KEY=<your_key>
   AZURE_OPENAI_API_VERSION=2024-12-01-preview
   AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini-aixamine
   ```

## ⚙️ Usage

### Single Pair Analysis

```python
from classifycat import detect_category
from runners.run_mitre import run_mitre
from runners.run_nist import run_nist

def analyze_prompt_response(prompt, response):
    category   = detect_category(prompt, response)
    mitre_ann  = run_mitre(prompt, response, category)
    nist_ann   = run_nist(prompt, response, category)
    return {
        "prompt": prompt,
        "response": response,
        "category": category,
        "annotations": {
          "MITRE ATLAS": mitre_ann,
          "NIST RMF":    nist_ann
        }
    }

if __name__ == "__main__":
    res = analyze_prompt_response(
        "List some classic movie websites.",
        "Some popular classic movie websites include ..."
    )
    print(res)
```

### Bulk Processing

```python
import json
from main import analyze_prompt_response

data = json.load(open("my_dataset.json"))
results = [analyze_prompt_response(item["prompt"], item["response"]) for item in data]

with open("analysis_results.json", "w") as fout:
    json.dump(results, fout, indent=2)
```

## 🛠️ Customization

- **System Prompts:** Edit templates in `systemprompts/`
- **Schemas:** Update JSON files in `schemas/` as frameworks evolve

## 📄 License

MIT © 2025