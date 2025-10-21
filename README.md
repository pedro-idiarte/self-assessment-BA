# Self-Assessment para Business Analysts

Este é um programa Python simples que permite aos Business Analysts (BAs) realizarem uma autoavaliação interativa de suas competências essenciais. O programa faz uma série de perguntas divididas em categorias e solicita respostas de 'sim' (y) ou 'não' (n). Ao final, ele calcula e exibe a pontuação do usuário em cada categoria.

## Funcionalidades

- **Autoavaliação Interativa:** Realize a avaliação respondendo a perguntas simples via linha de comando.
- **Categorias de Competência:** As perguntas são organizadas em categorias chave para Business Analysts.
- **Pontuação Clara:** Receba uma pontuação percentual para cada categoria, indicando áreas de força e oportunidades de melhoria.
- **Fácil de Usar:** Interface baseada em texto, sem dependências externas complexas.

## Como Usar

Para executar a autoavaliação, siga os passos abaixo:

### Pré-requisitos

Certifique-se de ter o Python 3 instalado em seu sistema.

### Instalação

1. Faça o download do arquivo `self_assessment.py` para o seu computador.
2. Abra um terminal ou prompt de comando e navegue até o diretório onde você salvou o arquivo.

### Execução

1. Execute o script Python usando o seguinte comando:

   ```bash
   python3 self_assessment.py
   ```

2. O programa começará a fazer perguntas. Para cada pergunta, digite `y` para "sim" ou `n` para "não" e pressione Enter.

   ```
   --- Início da Autoavaliação de Competências de Business Analyst ---

   Categoria: General Skills
   1. Do you have a process for making presentations? (y/n): y
   2. Do you understand the principles of effective written communication? (y/n): n
   ...
   ```

3. Continue respondendo a todas as perguntas. Ao final, o programa exibirá um resumo de suas pontuações por categoria.

   ```
   --- Resultados da Autoavaliação ---
   General Skills: X de 10 (Pontuação: X0%)
   User Acceptance Testing: Y de 10 (Pontuação: Y0%)
   ...
   --- Fim da Autoavaliação ---
   ```

## Estrutura do Projeto

O projeto consiste em um único arquivo Python:

- `self_assessment.py`: O script principal que contém as perguntas da autoavaliação e a lógica para processar as respostas e exibir os resultados.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões para melhorar as perguntas, adicionar novas categorias ou otimizar o código, sinta-se à vontade para abrir uma issue ou enviar um pull request.
