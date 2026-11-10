# PLANO DE TESTES — ANDROID / TERMUX

## Ambiente

- Android ARM64
- Termux
- Clang
- C
- IEEE 754, quando suportado

## Instalação

pkg update
pkg install clang git coreutils -y

## Testes

1. Compilar sem otimizações agressivas.
2. Executar os operandos históricos.
3. Registrar DBL_MANT_DIG, DBL_DIG e LDBL_MANT_DIG.
4. Comparar resultados com referência independente.
5. Repetir com diferentes opções de compilação.
6. Registrar CPU, sistema operacional, compilador e versão.
7. Comparar resultados com implementação de precisão arbitrária.

## Critérios

- Reprodutibilidade.
- Erro absoluto e relativo.
- Precisão efetiva.
- Ausência de fast-math nos testes de referência.
- Registro de ambiente e hashes.

## Limitação

O teste moderno não prova ausência de qualquer falha na CPU.
Ele verifica apenas os operandos e operações exercitados.
O teste histórico deve reproduzir o programa original de Mathisen
quando seu código-fonte for obtido e conferido.
