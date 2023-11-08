import csrfToken from './getCsrfToken.js';

const currentConversation = document.getElementById('current-conversation');

const messageInput = document.getElementById('message');
const sendMessageBtn = document.getElementById('send-message');

const messagesContainer = document.getElementById('messages-container');
const currentUser = parseInt(messagesContainer.dataset.user);

const conversationId = parseInt(
  new URLSearchParams(window.location.search).get('conversation')
);

if (conversationId) {
  currentConversation.classList.toggle('hidden');
}

sendMessageBtn.addEventListener('click', () => {
  if (messageInput.value === '') return;
  createMessage();
});

const createMessage = async () => {
  const response = await fetch(
    'http://127.0.0.1:8000/blog/api/create-message',
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
      },
      credentials: 'include',
      body: JSON.stringify({
        body: messageInput.value,
        conversation_id: conversationId,
      }),
    }
  );

  const data = await response.json();
  if (data.status === 'success') {
    messageInput.value = '';
    getMessages();
  }
};

const getMessages = async () => {
  const response = await fetch(
    'http://127.0.0.1:8000/blog/api/messages?conversation_id=' + conversationId
  );
  const data = await response.json();

  const tempFragment = document.createDocumentFragment();

  data.messages?.forEach((message) => {
    if (message.sender === currentUser) {
      const myMessage = `
        <li class="w-full flex flex-col items-end font-text font-light">
          <div class="p-2 bg-primary text-white rounded-md w-[90%] max-w-[450px]">
            <p class="leading-[28px]">
              ${message.body}
             </p>
          </div>
          <span class="text-text text-[14px] mt-2">${formatearFecha(
            message.created_at
          )}</span>
        </li>
      `;

      tempFragment.appendChild(
        document.createRange().createContextualFragment(myMessage)
      );
    } else {
      const otherMessage = `
        <li class="w-full flex flex-col font-text font-light">
          <div class="p-2 bg-gray-200 rounded-md w-[90%] max-w-[450px]">
            <p class="leading-[28px]">
              ${message.body}
            </p>
          </div>
          <span class="text-text text-[14px] mt-2">${formatearFecha(
            message.created_at
          )}</span>
        </li>
      `;
      tempFragment.appendChild(
        document.createRange().createContextualFragment(otherMessage)
      );
    }
  });

  messagesContainer.innerHTML = '';
  messagesContainer.appendChild(tempFragment);
};

getMessages();

function formatearFecha(fechaStr) {
  const fecha = new Date(fechaStr);
  const fechaActual = new Date();

  const optionsHora = { hour: '2-digit', minute: '2-digit' };
  const optionsDiaMesHora = {
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
  };

  if (fecha.toDateString() === fechaActual.toDateString()) {
    return fecha.toLocaleTimeString(undefined, optionsHora);
  } else {
    return fecha.toLocaleDateString(undefined, optionsDiaMesHora);
  }
}