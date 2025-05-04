# 🏦 Fechamento de Caixa

## 📌 Descrição
Este projeto automatiza o fechamento de caixa, permitindo o registro de **recibos**, **cheques** e **dinheiro** em uma planilha Excel. Os dados são organizados de forma clara e estruturada para facilitar consultas futuras.

## 🚀 Funcionalidades
- 📄 **Registro detalhado de recibos** (valor, quantidade e total).
- 💰 **Entrada de múltiplos valores em dinheiro**, somando automaticamente.
- ✍️ **Adição de cheques separados por vírgula**, com cálculo automático do total.
- ✅ **Tratamento de exceções**, garantindo que apenas números válidos sejam aceitos.
- 📊 **Geração de planilha Excel com todos os dados**, organizada e sem índices desnecessários.

## ⚙️ Tecnologias Utilizadas
- 🐍 Python
- 📊 Pandas
- 📄 OpenPyxl (para manipulação de arquivos `.xlsx`)

## 🛠️ Instalação
Para executar este projeto, siga os passos abaixo:

1. **Clone o repositório**:
   ```bash
    git clone https://github.com/Raphael2203/fechamento-caixa.git
    cd fechamento-caixa

2. **Crie um ambiente virtual (opcional, mas recomendado)**:
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows

3. **Instale as dependências**:
    pip install -r requirements.txt

▶️ **Como Usar**

Execute o script principal:

    python main.py

O programa irá solicitar entradas para recibos, cheques e dinheiro, e salvará os dados na planilha Excel.

📝 **Exemplo de Uso**

    Valor do recibo: 100.00
    Quantidade de recibos: 3
    Valor do recibo: (pressione Enter para finalizar)
    Digite os valores dos cheques separados por vírgula: 500, 200.50
    Digite um valor em dinheiro um por vez. Pressione Enter sem digitar nada para finalizar.
    Valor em dinheiro: 100
    Valor em dinheiro: 50
    Valor em dinheiro: (pressione Enter para finalizar)

📂 **Resultado**: 
Um arquivo Excel fechamento_caixa.xlsx contendo todos os dados organizados!

📌 **Contribuição**
Se quiser contribuir, sinta-se à vontade para abrir issues ou fazer um pull request! 

📜 **Licença**
Este projeto está licenciado sob a MIT License – veja o arquivo LICENSE para mais detalhes.