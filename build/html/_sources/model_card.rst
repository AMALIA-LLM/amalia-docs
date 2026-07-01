Ficha do Modelo
===============

O AMALIA é um modelo de linguagem aberto e criado especificamente para o
português de Portugal e para a cultura portuguesa.

Descrição do Modelo
-------------------

O AMALIA é desenvolvido por um consórcio de universidades e centros de
investigação portugueses, incluindo a Universidade NOVA de Lisboa,
Instituto Superior Técnico, Universidade de Coimbra, Universidade do
Porto, Universidade do Minho e pela Fundação para a Ciência e
Tecnologia. O desenvolvimento inclui colaborações com a Universidade
da Beira Interior, Universidade de Évora, e Instituto Superior de Engenharia
de Lisboa.

Esta colaboração é financiada pelos Programas de Desenvolvimento e
Inovação do Governo de Portugal, com o objetivo de criar um assistente
de IA avançado capaz de comunicar eficazmente em português europeu.

O AMALIA utiliza dados de fonte aberta no seu treino, como os dados
provenientes do `Arquivo.pt <https://arquivo.pt/>`__, por exemplo, e
outros dados curados especificamente em português europeu. O treino foi
realizado em duas fases: pré-treino e pós-treino. O pós-treino aplicou
técnicas de *Supervised Fine-Tuning* (SFT) e *Preference Tuning* (usando
*Direct Preference Optimization*, DPO).

O modelo está disponível no `HuggingFace <https://huggingface.co/amalia-llm/AMALIA-9B-0626-DPO>`__.

Detalhes de Treino
------------------

Dados de Treino
~~~~~~~~~~~~~~~

Os seguintes dados foram incluídos na fase de pré-treino do AMALIA:

-  Dados do `Arquivo.pt <https://arquivo.pt>`__, obtidos após
   processamento de coleções de páginas Web públicas e livros gratuitos;
-  Dados de pré-treino do modelo
   `EuroLLM <https://arxiv.org/abs/2506.04079>`__;
-  Amostras de dados de contexto longo
   `Stack-v2 <https://arxiv.org/abs/2402.19173>`__;
-  Dados sintéticos para melhorar a retenção em contexto longo filtrados
   a partir de *datasets* públicos
   (`needle-llama3-16x8k <https://huggingface.co/datasets/lvwerra/needle-llama3-16x8k>`__,
   `needle_32k_finetuning_dataset <https://huggingface.co/datasets/nanotron/needle_32k_finetuning_dataset>`__).

A componente de SFT de pós-treino incluiu uma mistura de dados criados
manualmente, gerados sinteticamente e obtidos de *datasets* públicos.
Estes dados focaram-se em quatro categorias de treino:

-  *Instruction Following* (Seguimento de Instruções):

   -  Dados sintéticos criados utilizando *personas* do
      `PersonaHub <https://arxiv.org/abs/2406.20094>`__ e
      `Nemotron <https://huggingface.co/datasets/nvidia/Nemotron-Personas-USA>`__;
   -  *Dataset* de instruções linguísticas portuguesas criado
      manualmente.

-  *Conversational Reasoning* (Raciocínio Conversacional):

   -  Dados sintéticos criados utilizando *personas* do
      `PersonaHub <https://arxiv.org/abs/2406.20094>`__ e
      `Nemotron <https://huggingface.co/datasets/nvidia/Nemotron-Personas-USA>`__;
   -  *Dataset AMALIA-Hardcoded* com conhecimento autorreferencial;
   -  Dados conversacionais gerados da Wikipedia;
   -  *Splits Chat* e *STEM* do `Nemotron Post-Training
      v1 <https://huggingface.co/datasets/nvidia/Nemotron-Post-Training-Dataset-v1>`__
      e
      `v2 <https://huggingface.co/datasets/nvidia/Nemotron-Post-Training-Dataset-v2>`__;
   -  *Subsets* do
      `smoltalk <https://www.semanticscholar.org/paper/SmolLM2%3A-When-Smol-Goes-Big-Data-Centric-Training-a-Allal-Lozhkov/54145fcb714653b1143bef312fdac821cccbfb62>`__:
      *smol-magpie-ultra* (de qualidade excelente) e *smol-summarize*
      (traduzido);
   -  *Subsets* do `smoltalk2 <https://huggingface.co/blog/smollm3>`__:
      *everyday-conversations* (traduzido) e *Table-GPT*;
   -  Um *split* customizado de SFT do
      `Hermes3 <https://arxiv.org/abs/2408.11857>`__;
   -  Mistura de SFT do `OLMo
      v2 <https://huggingface.co/datasets/allenai/tulu-3-sft-olmo-2-mixture>`__;
   -  `PTradutor <https://ojs.aaai.org/index.php/AAAI/article/view/34704>`__
      para traduções PT\ :math:`\leftrightarrow`\ EN;
   -  `WMT24++ <https://arxiv.org/abs/2502.12404>`__ para traduções
      multilingues\ :math:`\rightarrow`\ PT.

-  Matemática:

   -  Dados sintéticos criados utilizando *personas* do
      `PersonaHub <https://arxiv.org/abs/2406.20094>`__ e
      `Nemotron <https://huggingface.co/datasets/nvidia/Nemotron-Personas-USA>`__;
   -  *Splits Math* e *Code* do `Nemotron Post-Training
      v1 <https://huggingface.co/datasets/nvidia/Nemotron-Post-Training-Dataset-v1>`__
      e
      `v2 <https://huggingface.co/datasets/nvidia/Nemotron-Post-Training-Dataset-v2>`__;
   -  *Dataset* de problemas de matemática de escola primária
      `Orca-Math <https://huggingface.co/datasets/microsoft/orca-math-word-problems-200k>`__.

-  Segurança:

   -  Amostras de segurança do
      `EuroBlocks <https://huggingface.co/datasets/utter-project/EuroBlocks-SFT-Synthetic-1124>`__;
   -  Dados de segurança gerados pelo
      `DeepSeek-V3.2-Exp <https://github.com/deepseek-ai/DeepSeek-V3.2-Exp/blob/main/DeepSeek_V3_2.pdf>`__.

Para a componente de DPO foi usada uma amostra de dados com respostas
geradas em parte pelo próprio AMALIA-SFT. Foram ainda usados os dados:

-  `UltraFeedback <https://arxiv.org/abs/2310.01377>`__;
-  `Abbey4799/Complex-Instructions-DPO <https://huggingface.co/datasets/Abbey4799/Complex-Instructions-DPO>`__;
-  `kira/math-dpo <https://huggingface.co/datasets/kira/math-dpo>`__;
-  `Egida-DPO-Meta-LLaMa-3.1-70B-Instruct <https://link.springer.com/chapter/10.1007/978-3-032-02018-5_39>`__;
-  `HarmfulQA <https://arxiv.org/abs/2308.09662>`__;
-  Um dataset de segurança especifico para o contexto cultural
   português.

Processo de Treino
~~~~~~~~~~~~~~~~~~

No pré-treino, foram maioritariamente seguidos os hiperparâmetros do
EuroLLM, com a nova mistura de dados, aumentando o comprimento máximo de
sequência para 32k *tokens* e melhorando o seu conhecimento de português
europeu.

A fase de SFT visa melhorar as capacidades conversacionais e de
seguimento de instruções do AMALIA, com um foco especial no português
europeu, utilizando os conjuntos de dados descritos em `Dados de
Treino <#dados-de-treino>`__. O treino decorreu durante 76 horas,
recorrendo a 64 GPUs NVIDIA H100, totalizando em 14k *steps*.

A fase de DPO visa alinhar o comportamento do AMALIA com as preferências
humanas, refinando as respostas do modelo através da aprendizagem
baseada em comparações de pares. Nesta fase, o modelo aprende a
distinguir entre respostas de maior e menor qualidade para a mesma
instrução, otimizando-se para gerar *outputs* mais úteis, seguros e
alinhados com os valores desejados, minimizando simultaneamente
comportamentos indesejados, como alucinações, toxicidade ou desvios das
instruções fornecidas. O treino decorreu durante 12 horas, recorrendo a
64 GPUs NVIDIA H100.

Todas as fases de treino foram executadas no supercomputador
`MareNostrum5 <https://www.bsc.es/marenostrum/marenostrum-5>`__, alojado
no Barcelona Supercomputing Center, e no supercomputador `DEUCALION <https://rnca.fccn.pt/en/deucalion/>`__, alojado no Centro Avançado de Computação do Minho.

Avaliação
---------

No âmbito do AMALIA, foram desenvolvidos novos *benchmarks* com o objetivo de avaliar a *performance* do modelo em Português Europeu:

-  `ALBA <https://aclanthology.org/2026.propor-1.69/>`__ (*Automated Linguistics Benchmark for Baseline Assessment*):
   Avalia o desempenho em tarefas linguísticas em português europeu (pt-PT). A avaliação divide-se em oito dimensões: Fonética e Fonologia, Sintaxe, Morfologia, Lexicologia, Semântica Cultural, Jogos de Palavras, Análise do Discurso e Variedade Linguística.
-  `P3B3 <http://arxiv.org/abs/2606.16753>`__ (*pt-PT/pt-BR Bias Benchmark*):
   Avalia o viés (*bias*) dos modelos para as variantes de Português pt-PT e pt-BR.
-  `PHEB <https://lrec.elra.info/lrec2026-main-367>`__ (*Portuguese High School Exams Benchmark*):
   Baseado nos Exames Nacionais do Ensino Secundário de Portugal, avalia a capacidade de resolver tarefas alinhadas com o currículo educacional Português.
-  **CulturaVivaPT**:
   Foca-se na compreensão cultural e no conhecimento específico de Portugal, avaliando para responder a questões sobre temas diversos como festivais, gastronomia, história e desporto.
-  **SAUDADE**:
   Mede a compreensão de eventos históricos e culturais de Portugal sob uma perspetiva temporal.

Adicionalmente, vários *benchmarks* de referência foram traduzidos de inglês para português europeu recorrendo a um modelo de tradução dedicado.

Para garantir avaliações reproduzíveis, o processo de avaliação utiliza a framework `LLM Evaluation Harness <https://github.com/EleutherAI/lm-evaluation-harness>`__ com código e tarefas customizadas disponível no `GitHub <https://github.com/Amalia-LLM/amalia-lm-eval>`__.

Os resultados demonstram que, no ecossistema de modelos totalmente abertos (*fully open-source*), o AMALIA posiciona-se entre os **modelos de referência** para o português europeu, apresentando um desempenho ao nível do estado da arte. Em termos de segurança, o AMALIA encontra-se **alinhado** com os padrões e práticas de segurança observados nos modelos de referência atuais.
