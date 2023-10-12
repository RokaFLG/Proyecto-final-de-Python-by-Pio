const searchbar = document.getElementById('mobile-searchbar');
const activeSearch = document.getElementById('active-search');

activeSearch.addEventListener('click', () => {
  if (searchbar.classList.contains('w-[calc(100%-65px)]')) {
    searchbar.classList.replace('w-[calc(100%-65px)]', 'w-0');
    searchbar.classList.replace('p-2', '!p-0');
    searchbar.classList.replace('border-2', '!border-0');
    activeSearch.firstElementChild.classList.replace(
      'fa-circle-xmark',
      'fa-magnifying-glass'
    );
    return;
  }

  searchbar.classList.replace('w-0', 'w-[calc(100%-65px)]');
  searchbar.classList.replace('!p-0', 'p-2');
  searchbar.classList.replace('!border-0', 'border-2');
  activeSearch.firstElementChild.classList.replace(
    'fa-magnifying-glass',
    'fa-circle-xmark'
  );
});