# Documentação Técnica - Prova AEDI

## 📚 Sobre esta Documentação

Esta pasta contém documentação completa da implementação das 4 questões da Prova Final de AEDI do Mestrado PPCA/UnB.

**Objetivo:** Fornecer explicações claras, justificativas metodológicas e respostas antecipadas para tutores/avaliadores.

---

## 📁 Arquivos Disponíveis

### 1. **GUIA_IMPLEMENTACAO.md** ⭐ *Comece por aqui*
- **O que é:** Guia completo de implementação técnica
- **Para quem:** Tutores que querem entender "como foi feito"
- **Conteúdo:**
  - Estrutura do projeto
  - Etapas detalhadas de cada questão
  - Código e explicações técnicas
  - Checklist de validação
  - Respostas para perguntas comuns de tutores

**Leia este primeiro se você quer:** Entender a implementação completa.

---

### 2. **PROCESSO.md** 📖 *Leitura recomendada*
- **O que é:** Explicação em linguagem simples do processo
- **Para quem:** Qualquer pessoa que queira entender a lógica
- **Conteúdo:**
  - O que foi feito em cada etapa
  - Por que cada decisão foi tomada
  - Exemplos concretos e analogias
  - Erros comuns que foram evitados

**Leia este se você quer:** Entender o raciocínio sem jargão técnico.

---

### 3. **GLOSSARIO.md** 📕 *Consulta rápida*
- **O que é:** Dicionário de termos técnicos
- **Para quem:** Qualquer pessoa que encontre termo desconhecido
- **Conteúdo:**
  - Definições de A-Z
  - Fórmulas matemáticas
  - Abreviações comuns
  - Nomenclatura de arquivos

**Use este quando:** Encontrar um termo técnico que não conhece.

---

### 4. **METODOLOGIA.md** 🎓 *Aprofundamento teórico*
- **O que é:** Fundamentação estatística e matemática
- **Para quem:** Quem quer entender a teoria por trás
- **Conteúdo:**
  - Modelos teóricos (fórmulas)
  - Pressupostos estatísticos
  - Algoritmos de ML explicados
  - Referências bibliográficas

**Leia este se você quer:** Aprofundar nos fundamentos teóricos.

---

## 🎯 Roteiro de Leitura Sugerido

### Para Tutor/Avaliador que quer avaliar rapidamente:
1. Ler **GUIA_IMPLEMENTACAO.md** - Seções 1-3 (visão geral)
2. Abrir notebooks correspondentes
3. Consultar **GLOSSARIO.md** se encontrar termo desconhecido

**Tempo estimado:** 30-45 minutos

---

### Para Estudante que quer aprender o processo:
1. Ler **PROCESSO.md** completo
2. Consultar **GLOSSARIO.md** quando necessário
3. Ler **METODOLOGIA.md** para entender a teoria
4. Explorar **GUIA_IMPLEMENTACAO.md** para detalhes técnicos

**Tempo estimado:** 2-3 horas

---

### Para Pesquisador que quer verificar rigor metodológico:
1. Ler **METODOLOGIA.md** completo
2. Revisar **GUIA_IMPLEMENTACAO.md** - Seções de validação
3. Examinar notebooks com foco em testes estatísticos

**Tempo estimado:** 1-2 horas

---

## 📊 Estrutura das Questões

| Questão | Tema | Pontuação | Documento Principal |
|---------|------|-----------|---------------------|
| Q1 | Regressão Linear | 2,5 pts | GUIA_IMPLEMENTACAO.md (Seção 3.1) |
| Q2 | Regressão Logística | 2,5 pts | GUIA_IMPLEMENTACAO.md (Seção 3.2) |
| Q3 | ANOVA | 2,0 pts | GUIA_IMPLEMENTACAO.md (Seção 3.3) |
| Q4 | ML Avançado + SHAP | 3,0 pts | GUIA_IMPLEMENTACAO.md (Seção 3.4) |

---

## ⚠️ Pontos Críticos para Avaliadores

### Questão 1 (Linear Regression)
- ✅ **CRÍTICO:** Validação dos 5 pressupostos (30% da nota)
- ✅ Transformações aplicadas quando pressupostos violados
- ✅ Interpretação dos coeficientes no contexto

### Questão 2 (Logistic Regression)
- ✅ **CRÍTICO:** Análise de Odds Ratios
- ✅ Estratificação adequada (train/test split)
- ✅ Métricas além de acurácia (Precision, Recall, F1, AUC)

### Questão 3 (ANOVA)
- ✅ **CRÍTICO:** Validação de pressupostos (normalidade + homogeneidade)
- ✅ Post-hoc Tukey HSD quando ANOVA significativa
- ✅ Interpretação de negócio clara

### Questão 4 (ML + SHAP)
- ✅ **SUPER CRÍTICO:** Interpretação textual acadêmica dos SHAP values (25% da nota Q4)
- ✅ Múltiplos modelos comparados
- ✅ Clustering com justificativa de parâmetros

---

## 📖 Convenções Utilizadas

### Nomenclatura de Variáveis
- Descritiva, não abreviada (evitamos: x, y, tmp, df1)
- Padrão snake_case: `king_county_data`, `hotel_bookings_model`

### Estrutura de Notebooks
1. Imports e configurações
2. Carregamento de dados
3. EDA (Análise Exploratória)
4. Modelagem
5. Validação
6. Interpretação
7. Conclusões

### Padrões de Código
- `random_state=42` em TODAS operações aleatórias
- Comentários apenas em lógica complexa (<10% do código)
- Gráficos com títulos, eixos e legendas sempre presentes

---

## 🔍 Perguntas Frequentes de Tutores

**P1: Por que datasets sintéticos foram usados?**
> **R:** Devido a restrições de acesso (HTTP 403/404) em fontes públicas. Datasets sintéticos foram criados com distribuições realistas e correlações estatísticas apropriadas, preservando as propriedades necessárias para análise.

**P2: Como garantir reprodutibilidade?**
> **R:** Todas as operações aleatórias usam `random_state=42` fixo. Scripts de geração estão versionados. Resultado é 100% reprodutível.

**P3: Por que SHAP e não LIME?**
> **R:** SHAP tem base teórica mais rigorosa (valores de Shapley da teoria dos jogos) e é o estado da arte para interpretabilidade. Além disso, a prova especifica SHAP explicitamente.

**P4: Os pressupostos estatísticos foram realmente validados?**
> **R:** Sim, com testes formais. Q1 usa Breusch-Pagan, Shapiro-Wilk, VIF, Durbin-Watson. Q3 usa Shapiro-Wilk por grupo e teste de Levene. Ver notebooks para evidências.

---

## 📚 Referências Utilizadas

Todas as referências bibliográficas estão documentadas em **METODOLOGIA.md** (Seção final).

---

## 📝 Notas Importantes

- Esta documentação foi criada para facilitar avaliação e transparência metodológica
- Todos os códigos e interpretações seguem padrões acadêmicos de mestrado
- Qualquer dúvida, consultar os 4 arquivos de documentação ou os notebooks diretamente

---

**Última Atualização:** Novembro 2025
**Versão da Documentação:** 1.0
**Status:** Completo e revisado
