tickets = [
    {"id": 1, "tipo": "bug", "prioridade": "alta"},
    {"id": 2, "tipo": "duvida", "prioridade": "baixa"},
    {"id": 3, "tipo": "bug", "prioridade": "media"},
    {"id": 4, "tipo": "urgente", "prioridade": "alta"},
    {"id": 5, "tipo": "duvida", "prioridade": "media"}
]

urgentes = []
relatorio = {}

# separar tickets urgentes
for ticket in tickets:
    if ticket["prioridade"] == "alta":
        urgentes.append(ticket)

# contar tipos de ticket
for ticket in tickets:
    tipo = ticket["tipo"]
    if tipo in relatorio:
        relatorio[tipo] += 1
    else:
        relatorio[tipo] = 1

print("=== TICKETS URGENTES ===")
for t in urgentes:
    print(t)

print("\n=== RELATÓRIO POR TIPO ===")
for tipo, quantidade in relatorio.items():
    print(f"{tipo}: {quantidade}")

# gerar CSV
import csv

with open("relatorio.csv", "w", newline="") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(["Tipo", "Quantidade"])

    for tipo, quantidade in relatorio.items():
        writer.writerow([tipo, quantidade])

print("\nRelatório CSV gerado!")
