import sys
import unittest

def test_acumulacao_erros():
    print("=== [1/3] Teste de Acumulação de Erros (IEEE 754) ===")
    soma_direta = 0.0
    for _ in range(1_000_000):
        soma_direta += 0.00001
        
    diferenca = abs(soma_direta - 10.0)
    print(f"Soma acumulada: {soma_direta:.7f} | Desvio: {diferenca}")
    assert diferenca < 1e-4, "Erro excessivo de arredondamento detectado!"
    print("Status: OK\n")

def test_fdiv_pentium():
    print("=== [2/3] Teste de Reprodução do Bug do Pentium (FDIV) ===")
    x = 4195835.0
    y = 3145727.0
    resultado = x - (x / y) * y
    print(f"Resultado de x - (x/y)*y: {resultado}")
    if resultado == 0.0:
        print("Status: FPU íntegra (Sem o bug de 1994).\n")
    else:
        print("ALERTA: Divergência de hardware detectada!\n")

class TesteValidacaoLLM(unittest.TestCase):
    def test_media_ponderada(self):
        print("=== [3/3] Validação Determinística de Asserção (Contra-medida LLM) ===")
        # Função simulando lógica correta validada por teste unitário
        def funcao_segura(a, b):
            if b == 0:
                return 0
            return (a + b) / 2
            
        resultado = funcao_segura(10, 20)
        self.assertEqual(resultado, 15.0, "Erro: A lógica falhou no caso base!")
        print("Status: Asserção unitária aprovada.\n")

if __name__ == "__main__":
    print("Iniciando bateria de testes do comp.sys.intel...\n")
    test_acumulacao_erros()
    test_fdiv_pentium()
    
    # Roda os testes unitários baseados em classe
    suite = unittest.TestLoader().loadTestsFromTestCase(TesteValidacaoLLM)
    resultado_unittest = unittest.TextTestRunner(verbosity=1).run(suite)
    
    if not resultado_unittest.wasSuccessful():
        sys.exit(1)
    print("Todos os testes determinísticos passaram com sucesso!")
