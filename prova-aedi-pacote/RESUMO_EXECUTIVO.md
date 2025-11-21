# 📦 RESUMO EXECUTIVO - PACOTE PROVA AEDI

## 🎯 MISSÃO

Resolver **completamente** a Prova Final de AEDI do Mestrado UnB usando Claude Code (claude.ai/code).

---

## 📂 CONTEÚDO DESTE PACOTE

```
prova-aedi-pacote/
├── README.md                          ← Leia primeiro
├── RESUMO_EXECUTIVO.md               ← Este arquivo
├── INSTRUCOES_CLAUDE_CODE.md         ← Prompt mestre simplificado
├── REQUISITOS.txt                     ← pip install -r
├── questoes/
│   ├── Q1_REGRESSAO_LINEAR.md        ← Especificação detalhada Q1
│   ├── Q2_REGRESSAO_LOGISTICA.md     ← Especificação detalhada Q2
│   ├── Q3_ANOVA.md                   ← Especificação detalhada Q3
│   └── Q4_ML_AVANCADO.md             ← Especificação detalhada Q4
├── datasets/
│   └── FONTES_DATASETS.md            ← Links para download
└── entregas/
    └── CRITERIOS_AVALIACAO.md        ← O que a banca espera
```

---

## 🚀 OPÇÕES DE EXECUÇÃO

### ⚡ OPÇÃO 1: Comando Único (Mais Rápido)

1. Abra `claude.ai/code`
2. Faça upload de **TODOS os arquivos** deste pacote
3. Cole no chat:

```
Leia o arquivo INSTRUCOES_CLAUDE_CODE.md e execute TUDO que está descrito lá.
Resolva as 4 questões sequencialmente (Q1 → Q2 → Q3 → Q4).
```

4. Aguarde ~1-2 horas
5. Baixe arquivos gerados de `/mnt/user-data/outputs/`

**Vantagens:**
- Automático, mínima intervenção
- Context preservado entre questões

**Desvantagens:**
- Pode dar timeout (sessão muito longa)
- Difícil debugar se erro no meio

---

### 🎯 OPÇÃO 2: Questão por Questão (Mais Seguro)

1. Abra `claude.ai/code`
2. Faça upload de **TODOS os arquivos** deste pacote

**Para Q1:**
```
Leia o arquivo questoes/Q1_REGRESSAO_LINEAR.md e execute TUDO.
Crie notebook completo em notebooks/Q1_Regressao_Linear.ipynb
Exporte para HTML em exports/
```

**Para Q2:**
```
Leia o arquivo questoes/Q2_REGRESSAO_LOGISTICA.md e execute TUDO.
Crie notebook completo em notebooks/Q2_Regressao_Logistica.ipynb
Exporte para HTML em exports/
```

**Repetir para Q3 e Q4.**

**Vantagens:**
- Controle total
- Pode revisar cada questão antes de prosseguir
- Se der erro, só afeta uma questão

**Desvantagens:**
- Mais manual
- 4 interações necessárias

---

### 📋 OPÇÃO 3: GitHub Issues (Máximo Controle)

1. Crie repositório no GitHub: `prova-aedi-unb`
2. Faça upload deste pacote
3. Crie 4 Issues:

**Issue #1: Questão 1 - Regressão Linear**
```markdown
**Dataset:** King County House Sales
**Objetivo:** Modelo de Regressão Linear com validação de pressupostos

Ver especificação completa em: `questoes/Q1_REGRESSAO_LINEAR.md`

**Checklist:**
- [ ] EDA completo
- [ ] Modelo inicial
- [ ] Validação dos 5 pressupostos
- [ ] Ajustes e correções
- [ ] Interpretação final
- [ ] HTML exportado
```

**(Criar Issues #2, #3, #4 similares)**

4. No Claude Code:
```
Repositório: https://github.com/SEU_USER/prova-aedi-unb
Resolva Issue #1 completamente.
```

**Vantagens:**
- Máximo controle e organização
- Tracking de progresso
- Fácil retomar se interrompido

**Desvantagens:**
- Mais setup inicial
- Requer familiaridade com GitHub

---

## 📊 AS 4 QUESTÕES (OVERVIEW)

### Q1: Regressão Linear (2,5 pts) - 40min
- **Dataset:** King County Houses
- **Foco:** Pressupostos estatísticos
- **Crítico:** Linearidade, Homocedasticidade, Normalidade, VIF, Durbin-Watson

### Q2: Regressão Logística (2,5 pts) - 30min
- **Dataset:** Hotel Bookings
- **Foco:** Classificação + Features
- **Crítico:** Métricas (Prec/Rec), Curva ROC, Odds Ratio

### Q3: ANOVA (2,0 pts) - 25min
- **Dataset:** Online Retail
- **Foco:** Comparação de médias entre países
- **Crítico:** Pressupostos (Normalidade, Homocedasticidade), Post-hoc

### Q4: ML Avançado (3,0 pts) - 60min ⭐ **MAIS IMPORTANTE**
- **Dataset:** German Credit
- **Foco:** Múltiplos modelos + SHAP + Clustering
- **Crítico:** SHAP values com interpretação acadêmica (25% da nota Q4)

---

## ⏱️ TEMPO ESTIMADO

| Fase | Tempo |
|------|-------|
| Setup (instalar bibliotecas, baixar datasets) | 10min |
| Q1 - Regressão Linear | 40min |
| Q2 - Regressão Logística | 30min |
| Q3 - ANOVA | 25min |
| Q4 - ML Avançado | 60min |
| Integração final (exportar HTMLs, zipar) | 15min |
| **TOTAL** | **~3 horas** |

---

## 💰 CUSTO ESTIMADO

- **Claude Code (claude.ai/code):** ~$300-400 para resolução completa
- **Alternativa gratuita:** Pode usar sessões separadas, aproveitando free tier

---

## ✅ OUTPUT FINAL ESPERADO

Após execução completa, você terá:

```
prova-aedi-unb/
├── notebooks/
│   ├── Q1_Regressao_Linear.ipynb          ✅ Executável
│   ├── Q2_Regressao_Logistica.ipynb       ✅ Executável
│   ├── Q3_ANOVA.ipynb                     ✅ Executável
│   └── Q4_ML_Avancado.ipynb               ✅ Executável
├── exports/
│   ├── Q1_Regressao_Linear.html           📄 Para entregar
│   ├── Q2_Regressao_Logistica.html        📄 Para entregar
│   ├── Q3_ANOVA.html                      📄 Para entregar
│   ├── Q4_ML_Avancado.html                📄 Para entregar
│   └── shap_*.png                         🖼️ Gráficos SHAP (Q4)
├── models/
│   └── credit_model.pkl                   💾 Modelo treinado (Q4)
└── README.md                              📝 Documentação
```

**Compactar tudo:**
- `prova-aedi-completa.zip` (para entregar)

---

## 🎯 PONTOS CRÍTICOS (NÃO ESQUECER)

### Q1 - Regressão Linear
⚠️ **Validar TODOS os 5 pressupostos**
- Linearidade, Homocedasticidade, Normalidade, Multicolinearidade, Independência
- Se violados: CORRIGIR (log, remover features, etc)

### Q2 - Regressão Logística
⚠️ **Interpretar Odds Ratios**
- Não basta coeficiente, precisa exp(coef) = odds ratio
- Explicar com exemplo numérico

### Q3 - ANOVA
⚠️ **Pressupostos de novo!**
- Normalidade (Shapiro-Wilk), Homocedasticidade (Levene)
- Se violados: Kruskal-Wallis ou transformação log

### Q4 - ML Avançado
⚠️ **SHAP VALUES = 25% DA NOTA Q4**
- NÃO basta gerar gráficos
- Precisa INTERPRETAÇÃO ACADÊMICA:
  * "Variável X tem SHAP de Y, indicando que [teoria bancária]"
  * Conectar com literatura econômica/financeira
  * 5 parágrafos (1 por top feature)

---

## 🚨 ERROS QUE MATAM A NOTA

### Erros Graves (perda de 50%+)
1. ❌ Pular pressupostos (Q1, Q3)
2. ❌ SHAP sem interpretação contextual (Q4)
3. ❌ Código não executa
4. ❌ Não justificar decisões metodológicas

### Erros Médios (perda de 20-30%)
1. ⚠️ Pressupostos verificados mas não corrigidos
2. ⚠️ Interpretações superficiais ("X é importante" sem explicar)
3. ⚠️ Não comparar modelos antes vs depois

### Erros Leves (perda de 10-15%)
1. 🔸 Gráficos feios
2. 🔸 Tabelas não formatadas
3. 🔸 Código sem comentários

---

## 📖 ORDEM DE LEITURA RECOMENDADA

**ANTES de começar:**
1. `README.md` (visão geral)
2. `RESUMO_EXECUTIVO.md` (este arquivo)
3. `CRITERIOS_AVALIACAO.md` (entender o que banca espera)

**Para executar:**
4. `INSTRUCOES_CLAUDE_CODE.md` (prompt mestre)
5. `questoes/QX_*.md` (especificações detalhadas de cada questão)

**Apoio:**
6. `datasets/FONTES_DATASETS.md` (se precisar baixar datasets manualmente)
7. `REQUISITOS.txt` (se precisar instalar bibliotecas fora do Claude Code)

---

## 🤝 COMO PEDIR AJUDA AO CLAUDE CODE

Se Claude Code travar ou der erro:

**Erro: Dataset não encontrado**
```
Leia o arquivo datasets/FONTES_DATASETS.md e tente URLs alternativas.
Se nenhuma funcionar, me avise para eu fornecer o CSV.
```

**Erro: Biblioteca não instalada**
```
pip install [biblioteca] --break-system-packages
```

**Erro: Timeout**
```
Parou na Questão X. Continue de onde parou:
Leia questoes/QX_*.md e complete a partir da seção [NOME DA SEÇÃO].
```

**Erro: SHAP não funciona**
```
O modelo é tree-based? Use shap.TreeExplainer
O modelo é outro? Use shap.Explainer
```

---

## 🎓 NÍVEL DE ESCRITA

**MESTRADO = Rigor Acadêmico Máximo**

❌ **Graduação:**
"O modelo é bom porque R² deu 0.85"

✅ **Mestrado:**
"O modelo apresenta R² de 0.85, explicando 85% da variância de price. Entretanto, análise de resíduos revela heterocedasticidade (Breusch-Pagan p<0.01), sugerindo necessidade de transformação logarítmica para atender pressupostos da regressão linear clássica."

---

## 💪 MENSAGEM FINAL

**Você tem tudo que precisa neste pacote:**
- ✅ Especificações detalhadas das 4 questões
- ✅ Instruções passo a passo para Claude Code
- ✅ Links para todos os datasets
- ✅ Critérios de avaliação da banca
- ✅ Exemplos de código e interpretações

**Agora é só:**
1. Abrir claude.ai/code
2. Fazer upload deste pacote
3. Colar o prompt de INSTRUCOES_CLAUDE_CODE.md
4. Aguardar
5. Baixar e entregar

**Estimativa de economia:**
- Tempo economizado: ~20 horas de trabalho manual
- Qualidade: Nível mestrado, rigor acadêmico
- Resultado: 4 notebooks completos, prontos para entregar

---

**Boa sorte na prova! 🚀🎓**

**Dúvidas?** Releia os arquivos `.md` - tudo está documentado.
