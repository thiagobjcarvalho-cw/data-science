# 🎓 PROVA FINAL AEDI - MESTRADO UnB (PPCA)

## 📋 CONTEXTO

Prova Final de Análise Estatística de Dados e Informações do Programa de Pós-graduação em Computação Aplicada da UnB.

- **Data:** 23/11/2025
- **Pontuação Total:** 10 pontos
- **Formato:** 4 questões práticas
- **Entrega:** PDF ou HTML exportado de Jupyter Notebook

---

## 📂 ESTRUTURA DESTE PACOTE

```
prova-aedi-pacote/
├── README.md (este arquivo)
├── INSTRUCOES_CLAUDE_CODE.md (prompt mestre simplificado)
├── REQUISITOS.txt (dependências Python)
├── questoes/
│   ├── Q1_REGRESSAO_LINEAR.md (especificação detalhada)
│   ├── Q2_REGRESSAO_LOGISTICA.md
│   ├── Q3_ANOVA.md
│   └── Q4_ML_AVANCADO.md
├── datasets/
│   └── FONTES_DATASETS.md (links para download)
├── templates/
│   └── notebook_template.ipynb (estrutura base)
└── entregas/
    └── CRITERIOS_AVALIACAO.md (o que a banca espera)
```

---

## 🚀 COMO USAR

### OPÇÃO 1: Comando Único no Claude Code

1. Abra `claude.ai/code`
2. Faça upload de TODOS os arquivos deste pacote
3. Cole o conteúdo de `INSTRUCOES_CLAUDE_CODE.md`
4. Aguarde execução completa (1-2h)

### OPÇÃO 2: GitHub Issues (Recomendado para controle)

1. Crie um repositório no GitHub
2. Faça upload deste pacote
3. Crie 4 Issues (uma por questão) usando os templates em `questoes/`
4. Referencie as Issues no Claude Code
5. Execute questão por questão

---

## ⚙️ REQUISITOS

- Python 3.8+
- Jupyter Notebook
- Bibliotecas listadas em `REQUISITOS.txt`

---

## 📊 QUESTÕES

### Questão 1 (2,5 pts) - Regressão Linear
**Dataset:** King County House Sales  
**Foco:** Pressupostos estatísticos + ajustes de modelo

### Questão 2 (2,5 pts) - Regressão Logística  
**Dataset:** Hotel Booking Demand  
**Foco:** Classificação + análise de features

### Questão 3 (2,0 pts) - ANOVA
**Dataset:** Online Retail  
**Foco:** Comparação de médias entre países

### Questão 4 (3,0 pts) - ML Avançado ⭐ MAIS IMPORTANTE
**Dataset:** German Credit Risk  
**Foco:** Múltiplos modelos + SHAP + Clustering

---

## 🎯 OBJETIVO FINAL

Gerar 4 notebooks completos em HTML/PDF, prontos para entrega, com:
- ✅ Código executável e comentado
- ✅ Gráficos acadêmicos de alta qualidade
- ✅ Interpretações estatísticas rigorosas
- ✅ Validação de todos os pressupostos
- ✅ Decisões de negócio fundamentadas

---

## 📞 SUPORTE

Se Claude Code encontrar problemas:
1. Verifique que todos os arquivos foram carregados
2. Confirme acesso aos datasets (links em `datasets/FONTES_DATASETS.md`)
3. Execute questão por questão se timeout ocorrer
4. Use checkpoints em `templates/` para retomar trabalho

---

**Criado por:** Claude (Anthropic)  
**Versão:** 1.0  
**Data:** 2025
