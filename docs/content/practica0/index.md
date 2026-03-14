---
title: "Práctica 0: Markdown, Git, GitHub y Hugo"
date: 2026-03-12
draft: false
author: " Josselyn Alexa Rivera Chavez 379219"
categories: ["Paradigmas de Programación"]
tags: ["Markdown", "Git", "GitHub", "Hugo"]
---

# Reporte de practica 0: Uso de Markdown, Git, GitHub y Hugo

**Materia:** Paradigmas de la Programación  
**Docente:** M.I. José Carlos Gallegos Mariscal  
**Alumno:** Josselyn Alexa Rivera Chavez 
**Matrícula:** 379219
**Grupo:** 941 
---
En esta práctica se investigaron y utilizaron diferentes herramientas que son comunes en el desarrollo de software y en la publicación de documentación técnica. Estas herramientas permiten escribir documentación de manera sencilla, llevar control de versiones del código y publicar páginas web estáticas.

El reporte se divide en tres sesiones. En la primera se explica qué es Markdown y su sintaxis básica. En la segunda se describe el uso de Git y GitHub para el control de versiones. Finalmente, en la tercera sesión se explica cómo combinar estas herramientas con Hugo y GitHub Actions para crear y publicar una página estática.

---

# Primera sesión  
## Sintaxis y uso de Markdown

### ¿Qué es Markdown?

Markdown fue desarrollado en 2004 por John Gruber, y se refiere tanto a una manera de crear archivos de texto con formato simple como a una herramienta basada en el lenguaje de programación Perl que permite convertir esos archivos a HTML.

La idea principal de Markdown es que los archivos puedan leerse fácilmente como texto plano, pero que al mismo tiempo puedan convertirse a páginas web. Esto facilita la creación de documentación sin necesidad de utilizar editores complejos.

Muchos generadores de sitios estáticos y plataformas de desarrollo aceptan este formato. Por ejemplo, Github permite escribir documentación utilizando Markdown y la convierte automáticamente a HTML para su visualización en la web. Además, herramientas como Pandoc permiten convertir archivos Markdown a otros formatos como PDF, HTML o Word.

Los archivos Markdown se guardan normalmente con la extensión `.md` y pueden abrirse con editores de texto como Notepad, Sublime Text o Vim.

---
### ¿Cómo se utiliza Markdown?

Markdown se utiliza escribiendo texto plano junto con ciertos símbolos que permiten aplicar formato al contenido. Por ejemplo, el símbolo # se utiliza para crear títulos, los asteriscos permiten escribir texto en negrita o cursiva, y los guiones permiten crear listas.

Los archivos se guardan con la extensión `.md` y pueden abrirse con cualquier editor de texto como Notepad, Sublime Text o Visual Studio Code.

Posteriormente estos archivos pueden convertirse a HTML o a otros formatos mediante diferentes herramientas o plataformas que interpretan la sintaxis de Markdown.

---
### Sintaxis básica de Markdown

Markdown utiliza una sintaxis sencilla basada en símbolos para dar formato al texto.

#### Encabezados

Los encabezados se crean utilizando el símbolo `#`.

```
# Título principal
## Subtítulo
### Subsección
```

#### Texto en negrita y cursiva

```
**Texto en negrita**
*Texto en cursiva*
```

#### Listas

Lista con viñetas:

```
- Elemento 1
- Elemento 2
- Elemento 3
```

Lista numerada:

```
1. Primer elemento
2. Segundo elemento
3. Tercer elemento
```

#### Enlaces

```
[Texto del enlace](https://ejemplo.com)
```

#### Imágenes

```
![Texto alternativo](imagen.png)
```

#### Bloques de código

```python
print("Hola mundo")
```

Estas herramientas permiten organizar información de manera clara y sencilla, por lo que Markdown es ampliamente utilizado para escribir documentación técnica.

---

# Segunda sesión  
## Uso de Git y GitHub

### ¿Qué es Git y GitHub?

En el desarrollo de software es importante poder registrar los cambios que se realizan en un proyecto. Para esto se utilizan sistemas de control de versiones.

Git es un sistema de control de versiones distribuido de código abierto que permite realizar un seguimiento de los cambios en los archivos de un proyecto, como el código fuente o la documentación. Gracias a Git es posible regresar a versiones anteriores, trabajar en diferentes ramas y colaborar con otras personas.

Por otro lado, Github es una plataforma que permite almacenar repositorios Git en la nube. Funciona como un servidor remoto donde los desarrolladores pueden subir sus proyectos, colaborar con otros usuarios y mantener un respaldo del código.

La diferencia principal es que Git funciona de manera local en la computadora del desarrollador, mientras que GitHub permite compartir esos repositorios en internet.

---

### Comandos esenciales de Git

Para utilizar Git desde la terminal existen varios comandos básicos que permiten gestionar los cambios del proyecto.

Inicializar un repositorio:

```
git init
```

Preparar archivos para guardar cambios:

```
git add .
```

Guardar los cambios en el historial del repositorio:

```
git commit -m "mensaje"
```

Vincular el repositorio local con el repositorio remoto en GitHub:

```
git remote add origin URL_DEL_REPOSITORIO
```

Subir los cambios al repositorio remoto:

```
git push -u origin main
```

Consultar el estado del repositorio:

```
git status
```

Descargar cambios del repositorio remoto:

```
git pull
```

---

### Pasos para crear un repositorio en GitHub

1. Crear una cuenta en GitHub.
2. En la página principal seleccionar la opción **New repository**.
3. Escribir un nombre para el repositorio.
4. Agregar una descripción opcional.
5. Seleccionar si el repositorio será público o privado.
6. Hacer clic en **Create repository**.

Una vez creado el repositorio se pueden subir archivos desde la terminal utilizando Git o directamente desde la página web.

---

### Cómo subir información a GitHub

Existen dos formas principales de subir archivos.

**Usando la terminal**

1. Abrir la carpeta del proyecto.
2. Ejecutar:

```
git init
git add .
git commit -m "Primer commit"
git remote add origin URL_DEL_REPOSITORIO
git push -u origin main
```

**Usando la página web**

1. Abrir el repositorio en GitHub.
2. Seleccionar la opción **uploading an existing file**.
3. Arrastrar los archivos al navegador.
4. Confirmar los cambios con **Commit changes**.

---

# Tercera sesión  
## Uso de Hugo y GitHub Actions

Para publicar páginas web de manera sencilla se pueden utilizar generadores de sitios estáticos.

Hugo es un generador de sitios estáticos muy rápido que permite crear páginas web utilizando archivos Markdown. Hugo genera archivos HTML, CSS y JavaScript que pueden publicarse fácilmente en internet.

Por otro lado, GitHub Actions permite automatizar procesos dentro de GitHub. En este caso se puede utilizar para compilar el sitio generado con Hugo y publicarlo automáticamente en GitHub Pages cada vez que se suban cambios al repositorio.

---

### Crear un sitio estático con Hugo

Primero se debe instalar Hugo en el sistema. Después se puede crear un nuevo sitio ejecutando el siguiente comando:

```
hugo new site mi-sitio
```

Entrar a la carpeta del proyecto:

```
cd mi-sitio
```

Inicializar el repositorio Git:

```
git init
```

Agregar un tema al sitio:

```
git submodule add https://github.com themes/ananke
```

Configurar el tema en el archivo de configuración:

```
theme = "ananke"
```

Crear una nueva entrada o publicación:

```
hugo new posts/mi-primer-post.md
```

Para visualizar el sitio de forma local se puede ejecutar:

```
hugo server -D
```

Después se puede abrir el navegador y acceder a:

```
http://localhost:1313
```

---

### Subir el sitio a GitHub

Para publicar el sitio es necesario subir el proyecto a GitHub.

```
git add .
git commit -m "Sitio inicial de Hugo"
git branch -M main
git remote add origin URL_DEL_REPOSITORIO
git push -u origin main
```

Una vez que el repositorio se encuentra en GitHub, se puede configurar GitHub Actions para que genere automáticamente el sitio y lo publique en GitHub Pages.

---
## Enlaces del proyecto

Repositorio del portafolio en GitHub:  
https://github.com/JosselynAlexa/portafolio-PP

Página publicada en GitHub Pages:  
https://josselynalexa.github.io/portafolio-PP/practica0/
