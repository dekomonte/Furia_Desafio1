/*Scripts utilizados no Banco de Dados*/

--Criação do banco de dados da aplicação
CREATE DATABASE IF NOT EXISTS furia_chat;

--Criação da tabela com mensagens
USE furia_chat;

CREATE TABLE IF NOT EXISTS messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_input VARCHAR(255) NOT NULL,
    bot_response TEXT NOT NULL
);

--Inserções no banco
INSERT INTO messages (user_input, bot_response) VALUES
('Quando é o próximo jogo?', 'O próximo jogo é sábado às 18h!'),
('Qual a escalação da FURIA?', 'Confira a escalação atualizada no nosso site oficial.');
    