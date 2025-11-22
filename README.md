# 🎓 Trabalho DC - Mestrado UnB (PPCA)

Repositório pessoal para materiais acadêmicos do **Programa de Pós-Graduação em Computação Aplicada (PPCA)** da Universidade de Brasília.

---

## 📋 Sobre

Este repositório contém materiais de estudo, provas e trabalhos acadêmicos relacionados às disciplinas do mestrado, com foco especial em **Análise Estatística de Dados e Informações (AEDI)**.

---

## 📂 Estrutura do Repositório

```
trabalho-dc/
├── prova-aedi-pacote/          # Pacote completo para Prova Final AEDI
│   ├── questoes/               # Especificações detalhadas das 4 questões
│   ├── datasets/               # Fontes e links para datasets
│   ├── entregas/               # Critérios de avaliação
│   ├── README.md               # Documentação do pacote
│   ├── RESUMO_EXECUTIVO.md     # Visão geral e instruções de uso
│   └── INSTRUCOES_CLAUDE_CODE.md # Prompt mestre para automação
│
├── material-base/              # Materiais de referência
│   ├── Prova_AEDI_V2.ipynb     # Notebook da prova
│   ├── Prova_AEDI_V2.html      # Exportação HTML
│   ├── Prova.pdf               # Especificação da prova
│   └── ia.md                   # Notas sobre IA
│
└── previous-chat-resume.md     # Resumo de sessões anteriores
```

---

## 🎯 Conteúdo Principal: Prova AEDI

### Informações Gerais

- **Disciplina:** Análise Estatística de Dados e Informações
- **Programa:** Mestrado PPCA - UnB
- **Data de Entrega:** 23/11/2025
- **Pontuação Total:** 10 pontos
- **Formato:** 4 questões práticas

### Questões da Prova

| Questão | Tema | Dataset | Pontos | Foco Principal |
|---------|------|---------|--------|----------------|
| **Q1** | Regressão Linear | King County House Sales | 2,5 | Pressupostos estatísticos |
| **Q2** | Regressão Logística | Hotel Booking Demand | 2,5 | Classificação e features |
| **Q3** | ANOVA | Online Retail | 2,0 | Comparação de médias |
| **Q4** | ML Avançado + SHAP | German Credit Risk | 3,0 | Interpretabilidade (crítico) |

---

## 🚀 Como Usar

### Opção 1: Resolução Automatizada com Claude Code

O pacote `prova-aedi-pacote/` foi projetado para ser executado com Claude Code:

```bash
# 1. Faça upload de todos os arquivos para claude.ai/code
# 2. Execute o comando no chat:
Leia o arquivo INSTRUCOES_CLAUDE_CODE.md e execute TUDO que está descrito lá.
Resolva as 4 questões sequencialmente (Q1 → Q2 → Q3 → Q4).
```

### Opção 2: Resolução Manual/Questão por Questão

```bash
# Para cada questão (Q1, Q2, Q3, Q4):
Leia o arquivo questoes/Q{N}_{TEMA}.md e execute TUDO.
Crie notebook completo em notebooks/Q{N}_{Tema}.ipynb
Exporte para HTML em exports/
```

---

## ⚙️ Requisitos Técnicos

### Software Necessário

- Python 3.8+
- Jupyter Notebook
- Git

### Dependências Python

Consulte `prova-aedi-pacote/REQUISITOS.txt` para lista completa. Principais bibliotecas:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy statsmodels
pip install xgboost lightgbm shap jupyter openpyxl joblib
```

---

## 📊 Objetivos de Entrega

O resultado final esperado inclui:

- ✅ **4 notebooks Jupyter completos** (um por questão)
- ✅ **Exportações em HTML/PDF** prontas para submissão
- ✅ **Código bem comentado** e executável
- ✅ **Gráficos acadêmicos** de alta qualidade
- ✅ **Análises estatísticas rigorosas** com validação de pressupostos
- ✅ **Interpretações fundamentadas** (especialmente SHAP na Q4)
- ✅ **Decisões de negócio** baseadas em dados

---

## 📖 Documentação Adicional

- **`prova-aedi-pacote/README.md`** - Guia completo do pacote
- **`prova-aedi-pacote/RESUMO_EXECUTIVO.md`** - Visão executiva e estratégias de execução
- **`prova-aedi-pacote/questoes/*.md`** - Especificações detalhadas de cada questão
- **`prova-aedi-pacote/entregas/CRITERIOS_AVALIACAO.md`** - O que a banca avaliadora espera
- **`previous-chat-resume.md`** - Histórico de desenvolvimento e decisões técnicas

---

## 🔧 Suporte e Troubleshooting

### Problemas Comuns

1. **Erro ao baixar datasets**: Verifique `prova-aedi-pacote/datasets/FONTES_DATASETS.md` para URLs atualizadas
2. **Timeout em sessões longas**: Execute questão por questão (Opção 2)
3. **Dependências faltando**: Reinstale usando `pip install -r REQUISITOS.txt`
4. **Git push falhando**: Este repositório teve histórico de problemas com push - considere commits menores

---

## 📝 Notas de Desenvolvimento

Este repositório foi desenvolvido com assistência de Claude (Anthropic) para automatizar e documentar o processo de resolução da prova. Todos os artefatos foram criados para maximizar:

- **Reprodutibilidade**: Código e datasets versionados
- **Clareza**: Documentação extensiva em linguagem acessível
- **Qualidade**: Validações estatísticas e boas práticas de ML
- **Eficiência**: Automação via Claude Code para reduzir trabalho manual

---

## 📄 Licença

Material acadêmico pessoal. Todos os direitos reservados.

---

## 👤 Autor

Thiago Carvalho
Mestrado em Computação Aplicada - UnB (PPCA)
Disciplina: Análise Estatística de Dados e Informações

---

# IMPORTANTE

## 🔄 Recriação Completa do Trabalho (Nova Sessão)

Se você está iniciando uma nova sessão do Claude Code e precisa **recriar todo o trabalho AEDI do zero**, siga estas instruções:

### ⚡ Comando Rápido

Leia os arquivos na seguinte ordem:

previous-chat-resume.md (contexto da sessão anterior)
prompt-recreate.md (instruções de recriação)
@docs/README.md, @docs/GLOSSARIO.md, @docs/GUIA_IMPLEMENTACAO.md (referências)
Depois execute TODAS as instruções do prompt-recreate.md sequencialmente. Trabalhe de forma incremental, criando e commitando cada arquivo assim que terminar.


### 📋 O que será criado

Ao final da execução, você terá:

✅ **Documentação completa** (5 arquivos em @docs/)
✅ **Scripts Python** (3 scripts para datasets)
✅ **Datasets** (4 arquivos CSV totalizando ~24MB)
✅ **Estrutura de diretórios** completa
✅ **Tudo commitado** no branch correto

**Tempo estimado:** 30-45 minutos (execução automática)

---

**Última atualização:** Novembro 2025
