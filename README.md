# 🚗 Controle de Abastecimento (KM/L)

Sistema desenvolvido em Python para gestão de consumo de combustível, utilizando banco de dados SQLite para persistência e relatórios detalhados via terminal.

## 🛠️ Funcionalidades

- **Gerenciamento de Dados**: Cadastro de abastecimentos (Data, KM, Valor por Litro, Litros Totais).
- **Relatórios**: Histórico completo ordenado por data.
- **Análise de Consumo**:
  - Cálculo de KM/L do último abastecimento.
  - Variação de preço do combustível (Subiu/Baixou/Mesmo valor).
  - Cálculo de dias percorridos entre abastecimentos.
  - Média histórica total do veículo.
- **Segurança**: Opção de exclusão de registros com busca por ID e confirmação.

## 💻 Tecnologias

- Python 3.14
- SQLite3