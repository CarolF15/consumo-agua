# 💧 Projeto de Classificação de Consumo de Água Mensal 💧
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge\&logo=git\&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge\&logo=github\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)

Projeto desenvolvido para praticar lógica de programação com Python. O programa verifica a **Classificação do consumso mensal de água** baseado no **tipo de imóvel** e **quantidade de água utilizada** informados pelo usuário .

---

#  🎯 Objetivo do Programa 

* Desenvolver um algoritmo para identificar o tipo de consumo de água de acordo com condições pré-estabelecidas.
* Praticar o ciclo Entrada → Processamento → Saída: receber o tipo de imóvel e a quantidade de água utilizada mensalmente (m³), analisar as informações e informar o tipo de consumo.
* Utilizar estruturas de decisão `match/case` para classificar o consumo de água de acordo com as condições definidas para cada tipo de imóvel.

---

## 🧾 Regras de Classificação

| Tipo de imóvel | Condição | Classificação |
|---|---|---|
| Comercial | Qualquer consumo | Tarifa comercial aplicada |
| Apartamento | Consumo menor que 10 m³ | Consumo econômico |
| Apartamento ou casa | Consumo dentro do limite residencial | Consumo moderado |
| Demais casos | Consumo acima do limite residencial | Consumo excessivo |

## 🚀 Como Executar o Programa

### Pré-requisitos
* **Python 3.10** instalado.

### Passo a Passo

1. Clone este repositório:
   ```bash
   git clone https://github.com/CarolF15/consumo-agua.git
   ```

## 📁 Estrutura do Projeto

```text
calculo-desconto/
├── app.py       # Código principal do programa
└── README.md    # Documentação do projeto
```

## 🛠️ Tecnologias

* Python 3
* Git e GitHub