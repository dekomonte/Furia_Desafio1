const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const chatMessages = document.getElementById('chat-messages');
const perguntasContainer = document.getElementById('perguntas-container');

// Carregar as perguntas ao carregar a página
document.addEventListener('DOMContentLoaded', async () => {
  const response = await fetch('/perguntas');
  const data = await response.json();
  const perguntas = data.perguntas;

  perguntasContainer.innerHTML = '<h3>Escolha uma pergunta:</h3>';
  perguntas.forEach(pergunta => {
    const perguntaElement = document.createElement('button');
    perguntaElement.textContent = pergunta;
    perguntaElement.classList.add('pergunta-button');
    perguntaElement.onclick = () => enviarPergunta(pergunta);
    perguntasContainer.appendChild(perguntaElement);
  });
});

chatForm.addEventListener('submit', async (e) => {
  e.preventDefault(); // Impede o recarregamento da página

  const message = userInput.value.trim();
  if (!message) return;

  addMessage('user', message);

  const response = await fetch('/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message })
  });

  const data = await response.json();
  addMessage('bot', data.response);

  userInput.value = '';
  chatMessages.scrollTop = chatMessages.scrollHeight;
});

// Função para enviar a pergunta ao bot
function enviarPergunta(pergunta) {
  addMessage('user', pergunta);

  fetch('/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: pergunta })
  })
  .then(response => response.json())
  .then(data => {
    addMessage('bot', data.response);
  });
}

function addMessage(sender, text) {
  const messageDiv = document.createElement('div');
  messageDiv.classList.add('message', sender);
  messageDiv.textContent = text;
  chatMessages.appendChild(messageDiv);
}
