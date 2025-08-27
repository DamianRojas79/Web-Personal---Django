## Web Personal - Django



![License: MIT](https://img.shields.io/badge/License-MIT-green.svg) ![Badge en Desarollo](https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green)

## Índice

  

*[Título e imagen de portada](#Título-e-imagen-de-portada)

  

*[Insignias](#insignias)

  

*[Índice](#Todo-list)

  

*[Descripción del proyecto](#descripción-del-proyecto)

  

*[Estado del proyecto](#estado-del-proyecto)

  

*[Características de la aplicación y demostración](#características-de-la-aplicación-y-demostración)

  

*[Acceso al proyecto](#acceso-al-proyecto)

  

*[Tecnologías utilizadas](#tecnologías-utilizadas)  

*[Personas-Desarrolladores del Proyecto](#personas-desarrolladores)

  

*[Licencia](#licencia)

  

*[Conclusión](#conclusión)

  
  
  

## Descripción del Proyecto

**Web Personal** es una aplicación la cual te permite cargar tus proyectos de manera muy simple utilizando el panel de administrador que ofrece Django. También la aplicación cuenta con una  página **Acerca de** y **Contacto** de la persona  <br><br>

Imagen Proyecto  



  
  

## Estado del Proyecto

![Badge en Desarollo](https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green)


  

## Características de la aplicación y demostración

  

:hammer: **Funcionalidades del proyecto**

- `Funcionalidad 1`: **Panel Administrador** <br>

Desde el Panel de Administrador que ofrece Django se pueden cargar y gestionar fácilmente los proyectos que se desean subir al sitio.  <br><br>
Desde el panel se podran:
* Añadir un nuevo proyecto.
Permitiendo aqui ingresar Título, Descripción , Cargar una imagen y un Link de enlace del proyecto si se desea.
Imagen

* Listar los proyectos.
También desde el panel se pueden listar todos los proyectos cargados,  con las posibilidad de filtralos por Fecha de Creación o Fecha de Modificación 
Imagen

* Eliminar o Modificar los proyectos.
Se pueden modificar o eliminar los proyectos existentes.
Imagen


  


  

- `Funcionalidad 2`: **Menú de navegación** <br>

En la parte superior se encuentra el menú de navegación para acceder a las paginas de "Portafolio", "Acerca De" y "Contacto".
Imagen 
  



  
  

- `Funcionalidad 3`: **Página de Proyectos - Portfolio**<br>
En esta página se pueden visualizar todos los proyectos subidos ordenados desde los mas recientes alos mas antiguos.
Image
  
 


  

- `Funcionalidad 4`: **Página Acerca De** <br>

Esta página contiene una descripción personal de la persona con sus habilidades y cualidades. Debajo también se visualiza una barra de progreso con algunas de sus habilidades.



- `Funcionalidad 5`: **Página de Contacto** <br>

Página con los contactos personales.


  

- `Funcionalidad 6`: **Acceso a redes Sociales** <br>

En el pie de cada página se encuentran los accesos a las redes Sociales.
Imágen
  

  


  
  

## Acceso al Proyecto

  

Para descargar y ejecutar el proyecto se debe realizar los siguientes pasos:

  

:file_folder: **Acceso al proyecto**

- **Abrir terminal**<br>

Primero se debe abrir una terminal para ejecutar los comandos necesarios para descargar y ejecutar el proyecto.

  

- **Crear directorio para el proyecto**<br>

Ejecutar:<br>

mkdir Web-personal


  

- **Clonar repositorio**<br>

Para clonar el repositorio primero situarse en el directorio creado:<br>

Ejecutar:<br>

cd Web-personal <br>

Luego allí clonar el repositorio:<br>

Ejecutar:<br>

git clone git@github.com:DamianRojas79/Web-Personal-Django.git

  

:hammer_and_wrench: **Abre y ejecuta el programa**

- **Instalar python y modulo venv para crear entornos virtuales**<br>


Instalar Pyhton si no se tiene instalado

Ejecutar:

<i>sudo apt install python3</i> <br>

Instalar venv para poder crear entornos virtuales 

Ejecutar:

<i>sudo apt install -y python3-venv</i><br>

  
  
- **Crear entorno virtual para el proyecto**<br>

Se crea un entorno virtual para tener allí todos los paquetes necesarios para el proyecto.<br>

Para ello primero se debe entrar al directorio clonado.<br>

Ejecutar:

<i>cd Web-personal </i>

  

Luego se crea el entorno virtual:

Ejecutar:

<i>python -m venv env-todo</i>

  

- **Activar entorno virtual**

Ejecutar:

<i>source env-todo/bin/activate</i>

  

- **Instalar las dependencias para el proyecto**<br>

Se instalan las as dependencias necesarias que se encuentra dentro del archivo requirements.txt.<br>

Ejecutar:<br>

<i>pip install -r requirements.txt</i>

  

- **Ejecutar el programa**

Ejecutar:

<i>Python3 manage.py runserver</i>

  

- **Abrir Aplicación y  Panel Administrador**<br>

Desde cualquier navegador ingresar las siguiente URLs <br>

Aplicación:
http://localhost:8000/

Panel administrador:
http://localhost:8000/admin/


  

## :heavy_check_mark: Tecnologías Utilizadas

- **Python**<br>

- **HTML**<br>

- **Boostrap**<br>

- **Django**<br>

- **Jinja**<br>

- **Sqlite**<br>

  

## Personas Desarrolladoras del Proyecto

[<img src="https://avatars.githubusercontent.com/u/135189204?s=400&u=932907d7db09c6472e34c43c6b5ed27be7342bf4&v=4" width=115><br><sub> Damian Rojas </sub>](https://github.com/DamianRojas79)

  

## Licencia📄

  

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

  
Este proyecto cuenta con licencia conforme a los términos de la licencia MIT.  
  
## Conclusión
En el proyecto **Web Personal** se muestra la utilización de framework Django con su modelo  MVT (Model View Template). En esta primera etapa se cumplio con las necesidades esenciales del proyecto donde se permite subir proyectos desde el panel administrador. En una siguiente etapa también se puede pensar en que se puedan gestionar desde el panel Administrador las habilidades del Usuario para que estos puedan ser cargado desde allí y luego ser mostrados en el sitio.
  


