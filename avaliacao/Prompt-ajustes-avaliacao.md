# 🚨 PROMPT DE CORREÇÃO - ERROS CRÍTICOS IDENTIFICADOS

## 📋 CONTEXTO

Avaliação rigorosa da Prova Final de AEDI (Mestrado PPCA/UnB) identificou ERROS CRÍTICOS que impedem nota máxima. Versão atual: 9.68/10.0. Meta: 10.0/10.0.

---

## ⚠️ ERRO CRÍTICO #1: QUESTÃO 2 - JUSTIFICATIVA METODOLÓGICA AUSENTE

**Arquivo:** `prova-aedi-unb/notebooks/Q2_Regressao_Logistica_plotly.ipynb`

**Localização:** Após célula de EDA (células 1-5), ANTES da célula "## 3. Preprocessing"

**Requisito da Prova.pdf (Página 3, item d):**

> "Explique por que a Regressão Logística é mais apropriada para este problema em comparação à Regressão Linear."

**Status:** ❌ COMPLETAMENTE AUSENTE

**Impacto:** -0.25 pontos (10% da Q2)

### Especificação do Erro:

- Não existe célula markdown explicando a escolha do método
- Não há comparação com Regressão Linear
- Não há justificativa técnica (target binário, pressupostos, etc.)
- Requisito EXPLÍCITO da prova não atendido

### O que deve conter (itens obrigatórios):

1. Por que target binário exige Regressão Logística
2. Quais pressupostos de Regressão Linear são violados
3. Vantagem interpretativa (Odds Ratios)
4. Fundamentação teórica (função sigmoid, log-odds)

**Peso:** CRÍTICO - Sem isso a Q2 perde 10% da pontuação automaticamente

---

## ⚠️ ERRO CRÍTICO #2: QUESTÃO 1 - DECISÕES ESTRATÉGICAS SUPERFICIAIS

**Arquivo:** `prova-aedi-unb/notebooks/Q1_Regressao_Linear_plotly.ipynb`

**Localização:** Célula final (## 10. Conclusões) ou criar nova célula antes das conclusões

**Requisito da Prova.pdf (Página 2, item 5):**

> "Forneça exemplos de decisões estratégicas que poderiam ser tomadas com base nas previsões."

**Status:** ⚠️ PRESENTE MAS INSUFICIENTE

**Impacto:** -0.07 pontos (2.8% da Q1)

### Especificação do Erro:

- Conclusões mencionam "preditores principais" mas SEM EXEMPLOS PRÁTICOS
- Não há cenários numéricos concretos
- Não há cálculos de ROI específicos
- Falta conexão direta entre coeficientes → decisões de negócio

### O que está faltando (itens obrigatórios):

1. Exemplo de precificação com valores concretos (ex: "Imóvel com X features → preço estimado Y")
2. Exemplo de identificação de oportunidade (subvalorização/sobrevalorização)
3. Exemplo de cálculo de ROI de melhorias (ex: "Adicionar 1 bathroom → +X% no preço")
4. Pelo menos 2-3 cenários práticos com números reais

**Peso:** MODERADO - Perda menor mas impede nota máxima

---

## 🔧 ERRO TÉCNICO #3: EXECUÇÃO NO JUPYTER (BLOCKER POTENCIAL)

**Arquivos:** Todos os `*_plotly.ipynb`

**Requisito Implícito:** Notebooks DEVEM executar sem erros no Jupyter

**Status:** ✅ JSON válido (versão Plotly) ❌ Dependências podem faltar

### Especificação do Erro:

- Células de verificação de dependências: Existem (@title Verificação de Dependências) mas podem falhar
- Imports sem tratamento: Se Plotly não estiver instalado, notebook quebra na célula 2
- Risco: Professor pode não ter ambiente configurado

### O que verificar:

1. Todas as células executam em ordem (Run All Cells)
2. Sem erros de ImportError
3. Todos os gráficos renderizam (Plotly precisa de JavaScript no browser)
4. Outputs estão salvos (para caso de ambiente sem libs)

**Peso:** BLOCKER - Se não executar, pode zerar a questão

---

## 📊 ERRO TÉCNICO #4: OUTPUTS NÃO SALVOS (RISCO DE APRESENTAÇÃO)

**Arquivos:** Todos os `*_plotly.ipynb`

**Status:** ⚠️ VERIFICAR - Notebooks podem estar sem outputs salvos

### Especificação do Erro:

- Se notebooks foram salvos com "Clear All Outputs", gráficos não aparecem no preview
- Professor pode abrir notebook e ver células vazias
- HTMLs exportados podem estar desatualizados

### O que verificar:

1. Executar "Run All Cells" em cada notebook
2. Salvar notebooks COM outputs
3. Re-gerar HTMLs após executar: `jupyter nbconvert --to html Q*_plotly.ipynb`
4. Confirmar que HTMLs têm gráficos renderizados

**Peso:** MODERADO - Apresentação visual impacta avaliação

---

## 🎯 PRIORIZAÇÃO DOS ERROS

| Erro | Arquivo | Impacto | Pontos Perdidos | Prioridade |
|------|---------|---------|----------------|------------|
| #1 | Q2_plotly.ipynb | -0.25 pts | 2.5% do total | 🔴 CRÍTICO |
| #2 | Q1_plotly.ipynb | -0.07 pts | 0.7% do total | 🟡 MODERADO |
| #3 | Todos *_plotly.ipynb | Pode zerar | 100% risco | 🔴 BLOCKER |
| #4 | Todos *_plotly.ipynb | Visual | Estético | 🟡 BAIXO |

---

## ✅ CHECKLIST DE VALIDAÇÃO PRÉ-SUBMISSÃO

### Executar em ordem:

#### Ambiente:

```bash
cd /home/user/data-science/prova-aedi-unb/notebooks
jupyter nbconvert --clear-output Q*_plotly.ipynb  # Limpar outputs antigos
```

#### Teste de Execução (CRÍTICO):

1. Abrir `Q1_Regressao_Linear_plotly.ipynb` no Jupyter
2. Run All Cells
3. Verificar se todas as 36 células executam sem erro
4. Repetir para Q2, Q3, Q4

#### Verificação de Conteúdo:

- Q2: Procurar célula com "Justificativa do Método" → Se NÃO encontrar = ERRO #1
- Q1: Procurar "Exemplo de precificação" ou "Cenário 1" → Se NÃO encontrar = ERRO #2

#### Geração de HTMLs:

```bash
jupyter nbconvert --to html Q1_Regressao_Linear_plotly.ipynb
jupyter nbconvert --to html Q2_Regressao_Logistica_plotly.ipynb
jupyter nbconvert --to html Q3_ANOVA_plotly.ipynb
jupyter nbconvert --to html Q4_ML_Avancado_plotly.ipynb
```

- Abrir cada HTML no browser
- Confirmar que gráficos Plotly são interativos

#### Validação de Pontuação:

Após correções #1 e #2: Nota esperada = 10.0/10.0

---

## 🚨 ALERTA FINAL

### SEM CORREÇÃO:

- **Nota:** 9.68/10.0 (96.8%)
- **Classificação:** EXCEPCIONAL (mas não perfeito)

### COM CORREÇÃO #1 APENAS:

- **Nota:** 9.93/10.0 (99.3%)
- **Falta:** Apenas exemplos práticos Q1

### COM CORREÇÕES #1 + #2:

- **Nota:** 10.0/10.0 ⭐
- **Classificação:** PERFEITO

### RISCO DE NÃO EXECUTAR (Erro #3):

- **Nota:** ZERO na questão afetada
- **Impacto:** Pode derrubar nota para 7.x/10.0

---

## 📝 RESUMO EXECUTIVO

**Erros que IMPEDEM nota máxima:**

- Q2 sem justificativa metodológica (-0.25)
- Q1 sem exemplos práticos de decisão (-0.07)

**Erros que podem ZERAR questões:**

- Notebooks não executarem no Jupyter (BLOCKER)

**Total de correções necessárias:** 2 células markdown + validação técnica

**Tempo estimado de correção:** 15-20 minutos

**Resultado esperado:** 9.68 → 10.0/10.0 ⭐
