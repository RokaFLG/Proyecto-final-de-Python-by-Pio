const menuToggle = document.getElementById('menu-toggle');
const mobileMenu = document.getElementById('mobile-menu');
const openMenuIcon = document.getElementById('open-menu-icon');
const closeMenuIcon = document.getElementById('closed-menu-icon');

const closeMenu = (e) => {
  if (e.target !== menuToggle && !mobileMenu.contains(e.target)) {
    mobileMenu.classList.add('translate-x-full');
    openMenuIcon.classList.add('hidden');
    closeMenuIcon.classList.remove('hidden');
  }
};

menuToggle.addEventListener('click', (e) => {
  e.stopPropagation();
  mobileMenu.classList.toggle('translate-x-full');
  openMenuIcon.classList.toggle('hidden');
  closeMenuIcon.classList.toggle('hidden');
});

window.innerWidth <= 768
  ? document.addEventListener('click', closeMenu)
  : document.removeEventListener('click', closeMenu);