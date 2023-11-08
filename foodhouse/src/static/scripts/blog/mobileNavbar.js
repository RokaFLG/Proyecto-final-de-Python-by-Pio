const homeLink = document.querySelector('#home-link');
const favoritesLink = document.querySelector('#favorites-link');
const chatLink = document.querySelector('#chat-link');
const profileLink = document.querySelector('.profile-link');

if (window.location.pathname === '/blog/') {
  homeLink.classList.replace('text-slate-500', 'text-primary');
  homeLink.classList.replace('border-b-transparent', 'border-b-primary');
} else if (window.location.pathname === '/blog/favorites/') {
  favoritesLink.classList.replace('text-slate-500', 'text-primary');
  favoritesLink.classList.replace('border-b-transparent', 'border-b-primary');
} else if (window.location.pathname === '/blog/chat/') {
  chatLink.classList.replace('text-slate-500', 'text-primary');
  chatLink.classList.replace('border-b-transparent', 'border-b-primary');
} else {
  profileLink.classList.replace('text-slate-500', 'text-primary');
  profileLink.classList.replace('border-b-transparent', 'border-b-primary');
}