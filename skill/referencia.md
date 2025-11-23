# Referências - Análise Estatística de Dados e Informações (AEDI)

Este documento consolida as melhores referências, tutoriais e recursos para cada questão da prova de mestrado em Análise Estatística de Dados e Informações.

---

## QUESTÃO 1 - REGRESSÃO LINEAR (King County House Prices)

### Datasets

1. **King County House Sales Dataset**
   - Fonte: Kaggle
   - URL: https://www.kaggle.com/datasets/harlfoxem/housesalesprediction
   - Descrição: Dados de vendas de imóveis em King County (Seattle), EUA, com 21 variáveis incluindo preço, metragem, localização, etc.

### Tutoriais e Notebooks de Referência

1. **Predicting House Prices - Burhan Ykiyakoglu**
   - URL: https://www.kaggle.com/code/burhanykiyakoglu/predicting-house-prices/notebook
   - Qualidade: ⭐⭐⭐⭐⭐ (Altamente recomendado)
   - Destaques: Análise descritiva completa, feature engineering, validação de pressupostos

2. **House Price Prediction - Advanced Regression**
   - URL: https://www.kaggle.com/code/pmarcelino/comprehensive-data-exploration-with-python
   - Destaques: Tratamento de outliers, transformações, análise de resíduos detalhada

3. **King County House Prices EDA**
   - URL: https://www.kaggle.com/code/themrityunjaypathak/king-county-house-sales-analysis
   - Destaques: Visualizações geoespaciais, análise de correlação profunda

### Documentação Técnica

1. **Scikit-learn Linear Models**
   - URL: https://scikit-learn.org/stable/modules/linear_model.html
   - Seções importantes: LinearRegression, Ridge, Lasso, ElasticNet

2. **Statsmodels OLS**
   - URL: https://www.statsmodels.org/stable/regression.html
   - Uso: Para obter estatísticas detalhadas (p-values, intervalos de confiança)

3. **Assumptions of Linear Regression**
   - URL: https://towardsdatascience.com/verifying-the-assumptions-of-linear-regression-in-python-and-r-f4cd2907d4c0
   - Tópicos: Linearidade, normalidade, homocedasticidade, independência

### Testes de Pressupostos

1. **Shapiro-Wilk Test (Normalidade)**
   - Biblioteca: scipy.stats.shapiro
   - URL: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html

2. **Jarque-Bera Test (Normalidade)**
   - Biblioteca: scipy.stats.jarque_bera
   - URL: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.jarque_bera.html

3. **Breusch-Pagan Test (Homocedasticidade)**
   - Biblioteca: statsmodels.stats.diagnostic.het_breuschpagan
   - URL: https://www.statsmodels.org/stable/generated/statsmodels.stats.diagnostic.het_breuschpagan.html

4. **VIF - Variance Inflation Factor (Multicolinearidade)**
   - Biblioteca: statsmodels.stats.outliers_influence.variance_inflation_factor
   - URL: https://www.statsmodels.org/stable/generated/statsmodels.stats.outliers_influence.variance_inflation_factor.html

### Transformações de Variáveis

1. **Box-Cox Transformation**
   - Biblioteca: scipy.stats.boxcox
   - Artigo: https://towardsdatascience.com/box-cox-transformation-explained-51d745e34203

2. **Log Transformation**
   - Uso: np.log1p() para lidar com zeros
   - Quando usar: Dados com distribuição assimétrica à direita

3. **Feature Scaling**
   - StandardScaler vs MinMaxScaler
   - URL: https://scikit-learn.org/stable/modules/preprocessing.html

---

## QUESTÃO 2 - REGRESSÃO LOGÍSTICA (Hotel Booking Cancellation)

### Datasets

1. **Hotel Booking Demand Dataset**
   - Fonte: Kaggle / UCI Machine Learning Repository
   - URL: https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand
   - Descrição: Dados de reservas de hotéis com 119.390 registros e 32 variáveis

### Tutoriais e Notebooks de Referência

1. **Hotel Booking Demand - Exploratory Data Analysis**
   - URL: https://www.kaggle.com/code/marcuswingen/eda-of-bookings-and-ml-to-predict-cancelations
   - Qualidade: ⭐⭐⭐⭐⭐
   - Destaques: EDA completa, feature engineering, múltiplos modelos

2. **Predicting Hotel Booking Cancellations**
   - URL: https://www.kaggle.com/code/joyjitchatterjee/hotel-booking-cancellation-prediction-99-accuracy
   - Destaques: Tratamento de desbalanceamento, otimização de hiperparâmetros

3. **Hotel Booking - Business Insights**
   - URL: https://www.kaggle.com/code/gauravduttakiit/hotel-booking-analysis
   - Destaques: Análise de negócios, insights estratégicos

### Documentação Técnica

1. **Scikit-learn Logistic Regression**
   - URL: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
   - Parâmetros importantes: penalty, C, solver, max_iter

2. **Classification Metrics**
   - URL: https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics
   - Métricas: Accuracy, Precision, Recall, F1-Score, AUC-ROC

3. **Confusion Matrix**
   - URL: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html

### Métricas de Avaliação

1. **ROC Curve and AUC**
   - Artigo: https://towardsdatascience.com/understanding-auc-roc-curve-68b2303cc9c5
   - Biblioteca: sklearn.metrics.roc_curve, roc_auc_score

2. **Precision-Recall Trade-off**
   - Artigo: https://machinelearningmastery.com/precision-recall-and-f-measure-for-imbalanced-classification/
   - Quando usar: Dados desbalanceados

3. **Classification Report**
   - Biblioteca: sklearn.metrics.classification_report
   - URL: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html

### Feature Importance

1. **Coefficient Interpretation in Logistic Regression**
   - Artigo: https://towardsdatascience.com/understanding-logistic-regression-coefficients-ba5ed88df850
   - Conceitos: Odds ratio, log-odds, marginal effects

2. **Permutation Importance**
   - Biblioteca: sklearn.inspection.permutation_importance
   - URL: https://scikit-learn.org/stable/modules/permutation_importance.html

### Comparação: Logistic vs Linear Regression

1. **Why Not Linear Regression for Classification?**
   - Artigo: https://towardsdatascience.com/why-not-use-linear-regression-for-classification-279cfa2e2e8e
   - Tópicos: Problemas com valores fora de [0,1], pressupostos violados

2. **Binary Classification Best Practices**
   - URL: https://machinelearningmastery.com/types-of-classification-in-machine-learning/

---

## QUESTÃO 3 - ANOVA (Online Retail Sales)

### Datasets

1. **Online Retail Dataset**
   - Fonte: UCI Machine Learning Repository
   - URL: https://archive.ics.uci.edu/ml/datasets/Online+Retail
   - Kaggle: https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci
   - Descrição: Transações de varejo online (2009-2011) de UK-based retailer

### Tutoriais e Notebooks de Referência

1. **Online Retail Analysis with ANOVA**
   - URL: https://www.kaggle.com/code/fabiendaniel/customer-segmentation
   - Destaques: Análise por país, segmentação de clientes, análise RFM

2. **ANOVA in Python - Complete Guide**
   - URL: https://towardsdatascience.com/anova-analysis-of-variance-explained-with-python-implementation-1d82e16e8aec
   - Destaques: One-way, two-way, repeated measures ANOVA

3. **Statistical Analysis of Retail Data**
   - URL: https://www.kaggle.com/code/xiaozhouwang/in-depth-analysis-online-retail-dataset
   - Destaques: Múltiplas análises estatísticas, visualizações

### Documentação Técnica

1. **SciPy Stats - ANOVA**
   - URL: https://docs.scipy.org/doc/scipy/reference/stats.html
   - Funções: f_oneway, kruskal (non-parametric alternative)

2. **Statsmodels ANOVA**
   - URL: https://www.statsmodels.org/stable/anova.html
   - Uso: Para ANOVA mais complexas (two-way, factorial)

### Testes de Pressupostos ANOVA

1. **Normalidade**
   - Shapiro-Wilk: scipy.stats.shapiro
   - Anderson-Darling: scipy.stats.anderson
   - Kolmogorov-Smirnov: scipy.stats.kstest

2. **Homocedasticidade**
   - Levene's Test: scipy.stats.levene
   - URL: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levene.html
   - Bartlett's Test: scipy.stats.bartlett (mais sensível a não-normalidade)

3. **Independência**
   - Conceito: Observações devem ser independentes
   - Verificação: Design do estudo, análise de resíduos

### Testes Post-hoc

1. **Tukey HSD**
   - Biblioteca: statsmodels.stats.multicomp.pairwise_tukeyhsd
   - URL: https://www.statsmodels.org/stable/generated/statsmodels.stats.multicomp.pairwise_tukeyhsd.html
   - Uso: Comparações múltiplas após ANOVA significativa

2. **Bonferroni Correction**
   - Uso: Ajuste de p-values para múltiplas comparações
   - URL: https://www.statsmodels.org/stable/generated/statsmodels.stats.multitest.multipletests.html

3. **Dunnett's Test**
   - Uso: Comparação de múltiplos grupos com um grupo controle

### Alternativas Não-Paramétricas

1. **Kruskal-Wallis Test**
   - Biblioteca: scipy.stats.kruskal
   - Quando usar: Quando pressupostos da ANOVA são violados
   - URL: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kruskal.html

2. **Mann-Whitney U Test**
   - Biblioteca: scipy.stats.mannwhitneyu
   - Uso: Alternativa não-paramétrica para t-test

### Correções para Violações

1. **Transformações**
   - Log, sqrt, Box-Cox para corrigir não-normalidade e heterocedasticidade
   - Artigo: https://statisticsbyjim.com/basics/remove-heteroscedasticity-transformation/

2. **Welch's ANOVA**
   - Uso: Quando há heterocedasticidade
   - Não assume variâncias iguais

---

## QUESTÃO 4 - CREDIT RISK PREDICTION (Análise Complexa)

### Datasets

1. **German Credit Risk Dataset**
   - Fonte: UCI Machine Learning Repository / Kaggle
   - URL: https://www.kaggle.com/datasets/uciml/german-credit
   - Descrição: 1000 registros com 20 atributos para classificação de crédito

2. **Credit Card Approval Dataset**
   - URL: https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction
   - Alternativa com mais features

### Tutoriais e Notebooks - Modelagem

1. **Credit Risk Modeling - Complete Guide**
   - URL: https://www.kaggle.com/code/prashant111/credit-risk-analytics
   - Qualidade: ⭐⭐⭐⭐⭐
   - Destaques: Múltiplos modelos, feature engineering, SMOTE

2. **Advanced Credit Scoring Models**
   - URL: https://www.kaggle.com/code/kabure/credit-risk-model-analysis-xgboost-vs-others
   - Destaques: XGBoost, LightGBM, CatBoost comparison

3. **Credit Default Prediction**
   - URL: https://www.kaggle.com/code/caesarmario/credit-default-prediction-end-to-end-ml-project
   - Destaques: Pipeline completo, deployment considerations

### Machine Learning Models

#### Decision Trees

1. **Scikit-learn Decision Trees**
   - URL: https://scikit-learn.org/stable/modules/tree.html
   - Parâmetros: max_depth, min_samples_split, min_samples_leaf

2. **Visualizing Decision Trees**
   - Biblioteca: sklearn.tree.plot_tree
   - Artigo: https://towardsdatascience.com/visualizing-decision-trees-with-python-scikit-learn-4c50070a4f47

#### Random Forest

1. **Scikit-learn Random Forest**
   - URL: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
   - Parâmetros importantes: n_estimators, max_features, bootstrap

2. **Random Forest Best Practices**
   - Artigo: https://towardsdatascience.com/hyperparameter-tuning-the-random-forest-in-python-using-scikit-learn-28d2aa77dd74

#### XGBoost

1. **XGBoost Documentation**
   - URL: https://xgboost.readthedocs.io/en/latest/python/python_intro.html
   - Parâmetros: learning_rate, max_depth, n_estimators, subsample

2. **XGBoost for Classification**
   - Artigo: https://machinelearningmastery.com/develop-first-xgboost-model-python-scikit-learn/

3. **XGBoost Hyperparameter Tuning**
   - Artigo: https://towardsdatascience.com/xgboost-fine-tune-and-optimize-your-model-23d996fab663

#### SVM (Support Vector Machines)

1. **Scikit-learn SVM**
   - URL: https://scikit-learn.org/stable/modules/svm.html
   - Kernels: linear, poly, rbf, sigmoid

2. **SVM for Classification**
   - Artigo: https://towardsdatascience.com/support-vector-machines-explained-with-python-examples-cb65e8172c85

### SHAP Values (Explainability)

1. **SHAP Documentation**
   - URL: https://shap.readthedocs.io/en/latest/
   - Instalação: pip install shap

2. **SHAP for Credit Risk**
   - Artigo: https://towardsdatascience.com/explainable-ai-xai-a-guide-to-7-packages-in-python-to-explain-your-models-932967f0634b
   - Notebook: https://www.kaggle.com/code/dansbecker/shap-values

3. **SHAP Plots**
   - Summary Plot: Visão geral de feature importance
   - Waterfall Plot: Explicação individual
   - Force Plot: Contribuição de cada feature
   - Dependence Plot: Relação entre feature e SHAP value

4. **SHAP Tutorial - Advanced**
   - URL: https://shap-lrjball.readthedocs.io/en/latest/example_notebooks/overviews/An%20introduction%20to%20explainable%20AI%20with%20Shapley%20values.html
   - Tópicos: TreeExplainer, KernelExplainer, DeepExplainer

### K-Means Clustering

1. **Scikit-learn K-Means**
   - URL: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
   - Parâmetros: n_clusters, init, n_init, max_iter

2. **Elbow Method**
   - Artigo: https://www.geeksforgeeks.org/elbow-method-for-optimal-value-of-k-in-kmeans/
   - Uso: Determinar número ótimo de clusters

3. **Silhouette Score**
   - Biblioteca: sklearn.metrics.silhouette_score
   - URL: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html
   - Interpretação: Valores próximos a 1 indicam clusters bem definidos

4. **K-Means for Customer Segmentation**
   - Artigo: https://towardsdatascience.com/customer-segmentation-using-k-means-clustering-d33964f238c3
   - Aplicação em credit risk: Segmentar perfis de risco

### DBSCAN Clustering

1. **Scikit-learn DBSCAN**
   - URL: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html
   - Parâmetros: eps, min_samples

2. **DBSCAN for Outlier Detection**
   - Artigo: https://towardsdatascience.com/dbscan-clustering-explained-97556a2ad556
   - Vantagens: Identifica outliers automaticamente (-1 label)

3. **Choosing DBSCAN Parameters**
   - Método: k-distance graph
   - Artigo: https://medium.com/@tarammullin/dbscan-parameter-estimation-ff8330e3a3bd

4. **DBSCAN vs K-Means**
   - Artigo: https://towardsdatascience.com/how-dbscan-works-and-why-should-i-use-it-443b4a191c80
   - DBSCAN: Forma clusters de forma arbitrária, identifica outliers
   - K-Means: Requer número de clusters pré-definido, assume clusters esféricos

### Model Comparison

1. **Cross-Validation**
   - Biblioteca: sklearn.model_selection.cross_val_score
   - URL: https://scikit-learn.org/stable/modules/cross_validation.html

2. **Hyperparameter Tuning**
   - GridSearchCV: Busca exaustiva
   - RandomizedSearchCV: Busca aleatória (mais rápida)
   - URL: https://scikit-learn.org/stable/modules/grid_search.html

3. **Model Selection Best Practices**
   - Artigo: https://machinelearningmastery.com/compare-machine-learning-algorithms-python-scikit-learn/

### Imbalanced Data

1. **SMOTE (Synthetic Minority Over-sampling)**
   - Biblioteca: imblearn.over_sampling.SMOTE
   - URL: https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html

2. **Class Weighting**
   - Parâmetro: class_weight='balanced' em modelos sklearn
   - Artigo: https://machinelearningmastery.com/cost-sensitive-learning-for-imbalanced-classification/

3. **Threshold Adjustment**
   - Ajustar threshold de classificação baseado em recall desejado
   - Artigo: https://machinelearningmastery.com/threshold-moving-for-imbalanced-classification/

---

## VISUALIZAÇÃO COM PLOTLY

### Documentação Oficial

1. **Plotly Python Documentation**
   - URL: https://plotly.com/python/
   - Seções importantes: Basic Charts, Statistical Charts, Scientific Charts

2. **Plotly Express**
   - URL: https://plotly.com/python/plotly-express/
   - High-level interface para gráficos rápidos

3. **Plotly Graph Objects**
   - URL: https://plotly.com/python/graph-objects/
   - Low-level interface para controle detalhado

### Gráficos Estatísticos

1. **Histograms**
   - URL: https://plotly.com/python/histograms/

2. **Box Plots**
   - URL: https://plotly.com/python/box-plots/

3. **Violin Plots**
   - URL: https://plotly.com/python/violin/

4. **Scatter Plots**
   - URL: https://plotly.com/python/line-and-scatter/

5. **Heatmaps**
   - URL: https://plotly.com/python/heatmaps/

6. **Subplots**
   - URL: https://plotly.com/python/subplots/
   - Uso: Criar múltiplos gráficos em uma figura

### Gráficos para Machine Learning

1. **Confusion Matrix Heatmap**
   - Exemplo: https://plotly.com/python/heatmaps/#annotated-heatmap

2. **ROC Curves**
   - Exemplo: https://plotly.com/python/roc-and-pr-curves/

3. **Learning Curves**
   - Custom implementation com go.Scatter

4. **Feature Importance**
   - Bar charts com go.Bar

### Interatividade

1. **Hover Data**
   - Adicionar informações ao passar o mouse
   - Parâmetro: hover_data

2. **Dropdown Menus**
   - URL: https://plotly.com/python/dropdowns/
   - Uso: Alternar entre diferentes visualizações

3. **Range Sliders**
   - URL: https://plotly.com/python/range-slider/
   - Uso: Zoom em séries temporais

### Temas e Estilos

1. **Plotly Templates**
   - URL: https://plotly.com/python/templates/
   - Templates: plotly, plotly_white, plotly_dark, ggplot2, seaborn

2. **Color Scales**
   - URL: https://plotly.com/python/builtin-colorscales/
   - Importantes: Viridis, RdBu, Blues (colorblind-friendly)

---

## JUPYTER NOTEBOOK - MELHORES PRÁTICAS

### Estrutura e Organização

1. **Best Practices for Jupyter Notebooks**
   - Artigo: https://towardsdatascience.com/jupyter-notebook-best-practices-f430a6ba8c69
   - Tópicos: Organização de células, documentação, reproducibilidade

2. **Jupyter Notebook for Data Science**
   - Artigo: https://www.datacamp.com/tutorial/tutorial-jupyter-notebook
   - Guia completo para uso profissional

### Markdown para Documentação

1. **Markdown Guide**
   - URL: https://www.markdownguide.org/basic-syntax/
   - Sintaxe: Headers, lists, links, images, code blocks

2. **LaTeX in Markdown**
   - Uso: Fórmulas matemáticas
   - Exemplo: `$y = \beta_0 + \beta_1 x_1 + \epsilon$`
   - URL: https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Typesetting%20Equations.html

3. **Academic Writing in Jupyter**
   - Estrutura: Introdução, Metodologia, Resultados, Discussão, Conclusões

### Export e Apresentação

1. **nbconvert - Convert Notebooks**
   - URL: https://nbconvert.readthedocs.io/en/latest/
   - Formatos: PDF, HTML, slides, markdown

2. **Jupyter to PDF**
   - Comando: `jupyter nbconvert --to pdf notebook.ipynb`
   - Requer: pandoc e LaTeX

3. **Jupyter to HTML**
   - Comando: `jupyter nbconvert --to html notebook.ipynb`
   - Vantagem: Mantém interatividade do Plotly

### Reproducibilidade

1. **Requirements.txt**
   - Comando: `pip freeze > requirements.txt`
   - Uso: Documentar versões de bibliotecas

2. **Random Seeds**
   - Sempre definir: np.random.seed(42), random.seed(42)
   - Uso: Garantir reproducibilidade de resultados

3. **Environment Management**
   - Conda: https://docs.conda.io/en/latest/
   - venv: https://docs.python.org/3/library/venv.html

---

## BIBLIOTECAS PYTHON - REFERÊNCIAS

### Core Data Science

1. **Pandas**
   - URL: https://pandas.pydata.org/docs/
   - Cheat Sheet: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

2. **NumPy**
   - URL: https://numpy.org/doc/stable/
   - Tutorial: https://numpy.org/doc/stable/user/quickstart.html

3. **SciPy**
   - URL: https://docs.scipy.org/doc/scipy/
   - Stats module: https://docs.scipy.org/doc/scipy/reference/stats.html

### Machine Learning

1. **Scikit-learn**
   - URL: https://scikit-learn.org/stable/documentation.html
   - User Guide: https://scikit-learn.org/stable/user_guide.html
   - API Reference: https://scikit-learn.org/stable/modules/classes.html

2. **XGBoost**
   - URL: https://xgboost.readthedocs.io/
   - Python API: https://xgboost.readthedocs.io/en/latest/python/python_api.html

3. **SHAP**
   - URL: https://shap.readthedocs.io/
   - Examples: https://shap.readthedocs.io/en/latest/example_notebooks/overviews/An%20introduction%20to%20explainable%20AI%20with%20Shapley%20values.html

### Statistical Modeling

1. **Statsmodels**
   - URL: https://www.statsmodels.org/stable/index.html
   - Regression: https://www.statsmodels.org/stable/regression.html
   - ANOVA: https://www.statsmodels.org/stable/anova.html

2. **Pingouin**
   - URL: https://pingouin-stats.org/
   - Alternativa user-friendly para análises estatísticas

---

## ARTIGOS ACADÊMICOS E LIVROS

### Livros Recomendados

1. **"An Introduction to Statistical Learning" - James, Witten, Hastie, Tibshirani**
   - Tópicos: Regressão, classificação, árvores, SVM, clustering
   - PDF gratuito: https://www.statlearning.com/

2. **"The Elements of Statistical Learning" - Hastie, Tibshirani, Friedman**
   - Versão mais avançada do anterior
   - PDF gratuito: https://hastie.su.domains/ElemStatLearn/

3. **"Python for Data Analysis" - Wes McKinney**
   - Criador do Pandas
   - Foco em manipulação e análise de dados

4. **"Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" - Aurélien Géron**
   - Guia prático completo

### Artigos sobre Explainability

1. **"A Unified Approach to Interpreting Model Predictions" (SHAP)**
   - Autores: Lundberg & Lee (2017)
   - URL: https://arxiv.org/abs/1705.07874

2. **"Explainable AI: A Review of Machine Learning Interpretability Methods"**
   - Artigo review sobre métodos de interpretabilidade

### Artigos sobre Credit Risk

1. **"Credit Risk Modeling using Machine Learning: A Survey"**
   - Review de métodos de ML para risco de crédito

2. **"Comparison of Classification Methods for Credit Scoring"**
   - Comparação entre diferentes algoritmos

---

## RECURSOS ADICIONAIS

### Cursos Online

1. **Coursera - Machine Learning by Andrew Ng**
   - URL: https://www.coursera.org/learn/machine-learning

2. **Fast.ai - Practical Deep Learning**
   - URL: https://www.fast.ai/

3. **DataCamp - Data Science Track**
   - Cursos práticos com Python

### Comunidades e Fóruns

1. **Stack Overflow**
   - Tag: [python], [pandas], [scikit-learn], [statistics]

2. **Cross Validated (Stats StackExchange)**
   - URL: https://stats.stackexchange.com/
   - Foco em estatística e machine learning

3. **Reddit**
   - r/datascience
   - r/MachineLearning
   - r/statistics

### Blogs e Sites

1. **Towards Data Science**
   - URL: https://towardsdatascience.com/
   - Artigos sobre todos os tópicos da prova

2. **Machine Learning Mastery**
   - URL: https://machinelearningmastery.com/
   - Tutoriais práticos

3. **Analytics Vidhya**
   - URL: https://www.analyticsvidhya.com/blog/
   - Guias e tutoriais

---

## CHECKLIST FINAL - PADRÃO ACADÊMICO

### Estrutura do Relatório
- [ ] Título, autor, data, instituição
- [ ] Executive summary
- [ ] Introdução com contexto e objetivos
- [ ] Metodologia detalhada
- [ ] Resultados com visualizações
- [ ] Discussão com interpretações
- [ ] Conclusões e recomendações
- [ ] Referências bibliográficas

### Análise Estatística
- [ ] Estatísticas descritivas completas
- [ ] Testes de pressupostos documentados
- [ ] Resultados com p-values e intervalos de confiança
- [ ] Interpretação estatística E de negócios
- [ ] Discussão de limitações

### Visualizações
- [ ] Todas usando Plotly (interativas)
- [ ] Títulos, labels e legendas claras
- [ ] Cores adequadas (colorblind-friendly)
- [ ] Anotações em pontos importantes
- [ ] Exportadas corretamente no HTML/PDF

### Código
- [ ] Comentários explicativos
- [ ] Variáveis com nomes descritivos
- [ ] Funções reutilizáveis
- [ ] Random seeds definidos
- [ ] Warnings suprimidos quando apropriado

### Reproducibilidade
- [ ] Bibliotecas e versões documentadas
- [ ] Dados de origem citados
- [ ] Passos de pré-processamento claros
- [ ] Código executável sem erros
- [ ] Resultados consistentes em múltiplas execuções

---

**Este documento serve como guia completo de referências para desenvolver análises de nível de mestrado em Data Science e Statistical Analysis.**
