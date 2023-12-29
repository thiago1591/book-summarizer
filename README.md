# Book Summarizer

Esse projeto usa o modelo GPT-4 Turbo para resumir ou analisar cada capítulo de um livro

## Pré requisitos
1. Python
2. API key da openAI

## Instalação
1. Clone o repositório
2. No arquivo requirements.txt estão as dependências do projeto
4. Criar um arquivo .env de acordo com o .env.example, informando a API key

## Uso
1. O livro a ser resumido/analisado deve estar em formato txt e colocado na raiz da pasta book
2. Para saber onde começa e termina cada capítulo, é necessário editar manualmente o txt do livro, colocando a string capitulo1, capitulo2... antes de cada capitulo. Seguir esse formato.
3. Rodar `python prepare_book.py` Esse comando irá gerar uma pasta chapters na pasta book. Lá estará separado cada capítulo do livro.
4. Rodar `python app.py`

## Dicas
1. No arquivo app.py, a variável input_message é referente a mensagem que é enviada para o modelo do GPT. No meu caso, pedi uma análise detalhada de cada capítulo, porém, é possível pedir para a resposta ser mais resumida.
2. No arquivo app.py é possível mudar para usar o GPT 3.5 invés do 4