# CS1400-Biblioteca
Repositorio central de CS1400: Programación con Python. Por el resto del semester, utilizaremos GitHub para la entrega de los proyectos. 

# Antes de usar este repositorio, asegurate de haber terminado "M4 GitHub" en Canvas.

## 🛠 Cómo usar este repositorio
Sigue estas instrucciones para configurar tu espacio de trabajo, completar las tareas semanales, mantener tu proyecto actualizado y entregar tu trabajo para evaluación.

# Paso 1: Configuración Inicial (Solo se hace una vez)
Debes crear tu propia copia (un fork) de este repositorio para poder trabajar.
1.	Haz clic en el botón Fork en la esquina superior derecha de esta página de GitHub.
2.	En la opción Owner, selecciona tu usuario de GitHub. Deja el resto de las opciones por defecto.
3.	Haz clic en Create fork. 
¡Ahora tienes una copia propia de las tareas en tu cuenta!
4.	Clona tu fork a tu computadora:
o	En la página de tu fork, haz clic en el botón verde Code y copia la URL (HTTPS).
o	Abre tu terminal (o Símbolo del sistema / Command Prompt/Terminal en VSC) y ejecuta:

git clone <URL-DE-TU-FORK>
cd <NOMBRE-DEL-REPOSITORIO>

# Paso 2: Completar las Tareas Semanales
El repositorio está organizado por semanas (M05/, M06/, etc.), hay tareas por carpeta.
1.	Abre el archivo de la semana en VSC.
2.	Escribe tu código únicamente en las secciones indicadas con TODO dentro de los archivos.
3.	Prueba tu Código paso a paso (muchas veces) localmente en tu computadora antes de guardar y subir los cambios.
# Paso 3: Guardar y Subir tu Trabajo (Git Workflow)
Cada vez que avances o termines una tarea, guarda tus cambios en GitHub ejecutando estos comandos en la terminal:
1.	Prepara tus archivos modificados:

git add .

2.	Guarda los cambios localmente con un mensaje descriptivo:

git commit -m "Tarea 1 del Module 5 Paso 1 completada"

3.	Sube tu código a tu repositorio en GitHub:
git push origin main

Yo espero ver varios push cada vez. Nadie lo logra todo de un solo.
# Paso 4: Obtener Actualizaciones del Profesor
A lo largo del curso, puede ser que agregue cambios, nuevas tareas, pruebas automáticas o correcciones al repositorio original. Para traer esos cambios a tu computadora sin borrar tu trabajo, sigue estos pasos:
Desde la Terminal
Antes de empezar un nuevo modulo, ejecuta en tu terminal:

git pull https://github.com/megandeleonCS/CS1400-Biblioteca.git main

Utiliza:

git status

a menudo.
Nota: Procura hacer git commit de tus avances antes de descargar las actualizaciones del profesor para evitar conflictos en el código.
# Paso 5: Cómo Entregar las Tareas
1.	Entra a tu perfil de GitHub y abre tu fork de este repositorio.
2.	Verifica que tus últimos cambios aparezcan reflejados en la página.
3.	Copia la URL que aparece en la barra de direcciones de tu navegador (será algo como [https://github.com/TU-USUARIO/NOMBRE-DEL-REPO](https://github.com/TU-USUARIO/NOMBRE-DEL-REPO)).
4.	Envía esa URL a través Canvas.
Importante: NO envíes un "Pull Request" al repositorio del profesor. Únicamente sube tu trabajo a tu propio fork y entrega el enlace de tu repositorio.
