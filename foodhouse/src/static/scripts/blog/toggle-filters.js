const toggleButton = document.getElementById('toggle-filters');

const showFilters = () => {
  const filters = document.getElementById('mobile-filters');
  filters.classList.toggle('-translate-x-full');
  document.body.classList.toggle('overflow-hidden');
};

toggleButton.addEventListener('click', showFilters);

window.addEventListener('resize', () => {
  window.innerWidth >= 1024
    ? toggleButton.removeEventListener('click', showFilters)
    : toggleButton.addEventListener('click', showFilters);
});