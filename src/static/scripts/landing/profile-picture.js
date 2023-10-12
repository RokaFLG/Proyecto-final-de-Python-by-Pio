const profilePicContainer = document.getElementById(
    'profile-picture-container'
  );
  const fileInput = document.getElementById('file-input');
  
  profilePicContainer.addEventListener('click', () => {
    fileInput.click();
  
    fileInput.addEventListener('change', () => {
      const file = fileInput.files[0];
      const reader = new FileReader();
  
      reader.addEventListener('load', () => {
        const profileImage = document.getElementById('profile-image');
        profileImage.src = reader.result;
      });
  
      reader.readAsDataURL(file);
    });
  });