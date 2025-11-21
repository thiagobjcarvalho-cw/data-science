# 📝 CRITÉRIOS DE AVALIAÇÃO DA BANCA

## 🎯 O QUE A BANCA ESPERA (NÍVEL MESTRADO)

### DIFERENÇA: GRADUAÇÃO vs MESTRADO

| Aspecto | Graduação | Mestrado (VOCÊ) |
|---------|-----------|-----------------|
| **Pressupostos** | Menciona que existem | VALIDA TODOS com testes estatísticos |
| **Interpretação** | "R² é 0.85" | "R² de 0.85 indica que 85% da variância é explicada, porém análise de resíduos revela heterocedasticidade..." |
| **Justificativas** | "Usei log porque funcionou" | "Aplicamos transformação logarítmica porque teste de Breusch-Pagan (p<0.01) indicou heterocedasticidade, e log reduz variância de séries positivas (Box & Cox, 1964)" |
| **Gráficos** | Plot default do matplotlib | Figuras com títulos, labels, legendas, alta resolução, estilo acadêmico |
| **Código** | Funciona | Funciona + COMENTADO + JUSTIFICADO |

---

## 📊 BREAKDOWN POR QUESTÃO

### QUESTÃO 1: Regressão Linear (2,5 pts)

#### Análise Descritiva (0,5 pts)
**Critérios:**
- [ ] Estatísticas completas (não só describe())
- [ ] Gráficos profissionais (3+ tipos diferentes)
- [ ] Análise de outliers com método definido (IQR, Z-score)
- [ ] Texto interpretativo (2-3 parágrafos)

**Nota máxima se:**
- Identificou padrões relevantes (correlações, distribuições)
- Justificou decisões sobre outliers
- Conectou observações com contexto imobiliário

---

#### Modelo Inicial (0,75 pts)
**Critérios:**
- [ ] Modelo treinado corretamente (train/test split)
- [ ] Múltiplas métricas apresentadas (R², RMSE, MAE)
- [ ] Coeficientes interpretados (não só valores)
- [ ] Tabela bem formatada

**Nota máxima se:**
- Explicou significado prático dos coeficientes
- Identificou features mais/menos importantes
- Comparou train vs test (mencionou overfitting?)

---

#### Pressupostos (0,75 pts) ⚠️ **PESO ALTO**
**Critérios POR pressuposto:**

1. **Linearidade (0,15 pts)**
   - [ ] Plot resíduos vs fitted
   - [ ] Plot resíduos vs cada preditor (top 5)
   - [ ] Interpretação: "há/não há padrão sistemático"

2. **Homocedasticidade (0,15 pts)**
   - [ ] Teste de Breusch-Pagan OU White
   - [ ] p-valor reportado
   - [ ] Interpretação: "rejeitamos/não rejeitamos H0"

3. **Normalidade (0,15 pts)**
   - [ ] Q-Q plot
   - [ ] Teste de Shapiro-Wilk OU K-S
   - [ ] Histograma + curva normal
   - [ ] Interpretação adequada

4. **Multicolinearidade (0,15 pts)**
   - [ ] VIF calculado para TODAS features
   - [ ] Tabela ordenada por VIF
   - [ ] Identificou problemas (VIF>10)

5. **Independência (0,15 pts)**
   - [ ] Teste Durbin-Watson
   - [ ] Interpretação (ideal ≈ 2)

**Nota máxima se:**
- TODOS os 5 pressupostos foram verificados
- Testes estatísticos + visualizações
- Interpretações conectam estatística com consequências práticas
- Mencionou o que acontece se pressuposto é violado

**Perda de pontos se:**
- Pulou algum pressuposto (- 0,15 por pressuposto)
- Só fez plots SEM testes estatísticos (- 50%)
- Não interpretou resultados (-30%)

---

#### Ajustes (0,75 pts)
**Critérios:**
- [ ] Identificou problemas nos pressupostos
- [ ] Aplicou correções apropriadas (transformações, remoção de features)
- [ ] Justificou CADA decisão
- [ ] Retreinou modelo
- [ ] Comparou antes vs depois (tabela)
- [ ] Reverificou pressupostos

**Nota máxima se:**
- Correções resolveram os problemas (pressupostos OK após ajustes)
- Métricas melhoraram (R² maior, RMSE menor)
- Explicou POR QUE transformações funcionaram
- Feature engineering fundamentado em teoria/EDA

**Perda de pontos se:**
- Aplicou transformações "às cegas" (-40%)
- Não reverificou pressupostos (-30%)
- Não comparou com modelo original (-20%)

---

#### Interpretação (0,25 pts)
**Critérios:**
- [ ] Intervalos de confiança dos coeficientes (statsmodels)
- [ ] Identificou feature de maior impacto
- [ ] Limitações do modelo discutidas
- [ ] Aplicação prática sugerida

**Nota máxima se:**
- Recomendações acionáveis (ex: "focar em aumentar grade")
- Limitações são realistas (não genéricas)

---

### QUESTÃO 2: Regressão Logística (2,5 pts)

#### EDA (0,25 pts)
**Critérios:**
- [ ] Verificou balanceamento do target
- [ ] Gráficos bivariados (features vs target)
- [ ] Identificou features candidatas

---

#### Modelo (1,5 pts)
**Critérios:**
- [ ] Preprocessing justificado (encoding, scaling)
- [ ] Estratificação no split (stratify=y)
- [ ] class_weight se desbalanceamento >70/30
- [ ] Todas métricas: Acc, Prec, Rec, F1, AUC
- [ ] Matriz confusão + interpretação
- [ ] Curva ROC
- [ ] Discussão de threshold

**Nota máxima se:**
- Explicou trade-off Precision vs Recall no contexto hoteleiro
- Analisou múltiplos thresholds (não aceitou 0.5 como dado)
- Justificou escolha de class_weight ou SMOTE

---

#### Features (0,5 pts)
**Critérios:**
- [ ] Coeficientes + Odds Ratios
- [ ] Top 5 features identificadas
- [ ] Interpretação contextual (não só "X é importante")

**Nota máxima se:**
- Explicou Odds Ratio com exemplo numérico
- Conectou features com comportamento de clientes

---

#### Justificativa (0,25 pts)
**Critérios:**
- [ ] Explicou por que Logística > Linear para classificação
- [ ] Mencionou função sigmoid
- [ ] Limitações da Logística

---

### QUESTÃO 3: ANOVA (2,0 pts)

#### EDA (0,2 pts)
- [ ] Boxplots por país
- [ ] Estatísticas descritivas

---

#### ANOVA (0,8 pts)
**Critérios:**
- [ ] ANOVA para Quantity E UnitPrice
- [ ] Hipóteses declaradas (H0/H1)
- [ ] Tabela ANOVA (F, p-value)
- [ ] Interpretação adequada

**Nota máxima se:**
- Explicou significado de F-statistic
- Decisão fundamentada (rejeitar/não rejeitar H0)

---

#### Pressupostos (0,8 pts) ⚠️ **PESO ALTO**
**Critérios:**
- [ ] Normalidade: Shapiro-Wilk + Q-Q plots
- [ ] Homocedasticidade: Levene + Bartlett
- [ ] Independência: assumida e justificada
- [ ] SE VIOLADO: correção aplicada (log, Kruskal-Wallis, Welch's ANOVA)
- [ ] Modelo ajustado retreinado
- [ ] Pressupostos reverificados

**Nota máxima se:**
- Não ignorou pressupostos violados
- Correções foram apropriadas
- Comparou ANOVA original vs ajustado

---

#### Post-hoc (parte dos 0,8 pts acima)
- [ ] Tukey HSD executado
- [ ] Tabela de comparações
- [ ] Interpretação (quais pares diferem)

---

#### Interpretação (0,2 pts)
- [ ] Quais países diferem e por quê
- [ ] Decisões estratégicas

---

### QUESTÃO 4: ML Avançado (3,0 pts) ⭐ MAIS IMPORTANTE

#### Discussão (0,3 pts)
**Critérios:**
- [ ] Contexto bancário/econômico
- [ ] Custos de FP vs FN
- [ ] Relevância de ML
- [ ] 3-4 parágrafos bem escritos

---

#### EDA (0,45 pts)
**Critérios:**
- [ ] Verificou balanceamento
- [ ] Tratou missing (justificado)
- [ ] Gráficos bivariados (features vs target)
- [ ] Preprocessing completo (encoding, scaling)

---

#### Modelos (0,9 pts)
**Critérios:**
- [ ] 5 modelos treinados (Logística, Tree, RF, XGBoost, LightGBM)
- [ ] Justificou escolha de CADA modelo (1-2 frases)
- [ ] Tabela comparativa (Acc, Prec, Rec, F1, AUC)
- [ ] Curvas ROC (todas no mesmo gráfico)
- [ ] Modelo campeão escolhido e justificado

**Nota máxima se:**
- Critério de escolha foi apropriado (AUC + Recall para crédito)
- Comparou tempo de treinamento
- Matriz confusão do melhor modelo

---

#### SHAP (0,75 pts) ⚠️ **SUPER CRÍTICO - 25% da Q4**

**Breakdown detalhado:**

**Summary Plot Dot (0,15 pts)**
- [ ] Gráfico gerado e salvo
- [ ] Interpretação textual (eixos, cores, posições)
- [ ] Explicou padrões para top 3 features

**Summary Plot Bar (0,05 pts)**
- [ ] Gráfico gerado
- [ ] Ranking identificado

**Dependence Plots (0,15 pts)**
- [ ] Top 3 features plotadas
- [ ] Interpretação de relações não-lineares
- [ ] Mencionou interações (cores)

**Force Plots (0,15 pts)**
- [ ] 2 casos: good e bad
- [ ] Interpretação: quais features empurraram para cada lado
- [ ] Base value explicado

**INTERPRETAÇÃO ACADÊMICA (0,25 pts) ← PESO MÁXIMO**
- [ ] Parágrafo POR feature (top 5)
- [ ] Cada parágrafo tem:
  * SHAP value médio
  * Direção do efeito
  * Teoria econômica/bancária
  * Exemplo concreto
- [ ] Conecta com literatura/teoria

**Exemplo de parágrafo completo:**
"A variável checking_account_status apresenta SHAP value médio absoluto de 0.43, classificando-se como a 1ª mais importante. Valores positivos (saldo alto) reduzem risco (SHAP negativo). No contexto bancário, isso alinha-se com a teoria de restrição de liquidez (Deaton, 1991): indivíduos com poupança têm colchão financeiro para absorver choques de renda sem deixar de pagar dívidas. Por exemplo, cliente com €500 em conta tem 40% menos risco relativo que alguém com conta negativa."

**Perda de pontos se:**
- Só gerou gráficos SEM interpretação (-50%)
- Interpretação genérica "X é importante" (-40%)
- Não conectou com teoria bancária/econômica (-30%)
- Não fez force plots individuais (-20%)

---

#### Clustering (0,45 pts)
**Critérios:**

**K-Means (0,25 pts)**
- [ ] Elbow method
- [ ] Silhouette score
- [ ] Melhor k escolhido
- [ ] Perfis dos clusters interpretados
- [ ] Visualização (PCA)

**DBSCAN (0,15 pts)**
- [ ] Tuning de eps e min_samples
- [ ] Outliers analisados
- [ ] % bad payers entre outliers (se possível)

**Comparação (0,05 pts)**
- [ ] K-Means vs DBSCAN (diferenças metodológicas)
- [ ] Qual melhor para crédito? Justificou

---

#### Decisão Estratégica (0,3 pts)
**Critérios:**
- [ ] Políticas de concessão (thresholds, segmentação)
- [ ] Monitoramento de features (baseado em SHAP)
- [ ] Segmentação de produtos (clusters)
- [ ] Limitações discutidas (técnicas e éticas)
- [ ] Próximos passos

**Nota máxima se:**
- Recomendações são acionáveis
- Considerou custos de FP vs FN
- Mencionou ética e viés
- Sugeriu A/B testing

---

## 🚨 ERROS QUE TIRAM NOTA

### Erros Graves (-50% ou mais)
1. **Pular pressupostos** (Q1, Q3)
2. **Não interpretar SHAP** (só gerar gráficos) (Q4)
3. **Código não executa**
4. **Gráficos sem títulos/labels**
5. **Não justificar decisões metodológicas**

### Erros Médios (-20% a -30%)
1. Pressupostos verificados mas não corrigidos se violados
2. Interpretações superficiais ("X é importante" sem explicar por quê)
3. Não comparar modelos/métricas antes vs depois
4. Missing values tratados "na marra" sem justificar
5. Código sem comentários

### Erros Leves (-10% a -15%)
1. Gráficos com estética pobre
2. Tabelas não formatadas
3. Markdown escasso
4. Conclusões genéricas
5. Não mencionar limitações

---

## ✅ COMO GARANTIR NOTA MÁXIMA

### Checklist Mental
Para CADA questão, perguntar:
1. ✅ Valide TODOS os pressupostos? (Q1, Q3)
2. ✅ Interpretei os resultados no contexto? (todas)
3. ✅ Justifiquei TODAS as decisões? (todas)
4. ✅ Gráficos são profissionais? (todas)
5. ✅ Código está comentado? (todas)
6. ✅ SHAP tem interpretação acadêmica? (Q4)
7. ✅ Limitações foram discutidas? (todas)
8. ✅ Recomendações são acionáveis? (todas)

### Linguagem Acadêmica
❌ Errado: "O modelo ficou bom"  
✅ Certo: "O modelo apresentou AUC de 0.85, indicando boa capacidade discriminatória"

❌ Errado: "X é importante"  
✅ Certo: "X apresenta o maior SHAP value absoluto (0.43), sugerindo forte influência na predição devido a [teoria]"

❌ Errado: "Usei log porque sim"  
✅ Certo: "Aplicamos transformação logarítmica pois o teste de Breusch-Pagan (p<0.01) evidenciou heterocedasticidade"

---

## 📊 PESO FINAL DAS QUESTÕES

| Questão | Pontos | % da Nota |
|---------|--------|-----------|
| Q1 | 2,5 | 25% |
| Q2 | 2,5 | 25% |
| Q3 | 2,0 | 20% |
| Q4 | 3,0 | 30% |
| **TOTAL** | **10** | **100%** |

**Q4 é a mais importante!** Dedique 40% do tempo total nela.

---

## 🎯 EXPECTATIVA DA BANCA

"Esperamos ver trabalho de nível de **mestrado**, não graduação. Isso significa:
- Rigor metodológico: TODOS os pressupostos verificados
- Profundidade analítica: interpretações vão além do óbvio
- Conexão teoria-prática: resultados conectados com literatura/contexto
- Maturidade científica: limitações reconhecidas, próximos passos sugeridos
- Comunicação clara: gráficos profissionais, texto bem escrito

Um trabalho nota 10 não é apenas correto tecnicamente, mas demonstra compreensão profunda dos métodos e suas implicações práticas."

---

**Boa sorte! 🍀**
