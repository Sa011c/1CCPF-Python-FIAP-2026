

from pathlib import Path
import json

DATA_DIR = Path(__file__).resolve().parent/"data"
print(DATA_DIR)

"""DATA_DIR = Path(__file__).resolve().parent/"data"
print(DATA_DIR), usado para acessar o caminho até a pasta"""

DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "leads.json"

#CRUD
#CREATE -  creat_lead()
#READ _read_leads()
#UPDATE
#DELET

def read_leads():
    if not DB_PATH.exists():
        return []

    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JESONecodeError:
        #se corromper, começar vazio
        return []

def create_lead(lead_dict):
    leads = read_leads() #lista de lead
    leads.append(lead_dict)

    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")