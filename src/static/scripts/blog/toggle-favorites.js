import csrfToken from './getCsrfToken.js';

const getUserFavorites = async () => {
  const data = await fetch('http://127.0.0.1:8000/blog/api/favorites/');
  const dataJson = await data.json();
  return dataJson.favorites;
};

const updateFavoritesButtons = (favorites) => {
  const favButton = document.querySelectorAll('#toggle-favorites');
  favButton.forEach((recipe) => {
    const recipeId = parseInt(recipe.getAttribute('data-recipe'));
    if (favorites.includes(recipeId)) {
      if (
        window.location.pathname === '/blog/favorites/' ||
        window.location.pathname === '/blog/'
      ) {
        recipe.classList.replace('bg-[rgba(0,0,0,0.70)]', 'bg-rose-200');
      } else {
        recipe.classList.replace('bg-transparent', 'bg-rose-200');
      }
      recipe.removeEventListener('click', addToFavorites);
      recipe.addEventListener('click', async () => {
        const response = await deleteFromFavorites(recipeId);
        if (response.status === 'success') {
          getUserFavorites().then(updateFavoritesButtons);
          if (window.location.pathname === '/blog/favorites/') {
            const card = recipe.closest('.recipe-card');
            card.remove();

            const noRecipes = document.querySelector('#no-recipes');
            const recipes = document.querySelectorAll('.recipe-card');
            recipes.length === 0
              ? noRecipes.classList.replace('hidden', 'flex')
              : noRecipes.classList.replace('flex', 'hidden');
          }
        }
      });
    } else {
      if (
        window.location.pathname === '/blog/favorites/' ||
        window.location.pathname === '/blog/'
      ) {
        recipe.classList.replace('bg-rose-200', 'bg-[rgba(0,0,0,0.70)]');
      } else {
        recipe.classList.replace('bg-rose-200', 'bg-transparent');
      }
      recipe.removeEventListener('click', deleteFromFavorites);
      recipe.addEventListener('click', async () => {
        const response = await addToFavorites(recipeId);
        if (response.status === 'success') {
          getUserFavorites().then(updateFavoritesButtons);
        }
      });
    }
  });
};

const userFavorites = getUserFavorites().then(updateFavoritesButtons);

const addToFavorites = async (recipeId) => {
  const add = await fetch('http://127.0.0.1:8000/blog/api/add-favorites/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken,
    },
    credentials: 'include',
    body: JSON.stringify({
      recipe_id: recipeId,
    }),
  });
  const addJson = await add.json();
  return addJson;
};

const deleteFromFavorites = async (recipeId) => {
  const del = await fetch('http://127.0.0.1:8000/blog/api/delete-favorites/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken,
    },
    credentials: 'include',
    body: JSON.stringify({
      recipe_id: recipeId,
    }),
  });
  const delJson = await del.json();
  return delJson;
};