# Pios Food
Pios Food es un blog de recetas de comida, donde podés registrarte para ver las recetas que otros usuarios compartieron y crear las tuyas

La página cuenta con diferentes pantallas:
* Landing Page
* Registro
* Login
* Blog

## Landing Page
Es donde nuestros usuarios ingresan por primera vez. El objetivo es comentarles un poco acerca del sitio y convencerlos para que se creen una cuenta.

Aquí podemos navegar al blog y a la parte de About, donde se da más información acerca del sitio.

## Registro
Si el usuario quiere acceder al blog, debe tener una cuenta. Para eso, tiene que completar el formulario que se muestra en la imagen de abajo, donde se nos pide un email, un nombre de usuario y contraseña. Si ingresamos un mail inválido, dejamos campos vacíos o las contraseñas no coinciden, obtendremos un error y no podremos registrarnos.


## Login
Cuando ya tenemos la cuenta creada, tenemos que iniciar sesión. Se nos pide el mail y la contraseña que, en caso de ser incorrecta, nos lanzará un error.


## Blog
Es la parte más grande y con mayor funcionalidad del proyecto. Contamos con varias funcionalidades, detalladas brevemente a continuación:

### Página principal
Es donde van a aparecer listadas todas las recetas creadas. Contamos con un panel de filtros por comida y duración. En la parte superior hay una barra de búsqueda, una opción para acceder a nuestras recetas favoritas, sistema de chat y nuestro perfil.

Podemos aplicar una búsqueda por nombre de la receta, y obtendremos todas las recetas que coincidan o incluyan el término ingresado. En caso de no haber resultados, se nos notificará.



### Página de favoritos
Podemos agregar recetas a favoritos y acceder a ellas más facilmente en la página de favoritos.



### Página de detalle de receta
Si quiero acceder a una receta en particular, voy a poder ver su detalle, que incluye título, duración, dificultad, cantidad de likes, ingredientes, autor, cuando podemos cocinar esa receta y una descripción.


Desde aquí puedo realizar acciones como:
- Darle Like
- Añadirla a favoritos
- Ir al perfil del creador
- Editarla y eliminarla (si soy el autor)

### Perfil
Puedo acceder a mi perfil o al de otro usuario y ver las recetas creadas, junto con su información y algunos datos extra. Si estoy en mi perfil, voy a poder editarlo. Si estoy en el perfil de otro usuario, voy a tener la opción de enviarle un mensaje.


### Editar perfil
Vamos a poder completar nuestro perfil con nuestra foto de perfil, nombre y una descripción. Esta opción también la tenemos inmediatamente luego de registrarnos en el sitio.



### Crear / Editar receta
Podemos crear nuestra propia receta, así como también editarla. Cuando guardamos el formulario, se aplican validaciones y la receta se guarda como la más reciente en la página principal y también en nuestro perfil en la parte de mis recetas.


### Sistema de chat
La aplicación cuenta con un sistema de chat. Podemos enviar mensajes a otros usuarios.



## Tecnologías usadas
Para el desarrollo, se utilizó:
- Django
- Django REST Framework
- JavaScript
- TailwindCSS
- SQLite3

