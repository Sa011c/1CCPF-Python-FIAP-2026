from model import model_lead
import repo

def add_lead():
    name = input("Nome: ")
    email = input("E-mail: ")
    company = input("Empresa: ")
    stage = input("Estágio de vendas: ")

    if not name or not email or "@" not in email:
        print("Nome e/ou e-mail válido são obrigatórios")
        return


    print(name, email, company, stage)

    """Precisar chamar model para modelar os dados, 
    depois de modelado..."""
    print(model_lead(name, company, email, stage))
    repo.create_lead(model_lead(name, company, email, stage))


def list_leds():
    leads = repo.read_leads()

    if not leads:
        print("nenhum lead ainda")
        return

    print("\n# | Nome     |Empresa     |E-mail")
    for i, lead in enumerate(leads):
        print(f"{i:02d}| {lead["name"]:<20} | {lead["company"]:<17} | {lead["email"]:<20}")


def main(): 
    while True:
        print("\nMini CRM - 1ª aula - (adicionar/lista)")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[0] Sair do programa")

        opt = input("escolha uma opção:").strip()
        if opt == "1":
            add_lead()
        elif opt == "2":
            print("Listar leads")
        elif opt == "0":
            print("Até mais")
            break
        else:
            print("Opção inválida")
if __name__ == "__main__":
    main()