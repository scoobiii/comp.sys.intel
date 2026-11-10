# CONTEXTO

O Pentium FDIV foi um defeito de implementação da unidade de ponto
flutuante dos processadores Intel Pentium P5.

Cronologia:
- 30/10/1994: Thomas R. Nicely comunica o erro.
- 03/11/1994: Terje Mathisen publica confirmação e programa de teste
  no newsgroup comp.sys.intel.
- 04/11/1994: Andreas Kaiser divulga outros operandos afetados.
- 14-15/11/1994: Tim Coe e Cleve Moler ampliam a análise pública.

O exemplo clássico:
x = 4195835
y = 3145727

A expressão x - (x/y)*y deveria resultar em zero, dentro dos
limites de arredondamento da representação utilizada.
Em determinados Pentium defeituosos, o resultado podia ser 256.

Outro teste histórico:
x = 824633702441
x * (1/x)

Pentiums afetados podiam retornar:
0.999999996274709702

A falha estava associada a entradas ausentes na tabela de constantes
do algoritmo SRT radix-4 da unidade FDIV.

Referência histórica:
Cleve Moler:
https://blogs.mathworks.com/cleve/2013/04/29/pentium-division-bug/

Repositório histórico:
https://groups.google.com/g/comp.sys.intel/c/_7nkf1iyxaU

Nota de correção:
A publicação de Mathisen foi em comp.sys.intel.
A afirmação anterior de que teria sido em comp.soft-sys.intel estava
incorreta.
