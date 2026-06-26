Multimodal Model Card
=====================

O AMALIA-VL é um modelo de multimodal (visão e linguagem) aberto e criado especificamente para o
português de Portugal e para a cultura portuguesa.

Descrição do Modelo
-------------------

O AMALIA-VL é desenvolvido no âmbito do projeto AMALIA.

O projeto AMALIA é desenvolvido por um consórcio de universidades e centros de
investigação portugueses, incluindo a Universidade NOVA de Lisboa,
Instituto Superior Técnico, Universidade de Coimbra, Universidade do
Porto, Universidade do Minho e pela Fundação para a Ciência e
Tecnologia. O desenvolvimento inclui colaborações com a Universidade
da Beira Interior, Universidade de Évora, e Instituto Superior de Engenharia
de Lisboa.

Esta colaboração é financiada pelos Programas de Desenvolvimento e
Inovação do Governo de Portugal, com o objetivo de criar um assistente
de IA avançado capaz de comunicar de forma eficaz em português europeu.

O AMALIA-VL utiliza dados de fonte aberta no seu treino, e
outros dados curados especificamente em português europeu. O AMALIA-VL é treinado com pós treino a partir do AMALIA. O treino foi feito em três
fases: *Modality Alignment*, *Visual Instruction Following* e *Preference Tuning*.
As primeiras duas fases são realizadas através de *Supervised Fine-Tuning* (SFT),
e a última fase é realizada usando *Direct Preference Optimization* (DPO).

Detalhes de Treino Multimodal
-----------------------------

Dados de Treino
~~~~~~~~~~~~~~~

Para a primeira fase, *Modality Alignment*, foram usados 500.000 pares de imagem e texto do
dataset `PD12M <https://huggingface.co/datasets/PD12M>`__. Estes foram parcialmente traduzidos
para português europeu através do `Gemma 3 <https://arxiv.org/abs/2503.19786>`__.

Para a seguinte fase, *Visual Instruction Following*, foi adotada uma mistura de dados sintéticos
e dados públicos, que se dividem nas seguintes categorias:

-  *Image Grounding* (Ancoragem de respostas a imagens):

   -  Splits de extração de bounding boxes (caixas de coordenadas visuais) do `Nemotron VLM Dataset v2 <https://huggingface.co/datasets/nvidia/Nemotron-VLM-Dataset-v2>`__.

-  *General VQA* (Perguntas e Respostas Visuais Gerais):

   -  Dados sintéticos criados para perguntas e respostas visuais com foco em português europeu, usando coleções de imagens abertas como o `PD12M <https://huggingface.co/datasets/PD12M>`__ e o `Open Images <https://storage.googleapis.com/openimages/web/index.html>`__;
   -  *Dataset AMALIA-Hardcoded* com conhecimento autorreferencial;
   -  Dados conversacionais gerados a partir da Wikipedia;
   -  *Splits* de *VQA* do `Nemotron VLM Dataset v1 <https://huggingface.co/datasets/nvidia/Llama-Nemotron-VLM-Dataset-v1>`__;
   -  Vários outros conjuntos de dados públicos de *VQA* obtidos através da coleção `FineVision <https://huggingface.co/datasets/HuggingFaceM4/FineVision>`__, incluindo:

      -  `VQAv2 <https://visualqa.org>`__;
      -  `VisDialog <https://visualdialog.org>`__;
      -  `MMEvol <https://arxiv.org/pdf/2409.05840>`__;
      -  `LLaVA-150k <https://huggingface.co/datasets/liuhaotian/LLaVA-Instruct-150K>`__.

-  *OCR* (Extração Óptica de Caracteres):

   -  Dados sintéticos criados para reconhecimento visual de código;
   -  *Splits* de *OCR* do `Nemotron VLM Dataset v1 <https://huggingface.co/datasets/nvidia/Llama-Nemotron-VLM-Dataset-v1>`__;
   -  `IIIT-5k <https://cvit.iiit.ac.in/research/projects/cvit-projects/the-iiit-5k-word-dataset>`__.

-  *OCR QA* (Perguntas e Respostas sobre texto em imagens):

   -  Dados sintéticos em português europeu para reconhecimento e compreensão visual de texto;
   -  `TextVQA <https://textvqa.org>`__;
   -  `OCR-VQA <https://ocr-vqa.github.io>`__.

-  *Chart & Table Understanding* (Compreensão de Gráficos e Tabelas):

   -  Dados sintéticos para compreensão de gráficos e tabelas em português europeu e contextos multilingues;
   -  Conjuntos de dados de compreensão de gráficos e tabelas do `Nemotron VLM Dataset v1 <https://huggingface.co/datasets/nvidia/Llama-Nemotron-VLM-Dataset-v1>`__ e `v2 <https://huggingface.co/datasets/nvidia/Nemotron-VLM-Dataset-v2>`__.

-  Outros:

   -  Dados sintéticos para descrição de imagens e compreensão de cenas, em português europeu e inglês;
   -  Dados sintéticos para conhecimento e reconhecimento de cultura portuguesa;
   -  Dados sintéticos para compreensão e interpretação de código em imagens;
   -  Dados públicos de compreensão matemática visual:

      -  `CLEVR-Math <https://arxiv.org/abs/2208.05358>`__;
      -  `Geomverse <https://arxiv.org/abs/2312.12241>`__;
      -  `CoSyn-Math <https://huggingface.co/datasets/allenai/CoSyn-400K>`__;
   -  Dados sintéticos e públicos para compreensão de documentos visuais, incluindo `DocVQA <https://docvqa.org>`__;
   -  Reutilização de dados de instrução textual do AMALIA-LLM para preservar o alinhamento entre as capacidades de linguagem e visão do modelo.

Para a fase final, de otimização de preferências, foram utilizados os seguintes conjuntos de dados:

-  `MMPR <https://huggingface.co/datasets/OpenGVLab/MMPR-v1.2>`__: um dataset de otimização de preferências multimodal, usado no treino do modelo `InternVL 3.5 <https://arxiv.org/abs/2508.18265>`__;
-  Dados sintéticos de otimização de preferências multimodal, criados com base nos conjuntos de dados de treino da fase anterior, com o objetivo de melhorar a capacidade do modelo distinguir respostas de maior e menor qualidade para a mesma instrução.

Processo de Treino
~~~~~~~~~~~~~~~~~~

A fase inicial de *Modality Alignment* tem como objetivo alinhar as
representações de visão e linguagem do modelo, permitindo que o
AMALIA-VL compreenda e integre informações visuais e textuais de forma
eficaz. Para isto, apenas é treinado o conetor de modalidades, mantendo
ambos os modelos de visão e linguagem congelados. Esta fase demorou 4
horas em 8 GPUs NVIDIA H100, totalizando 2k *steps*.

A segunda fase, de *Visual Instruction Following*, tem como objetivo
ensinar o modelo a seguir instruções visuais e executar variadas tarefas
com base em *inputs* visuais, incluindo perguntas e respostas visuais,
ancoragem de respostas a imagens, compreensão de gráficos e tabelas,
reconhecimento de texto em imagens e compreensão de cenas. Nesta fase,
o modelo é treinado em regime de *Supervised Fine-Tuning* (SFT) e todos os
parâmetros do modelo são treinados. Aqui, o modelo tem um contexto
máximo de 16384 *tokens*, e uma capacidade de até 7800 *tokens* visuais por
imagem. O treino decorreu durante 96 horas, recorrendo a 128 GPUs NVIDIA
H100, totalizando 49k *steps*.

A fase final de treino, de DPO, visa refinar as respostas do modelo através
da aprendizagem baseada em comparações de pares. Nesta fase, para a mesma instrução, o modelo aprende a
maximizar a probabilidade de gerar respostas de maior qualidade e minimizar a
probabilidade de gerar respostas de menor, otimizando-se para gerar *outputs* mais úteis, seguros e
alinhados com os valores desejados, minimizando simultaneamente
comportamentos indesejados, como alucinações, toxicidade ou desvios das
instruções fornecidas. O treino decorreu durante 12 horas, recorrendo a
128 GPUs NVIDIA H100.

Todas as fases de treino foram executadas no supercomputador
`MareNostrum5 <https://www.bsc.es/marenostrum/marenostrum-5>`__, alojado
no Barcelona Supercomputing Center.

Avaliação
---------

Para avaliar o desempenho do AMALIA-VL, foram traduzidas 18 *benchmarks*
multimodais para português europeu, utilizando modelos de estado da
arte. Para garantir a qualidade das traduções, foi realizada uma
revisão humana em *subsets* dos dados para validar a precisão e a
fluidez das traduções.

Adicionalmente, foram criados dois *benchmarks* para avaliar o AMALIA-VL
em capacidades específicas do português europeu e da cultura portuguesa:

-  **PorTEXTO** (*European Portuguese Benchmark for Visual Text Extraction*):
   desenvolvido para avaliar o desempenho dos modelos abertos na extração de texto pt-PT
   a partir de imagens, incluindo: documentos com texto escrito manualmente,
   texto em ambientes reais e típicos na cultura portuguesa, e documentos com texto
   sinteticamente gerado sobre imagens de fundo;
-  **CARAVELA** (*Cultural Awareness and Recognition Assessment for Visual Entity Literacy and Analysis*):
   desenvolvido para avaliar o conhecimento dos modelos sobre a cultura e a história portuguesas,
   abrangendo cinco categorias distintas: Arte, Gastronomia, Localidades, Monumentos e Personalidades.

A avaliação mostra que, dentro dos modelos abertos, o AMALIA-VL é
**altamente competitivo** em português europeu, com excelente desempenho
em tarefas de compreensão de texto em imagens e em tarefas de
ancoragem de respostas a imagens.
