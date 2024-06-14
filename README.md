```markdown
# Generative AI Web Interface

Esta é uma aplicação Flask que fornece uma interface web para interagir com um modelo de IA generativo, utilizando a API da Google. A aplicação permite que os usuários enviem perguntas e recebam respostas formatadas, incluindo código com numeração de linha e texto em negrito.

## Características

- Interface web simples e intuitiva.
- Integração com a API da Google para geração de conteúdo.
- Formatação de respostas com código em bloco, texto em negrito e quebras de linha.
- Numeração de linha para blocos de código, com números não selecionáveis.
- Tela de carregamento enquanto a resposta é processada.
- Histórico de conversas e contexto ainda não está implementado.

## Requisitos

- Python 3.6 ou superior.
- Flask.
- google-generativeai.

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/henriquefarisco/generativeai.git
   cd generativeai
   ```

2. Crie um ambiente virtual e ative-o:
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   ```sh
   pip install flask google-generativeai
   ```

4. Configure a chave da API do Google:
   - Substitua `SUA API AQUI DO GEMINI` no arquivo `app.py` pela sua chave de API da Google.

5. Execute a aplicação:
   ```sh
   sudo python app.py  # Use sudo para permitir que Flask escute na porta 80
   ```

## Configuração de Acesso pelo Nome da Máquina

Para acessar a aplicação pelo nome da máquina (por exemplo, `http://generativeia/`), siga os passos abaixo:

1. Edite o arquivo `hosts` no seu sistema:

   ### No Windows
   - Abra o `Bloco de Notas` como administrador.
   - Edite o arquivo `C:\Windows\System32\drivers\etc\hosts` e adicione:
     ```
     SEU-IP generativeia
     ```

   ### No Linux/MacOS
   - Abra o terminal.
   - Edite o arquivo `/etc/hosts` com permissões de superusuário:
     ```sh
     sudo nano /etc/hosts
     ```
   - Adicione a seguinte linha:
     ```
     SEU-IP generativeia
     ```

## Estrutura do Projeto

```
/generative-ia
    /templates
        index.html
    /static
        /css
            style.css
        /js
            script.js
    app.py
```

## Contribuição

Sinta-se à vontade para contribuir com este projeto, enviando pull requests ou abrindo issues no GitHub.

## Licença

Este projeto está licenciado sob a MIT License.
