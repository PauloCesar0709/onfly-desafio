# Declaração de uso da IA

## Ferramenta e Modelo

- **Ferramenta**: Claude Code (cli)
- **Modelo**: Claude Opus 5.5

---

## O que a IA fez

- Leu o README.md para melhor contextualização acerca do projeto, além das pastas `src`, `data` e `tests`
- Identificou os 6 defeitos e a causa raiz de cada um
- Validou as correções em uma cópia isolada do projeto e conferiu os totais com um cálculo independente
- Produziu dois documentos de estudo do código. O primeiro consiste em uma análise detalhada sobre o código, acerca de como ele funciona, o que deve fazer e o que esta errado. O segundo trazia o roteiro de correção, juntamente com a justificativa de cada alteração e testes adicionais para validá-las

---

## O que eu fiz

- Estudei e analisei os dois documentos produzidos pela IA (Análise do código e roteiro de correções)
- Apliquei as correções de forma manual em cada um dos problemas encontrados, além de testar a aplicação e conferir se elas tinham sido bem sucedidas 
- Também analisei os testes adicionais sugeridos, escolhi somente os que eram realmente necessários para validar as alterações, escrevi, rodei e conferi todos eles
- Organizei todos os commits realizados, dividindo um para cada correção
- Escrevi a documentação necessária e publiquei o repositório

---

## Porquê escolhi utilizar a IA dessa forma

### Contexto

Como o prazo era apertado para a realização do desafio (menos de 48h) devido a outros compromissos pessoais, juntamente com o pouco conhecimento técnico do código, por causa de ainda me encontrar no 2º período do curso de Engenharia de Software, decidi delegar a tarefa de análise do código e descoberta dos erros para a IA, fazendo com que ele me retornasse dois documentos que me ajudariam a entender mais profundamente sobre o código e o problema, bem como descobrir o que precisava ser alterado e o porquê.

### Aplicação prática

Com os documentos em mãos, realizei um breve estudo sobre o código, podendo compreender mais sobre seu funcionamento, após isso também realizei um estudo com o roteiro de correções, que me fez entender mais acerca dos erros, porquê consertá-los e como fazer isso. Depois, ao finalizar a entrega e escrever toda a documentação, tive mais propriedade para falar o que consertei, qual a linha de raciocínio usada e como realizei as alterações. Além disso, consegui compreender cada teste adicional proposto e implementá-los com sucesso, ao todo foram 4 testes adicionais.

### Técnicas utilizadas

Para este projeto, busquei utilizar a estrutura dos 4Ds (4D Framework) proposto pelo Prof. Rick Dakan e pelo Prof. Joseph Feller, em parceria com a Anthropic.

#### 4D Framework

| Competência | Significado | Como utilizei no projeto |
|-------------|-------------|--------------------------|
| Delegação | Visão clara e escolha estratégica de como a IA se encaixa no processo | Por causa do contexto já indicado e devido as minhas capacidades técnicas serem limitadas para o problema, decidi por deixar a parte de análise e revisão do código para IA, deixando para mim realizar as alterações, implementar os novos testes e escrever a documentação. |
| Descrição | Articular as necessidades e visões de uma forma que prepare a IA para um maior sucesso colaborativo | Construi um prompt de comando detalhado, procurando explicar a IA cada etapa do processo, indicando a ela ações e permissões claras, além de delegar tarefas e mostrar como ela atuaria no projeto. O intuito era utilizar o mínimo de comandos para não lotar a janela de contexto do agente e fazê-lo alucinar |
| Discernimento | Desenvolver o julgamento e a percepção crítica para separar o que é útil do que não é | Realizei toda a revisão dos dois documentos gerados, para verificar se as alterações propostas estavam de acordo com o intuito do programa e a resolução do problema. Dessa forma, analisei se cada alteração e teste adicional recomendado era realmente útil e necessário para o contexto do projeto. Por fim, concluí que todas as alterações eram necessárias, mas que nem todos os testes indicados eram realmente úteis para o projeto, escolhendo, portanto, somente aqueles realmente necessários para validar as alterações. |
| Diligência | Assumir a responsabilidade pelo trabalho com a IA e garantir a qualidade dos produtos finais criados por ela | Devido a esse desafio fazer parte de um processo seletivo para uma vaga de estágio, julguei não ser responsável colocar a IA para realizar as alterações, pois por mais que a minha capacidade técnica atual e o tempo fossem um problema para a resolução, o intuito era que, por meio dos documentos gerados por ela, eu pudesse entender e aprender tudo que necessitava, para assim ter propriedade para avaliar, realizar e julgar cada alteração e cada teste adicional proposto. Além disso, realizar a conferência do que foi gerado por ela, testar e verificar cada alteração me permitiu garantir a qualidade da solução gerada e finalizar esse desafio com êxito. |
