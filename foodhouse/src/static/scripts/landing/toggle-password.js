const toggleButton = document.getElementById('toggle-password');
const passwordInput = document.getElementById('id_password');
const emailInput = document.getElementById('id_email');

toggleButton.addEventListener('click', function (e) {
  const type =
    passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
  passwordInput.setAttribute('type', type);
  type === 'text'
    ? toggleButton.firstElementChild.classList.replace('fa-eye', 'fa-eye-slash')
    : toggleButton.firstElementChild.classList.replace(
        'fa-eye-slash',
        'fa-eye'
      );
});

window.addEventListener('resize', () => {
  if (window.innerWidth >= 1024) {
    emailInput.placeholder = 'johndoe@something.com';
    passwordInput.placeholder = 'password123';
  } else {
    emailInput.placeholder = 'Email';
    passwordInput.placeholder = 'Password';
  }
});