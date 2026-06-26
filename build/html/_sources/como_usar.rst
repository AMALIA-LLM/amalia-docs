Como Usar
=========

Acesso via API
--------------

O AMALIA está disponível via API no `IAedu <https://iaedu.pt>`__ para
professores e investigadores. Após realizar login e escolher o modelo
AMALIA, os parâmetros da API podem ser obtidos clicando na roda no canto
superior direito. Com estes, é possível interagir com o modelo usando o
código:

.. code:: python

   import requests
   import json
   formData = {
       "channel_id": channel_id,
       "thread_id": thread_id,
       "user_info": "{}",
       "message": message
   }
   response = requests.post(
       url=endpoint,
       headers= {'x-api-key': api_key },
       data=formData
   )

   for line in response.text.split('\n\n'):
       jsonline = json.loads(line)
       if jsonline["type"] == "message":
           print(jsonline["content"]["content"])
           break

Neste exemplo, ``message`` representa a mensagem enviada ao modelo e
``thread_id`` é o identificador da conversa, para manutenção do
contexto.

.. raw:: html

   <!-- No caso de aceder ao modelo via uma API disponibilizada por vLLM, o código a usar é:

   ````python
   import requests
   headers = {
       "Content-Type": "application/json",
       "Authorization": token
   }
   payload = {
       "model": model_name,
       "messages": [
           {
               "role": "user",
               "content": message
           }
       ]
   }
   response = requests.post(url, headers=headers, json=payload)
   if response.status_code == 200:
       print(response.json()['choices'][0]['message']['content'])
   ````

   Aqui, o pedido é enviado para o endereço indicado em ``url``, autenticado com um certo ``token``. O modelo com o nome indicado em ``model_name`` responderá então à mensagem  enviada em ``message``.

   Para manter o contexto de uma conversa por esta via, as mensagens anteriores poderão ser incluídas na lista de ``messages``, indicando o ``role`` de ``user`` ou ``assistant`` para mensagens do utilizador e do AMALIA respetivamente. -->

Acesso ao Modelo Público
------------------------

O AMALIA está publicamente disponível em código-aberto via `HuggingFace <https://huggingface.co/amalia-llm>`__.

Como servir uma API localmente
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para servir localmente o AMALIA, o hardware mínimo é de uma GPU `NVIDIA A100 40GB <https://www.nvidia.com/en-eu/data-center/a100/>`__, sendo que
para aplicações com vários clientes é recomendado um mínimo de 4 destas GPUs.
O software recomendado é o `vLLM <https://vllm.ai/>`__ instalado em ambiente `conda <https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html>`__ com Python 3.12+:

.. code:: shell

   conda create -n vllm_env python=3.12
   uv pip install vllm --torch-backend=auto
   # Login HuggingFace
   hf auth login

O seguinte *script* ``serve_llm.sh`` exemplifica como servir o AMALIA com vLLM recorrendo ao gestor de recursos `slurm <https://slurm.schedmd.com/overview.html>`__:

.. code:: bash

   #!/bin/bash
   #SBATCH --job-name=vllm-serve
   #SBATCH --partition=slurm_queue
   #SBATCH --nodes=1
   #SBATCH --ntasks=1
   #SBATCH --gres=gpu:nvidia_a100-40gb:4  # Pedir 4 GPUs
   #SBATCH --cpus-per-task=64             # Alocar CPUs do sistema
   #SBATCH --mem=256G                     # Alocar memória RAM do sistema
   #SBATCH --output=logs/%x-%j.out
   #SBATCH -e logs/%x-%j.err

   # Ativar o ambiente conda
   eval "$(conda shell.bash hook)"
   source activate vllm_env

   # Correr vLLM
   # $1: Nome do modelo, $2: Host $3: Porto, $4: Chave API $5: Chat template
   python -m vllm.entrypoints.openai.api_server \
       --model "$1" \
       --host "$2" \
       --port "$3" \
       --tokenizer-mode hf \
       --config-format hf \
       --tensor-parallel-size 4 \
       --gpu-memory-utilization 0.90 \
       --api-key "$4" \
       --chat-template "$5"

Como exemplo, para correr localmente o modelo de texto no porto 8001, com uma certa chave de API ``api_key``, o *script* pode ser lançado com o comando abaixo.
O ficheiro ``chat_template.jinja`` padrão está disponível no repositório HuggingFace.

.. code:: shell

   sbatch serve_llm.sh amalia-llm/AMALIA-9B-50-DPO 0.0.0.0 8001 api_key ./chat_template.jinja

Utilização de API local
~~~~~~~~~~~~~~~~~~~~~~~

Tendo o modelo disponível em servidor local, um exemplo simples de utilização
com ``curl`` é:

.. code:: shell

   curl -X POST http://127.0.0.1:8001/v1/chat/completions \
       -H "Content-Type: application/json" \
       -H "Authorization: Bearer api_key" \
       --data '{"model": "amalia-llm/AMALIA-9B-50-DPO", "messages": [{"role": "user", "content": "Olá"}]}'

Ou usando Python:

.. code:: python

   import requests

   url = "http://127.0.0.1:8001/v1/chat/completions"

   headers = {
       "Content-Type": "application/json",
       "Authorization": "Bearer api_key"
   }

   payload = {
       "model": "amalia-llm/AMALIA-9B-50-DPO",
       "messages": [
           {
               "role": "user",
               "content": "Olá"
           }
       ]
   }

   response = requests.post(url, headers=headers, json=payload)

   if response.status_code == 200:
       print(response.json()['choices'][0]['message']['content'])
   else:
       print(f"Error {response.status_code}: {response.text}")

Uma API local servida com vLLM desta forma segue o `formato de API da OpenAI <https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create>`__.

Os exemplos anteriores mostram como enviar mensagens únicas ao modelo.
Para fornecer contexto anterior de uma conversa, basta juntar turnos anteriores à lista de ``messages``, como por exemplo:

.. code:: python

   "messages": [
       {
           "role": "user",
           "content": "Por favor trata-me por Miguel"
       },
       {
           "role": "assistant",
           "content": "Olá, Miguel. Como posso ajudar-te hoje?"
       },
       {
           "role": "user",
           "content": "Qual é o meu nome?"
       }
   ]

Outros parâmetros opcionais que poderão ser úteis são:

-  ``max_completion_tokens``: Permite limitar o número de *tokens* da resposta do modelo;
-  ``temperature``: Permite ajustar a variância das respostas. Um valor de 0 produz respostas deterministas,
   valores mais próximos de 1 permitem mais variância;
-  ``stream``: Se ``true``, o modelo funcionará em formato de *streaming*, respondendo *token* a *token* à medida que estes são gerados em tempo real.
   O processamento da resposta deverá ser feita de forma diferente que anteriormente dado o seu formato diferente.

Um exemplo de utilização destes parâmetros é:

.. code:: python

   payload = {
       "model": "amalia-llm/AMALIA-9B-50-DPO",
       "messages": [
           {
               "role": "user",
               "content": "Olá"
           }
       ],
       "max_completion_tokens": 300,
       "temperature": 0,
       "stream": True
   }

Utilização do Modelo Multimodal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Com a versão multimodal (visão e linguagem) do AMALIA é possível também carregar imagens no *input* do utilizador, permitindo que o modelo responda a perguntas sobre o conteúdo da imagem.
Para tal, basta seguir os passos detalhados anteriormente, adicionando apenas um *path* para a imagem ao ``content`` da mensagem, da forma:

.. code:: python

   payload = {
       "model": "amalia-llm/AMALIA-VL-DPO",
       "messages": [
           {
               "role": "user",
               "content": [
                   {
                       "type": "image",
                       "image": "path/to/image.png"
                   },
                   {
                       "type": "text",
                       "text": "O que está nesta imagem?"
                   }
               ]
           }
       ]
   }

