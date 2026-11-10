import sys
import math

def simular_truncamento_bf16(valor):
    """
    Simula o efeito de truncamento de mantissa do formato BF16 (Bfloat16),
    comum em GPUs de IA para acelerar o treinamento e inferência.
    O BF16 reduz a precisão da mantissa para 7 bits (contra 23 do FP32).
    """
    # Representação didática de perda de precisão por arredondamento agressivo
    # Multiplicamos por um fator de perda de resolução e arredondamos
    fator_escala = 2**7 # 7 bits de mantissa no BF16
    return round(valor * fator_escala) / fator_escala

def test_precisao_gpu_vs_cpu():
    print("=== Teste de Simulação: Precisão Reduzida (CPU vs GPU / BF16) ===")
    
    # Valor de referência de alta precisão (FP32)
    valor_real = 3.141592653589793
    
    # Simulando a mesma operação em baixa precisão (comportamento de GPU em IA)
    valor_bf16_simulado = simular_truncamento_bf16(valor_real)
    
    # Calculando o desvio provocado pela otimização de hardware
    desvio = abs(valor_real - valor_bf16_simulado)
    
    print(f"Valor Exato (FP32):          {valor_real}")
    print(f"Valor Reduzido (BF16/GPU):   {valor_bf16_simulado}")
    print(f"Ruído de Arredondamento:     {desvio}")
    
    # O teste unitário valida que o desvio existe, justificando por que 
    # a GPU é ótima para estatística de IA mas péssima para CAD/Engenharia exata
    assert desvio > 0, "Erro: Esperava-se perda de precisão na simulação de baixa precisão."
    print("Status: Divergência de arredondamento de hardware mapeada com sucesso!\n")

if __name__ == "__main__":
    print("Iniciando simulação de comportamento de GPU em baixa precisão...\n")
    test_precisao_gpu_vs_cpu()
    print("Teste de GPU concluído com sucesso!")
