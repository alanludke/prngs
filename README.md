Atribuição de geração de números pseudo-aleatórios e verificação de primos, para o curso de Segurança da Computação da Universidade Federal de Santa Catarina (UFSC).

Para PRNG, escolhi os algoritmos de Lehmer (também conhecido como Park-Miller) e Blum Blum Shub
Para a verificação de primos eu escolhi o método de Fermat e Miller-Rabin.

Para rodar o programa em seu computador, clone o repositório, acesse a localização pelo seu terminal e entre na pasta src com 
``````
cd src
``````

para testar e gerar números pseudo-aleatórios:

``````
py prgn_test.py
``````
isso criará 3 arquivos na sua pasta:
- bbs.txt tem todos os números PR criados para cada tamanho definido usando o algoritmo do BlumBlumShub
- parkMiller.txt tem todos os números PR criados para cada tamanho definido usando o algoritmo de Park-Miller
- results.csv tem o tempo necessário para gerar esses números

para testar os métodos de verificação de prime:
``````
py primes_test.py
``````
Este teste consiste em verificar números primos e não primos, calculando o tempo para cada um deles.

isso criará 2 arquivos na sua pasta:
- fermat_results.csv e miller_rabin_results.csv, com os tempos necessários para verificar números primos e não primos de diferentes tamanhos.

para executar todo o projeto (criar números pseudo-aleatórios e testar se são primos):
``````
py generate_primes.py
``````
isso criará 2 arquivos na sua pasta:
- gerado_primes.csv com os tempos necessários para gerar números primos PR
- gerado_primes.txt com os números primos PR gerados