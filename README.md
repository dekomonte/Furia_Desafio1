
# Processo Seletivo FURIA - Desafio 1 (Chatbot)

Repositório com a solução do desafio do PS da Fúria.

### Instruções (Requisitos)

**Objetivo:** Desenvolver um caso de uso conversacional relacionado à FURIA (Telegram, web chat ou mobile chat).  
**Proposta:** Criar um chat para os fãs do time de CS da FURIA. O chat deve conter tudo que você, como fã, gostaria de ver para acompanhar e interagir com o time.

---

### Decisões de Desenvolvimento

Durante o desenvolvimento deste chatbot, algumas decisões importantes foram tomadas para garantir a funcionalidade, a organização e a escalabilidade do projeto. Aqui estão algumas dessas decisões:

* Simplicidade. 
* Banco de dados.
* Python. 

---

### Instalação e Execução

1. **Clone o repositório:**

   Primeiro, clone o repositório para sua máquina local:

   ```bash
   git clone https://github.com/dekomonte/Furia_Desafio1.git
   cd Furia_Desafio1
   ```

2. **(Opcional) Crie um ambiente virtual:**

   Caso queira isolar as dependências do projeto, você pode criar um ambiente virtual. Se estiver utilizando `venv`, execute:

   ```bash
   python -m venv venv
   ```

3. **(Opcional) Ative o ambiente virtual:**

   - No **Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - No **macOS/Linux**:

     ```bash
     source venv/bin/activate
     ```

4. **Instale as dependências:**

   Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

5. **Configure o banco de dados:**

   Certifique-se de ter o banco de dados MySQL configurado. Crie o banco de dados `furia_chat` conforme as especificações no arquivo `app.py`. O banco de dados deve conter as tabelas necessárias para armazenar as perguntas e respostas do chatbot.

   O arquivo **db.sql** contém os comandos utilizados para criação e inserção das informações no banco de dados.

6. **Execute a aplicação:**

   Após a instalação e configuração, inicie o servidor Flask para rodar a aplicação:

   ```bash
   flask --app app run
   ```

7. **Acesse o Chat:**

   Abra o navegador e acesse a aplicação no endereço:

   ```bash
   http://127.0.0.1:5000/
   ```

   O chatbot estará pronto para interagir com você!

---

### Estrutura de Pastas

```plaintext
project/
│
├── app.py                  # Código principal do Flask (Backend)
├── public/                 # Arquivos estáticos (CSS, JS, Imagem da Logo)
│   ├── style.css           # Estilos do chat
│   ├── script.js           # Lógica do JavaScript
│   └── logo.png            # Logo da FURIA
├── index.html              # Página inicial do chat (fora da pasta public)
├── requirements.txt        # Dependências do Python
├── .gitignore              # Arquivos e pastas a serem ignorados pelo Git
└── README.md               # Documentação do projeto
```

---

### Funcionalidades

- **Chat Interativo:** O chatbot interage com o usuário respondendo com base em perguntas pré-definidas armazenadas no banco de dados MySQL.
- **Perguntas Dinâmicas:** O chatbot apresenta ao usuário uma lista de perguntas que ele pode selecionar para obter respostas.
- **Base de Dados:** As perguntas e respostas são armazenadas e recuperadas de um banco de dados MySQL.
- **Frontend Responsivo:** A interface é simples e responsiva, permitindo interações em diferentes dispositivos.

---

### Endpoints

- **`/chat`**: Endpoint que recebe uma mensagem do usuário e responde com a mensagem do bot. 
    - Método: `POST`
    - Corpo da requisição: `{ "message": "mensagem do usuário" }`
    - Resposta: `{ "response": "resposta do bot" }`
  
- **`/perguntas`**: Endpoint que retorna todas as perguntas disponíveis no banco de dados.
    - Método: `GET`
    - Resposta: `{ "perguntas": ["pergunta1", "pergunta2", ...] }`

---

### Tecnologias Utilizadas

- **Python** com **Flask** para o backend.
- **MySQL** para o banco de dados.
- **HTML**, **CSS** e **JavaScript** para o frontend.
- **Git** para controle de versão.
- **ChatGPT** para codificação e verificação de erros. 

---

### Projetos Futuros

* Mensagem de Boas-Vindas Personalizada: Implementar uma mensagem de boas-vindas mais interativa e personalizada para o usuário, criando uma experiência inicial mais acolhedora e personalizada.
* Expandir o reconhecimento de perguntas, permitindo que o chatbot entenda uma variedade maior de consultas e não apenas aquelas predefinidas, utilizando técnicas de processamento de linguagem natural (PNL) ou integração com APIs externas.
* Melhorias na Inteligência do Sistema: Incorporar algoritmos de aprendizado de máquina para tornar o chatbot mais inteligente e capaz de oferecer respostas mais precisas e contextuais, aprendendo com interações anteriores e adaptando-se às necessidades do usuário.
* Relatórios de Interação: Criar um painel administrativo para o time de desenvolvimento, onde é possível visualizar métricas como volume de interações, satisfação dos usuários, perguntas mais frequentes e outros dados úteis para a análise do uso do chatbot.
* ETC

---

### Contribuições

Se você quiser contribuir com melhorias para este projeto, fique à vontade para abrir um **pull request**. Qualquer sugestão é bem-vinda!
