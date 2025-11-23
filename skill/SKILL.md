# Data Science & Statistical Analysis - Academic Master's Level

## Overview
Comprehensive skill for advanced statistical analysis and data science, designed for academic research and business intelligence at master's degree level. Specializes in regression analysis, classification, ANOVA, clustering, and explainable AI with industry-standard practices.

## Core Competencies

### 1. Statistical Modeling
- Linear Regression (OLS, Ridge, Lasso, ElasticNet)
- Logistic Regression (Binary, Multinomial)
- ANOVA (One-way, Two-way, Factorial)
- Assumption testing and model diagnostics
- Residual analysis and heteroscedasticity detection

### 2. Machine Learning
- Supervised Learning: Decision Trees, Random Forest, XGBoost, SVM
- Unsupervised Learning: K-Means, DBSCAN, Hierarchical Clustering
- Model evaluation: Cross-validation, Hyperparameter tuning
- Performance metrics: Accuracy, Precision, Recall, F1-Score, AUC-ROC

### 3. Explainable AI
- SHAP (SHapley Additive exPlanations) values
- Feature importance analysis
- Partial Dependence Plots (PDP)
- Local Interpretable Model-agnostic Explanations (LIME)

### 4. Data Visualization
- **Primary tool: Plotly** (interactive, publication-ready)
- Distribution analysis (histograms, box plots, violin plots)
- Correlation matrices and heatmaps
- Regression diagnostics plots
- Confusion matrices and ROC curves
- SHAP summary and force plots

## Technical Stack

### Required Libraries
```python
# Core Data Science
import pandas as pd
import numpy as np
from scipy import stats

# Visualization (ALWAYS USE PLOTLY)
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff

# Statistical Modeling
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import (
    mean_squared_error, r2_score, mean_absolute_error,
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score, roc_curve
)
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm
from scipy.stats import shapiro, normaltest, jarque_bera, anderson, levene, bartlett

# Machine Learning Models
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.svm import SVC

# Clustering
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score, davies_bouldin_score

# Explainability
import shap

# Warnings suppression
import warnings
warnings.filterwarnings('ignore')
```

## Workflow Structure

### Phase 1: Exploratory Data Analysis (EDA)

#### 1.1 Data Loading & Initial Inspection
```python
# Load data
df = pd.read_csv('dataset.csv')

# Basic info
print("=" * 80)
print("DATASET OVERVIEW")
print("=" * 80)
print(f"\nShape: {df.shape[0]} rows × {df.shape[1]} columns\n")
print(df.info())
print("\n" + "=" * 80)
print("FIRST ROWS")
print("=" * 80)
print(df.head())

# Missing values analysis
missing = pd.DataFrame({
    'Column': df.columns,
    'Missing_Count': df.isnull().sum(),
    'Missing_Percentage': (df.isnull().sum() / len(df) * 100).round(2)
})
missing = missing[missing['Missing_Count'] > 0].sort_values('Missing_Count', ascending=False)
print("\n" + "=" * 80)
print("MISSING VALUES ANALYSIS")
print("=" * 80)
print(missing)
```

#### 1.2 Descriptive Statistics (USE PLOTLY)
```python
# Summary statistics
print("\n" + "=" * 80)
print("DESCRIPTIVE STATISTICS - NUMERICAL VARIABLES")
print("=" * 80)
print(df.describe().round(2))

# For categorical variables
categorical_cols = df.select_dtypes(include=['object']).columns
if len(categorical_cols) > 0:
    print("\n" + "=" * 80)
    print("DESCRIPTIVE STATISTICS - CATEGORICAL VARIABLES")
    print("=" * 80)
    for col in categorical_cols:
        print(f"\n{col}:")
        print(df[col].value_counts())
```

#### 1.3 Distribution Analysis with Plotly
```python
def plot_distributions(df, numerical_cols, title_prefix=""):
    """
    Create interactive distribution plots using Plotly
    """
    n_cols = len(numerical_cols)
    n_rows = (n_cols + 2) // 3
    
    fig = make_subplots(
        rows=n_rows, 
        cols=3,
        subplot_titles=[f"{col}" for col in numerical_cols],
        vertical_spacing=0.1,
        horizontal_spacing=0.1
    )
    
    for idx, col in enumerate(numerical_cols):
        row = idx // 3 + 1
        col_pos = idx % 3 + 1
        
        fig.add_trace(
            go.Histogram(
                x=df[col],
                name=col,
                marker_color='lightblue',
                showlegend=False,
                nbinsx=30
            ),
            row=row,
            col=col_pos
        )
    
    fig.update_layout(
        title_text=f"{title_prefix}Distribution Analysis",
        height=300 * n_rows,
        showlegend=False
    )
    
    fig.show()

# Usage
numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
plot_distributions(df, numerical_cols)
```

#### 1.4 Correlation Analysis with Plotly
```python
def plot_correlation_matrix(df, numerical_cols, title="Correlation Matrix"):
    """
    Create interactive correlation heatmap using Plotly
    """
    corr_matrix = df[numerical_cols].corr()
    
    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='RdBu',
        zmid=0,
        text=corr_matrix.values.round(2),
        texttemplate='%{text}',
        textfont={"size": 10},
        colorbar=dict(title="Correlation")
    ))
    
    fig.update_layout(
        title=title,
        width=800,
        height=700,
        xaxis={'side': 'bottom'},
        yaxis={'autorange': 'reversed'}
    )
    
    fig.show()
    
    return corr_matrix

# Usage
corr_matrix = plot_correlation_matrix(df, numerical_cols)
```

### Phase 2: Linear Regression (Question 1)

#### 2.1 Model Construction
```python
# Prepare data
X = df[feature_columns]
y = df[target_column]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Build model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Coefficients
coef_df = pd.DataFrame({
    'Feature': feature_columns,
    'Coefficient': model.coef_
}).sort_values('Coefficient', key=abs, ascending=False)

print("\n" + "=" * 80)
print("MODEL COEFFICIENTS")
print("=" * 80)
print(coef_df)
print(f"\nIntercept: {model.intercept_:.2f}")

# Performance metrics
r2_train = r2_score(y_train, y_pred_train)
r2_test = r2_score(y_test, y_pred_test)
rmse_train = np.sqrt(mean_squared_error(y_train, y_pred_train))
rmse_test = np.sqrt(mean_squared_error(y_test, y_pred_test))
mae_test = mean_absolute_error(y_test, y_pred_test)

print("\n" + "=" * 80)
print("MODEL PERFORMANCE")
print("=" * 80)
print(f"R² Score (Train): {r2_train:.4f}")
print(f"R² Score (Test): {r2_test:.4f}")
print(f"RMSE (Train): {rmse_train:.2f}")
print(f"RMSE (Test): {rmse_test:.2f}")
print(f"MAE (Test): {mae_test:.2f}")
```

#### 2.2 Assumptions Testing
```python
def check_linear_regression_assumptions(X, y, y_pred, model_name="Linear Regression"):
    """
    Comprehensive assumption testing for linear regression
    """
    print("\n" + "=" * 80)
    print(f"ASSUMPTIONS TESTING - {model_name}")
    print("=" * 80)
    
    # Calculate residuals
    residuals = y - y_pred
    
    # 1. Linearity (correlation between residuals and predictions should be 0)
    print("\n1. LINEARITY TEST")
    print("-" * 80)
    linearity_corr = np.corrcoef(y_pred, residuals)[0, 1]
    print(f"Correlation (predictions vs residuals): {linearity_corr:.4f}")
    print("✓ PASS" if abs(linearity_corr) < 0.1 else "✗ FAIL - Non-linear relationship detected")
    
    # 2. Normality of residuals
    print("\n2. NORMALITY OF RESIDUALS")
    print("-" * 80)
    
    # Shapiro-Wilk test
    stat_shapiro, p_shapiro = shapiro(residuals)
    print(f"Shapiro-Wilk Test: statistic={stat_shapiro:.4f}, p-value={p_shapiro:.4f}")
    print("✓ PASS (normal)" if p_shapiro > 0.05 else "✗ FAIL (not normal)")
    
    # Jarque-Bera test
    stat_jb, p_jb = jarque_bera(residuals)
    print(f"Jarque-Bera Test: statistic={stat_jb:.4f}, p-value={p_jb:.4f}")
    print("✓ PASS (normal)" if p_jb > 0.05 else "✗ FAIL (not normal)")
    
    # 3. Homoscedasticity (Breusch-Pagan test)
    print("\n3. HOMOSCEDASTICITY TEST")
    print("-" * 80)
    
    # Add constant for statsmodels
    X_with_const = sm.add_constant(X)
    bp_test = het_breuschpagan(residuals, X_with_const)
    
    labels = ['LM Statistic', 'LM-Test p-value', 'F-Statistic', 'F-Test p-value']
    print(dict(zip(labels, bp_test)))
    print("✓ PASS (homoscedastic)" if bp_test[1] > 0.05 else "✗ FAIL (heteroscedastic)")
    
    # 4. Multicollinearity (VIF)
    print("\n4. MULTICOLLINEARITY TEST (VIF)")
    print("-" * 80)
    
    vif_data = pd.DataFrame()
    vif_data["Feature"] = X.columns
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    vif_data = vif_data.sort_values('VIF', ascending=False)
    
    print(vif_data)
    print("\nInterpretation:")
    print("  VIF < 5: No multicollinearity")
    print("  5 ≤ VIF < 10: Moderate multicollinearity")
    print("  VIF ≥ 10: High multicollinearity (problematic)")
    
    high_vif = vif_data[vif_data['VIF'] >= 10]
    if len(high_vif) > 0:
        print(f"\n✗ WARNING: {len(high_vif)} features with high VIF detected")
    else:
        print("\n✓ PASS: No concerning multicollinearity")
    
    return residuals

# Usage
residuals = check_linear_regression_assumptions(X_train, y_train, y_pred_train)
```

#### 2.3 Diagnostic Plots with Plotly
```python
def plot_regression_diagnostics(y_true, y_pred, residuals, model_name="Linear Regression"):
    """
    Create comprehensive diagnostic plots using Plotly
    """
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=(
            'Predicted vs Actual',
            'Residuals vs Predicted',
            'Q-Q Plot',
            'Residuals Distribution'
        ),
        specs=[[{"type": "scatter"}, {"type": "scatter"}],
               [{"type": "scatter"}, {"type": "histogram"}]]
    )
    
    # 1. Predicted vs Actual
    fig.add_trace(
        go.Scatter(
            x=y_true,
            y=y_pred,
            mode='markers',
            marker=dict(color='lightblue', size=5, opacity=0.6),
            name='Predictions',
            showlegend=False
        ),
        row=1, col=1
    )
    
    # Perfect prediction line
    min_val = min(y_true.min(), y_pred.min())
    max_val = max(y_true.max(), y_pred.max())
    fig.add_trace(
        go.Scatter(
            x=[min_val, max_val],
            y=[min_val, max_val],
            mode='lines',
            line=dict(color='red', dash='dash'),
            name='Perfect Prediction',
            showlegend=False
        ),
        row=1, col=1
    )
    
    # 2. Residuals vs Predicted
    fig.add_trace(
        go.Scatter(
            x=y_pred,
            y=residuals,
            mode='markers',
            marker=dict(color='lightcoral', size=5, opacity=0.6),
            name='Residuals',
            showlegend=False
        ),
        row=1, col=2
    )
    
    # Zero line
    fig.add_hline(y=0, line_dash="dash", line_color="red", row=1, col=2)
    
    # 3. Q-Q Plot
    sorted_residuals = np.sort(residuals)
    theoretical_quantiles = stats.norm.ppf(np.linspace(0.01, 0.99, len(sorted_residuals)))
    
    fig.add_trace(
        go.Scatter(
            x=theoretical_quantiles,
            y=sorted_residuals,
            mode='markers',
            marker=dict(color='lightgreen', size=5, opacity=0.6),
            name='Q-Q Plot',
            showlegend=False
        ),
        row=2, col=1
    )
    
    # Q-Q line
    fig.add_trace(
        go.Scatter(
            x=theoretical_quantiles,
            y=theoretical_quantiles,
            mode='lines',
            line=dict(color='red', dash='dash'),
            name='Normal Line',
            showlegend=False
        ),
        row=2, col=1
    )
    
    # 4. Residuals Distribution
    fig.add_trace(
        go.Histogram(
            x=residuals,
            marker_color='lightyellow',
            name='Residuals',
            showlegend=False,
            nbinsx=50
        ),
        row=2, col=2
    )
    
    # Update axes labels
    fig.update_xaxes(title_text="Actual Values", row=1, col=1)
    fig.update_yaxes(title_text="Predicted Values", row=1, col=1)
    
    fig.update_xaxes(title_text="Predicted Values", row=1, col=2)
    fig.update_yaxes(title_text="Residuals", row=1, col=2)
    
    fig.update_xaxes(title_text="Theoretical Quantiles", row=2, col=1)
    fig.update_yaxes(title_text="Sample Quantiles", row=2, col=1)
    
    fig.update_xaxes(title_text="Residuals", row=2, col=2)
    fig.update_yaxes(title_text="Frequency", row=2, col=2)
    
    fig.update_layout(
        title_text=f"{model_name} - Diagnostic Plots",
        height=800,
        showlegend=False
    )
    
    fig.show()

# Usage
plot_regression_diagnostics(y_test, y_pred_test, y_test - y_pred_test)
```

#### 2.4 Model Adjustments & Transformations
```python
def apply_transformations(df, target_col, transformation='log'):
    """
    Apply transformations to handle assumption violations
    """
    transformations = {
        'log': lambda x: np.log1p(x),
        'sqrt': lambda x: np.sqrt(x),
        'box-cox': lambda x: stats.boxcox(x + 1)[0]  # +1 to handle zeros
    }
    
    if transformation in transformations:
        df_transformed = df.copy()
        df_transformed[f'{target_col}_transformed'] = transformations[transformation](df[target_col])
        return df_transformed
    else:
        raise ValueError(f"Transformation '{transformation}' not supported")

# Example: Log transformation
if residuals.std() > threshold:  # if heteroscedasticity detected
    print("\n" + "=" * 80)
    print("APPLYING LOG TRANSFORMATION TO TARGET VARIABLE")
    print("=" * 80)
    
    # Transform target
    y_train_log = np.log1p(y_train)
    y_test_log = np.log1p(y_test)
    
    # Refit model
    model_log = LinearRegression()
    model_log.fit(X_train, y_train_log)
    
    # Predictions (transform back)
    y_pred_train_log = np.expm1(model_log.predict(X_train))
    y_pred_test_log = np.expm1(model_log.predict(X_test))
    
    # New metrics
    r2_test_log = r2_score(y_test, y_pred_test_log)
    rmse_test_log = np.sqrt(mean_squared_error(y_test, y_pred_test_log))
    
    print(f"\nImproved R² Score (Test): {r2_test_log:.4f}")
    print(f"Improved RMSE (Test): {rmse_test_log:.2f}")
```

### Phase 3: Logistic Regression (Question 2)

#### 3.1 Model Construction & Evaluation
```python
# Prepare data
X = df[feature_columns]
y = df[target_column]

# Encode target if necessary
if y.dtype == 'object':
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build model
log_model = LogisticRegression(random_state=42, max_iter=1000)
log_model.fit(X_train_scaled, y_train)

# Predictions
y_pred_train = log_model.predict(X_train_scaled)
y_pred_test = log_model.predict(X_test_scaled)
y_pred_proba = log_model.predict_proba(X_test_scaled)[:, 1]

# Metrics
print("\n" + "=" * 80)
print("LOGISTIC REGRESSION - PERFORMANCE METRICS")
print("=" * 80)

accuracy_train = accuracy_score(y_train, y_pred_train)
accuracy_test = accuracy_score(y_test, y_pred_test)
precision = precision_score(y_test, y_pred_test)
recall = recall_score(y_test, y_pred_test)
f1 = f1_score(y_test, y_pred_test)
auc = roc_auc_score(y_test, y_pred_proba)

print(f"Accuracy (Train): {accuracy_train:.4f}")
print(f"Accuracy (Test): {accuracy_test:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")
print(f"AUC-ROC: {auc:.4f}")

print("\n" + "-" * 80)
print("CLASSIFICATION REPORT")
print("-" * 80)
print(classification_report(y_test, y_pred_test))
```

#### 3.2 Confusion Matrix with Plotly
```python
def plot_confusion_matrix(y_true, y_pred, labels=None, title="Confusion Matrix"):
    """
    Create interactive confusion matrix using Plotly
    """
    cm = confusion_matrix(y_true, y_pred)
    
    if labels is None:
        labels = [f"Class {i}" for i in range(len(cm))]
    
    # Calculate percentages
    cm_percent = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] * 100
    
    # Create annotations
    annotations = []
    for i in range(len(cm)):
        for j in range(len(cm)):
            annotations.append(
                dict(
                    text=f"{cm[i, j]}<br>({cm_percent[i, j]:.1f}%)",
                    x=labels[j],
                    y=labels[i],
                    showarrow=False,
                    font=dict(color="white" if cm[i, j] > cm.max() / 2 else "black")
                )
            )
    
    fig = go.Figure(data=go.Heatmap(
        z=cm,
        x=labels,
        y=labels,
        colorscale='Blues',
        showscale=True
    ))
    
    fig.update_layout(
        title=title,
        xaxis=dict(title="Predicted Label"),
        yaxis=dict(title="True Label"),
        annotations=annotations,
        width=600,
        height=500
    )
    
    fig.show()

# Usage
plot_confusion_matrix(y_test, y_pred_test, labels=['Not Cancelled', 'Cancelled'])
```

#### 3.3 ROC Curve with Plotly
```python
def plot_roc_curve(y_true, y_pred_proba, title="ROC Curve"):
    """
    Create interactive ROC curve using Plotly
    """
    fpr, tpr, thresholds = roc_curve(y_true, y_pred_proba)
    auc_score = roc_auc_score(y_true, y_pred_proba)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=fpr,
        y=tpr,
        mode='lines',
        name=f'ROC Curve (AUC = {auc_score:.3f})',
        line=dict(color='darkorange', width=2)
    ))
    
    fig.add_trace(go.Scatter(
        x=[0, 1],
        y=[0, 1],
        mode='lines',
        name='Random Classifier',
        line=dict(color='navy', width=2, dash='dash')
    ))
    
    fig.update_layout(
        title=title,
        xaxis=dict(title='False Positive Rate'),
        yaxis=dict(title='True Positive Rate'),
        width=700,
        height=600,
        legend=dict(x=0.6, y=0.1)
    )
    
    fig.show()

# Usage
plot_roc_curve(y_test, y_pred_proba)
```

#### 3.4 Feature Importance Analysis
```python
def plot_feature_importance_logistic(model, feature_names, top_n=15):
    """
    Plot feature importance for logistic regression using coefficients
    """
    # Get absolute coefficients
    importance = np.abs(model.coef_[0])
    
    # Create dataframe
    importance_df = pd.DataFrame({
        'Feature': feature_names,
        'Importance': importance
    }).sort_values('Importance', ascending=False).head(top_n)
    
    # Plot
    fig = go.Figure(go.Bar(
        x=importance_df['Importance'],
        y=importance_df['Feature'],
        orientation='h',
        marker_color='lightblue'
    ))
    
    fig.update_layout(
        title=f'Top {top_n} Most Important Features',
        xaxis_title='Absolute Coefficient Value',
        yaxis_title='Feature',
        height=500,
        yaxis={'autorange': 'reversed'}
    )
    
    fig.show()
    
    return importance_df

# Usage
importance_df = plot_feature_importance_logistic(log_model, feature_columns)
print("\n" + "=" * 80)
print("FEATURE IMPORTANCE")
print("=" * 80)
print(importance_df)
```

### Phase 4: ANOVA (Question 3)

#### 4.1 ANOVA Implementation
```python
def perform_anova(df, group_col, value_col):
    """
    Perform one-way ANOVA with comprehensive reporting
    """
    print("\n" + "=" * 80)
    print(f"ONE-WAY ANOVA: {value_col} by {group_col}")
    print("=" * 80)
    
    # Group data
    groups = [group[value_col].values for name, group in df.groupby(group_col)]
    group_names = df[group_col].unique()
    
    # Descriptive statistics by group
    print("\nDESCRIPTIVE STATISTICS BY GROUP")
    print("-" * 80)
    desc_stats = df.groupby(group_col)[value_col].describe()
    print(desc_stats)
    
    # Perform ANOVA
    f_statistic, p_value = stats.f_oneway(*groups)
    
    print("\n" + "-" * 80)
    print("ANOVA RESULTS")
    print("-" * 80)
    print(f"F-Statistic: {f_statistic:.4f}")
    print(f"P-Value: {p_value:.4f}")
    
    if p_value < 0.05:
        print(f"\n✓ RESULT: Reject H0 (p < 0.05)")
        print(f"There ARE significant differences between group means.")
    else:
        print(f"\n✗ RESULT: Fail to reject H0 (p ≥ 0.05)")
        print(f"There are NO significant differences between group means.")
    
    return f_statistic, p_value, groups, group_names

# Usage
f_stat, p_val, groups, group_names = perform_anova(df, 'Country', 'Quantity')
```

#### 4.2 ANOVA Assumptions Testing
```python
def check_anova_assumptions(groups, group_names):
    """
    Test ANOVA assumptions: normality and homoscedasticity
    """
    print("\n" + "=" * 80)
    print("ANOVA ASSUMPTIONS TESTING")
    print("=" * 80)
    
    # 1. Normality test (Shapiro-Wilk for each group)
    print("\n1. NORMALITY TEST (Shapiro-Wilk)")
    print("-" * 80)
    
    normality_results = []
    for i, group in enumerate(groups):
        if len(group) >= 3:  # Shapiro-Wilk requires at least 3 samples
            stat, p = shapiro(group)
            normality_results.append({
                'Group': group_names[i],
                'Statistic': stat,
                'P-Value': p,
                'Normal': 'Yes' if p > 0.05 else 'No'
            })
    
    norm_df = pd.DataFrame(normality_results)
    print(norm_df)
    
    all_normal = all(norm_df['P-Value'] > 0.05)
    print(f"\n{'✓ PASS' if all_normal else '✗ FAIL'}: {'All groups' if all_normal else 'Some groups'} {'appear' if all_normal else 'do not appear'} normally distributed")
    
    # 2. Homoscedasticity test (Levene's test)
    print("\n2. HOMOSCEDASTICITY TEST (Levene's Test)")
    print("-" * 80)
    
    stat_levene, p_levene = levene(*groups)
    print(f"Levene's Statistic: {stat_levene:.4f}")
    print(f"P-Value: {p_levene:.4f}")
    
    if p_levene > 0.05:
        print("\n✓ PASS: Homoscedasticity assumption met (equal variances)")
    else:
        print("\n✗ FAIL: Heteroscedasticity detected (unequal variances)")
        print("Consider using Welch's ANOVA or transformations")
    
    return all_normal, p_levene > 0.05

# Usage
is_normal, is_homoscedastic = check_anova_assumptions(groups, group_names)
```

#### 4.3 Post-hoc Tests
```python
def perform_posthoc_tukey(df, group_col, value_col):
    """
    Perform Tukey HSD post-hoc test
    """
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    
    print("\n" + "=" * 80)
    print("POST-HOC TEST: TUKEY HSD")
    print("=" * 80)
    
    tukey_result = pairwise_tukeyhsd(
        endog=df[value_col],
        groups=df[group_col],
        alpha=0.05
    )
    
    print(tukey_result)
    
    return tukey_result

# Usage (if ANOVA is significant)
if p_val < 0.05:
    tukey_result = perform_posthoc_tukey(df, 'Country', 'Quantity')
```

#### 4.4 ANOVA Visualization with Plotly
```python
def plot_anova_results(df, group_col, value_col):
    """
    Create comprehensive ANOVA visualization
    """
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Box Plot by Group', 'Violin Plot by Group'),
        column_widths=[0.5, 0.5]
    )
    
    # Box plot
    for group in df[group_col].unique():
        group_data = df[df[group_col] == group][value_col]
        fig.add_trace(
            go.Box(
                y=group_data,
                name=str(group),
                showlegend=False,
                marker_color='lightblue'
            ),
            row=1, col=1
        )
    
    # Violin plot
    for group in df[group_col].unique():
        group_data = df[df[group_col] == group][value_col]
        fig.add_trace(
            go.Violin(
                y=group_data,
                name=str(group),
                showlegend=False,
                marker_color='lightcoral'
            ),
            row=1, col=2
        )
    
    fig.update_layout(
        title_text=f"ANOVA Analysis: {value_col} by {group_col}",
        height=500,
        showlegend=False
    )
    
    fig.update_yaxes(title_text=value_col, row=1, col=1)
    fig.update_yaxes(title_text=value_col, row=1, col=2)
    fig.update_xaxes(title_text=group_col, row=1, col=1)
    fig.update_xaxes(title_text=group_col, row=1, col=2)
    
    fig.show()

# Usage
plot_anova_results(df, 'Country', 'Quantity')
```

### Phase 5: Advanced ML & Explainability (Question 4)

#### 5.1 Multiple Model Comparison
```python
def compare_classification_models(X_train, X_test, y_train, y_test):
    """
    Train and compare multiple classification models
    """
    print("\n" + "=" * 80)
    print("MULTIPLE MODEL COMPARISON")
    print("=" * 80)
    
    # Define models
    models = {
        'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
        'Decision Tree': DecisionTreeClassifier(random_state=42, max_depth=10),
        'Random Forest': RandomForestClassifier(random_state=42, n_estimators=100),
        'XGBoost': XGBClassifier(random_state=42, n_estimators=100, eval_metric='logloss'),
        'SVM': SVC(random_state=42, probability=True)
    }
    
    # Store results
    results = []
    trained_models = {}
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    for name, model in models.items():
        print(f"\nTraining {name}...")
        
        # Train
        model.fit(X_train_scaled, y_train)
        
        # Predict
        y_pred = model.predict(X_test_scaled)
        y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]
        
        # Metrics
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        auc = roc_auc_score(y_test, y_pred_proba)
        
        results.append({
            'Model': name,
            'Accuracy': accuracy,
            'Precision': precision,
            'Recall': recall,
            'F1-Score': f1,
            'AUC-ROC': auc
        })
        
        trained_models[name] = model
    
    # Create comparison dataframe
    results_df = pd.DataFrame(results).sort_values('F1-Score', ascending=False)
    
    print("\n" + "-" * 80)
    print("MODEL COMPARISON RESULTS")
    print("-" * 80)
    print(results_df.round(4))
    
    return results_df, trained_models, scaler

# Usage
results_df, trained_models, scaler = compare_classification_models(
    X_train, X_test, y_train, y_test
)
```

#### 5.2 Model Comparison Visualization
```python
def plot_model_comparison(results_df):
    """
    Visualize model comparison using Plotly
    """
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'AUC-ROC']
    
    fig = go.Figure()
    
    for metric in metrics:
        fig.add_trace(go.Bar(
            name=metric,
            x=results_df['Model'],
            y=results_df[metric],
            text=results_df[metric].round(3),
            textposition='auto',
        ))
    
    fig.update_layout(
        title='Model Performance Comparison',
        xaxis_title='Model',
        yaxis_title='Score',
        barmode='group',
        height=600,
        legend=dict(x=1.05, y=1)
    )
    
    fig.show()

# Usage
plot_model_comparison(results_df)
```

#### 5.3 SHAP Values Analysis
```python
def analyze_shap_values(model, X_train, X_test, feature_names, model_name="Model"):
    """
    Comprehensive SHAP analysis with multiple visualizations
    """
    print("\n" + "=" * 80)
    print(f"SHAP VALUES ANALYSIS - {model_name}")
    print("=" * 80)
    
    # Create explainer
    if hasattr(model, 'predict_proba'):
        explainer = shap.Explainer(model, X_train)
    else:
        explainer = shap.KernelExplainer(model.predict, X_train)
    
    # Calculate SHAP values
    print("\nCalculating SHAP values...")
    shap_values = explainer(X_test)
    
    # 1. Summary Plot (Bar)
    print("\n1. Global Feature Importance (Summary Plot - Bar)")
    shap.summary_plot(shap_values, X_test, feature_names=feature_names, 
                      plot_type="bar", show=False)
    plt.tight_layout()
    plt.show()
    
    # 2. Summary Plot (Beeswarm)
    print("\n2. Feature Impact Distribution (Summary Plot - Beeswarm)")
    shap.summary_plot(shap_values, X_test, feature_names=feature_names, show=False)
    plt.tight_layout()
    plt.show()
    
    # 3. Feature importance dataframe
    feature_importance = pd.DataFrame({
        'Feature': feature_names,
        'Mean_SHAP': np.abs(shap_values.values).mean(axis=0)
    }).sort_values('Mean_SHAP', ascending=False)
    
    print("\n" + "-" * 80)
    print("TOP 10 MOST IMPORTANT FEATURES (by mean absolute SHAP)")
    print("-" * 80)
    print(feature_importance.head(10))
    
    # 4. Waterfall plot for first prediction
    print("\n3. Individual Prediction Explanation (Waterfall Plot)")
    shap.plots.waterfall(shap_values[0], show=False)
    plt.tight_layout()
    plt.show()
    
    return shap_values, feature_importance

# Usage
# Select best model
best_model_name = results_df.iloc[0]['Model']
best_model = trained_models[best_model_name]

# Scale data
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Analyze SHAP
shap_values, feature_importance = analyze_shap_values(
    best_model, 
    X_train_scaled[:100],  # Use sample for faster computation
    X_test_scaled[:100],
    X_train.columns.tolist(),
    best_model_name
)
```

#### 5.4 K-Means Clustering
```python
def perform_kmeans_analysis(X, n_clusters_range=range(2, 11)):
    """
    Perform K-Means clustering with optimal cluster selection
    """
    print("\n" + "=" * 80)
    print("K-MEANS CLUSTERING ANALYSIS")
    print("=" * 80)
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Elbow method
    inertias = []
    silhouette_scores = []
    
    for n_clusters in n_clusters_range:
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        labels = kmeans.fit_predict(X_scaled)
        
        inertias.append(kmeans.inertia_)
        silhouette_scores.append(silhouette_score(X_scaled, labels))
    
    # Plot elbow curve
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Elbow Method', 'Silhouette Score')
    )
    
    fig.add_trace(
        go.Scatter(
            x=list(n_clusters_range),
            y=inertias,
            mode='lines+markers',
            name='Inertia',
            marker=dict(color='blue', size=8)
        ),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Scatter(
            x=list(n_clusters_range),
            y=silhouette_scores,
            mode='lines+markers',
            name='Silhouette Score',
            marker=dict(color='green', size=8)
        ),
        row=1, col=2
    )
    
    fig.update_xaxes(title_text="Number of Clusters", row=1, col=1)
    fig.update_yaxes(title_text="Inertia", row=1, col=1)
    fig.update_xaxes(title_text="Number of Clusters", row=1, col=2)
    fig.update_yaxes(title_text="Silhouette Score", row=1, col=2)
    
    fig.update_layout(
        title_text="K-Means: Optimal Cluster Selection",
        height=400,
        showlegend=False
    )
    
    fig.show()
    
    # Select optimal number of clusters (highest silhouette score)
    optimal_k = list(n_clusters_range)[np.argmax(silhouette_scores)]
    
    print(f"\nOptimal number of clusters: {optimal_k}")
    print(f"Silhouette Score: {max(silhouette_scores):.4f}")
    
    # Final clustering
    kmeans_final = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
    cluster_labels = kmeans_final.fit_predict(X_scaled)
    
    # Cluster analysis
    print("\n" + "-" * 80)
    print("CLUSTER PROFILES")
    print("-" * 80)
    
    X_with_clusters = X.copy()
    X_with_clusters['Cluster'] = cluster_labels
    
    cluster_profiles = X_with_clusters.groupby('Cluster').mean()
    print(cluster_profiles)
    
    # Cluster sizes
    cluster_sizes = pd.Series(cluster_labels).value_counts().sort_index()
    print("\n" + "-" * 80)
    print("CLUSTER SIZES")
    print("-" * 80)
    print(cluster_sizes)
    
    return kmeans_final, cluster_labels, X_scaled

# Usage
kmeans_model, cluster_labels, X_scaled = perform_kmeans_analysis(X)
```

#### 5.5 DBSCAN Clustering
```python
def perform_dbscan_analysis(X_scaled, eps_range=np.arange(0.3, 2.0, 0.1)):
    """
    Perform DBSCAN clustering for outlier detection
    """
    print("\n" + "=" * 80)
    print("DBSCAN CLUSTERING ANALYSIS")
    print("=" * 80)
    
    # Find optimal eps
    n_clusters_list = []
    n_noise_list = []
    
    for eps in eps_range:
        dbscan = DBSCAN(eps=eps, min_samples=5)
        labels = dbscan.fit_predict(X_scaled)
        
        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
        n_noise = list(labels).count(-1)
        
        n_clusters_list.append(n_clusters)
        n_noise_list.append(n_noise)
    
    # Plot parameter selection
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Number of Clusters', 'Number of Outliers')
    )
    
    fig.add_trace(
        go.Scatter(
            x=eps_range,
            y=n_clusters_list,
            mode='lines+markers',
            marker=dict(color='purple', size=6)
        ),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Scatter(
            x=eps_range,
            y=n_noise_list,
            mode='lines+markers',
            marker=dict(color='red', size=6)
        ),
        row=1, col=2
    )
    
    fig.update_xaxes(title_text="Eps Parameter", row=1, col=1)
    fig.update_yaxes(title_text="Number of Clusters", row=1, col=1)
    fig.update_xaxes(title_text="Eps Parameter", row=1, col=2)
    fig.update_yaxes(title_text="Number of Outliers", row=1, col=2)
    
    fig.update_layout(
        title_text="DBSCAN: Parameter Selection",
        height=400,
        showlegend=False
    )
    
    fig.show()
    
    # Select optimal eps (balance between clusters and outliers)
    optimal_idx = np.argmax(np.array(n_clusters_list) * (1 - np.array(n_noise_list) / len(X_scaled)))
    optimal_eps = eps_range[optimal_idx]
    
    print(f"\nOptimal eps parameter: {optimal_eps:.2f}")
    
    # Final DBSCAN
    dbscan_final = DBSCAN(eps=optimal_eps, min_samples=5)
    dbscan_labels = dbscan_final.fit_predict(X_scaled)
    
    n_clusters = len(set(dbscan_labels)) - (1 if -1 in dbscan_labels else 0)
    n_outliers = list(dbscan_labels).count(-1)
    
    print(f"Number of clusters: {n_clusters}")
    print(f"Number of outliers: {n_outliers} ({n_outliers/len(X_scaled)*100:.2f}%)")
    
    # Outlier analysis
    print("\n" + "-" * 80)
    print("OUTLIER ANALYSIS")
    print("-" * 80)
    
    outlier_mask = dbscan_labels == -1
    print(f"Total outliers detected: {outlier_mask.sum()}")
    print(f"Percentage of dataset: {outlier_mask.sum()/len(X_scaled)*100:.2f}%")
    
    return dbscan_final, dbscan_labels, outlier_mask

# Usage
dbscan_model, dbscan_labels, outlier_mask = perform_dbscan_analysis(X_scaled)
```

## Academic Report Structure

### Jupyter Notebook Cell Organization

```markdown
# [Title] - Statistical Analysis and Data Science

**Author:** [Name]  
**Institution:** Programa de Pós-graduação em Computação Aplicada – PPCA (UnB)  
**Date:** [Date]  
**Dataset:** [Dataset Name]

---

## Executive Summary

[Brief overview of the problem, methodology, key findings, and business recommendations]

---

## 1. Introduction

### 1.1 Problem Context

[Explain the business/research problem]

### 1.2 Objectives

[Clear statement of analysis objectives]

### 1.3 Dataset Description

[Describe the dataset, source, variables, and relevance]

---

## 2. Methodology

### 2.1 Data Collection and Preparation

[Describe data collection process, cleaning steps, handling missing values]

### 2.2 Exploratory Data Analysis (EDA)

[Descriptive statistics, distribution analysis, correlation analysis]

### 2.3 Statistical Methods Applied

[Detailed description of statistical methods: regression, classification, ANOVA, clustering]

### 2.4 Model Development

[Model selection, training process, hyperparameter tuning]

### 2.5 Model Evaluation

[Metrics used, validation strategy, comparison criteria]

---

## 3. Results

### 3.1 Descriptive Analysis

[Present descriptive statistics with visualizations]

### 3.2 Model Performance

[Present model results with metrics, confusion matrices, ROC curves]

### 3.3 Feature Importance and Explainability

[SHAP analysis, feature importance rankings, interpretations]

### 3.4 Clustering Analysis

[K-Means and DBSCAN results, cluster profiles, outlier detection]

---

## 4. Discussion

### 4.1 Statistical Interpretation

[Interpret results in statistical terms: significance, effect sizes, model validity]

### 4.2 Business Implications

[Translate statistical findings into business insights]

### 4.3 Limitations

[Discuss assumptions, limitations, potential biases]

### 4.4 Assumptions Validation

[Present results of assumption tests and how violations were addressed]

---

## 5. Conclusions and Recommendations

### 5.1 Key Findings

[Summarize main findings]

### 5.2 Strategic Recommendations

[Provide actionable business recommendations based on analysis]

### 5.3 Future Work

[Suggest improvements and future research directions]

---

## 6. References

[List all data sources, academic papers, libraries used]

---

## Appendix

### A. Code Repository
### B. Additional Visualizations
### C. Detailed Statistical Tests
```

## Best Practices for Academic Excellence

### 1. Statistical Rigor
- Always test assumptions before applying statistical methods
- Report effect sizes, not just p-values
- Use appropriate corrections for multiple testing
- Validate models on holdout data
- Report confidence intervals where applicable

### 2. Visualization Standards
- Use Plotly for all visualizations (interactive, publication-ready)
- Include proper axis labels, titles, and legends
- Use colorblind-friendly palettes
- Add annotations to highlight key findings
- Maintain consistent styling across all plots

### 3. Code Quality
- Use descriptive variable names
- Add comments explaining complex logic
- Follow PEP 8 style guide
- Create reusable functions for repeated tasks
- Include docstrings for all functions

### 4. Documentation
- Use markdown cells extensively
- Explain every analytical decision
- Link findings to business context
- Cite sources for methodologies
- Include mathematical formulations where relevant

### 5. Reproducibility
- Set random seeds for all stochastic processes
- Document library versions
- Save preprocessed data
- Export final models
- Provide clear instructions for replication

## Critical Reminders

1. **ALWAYS use Plotly** for visualizations (never matplotlib/seaborn in final deliverables)
2. **Test assumptions** before applying any statistical method
3. **Interpret results** in both statistical AND business contexts
4. **Document thoroughly** - assume the reader is a peer reviewer
5. **Validate models** - never trust a single metric
6. **Handle imbalanced data** - use stratification, SMOTE if needed
7. **Scale features** for distance-based algorithms
8. **Cross-validate** - never report only training performance
9. **Explain decisions** - justify every methodological choice
10. **Think critically** - question results that seem too good

## Output Format

- Export to **PDF** or **HTML** from Jupyter Notebook
- Include code cells with outputs
- Use markdown cells for explanations
- Ensure all visualizations are rendered
- Check that all sections are complete
- Proofread for clarity and coherence

---

**This skill enables Claude Code to perform master's-level statistical analysis and data science with academic rigor, business acumen, and technical excellence.**
