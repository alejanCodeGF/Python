# * ¡Estoy de celebración! He publicado mi primer libro:
# * "Git y GitHub desde cero"
# * - Papel: mouredev.com/libro-git
# * - eBook: mouredev.com/ebook-git
# *
# * ¿Sabías que puedes leer información de Git y GitHub desde la gran
# * mayoría de lenguajes de programación?
# *
# * Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
# * - Hash
# * - Autor
# * - Mensaje
# * - Fecha y hora
# *
# * Ejemplo de salida:
# * Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
# *
# * Se permite utilizar librerías que nos faciliten esta tarea.

import git

# Ruta del repositorio
repo_path = r"B:\Programación (Github)\retos-programacion-2023"

# Crear objeto Repo
repo = git.Repo(repo_path)

# Obtener los últimos 10 commits
commits = repo.iter_commits(max_count=10)

# Mostrar información de cada commit
for commit in commits:
    print("Hash: ", commit.hexsha)
    print("Autor: ", commit.author.name)
    print("Mensaje: ", commit.message, end="")
    print("Fecha y hora: ", commit.authored_datetime)
    print("-----------------------")