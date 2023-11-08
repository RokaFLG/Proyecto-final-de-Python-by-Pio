import csrfToken from './getCsrfToken.js';

const sendMessageBtn = document.getElementById('send-message');

sendMessageBtn?.addEventListener('click', () => {
  const participantId = parseInt(sendMessageBtn.dataset.participant);
  startConversation(participantId);
});

const startConversation = async (participantId) => {
  const response = await fetch(
    'http://127.0.0.1:8000/blog/api/create-conversation',
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
      },
      credentials: 'include',
      body: JSON.stringify({ participant_id: participantId }),
    }
  );
  const data = await response.json();
  if (data.status === 'success') {
    window.location.href = `/blog/chat/?conversation=${data.conversation_id}`;
  }
};