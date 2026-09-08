
from datetime import date 
""" datatime é uma biblioteca importada para
 adicionar a data em que o ususario foi cadastrado de forma altomatica"""

def model_lead(name, company, email, stage):
    return {
        "name": name,
        "company": company,
        "emai": email,
        "stage": stage,
        "created": date.today().isoformat()
    }