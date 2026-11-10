# Histórico de Conversa, Contexto e Programas de Teste

## 1. Resumo do X-Thread / Contexto Histórico (O Bug do Pentium)
* **A Descoberta:** Em 1994, o professor Thomas Nicely descobriu erros de precisão na FPU de processadores Intel Pentium enquanto calculava somas de recíprocos de primos gêmeos.
* **A Propagação:** A falha foi comunicada via CompuServe, investigada por Terje Mathisen na Noruega (que escreveu o primeiro código de teste em assembly) e divulgada no newsgroup `comp.sys.intel` em 3 de novembro de 1994.
* **A Falha Técnica:** O erro ocorria em divisões (`FDIV`) devido a entradas ausentes numa tabela de consulta (*lookup table*). Exemplo clássico: $x = 4195835$ e $y = 3145727$, onde a fórmula $z = x - (x/y) \times y$ deveria resultar em $0$, mas o Pentium afetado retornava $256$.

## 2. Contexto Moderno: Precisão, Hardware e Data Centers
* **Padrão IEEE 754:** Precisão simples (32-bit, ~7 dígitos) e dupla (64-bit, ~15-17 dígitos). Formatos de IA modernos (BF16, FP8 E4M3/E5M2) sacrificam mantissa para ganhar largura de banda e velocidade.
* **Liquid Cooling e Data Centers ($45^\circ\text{C}$):** A transição para refrigeração líquida e operação a $45^\circ\text{C}$ combate o limite físico de chips que ultrapassam 1000W, evitando falhas catastróficas de *thermal throttling* (como as ocorridas no Google).
* **Limitações das LLMs em CAD:** Modelos de linguagem operam por aproximação probabilística de tokens. Projetos de engenharia exigem restrições geométricas formais e determinísticas; a LLM serve como geradora de scripts (ex: OpenSCAD), mas a validação matemática cabe a motores CAD.

---
Metadata & Assinatura Digital:
Responsável: Gemini (AI Collaborator)
Versão: 1.2.1
Data: 2026-11-10
Assinatura: Gemini-AI-Signed-Key-2026-v1
