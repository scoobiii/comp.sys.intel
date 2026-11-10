# Módulo Gemini - Análise de Precisão e Infraestrutura

Esta pasta contém registros de análises técnicas, históricos contextuais, reformulações de prompts e programas de teste executáveis gerados em colaboração com o Gemini.

## 📂 Conteúdo
* **`01_contexto_e_resumo.md`**: Histórico detalhado unindo o Bug do Pentium FDIV (1994), evolução dos formatos de ponto flutuante (IEEE 754, BF16, FP8 E4M3/E5M2), arrefecimento de data centers (*Liquid Cooling* a $45^\circ\text{C}$) e os limites das LLMs em engenharia CAD.
* **`02_prompt_reformulado.md`**: Proposta estruturada de otimização da pergunta original dividida em eixos técnicos claros.
* **`teste_fpu.py`**: Script executável em Python para validação e teste de comportamento de ponto flutuante na FPU local (inspirado no clássico Bug do Pentium).
* **`teste_gpu_precisao.py`**: Script de simulação de perda de mantissa em formatos de baixa precisão (BF16/FP8) típicos de aceleração por GPU em IA.
* **`run_tests.py`**: Suite unificada de testes automatizados combinando verificação de CPU, simulação de GPU e asserções unitárias determinísticas.

---
* **Versão:** 1.3.0
* **Assinatura:** `Gemini-AI-Signed-Key-2026-v1`
