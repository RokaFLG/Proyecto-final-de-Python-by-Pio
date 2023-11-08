const addIngredientsField = document.getElementById('addIngredients');
const addButton = document.getElementById('addButton');
const ingredientsContainer = document.getElementById('ingredientsContainer');

const djangoIngredients = document.getElementById('id_ingredients');

const ingredients = [];

const createIngredient = (name) => {
  const ingredientItem = `
    <li class="w-full flex items-center justify-between" id="ingredient-${
      ingredients.length
    }">
      <p class="font-medium font-title">${name.trim()}</p>
        <button type="button" onclick="removeIngredient(event)"
          class="text-rose-500 hover:text-rose-700 transition-colors text-[17px] font-title">
          Remove
        </button>
    </li>
  `;

  ingredientsContainer.appendChild(
    document.createRange().createContextualFragment(ingredientItem)
  );

  ingredients.push(name);

  djangoIngredients.value = `
    {
      "ingredients": ${JSON.stringify(ingredients)}
    }
  `;
};

const removeIngredient = (e) => {
  const ingredientId = e.target.parentNode.id;
  const ingredientIndex = ingredientId.split('-')[1];

  ingredients.splice(ingredientIndex, 1);
  e.target.parentNode.remove();

  djangoIngredients.value = `{"ingredients": ${JSON.stringify(ingredients)}}
  `;
};

addButton.addEventListener('click', () => {
  createIngredient(addIngredientsField.value);
  addIngredientsField.value = '';
});

if (djangoIngredients.value) {
  const djangoIngredientsValue = JSON.parse(djangoIngredients.value);

  djangoIngredientsValue.ingredients.forEach((ingredient) => {
    createIngredient(ingredient);
  });
}