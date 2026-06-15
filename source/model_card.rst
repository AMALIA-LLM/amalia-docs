Model Card
==========

O AMALIA é um modelo de linguagem aberto e criado especificamente para o
português de Portugal e para a cultura portuguesa.

Descrição do Modelo
-------------------

O AMALIA é desenvolvido por um consórcio de universidades e centros de
investigação portugueses, incluindo a Universidade NOVA de Lisboa,
Instituto Superior Técnico, Universidade de Coimbra, Universidade do
Porto, Universidade do Minho e pela Fundação para a Ciência e
Tecnologia.

Esta colaboração é financiada pelos Programas de Desenvolvimento e
Inovação do Governo de Portugal, com o objetivo de criar um assistente
de IA avançado capaz de comunicar eficazmente em várias linguagens, mas
com foco no português europeu.

O AMALIA utiliza dados de fonte aberta no seu treino, como os dados
provenientes do `Arquivo.pt <https://arquivo.pt/>`__, por exemplo, e
outros dados curados especificamente em português europeu. O treino foi
realizado em duas fases: pré-treino e pós-treino. O pós-treino aplicou
técnicas de *Supervised Fine-Tuning* (SFT) e *Preference Tuning* (usando
*Direct Preference Optimization*, DPO).

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
   (`1 <https://huggingface.co/datasets/lvwerra/needle-llama3-16x8k>`__,
   `2 <https://huggingface.co/datasets/nanotron/needle_32k_finetuning_dataset>`__).

A componente de SFT de pós-treino incluiu uma mistura de dados criados
manualmente, gerados sintenticamente e obtidos de *datasets* públicos.
Estes dados focaram-se em quatro categorias de treino:

-  *Instruction Following* (Seguimento de Instruções):

   -  Dados sintéticos criados por *personas* do
      `PersonaHub <https://arxiv.org/abs/2406.20094>`__ e
      `Nemotron <https://huggingface.co/datasets/nvidia/Nemotron-Personas-USA>`__;
   -  *Dataset* de instruções linguísticas portuguesas criado
      manualmente.

-  *Conversational Reasoning* (Raciocínio Conversacional):

   -  Dados sintéticos criados por *personas* do PersonaHub e Nemotron;
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

   -  Dados sintéticos criados por *personas* do PersonaHub e Nemotron;
   -  *Splits Math* e *Code* do Nemotron Post-Training v1 and v2;
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
sequência para 32K *tokens* e melhorando o seu conhecimento de português
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
instrução, optimizando-se para gerar *outputs* mais úteis, seguros e
alinhados com os valores desejados, minimizando simultaneamente
comportamentos indesejados, como alucinações, toxicidade ou desvios das
instruções fornecidas. O treino decorreu durante 12 horas, recorrendo a
64 GPUs NVIDIA H100.

Todas as fases de treino foram executadas no supercomputador
`MareNostrum5 <https://www.bsc.es/marenostrum/marenostrum-5>`__, alojado
no Barcelona Supercomputing Center.

Avaliação
---------

No âmbito do AMALIA, foram desenvolvidos dois *benchmarks* com o
objetivo de avaliar a performance linguística do modelo: 

- **ALBA** (*Automated Linguistics Benchmark for Baseline Assessment*): um
  *benchmark* desenvolvido de modo a obter um teste diagnóstico que
  providencia uma visão geral das capacidades do modelo e cujo objetivo é
  avaliar a performance de LLMs em tarefas linguísticas em português
  europeu. Para tal, foram selecionadas oito dimensões: Fonética e
  Fonologia, Sintaxe, Morfologia, Lexicologia, Semântica Cultural, Jogos
  de Palavras, Análise do Discurso e Variedade Linguística; 
- **P3B3** (*pt-PT/pt-BR Bias Benchmark*): um *benchmark* cujo objetivo é avaliar o
  viés entre variedades de português em LLMs devido ao desequilíbrio de
  dados disponíveis nas variedades de português europeu e de português do
  Brasil.

Adicionalmente, foi criado um *benchmark* com os Exames Nacionais do
Ensino Secundário em Portugal e foram ainda traduzidos outros
*benchmarks* de inglês para português europeu usando um modelo de
tradução dedicado.

A avaliação mostra que, dentro dos modelos abertos, **o AMALIA é o
modelo aberto estado da arte em Português Europeu**, apresentando melhor
*performance* que modelos abertos anteriores. Em raciocínio e
compreensão linguística, o modelo tem *performance* comparável com o
estado da arte, revelando excelente qualidade e fluência em texto
Português Europeu em tarefas generativas.

Em termos de segurança, o AMALIA demonstra-se alinhado com os padrões de
segurança do estado da arte.
