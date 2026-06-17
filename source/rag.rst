Utilização com RAG
==================

*Retrieval Augmented Generation* (RAG), ou geração aumentada por
obtenção de dados, é uma técnica usada para melhorar as respostas por um
LLM com recurso a informação guardada externamente. Desta forma, o
modelo poderá responder de forma mais precisa e com informação factual
em domínios específicos recorrendo a bases de dados de documentos
selecionados.

Um fluxo comum de RAG começa por extrair termos de pesquisa
relevantes a partir da mensagem do utilizador. Com estes termos é feita
uma pesquisa numa base de dados de onde se obtêm um conjunto de documentos
potencialmente relevantes para responder ao utilizador. Estes documentos
são introduzidos no contexto do modelo para a resposta final ser
gerada com as devidas citações.

Indexação e Pesquisa de Documentos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para garantir que os documentos obtidos para o RAG são relevantes para o
utilizador, a pesquisa na base de dados deverá ter uma componente
semântica e não deve basear-se apenas nos termos usados. Por este motivo, é
recomendada a utilização de uma base de dados que permita esta
funcionalidade, como é o caso do
`OpenSearch <https://opensearch.org/>`__.

De forma a tirar partido de pesquisa semântica, é necessário gerar
vetores de *embeddings* semânticos para cada documento usando um modelo
do tipo *SentenceTransformers*, existindo uma variedade de modelos
multilingues deste tipo publicamente disponíveis.

Após proceder à indexação dos documentos na base de dados junto com os
seus vetores de *embeddings*, poderá então ser realizada a pesquisa
semântica com recurso ao mesmo modelo *SentenceTransformers*.

Implementação do Fluxo de RAG
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tendo a base de dados para RAG disponível, é possível definir uma
sequência de *prompts* a enviar ao AMALIA a partir da mensagem do
utilizador. Sendo que este fluxo poderá ter passos diferentes dependendo
do caso de uso, esta secção descreve uma implementação simples para
ilustração.

O primeiro passo poderá passar por detetar se é necessária uma pesquisa
na base de dados para responder ao utilizador. Para tal, pode ser criada
uma *prompt* para o AMALIA com esta questão e a ``mensagem`` original,
junto com um conjunto de regras e exemplos de situações em que deverá ou
não ser feita pesquisa. Um exemplo genérico é:

.. code:: text

   Com base na seguinte frase: "{mensagem}"
   Devemos fazer uma pesquisa na base de dados? Só podes responder com sim ou não.
   Situações em que deves fazer pesquisa:
   - Tens informação limitada ou incerta sobre o assunto
   - Precisas de informação factual atualizada
   - Tens dúvidas sobre a exatidão da tua informação
   - A pergunta requer exatidão ou detalhes específicos
   <...>
   Situações em que não deves fazer pesquisa:
   - Discussões gerais ou opiniões pessoais
   - Cumprimentos ou despedidas
   - Conversas informais que não requerem informação factual
   <...>
   EXEMPLOS:
   Pergunta: "Quem é <pessoa específica>?" → Sim
   Pergunta: "O que é <assunto específico>?" → Sim
   Pergunta: "Como estás?" → Não
   Pergunta: "Olá bom dia!" → Não
   <...>
   A tua resposta [Sim/Não]:

De seguida, caso a resposta anterior seja afirmativa, poder-se-á pedir
ao AMALIA para extrair os termos essenciais da ``mensagem`` original e
aplicar formatações necessárias para melhorar os resultados da pesquisa.
Genericamente, esta *prompt* poderá ter a forma:

.. code:: text

   Com base na pergunta do utilizador, gera uma query de pesquisa para a base de dados.
   Pergunta: "{mensagem}"
   Regras para criar a query:
   - Mantém apenas os termos essenciais
   - Escreve em minúsculas exceto nomes próprios
   - Não uses aspas ou caracteres especiais
   <...>
   EXEMPLOS:
   Pergunta: "Quem é <pessoa específica>?" → Query: "<pessoa específica>"
   Pergunta: "O que é <assunto específico>?" → Query: "<assunto específico>"
   <...>
   Responde apenas completando a próxima frase.
   Query de pesquisa:

Após realizar a pesquisa com a ``query`` e obter um conjunto de
documentos relevantes e as suas fontes, estes poderão ser então
adicionados ao contexto da *prompt* final ao AMALIA para responder à
``mensagem`` original. Um exemplo genérico é:

.. code:: text

   Encontrámos <n> resultados para a pesquisa: {query}

   Aqui estão os resultados:

   <primeiro documento e fonte>

   <segundo documento e fonte>
   <...>

   Com base nesta informação responde ao pedido do utilizador com os dados
   relevantes, citando as fontes necessárias: {user_message}

No final, o utilizador obterá uma resposta correta e detalhada conforme
os documentos indexados na base de dados assim como as suas citações.

Segurança
~~~~~~~~~

Em diversas aplicações, será útil garantir que os pedidos dos utilizadores
respeitam normas de segurança antes de realizar qualquer processamento.

Para este propósito, foi utilizado o `Qwen3Guard <https://qwen.ai/blog?id=qwen3guard>`__
em vários casos de uso do AMALIA, sendo
possível classificar os pedidos dos utilizadores como seguros, inseguros
ou controversos, bem como obter uma categoria para o tipo de insegurança.

Com esta informação, o fluxo da aplicação poderá ser adaptado
para devolver respostas padrão seguras quando os pedidos não são seguros.

