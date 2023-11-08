import csrfToken from './getCsrfToken.js';

const deleteRecipe = document.getElementById('delete-recipe');
const confirmModal = document.getElementById('confirm-modal');
const closeModalButton = document.querySelector('.close-modal');
const confirmDeleteButton = document.getElementById('confirm-delete');

deleteRecipe?.addEventListener('click', () => {
  document.body.classList.toggle('overflow-hidden');
  confirmModal.classList.replace('hidden', 'flex');
});

closeModalButton.addEventListener('click', () => {
  document.body.classList.toggle('overflow-hidden');
  confirmModal.classList.replace('flex', 'hidden');
});

confirmDeleteButton.addEventListener('click', async () => {
  const deleteRecipe = await fetch(
    'http://127.0.0.1:8000/blog/api/delete-recipe/',
    {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
      },
      credentials: 'include',
      body: JSON.stringify({
        recipe_id: parseInt(confirmDeleteButton.dataset.recipeid),
      }),
    }
  );
  const response = await deleteRecipe.json();
  if (response.status === 'success') {
    window.location.href = '/blog/';
  }
});