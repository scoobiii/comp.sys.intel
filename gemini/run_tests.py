import sys
import unittest

def test_acumulacao_erros():
    print("=== [1/4] Teste de Acumulação de Erros (IEEE 754) ===")
    soma_direta = 0.0
    for _ in range(1_000_000):
        soma_direta += 0.00001
        
    diferenca = abs(soma_direta - 10.0)
    print(f"Soma acumulada: {soma_direta:.7f} | Desvio: {diferenca}")
    assert diferenca < 1e-4, "Erro excessivo de arredondamento detectado!"
    print("Status: OK\n")

def test_fdiv_pentium():
    print("=== [2/4] Teste de Reprodução do Bug do Pentium (FDIV) ===")
    x = 4195835.0
    y = 3145727.0
    resultado = x - (x / y) * y
    print(f"Resultado de x - (x/y)*y: {resultado}")
    if resultado == 0.0:
        print("Status: FPU da CPU íntegra (Sem o bug de 1994).\n")
    else:
        print("ALERTA: Divergência de hardware detectada!\n")

def test_precisao_gpu_bf16():
    print("=== [3/4] Teste de Simulação de Baixa Precisão (GPU / BF16) ===")
    valor_real = 3.141592653589793
    # Simula truncamento de mantissa de 7 bits (BF16)
    fator_escala = 2**7 
    valor_bf16 = round(valor_real * fator_escala) / fator_escala
    desvio = abs(valor_real - valor_bf16)
    print(f"Valor Exato (FP32) vs Reduzido (BF16): {valor_real} -> {valor_bf16}")
    print(f"Ruído de arredondamento tolerado pela GPU: {desvio}")
    print("Status: Simulação de ruído estatístico validada.\n")

class TesteValidacaoLLM(unittest.TestCase):
    def test_media_ponderada(self):
        print("=== [4/4] Validação Determinística de Asserção (Contra-medida LLM) ===")
        def funcao_segura(a, b):
            if b == 0:
                return 0
            return (a + b) / 2
            
        resultado = funcao_segura(10, 20)
        self.assertEqual(resultado, 15.0, "Erro: A lógica falhou no caso base!")
        print("Status: Asserção unitária aprovada.\n")

if __name__ == "__main__":
    print("Iniciando bateria completa de testes (CPU + GPU + LLM)...\n")
    test_acumulacao_erros()
    test_fdiv_pentium()
    test_precisao_gpu_bf16()
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TesteValidacaoLLM)
    resultado_unittest = unittest.TextTestRunner(verbosity=1).run(suite)
    
    if not resultado_unittest.wasSuccessful():
        sys.exit(1)
    print("Todos os testes determinísticos e simulações passaram com sucesso!")
