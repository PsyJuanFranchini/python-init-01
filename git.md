# Guía para trabajar con [GIT](https://git-scm.com/)

`git` es un sistema de control de versiones que permite administrar principalmente proyectos de software (y otros tipos de proyectos también).

Existen diferentes formas de usar `git`. La principal es usando CLI (línea de comandos). Otra forma puede ser a través de interfaces gráficas: entornos de desarrollo como `Intellij`, `Visual Studio Code`, etc, etc.

`Bitbucket` o `Github` son empresas que proveen los servidores para poder hacer el código distribuido, además de otras funcionalidades. Estas empresas hacen uso de `git` para ofrecer dichos servicios.

Para profundizar más sobre `git`, se recomienda [Git Book](https://git-scm.com/book/en/v2)

## git CLI (línea de comandos)

### Cómo clonar el repositorio en mi computadora (en otras palabras mi "local")?
```
git clone https://github.com/Bipost/front-end.git [Nombre de la carpeta en mi compu]
// o usando SSH
git clone git@github.com:Bipost/front-end.git [Nombre de la carpeta en mi compu]
```

### Cómo cambiar de branch?
```
git checkout [nombre del branch]

// Ejemplos:
git checkout master
git checkout develop
git checkout feature-BIP-XX
```

### Cómo crear un nuevo branch?
```
// Ejecutar en el branch desde el cual quiero crear el nuevo branch
git checkout -b [nombre del branch]

// Ejemplo:
git checkout -b feature-BIP-XX
```
Nota importante: se recomienda no usar `/` en los nombres de branch.

### Cómo veo los cambios que hice hasta el momento?
```
git status
// o
git diff
```

### Cómo agregar los cambios/archivos nuevos para hacer el commit?
```
git add [aca el/los archivo/s]

// Ejemplo:
git add src/components/contacts/contact.js src/app/App.js
```

### Cómo agregar TODOS los cambios/archivos nuevos para hacer el commit?
```
git add .
```

### Cómo hacer el commit?
```
git commit -m "Mensaje del commit"
```

### Ya hice el commit/s. Cómo envío los cambios al repositorio remoto (a Github)?
```
git push origin [nombre de mi branch]
```
Ejemplo:
```
git push origin feature-BIP-XX
```

### Cómo actualizo mi branch con lo que está en develop?
Ejecute en ORDEN los siguientes comandos:
```
git checkout develop
git pull origin develop
git checkout [mi branch]  // ejemplo: git checkout feature-BIP-XX
git rebase develop
git push origin [mi branch] // envía los cambios a Github
```

### Cómo agrego más cambios al último commit que hice?
```
git add .
git commit --amend
```

### Cómo veo la lista de commits de mi branch?
```
git log
```