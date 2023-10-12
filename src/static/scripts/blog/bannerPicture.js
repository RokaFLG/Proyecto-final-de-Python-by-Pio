const recipePicContainer = document.getElementById('recipe-picture-container');
const fileInput = document.getElementById('file-input');

recipePicContainer.addEventListener('click', () => {
  fileInput.click();

  fileInput.addEventListener('change', () => {
    const file = fileInput.files[0];
    const reader = new FileReader();

    reader.addEventListener('load', () => {
      const recipeImage = document.getElementById('recipe-image');
      recipeImage.src = reader.result;
    });

    reader.readAsDataURL(file);
  });
});