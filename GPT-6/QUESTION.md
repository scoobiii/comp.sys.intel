# PERGUNTA

## Questão original

Como o caso Pentium FDIV de 1994 pode ser reproduzido em um Android
ARM64 usando Termux? Quantas casas decimais os processadores atuais
conseguem representar com precisão? Qual a relação entre FPU, CPU e
GPU? Como precisão numérica, temperatura, desempenho e consumo
energético afetam LLMs e projetos CAD? A adoção de refrigeração
líquida com fornecimento de água a 45 °C decorre de evolução
tecnológica, economia ou regulamentação?

## Pergunta reformulada por GPT-6

Como construir um benchmark reproduzível de integridade
computacional, executável em Android ARM64/Termux, que permita
comparar a precisão numérica e a estabilidade de CPU, FPU, GPU e
LLMs, usando o Pentium FDIV como referência histórica?

O benchmark deve:

1. Reproduzir os casos históricos do FDIV.
2. Distinguir precisão binária, dígitos significativos e erro numérico.
3. Comparar FP64, FP32, FP16, BF16 e formatos quantizados quando
   efetivamente suportados pelo hardware/software.
4. Medir desempenho, temperatura, frequência e energia quando
   houver sensores e instrumentos disponíveis.
5. Avaliar se a quantização altera a qualidade das respostas de LLM.
6. Verificar geometria CAD com critérios determinísticos:
   dimensões, volume, bounding box, topologia e validade do sólido.
7. Relacionar eficiência térmica do datacenter com energia por
   operação útil e validada.
8. Registrar código, ambiente, versões, resultados e SHA-256.

Hipótese central:
Desempenho computacional não equivale a integridade numérica,
e integridade numérica não equivale à correção semântica de um LLM.
