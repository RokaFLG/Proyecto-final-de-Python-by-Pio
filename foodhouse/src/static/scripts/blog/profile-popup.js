const profileContainers = document.querySelectorAll('#profile-container');
const optionsContainer = document.querySelectorAll('#options-container');

profileContainers.forEach((profileContainer) => {
  profileContainer.addEventListener('click', () => {
    optionsContainer.forEach((optionsContainer) => {
      optionsContainer.classList.toggle('hidden');
    });
  });
});