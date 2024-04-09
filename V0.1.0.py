from tabulate import tabulate
nome=input("Insira o nome do produto:  ")
if any(char.isdigit() for char in nome):
    print("Digite apenas letras!")
else:
    variaveis= True
    while variaveis:
        try:
            ml=float(input("Insira a margem de lucro do produto: "))
            cp=float(input("Insira o custo do produto: "))
            cf=float(input("Insira o custo fixo/adminstrativo do produto: "))
            cv=float(input("Insira a comissão de Vendas   do produto: "))
            iv=float(input("Insira os impostos (sobre venda)  do produto: "))

        except ValueError:
            print("Somente valores NÚMERICOS!")
        else:
            variaveis= False
            ml= ml/100
            cf= cf/100
            cv= cv/100
            iv= iv/100
            pv= float("{:.2f}".format(cp / (1-(cf+cv+iv+ml))))
            pvP= 100
            cpP= float("{:.2f}".format(cp/pv*100))
            cfV= float("{:.2f}".format(cf*pv))
            cvV= float("{:.2f}".format(cv*pv))
            ivV= float("{:.2f}".format(iv*pv))

            dados = [
        [nome, "Valor", " %",],
        ["A. Preço de venda", pv, str(pvP)+"%"],
        ["B. Custo do produto", cp, str(cpP)+"%"],
        ["C. Receita Bruta (A-B)", pv-cp, str(pvP-cpP)+"%"],
        ["D. Custo Fixo/Administrativo", cfV, str(cf*100)+"%"],
        ["E. Comissão de Vendas ", cvV, str(cv*100)+"%" ],
        ["F. Impostos sobre venda", ivV, str(iv*100)+"%"],
        ["G. Outros custos(D+E+F)", cfV+cvV+ivV, str((cf+iv+cv)*100)+"%"],
        ["H. Rentabilidade (C-G)", (pv-cp)-(cfV+cvV+ivV), str((pvP-cpP)-(cf+iv+cv)*100)+"%" ]
            ]
    tabela = tabulate(dados, headers="firstrow", tablefmt="fancy_grid")
    print (tabela)

    print("\n\n\n\n")

    dados = [
    ["Classificação", "Lucro"],
    ["Alto", ">20%"],
    ["Médio", ">10-20%"],
    ["Baixo", ">0-10%"],
    ["Equlíbrio", "=0"],
    ["Prejuízo", "<0%"]
    ]
    nome= ["Tabela de lucros", ""]
    tabela = tabulate(dados, headers=  nome, tablefmt="fancy_grid")
    print(tabela)
    if (pvP-cpP)-(cf+iv+cv)*100>20:
        print("O lucro obtido é alto!")
    elif (pvP-cpP)-(cf+iv+cv)*100>10:
        print("O lucro obtido é médio!")
    elif (pvP-cpP)-(cf+iv+cv)*100>0:
        print("O lucro obtido é baixo!")
    elif (pvP-cpP)-(cf+iv+cv)*100==0:
        print("Não houve lucro!")
    elif (pvP-cpP)-(cf+iv+cv)*100<0:
        print("Houve pejuízo!")


