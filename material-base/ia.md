https://towardsdatascience.com/become-a-better-data-scientist-with-these-prompt-engineering-hacks/


https://www.reddit.com/r/ChatGPTPromptGenius/comments/1jsglkm/help_me_to_generate_perfect_prompts_to_learn_data/

https://github.com/travistangvh/ChatGPT-Data-Science-Prompts


Excelente iniciativa. No nível de mestrado, o uso da IA muda de "faça isso para mim" para "atue como meu par intelectual e assistente técnico". A banca espera rigor metodológico, validação de premissas e interpretação crítica, não apenas código que roda.
Para orientar o Gemini dentro do Google Colab (seja via chat lateral ou células de código com %%gemini se disponível), você deve usar uma estrutura de Engenharia de Prompt focada em Ciência de Dados.
Aqui está o guia prático de como instruir a IA para obter resultados de nível acadêmico.
A Estrutura de Ouro: Contexto + Atuação + Tarefa + Restrição
Nunca peça apenas "analise os dados". Use esta estrutura mental antes de digitar:
 * Atuação (Persona): Defina quem o Gemini deve ser.
 * Contexto: O que são os dados? (O Gemini no Colab consegue "ler" o nome das variáveis do seu DataFrame ativo).
 * Tarefa: O que você quer especificamente (código, explicação matemática, gráfico).
 * Restrição/Formato: Nível de significância, biblioteca específica, saída em LaTeX.
Exemplos Práticos por Etapa do Trabalho
Aqui estão templates de como você deve falar com o Gemini no Colab.
A. Para Limpeza e Preparação (Data Cleaning)
No mestrado, você precisa justificar por que removeu um dado.
 * Prompt Ruim: "Limpe os dados."
 * Prompt Mestre:
   > "Atue como um Engenheiro de Dados. Analise o dataframe df. Identifique valores nulos e outliers na coluna 'renda'. Escreva um código Python para tratar esses nulos usando a mediana (para não distorcer a distribuição) e justifique brevemente por que a mediana é melhor que a média neste caso."
   > 
B. Para Análise Exploratória (EDA)
Você precisa entender a distribuição dos dados antes de aplicar testes.
 * Prompt Mestre:
   > "Gere estatísticas descritivas para as variáveis numéricas. Em seguida, crie um código usando a biblioteca Seaborn para plotar um histograma com uma linha de densidade (KDE) para verificar visualmente se a distribuição se aproxima de uma Normal. Use cores acadêmicas e sóbrias."
   > 
C. Para Testes Estatísticos (O Coração do Trabalho)
Aqui o rigor é máximo. Você precisa validar premissas.
 * Prompt Mestre:
   > "Preciso verificar a correlação entre as variáveis X e Y.
   >  * Primeiro, escreva um código para aplicar o teste de Shapiro-Wilk e verificar a normalidade dos resíduos.
   >  * Se for normal, use Pearson; se não, use Spearman.
   >  * Implemente uma estrutura if/else que decida qual teste usar automaticamente.
   >  * Plote o resultado e interprete o p-valor considerando um alfa de 0.05."
   > 
D. Para Visualização de Dados
 * Prompt Mestre:
   > "Crie um Boxplot comparativo. Quero visualizar a dispersão da variável 'Valor' agrupada por 'Categoria'. Adicione anotações no gráfico mostrando onde está a mediana e destaque os outliers em vermelho. O gráfico deve estar pronto para ser inserido em um artigo acadêmico (alta resolução, fontes legíveis)."
   > 
Dicas de "Power User" no Colab
 * Referencie o DataFrame Ativo: O Gemini no Colab tem acesso ao contexto da memória. Use sempre o nome da variável real.
   * Diga: "Olhe para o dataframe chamado df_financas..."
   * Não diga: "Olhe para os meus dados..."
 * Peça a Matemática (LaTeX): Para sua dissertação, você precisará das fórmulas.
   * Prompt: "Além do código Python, forneça a fórmula matemática do cálculo do Desvio Padrão Amostral em formato LaTeX para que eu possa colar no meu texto."
 * Iteração de Erros: Se o código der erro, não tente consertar sozinho imediatamente.
   * Clique no botão "Explain Error" que aparece no Colab ou copie o erro e diga: "O código retornou este erro. Analise a estrutura do dataframe df novamente e corrija o código."
 * Solicite Interpretação Crítica:
   * Prompt: "O teste T resultou em um p-valor de 0.03. Como estatístico, o que isso implica para a minha hipótese nula? Existe algum risco de Erro Tipo I neste cenário?"
O que NÃO fazer (Armadilhas Acadêmicas)
 * Não confie cegamente na limpeza: Sempre peça para ele mostrar o que foi removido. ("Mostre quantas linhas foram perdidas após remover os nulos").
 * Não peça para ele "escrever a conclusão": Peça para ele interpretar os resultados. A conclusão final e a conexão com a literatura devem ser suas.
 * Alucinação de Bibliotecas: Às vezes ele usa bibliotecas que não estão instaladas. Se acontecer, peça: "Reescreva usando apenas Pandas e Scipy padrão".
Próximo passo que posso fazer por você:
Para te ajudar a começar com o pé direito, você gostaria que eu montasse um "Prompt Mestre de Inicialização"? Seria um texto que você cola no início da conversa com o Gemini no Colab para definir as regras do jogo (ex: definir que ele é um estatístico acadêmico, que deve sempre comentar o código e usar bibliotecas específicas) para toda a sessão de trabalho.