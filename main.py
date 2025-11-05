def saludo(nombre: str) -> str:
    return f"hola, {nombre}! bienvenido a git, commit exitoso."

if __name__ == "__main__":
    nombre = input("¿tu nombre? ")
    print(saludo(nombre))
    