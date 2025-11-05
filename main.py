def saludo(nombre: str) -> str:
    return f"hola, {nombre}! bienvenido a git, commit exitoso :3"

if __name__ == "__main__":
    nombre = input("¿tu nombre? ")
    print(saludo(nombre))
    print("editar desde github")
