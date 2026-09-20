"""Consumo de água residencial e comercial
Arquivo: app.py
Pasta: projetos/consumo-agua"""

# Declaração de variáveis e entrada de dados
tipo_imovel = input("Digite seu tipo de imóvel (comercial, apartamento, casa): ")

if tipo_imovel not in ("comercial", "Comercial", "apartamento", "Apartamento", "casa", "Casa"):
    print("Tipo de imóvel inválido. Informe comercial, apartamento ou casa.")
else:
    consumo_mensal_agua = float(input("Digite o consumo mensal de água em metros cúbicos (m³): "))

    # Aplicação das condições e apresentação dos resultados
    match tipo_imovel:

        # Imóvel Comercial - Consultar plano corporativo
        case "comercial" | "Comercial":
            print("Tarifa Comercial aplicada - consulte plano corporativo")

        # Imovel Apartamento e consumo menor que 10m³ - Consumo econômico
        case "apartamento" | "Apartamento" if consumo_mensal_agua < 10:
            print("Consumo econômico - excelente controle da água!")

        # Imovel Casa ou Apartamento e consumo menor ou igual a 25m³ - Consumo moderado
        case "casa" | "Casa" | "apartamento" | "Apartamento" if consumo_mensal_agua <= 25:
            print("Consumo moderado - dentro do padrão residencial.")

        # Imóvel não Comercial e consumo maior que 35m³ - Consumo excessivo
        case _ :
            print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")
    