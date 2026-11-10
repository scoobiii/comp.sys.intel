import sys

def testar_precisao_fpu():
    print("=== Teste de Precisão de Ponto Flutuante ===")
    x = 4195835.0
    y = 3145727.0
    z = x - (x / y) * y
    print(f"X: {x}")
    print(f"Y: {y}")
    print(f"Resultado de x - (x/y)*y: {z}")
    if z == 0.0:
        print("Status: OK (Processador atual sem o bug clássico de 1994).")
    else:
        print("Status: Divergência detectada!")
    print(f"Plataforma: {sys.version}")

if __name__ == "__main__":
    testar_precisao_fpu()
