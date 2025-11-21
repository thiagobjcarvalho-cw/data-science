# 🤖 INSTRUÇÕES PARA CLAUDE CODE

## MISSÃO

Resolver completamente a Prova Final de AEDI do Mestrado UnB. Você tem acesso a todos os arquivos necessários neste pacote.

---

## COMANDO PRINCIPAL

```bash
# 1. Setup inicial
cd /home/claude
mkdir -p prova-aedi-unb/{dados,notebooks,exports,models}
cd prova-aedi-unb

# 2. Instalar dependências
pip install -q pandas numpy matplotlib seaborn scikit-learn scipy statsmodels xgboost lightgbm shap jupyter openpyxl

# 3. Executar sequencialmente
# Q1 -> Q2 -> Q3 -> Q4
```

---

## WORKFLOW POR QUESTÃO

### Para CADA questão (Q1, Q2, Q3, Q4):

1. **Ler especificação:** Abra o arquivo `questoes/QX_*.md`
2. **Criar notebook:** Em `notebooks/QX_*.ipynb`
3. **Implementar todas as etapas:**
   - EDA completo
   - Modelagem
   - Validação de pressupostos (CRÍTICO)
   - Interpretações acadêmicas
   - Conclusões de negócio
4. **Exportar HTML:** `jupyter nbconvert --to html ...`
5. **Salvar em:** `exports/`

---

## ESTRUTURA DE CADA NOTEBOOK

```python
# HEADER
"""
# Questão X: [TÍTULO]
## Mestrado PPCA/UnB - AEDI
### Dataset: [NOME]
"""

# 1. IMPORTS
import pandas as pd
import numpy as np
# ... (todos necessários)

# 2. CARREGAR DADOS
# Ver fontes em datasets/FONTES_DATASETS.md

# 3. EDA
# - Estatísticas descritivas
# - Gráficos (alta qualidade, style acadêmico)
# - Análise de outliers/missing

# 4. MODELAGEM
# - Preparação de dados
# - Train/test split
# - Treinar modelo(s)
# - Métricas

# 5. VALIDAÇÃO DE PRESSUPOSTOS (se aplicável)
# - Testes estatísticos
# - Interpretação de p-valores
# - Correções necessárias

# 6. INTERPRETAÇÃO
# - Contexto de negócio
# - Limitações
# - Recomendações

# 7. CONCLUSÃO
# Resumo executivo (2-3 parágrafos)
```

---

## PRIORIDADES POR QUESTÃO

### Q1 - Regressão Linear (2,5 pts)
**FOCO CRÍTICO:** Pressupostos estatísticos
- ⚠️ Linearidade
- ⚠️ Homocedasticidade (Breusch-Pagan)
- ⚠️ Normalidade (Shapiro-Wilk, Q-Q plot)
- ⚠️ Multicolinearidade (VIF)
- ⚠️ Independência (Durbin-Watson)
- **SE VIOLADO:** Aplicar correções (log, Box-Cox, remover features)

### Q2 - Regressão Logística (2,5 pts)
**FOCO CRÍTICO:** Métricas e Features
- Matriz de confusão + interpretação
- Curva ROC com AUC
- Top features (coeficientes + odds ratio)
- Justificar escolha vs Regressão Linear

### Q3 - ANOVA (2,0 pts)
**FOCO CRÍTICO:** Pressupostos
- Normalidade por grupo
- Homocedasticidade (Levene)
- SE VIOLADO: Kruskal-Wallis ou transformação
- Post-hoc: Tukey HSD

### Q4 - ML Avançado (3,0 pts) ⭐ MAIS IMPORTANTE
**FOCO CRÍTICO:** SHAP Values (25% da nota!)
- Treinar múltiplos modelos (Logística, Tree, RF, XGBoost, LightGBM)
- **SHAP obrigatório:**
  * Summary plot (dot + bar)
  * Dependence plots (top 3 features)
  * Force plots (2 casos: good/bad)
  * **INTERPRETAÇÃO ACADÊMICA:** Conectar com teoria bancária/econômica
- Clustering (K-Means + DBSCAN)
- Decisão estratégica baseada em resultados

---

## REGRAS DE OURO

### ✅ SEMPRE FAZER:
- Comentar código linha por linha
- Usar `random_state=42` em TUDO
- Justificar TODAS as decisões metodológicas
- Interpretar resultados no contexto (bancário/imobiliário/hoteleiro)
- Validar pressupostos ANTES de confiar em modelos
- Gráficos: `figsize=(10,6)`, fontes 12pt, alta resolução
- Markdown explicativo entre células

### ❌ NUNCA FAZER:
- Pular validação de pressupostos
- Apresentar métricas sem interpretação
- Usar transformações sem justificar
- Ignorar outliers sem analisar
- Código sem comentários
- Gráficos sem títulos/labels/unidades

---

## CRITÉRIOS DE QUALIDADE (Checklist)

Antes de marcar questão como completa:

- [ ] Código executa sem erros
- [ ] Todos os gráficos renderizaram
- [ ] Pressupostos foram verificados (testes + plots)
- [ ] Se pressupostos violados, correções foram aplicadas
- [ ] Métricas apresentadas em tabelas formatadas
- [ ] Interpretações conectam estatística com contexto real
- [ ] Conclusão responde: "E daí? Qual a decisão?"
- [ ] HTML exportado está legível e completo

---

## EXPORTAÇÃO FINAL

```bash
cd /home/claude/prova-aedi-unb

# Exportar cada notebook
for notebook in notebooks/*.ipynb; do
    jupyter nbconvert --to html "$notebook" --output-dir exports/
done

# Zipar tudo
cd /home/claude
zip -r prova-aedi-completa.zip prova-aedi-unb/

# Copiar para outputs (para download)
cp -r prova-aedi-unb /mnt/user-data/outputs/
cp prova-aedi-completa.zip /mnt/user-data/outputs/

echo "✅ PROVA COMPLETA - Pronta para entrega!"
```

---

## TEMPO ESTIMADO

- Q1: 40 minutos
- Q2: 30 minutos
- Q3: 25 minutos
- Q4: 60 minutos
- **TOTAL: ~2h30**

---

## TROUBLESHOOTING

### Erro: Dataset não encontrado
→ Consulte `datasets/FONTES_DATASETS.md` para URLs alternativas

### Erro: Biblioteca não instalada
→ Execute: `pip install [biblioteca] --break-system-packages`

### Erro: Timeout de sessão
→ Execute questões separadamente, não todas de uma vez

### Erro: SHAP não funciona
→ Verifique que modelo é tree-based (XGBoost/RF/LightGBM)
→ Use `explainer = shap.TreeExplainer(model)`

---

## NÍVEL DE ESCRITA ESPERADO

**MESTRADO** = Rigor acadêmico máximo

❌ Errado: "O modelo é bom porque R² deu 0.85"  
✅ Certo: "O modelo apresenta R² de 0.85, indicando que 85% da variância de price é explicada pelas features. Entretanto, a análise de resíduos revela heterocedasticidade (Breusch-Pagan p<0.01), sugerindo que transformação logarítmica da variável target pode ser necessária para atender aos pressupostos da regressão linear."

---

**INICIE AGORA!** Leia cada arquivo em `questoes/` e execute sequencialmente.
