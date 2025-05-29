# Cap3-ImplementandoalgoritmosdeMachineLearningcomScikitlearn
A classificação de grãos é uma etapa fundamental no controle de qualidade dentro da cadeia produtiva agrícola. Atualmente, em muitas cooperativas de pequeno e médio porte, esse processo ainda é realizado de forma manual por especialistas, utilizando inspeção visual e ferramentas simples.

---

# 🌾 **Projeto: Da Terra ao Código — Automatizando a Classificação de Grãos com Machine Learning**

---

## 📄 **Descrição do Projeto**

A classificação de grãos é uma etapa fundamental no controle de qualidade dentro da cadeia produtiva agrícola. Atualmente, em muitas cooperativas de pequeno e médio porte, esse processo ainda é realizado de forma manual por especialistas, utilizando inspeção visual e ferramentas simples. Isso gera desafios como alta demanda de tempo, custos operacionais elevados e possíveis erros humanos, afetando diretamente a eficiência e a qualidade do produto final.

Este projeto tem como foco o desenvolvimento de um sistema inteligente capaz de realizar a **classificação automática de grãos de trigo** com base em suas características físicas. A solução utiliza algoritmos de **Machine Learning** aplicados ao **"Seeds Dataset"** do UCI Machine Learning Repository, com amostras de três tipos de trigo: **Kama, Rosa e Canadian**.

Além do desenvolvimento dos modelos, será criado um **dashboard interativo utilizando Streamlit**, que permitirá que qualquer usuário — mesmo sem conhecimento técnico — possa realizar classificações, visualizar análises e extrair informações úteis sobre os grãos analisados.

---

## ✅ **Justificativa**

O desenvolvimento deste projeto se justifica pela necessidade crescente de **automatizar processos agrícolas**, tornando-os mais precisos, eficientes e acessíveis, especialmente para pequenos produtores e cooperativas.

### 💡 **Por que é necessário?**

* Processos manuais estão sujeitos a erros e inconsistências.
* Reduz o custo com mão de obra especializada.
* Aumenta a produtividade e padronização na classificação.
* Traz acessibilidade à tecnologia de análise de dados no campo.

### 🌎 **Impacto Esperado**

* Modernização das práticas agrícolas.
* Redução de custos operacionais.
* Tomada de decisão mais assertiva.
* Contribuição para a transformação digital no agronegócio.

---

## 🎯 **Objetivos**

### 🔹 **Objetivo Geral**

Desenvolver uma solução baseada em Machine Learning capaz de classificar grãos de trigo automaticamente a partir de suas características físicas, utilizando um dashboard interativo para facilitar a utilização pelos usuários.

### 🔸 **Objetivos Específicos**

* Realizar análise exploratória e pré-processamento dos dados.
* Implementar e comparar diferentes modelos de classificação.
* Otimizar os modelos para aumentar a acurácia e a robustez.
* Avaliar os modelos utilizando métricas como acurácia, precisão, recall, F1-score e matriz de confusão.
* Desenvolver um dashboard interativo que permita a utilização do modelo de classificação.
* Documentar todo o processo no GitHub com código, relatórios e arquivos auxiliares.

---

## 🔬 **Metodologia — CRISP-DM**

O projeto segue as etapas da metodologia **CRISP-DM (Cross Industry Standard Process for Data Mining)**, amplamente utilizada para desenvolvimento de projetos de ciência de dados.

### 🚦 **Etapas:**

1. **Entendimento do Negócio**

#### Fluxo de Dados

1. O dataset original está em formato `.txt`.
2. Os dados serão carregados em memória com `pandas` para pré-processamento.
3. Após o tratamento, o dataset limpo será salvo em `.csv`.
4. Os dados tratados serão usados para:
   - Treinamento de modelos de Machine Learning.
   - Análises estatísticas.
   - Visualizações.

#### Estrutura de Dados

| Coluna | Descrição |
|--------|----------|
| area | Área da semente |
| perimeter | Perímetro |
| compactness | Compacidade |
| kernel_length | Comprimento do grão |
| kernel_width | Largura do grão |
| asymmetry | Coeficiente de assimetria |
| kernel_groove | Comprimento do sulco do grão |
| class | Classe (1, 2 ou 3) |

#### Armazenamento

- **Dados brutos**: txt
- **Dados tratados**: txt limpo
- **Modelos**: arquivos `.pkl` ou similares
- **Resultados**: 

#### Banco de Dados

- Decidiu-se utilizar **txt** como estrutura de armazenamento.


2. **Entendimento dos Dados**

   * Análise do dataset "Seeds Dataset".
   * Compreensão das variáveis:

     * Área, Perímetro, Compacidade, Comprimento do Núcleo, Largura do Núcleo, Coeficiente de Assimetria, Comprimento do Sulco.

3. **Preparação dos Dados**

   * Verificação de valores ausentes.
   * Detecção e tratamento de outliers.
   * Normalização ou padronização dos dados.
   * Criação de visualizações (boxplots, histogramas, scatterplots, heatmap de correlação).

4. ## 📈 Machine Learning

###  Escolha e Avaliação de Algoritmos

Para esta fase do projeto, decidimos realizar o **treinamento e avaliação com múltiplos algoritmos** de Machine Learning, com o objetivo de identificar aquele que oferece o melhor desempenho para o problema de **prever a necessidade de irrigação**.

O problema foi modelado como uma **classificação binária**, onde o modelo deve prever se a irrigação é necessária (`1`) ou não (`0`), com base em variáveis como umidade do solo, níveis de nutrientes, temperatura e hora do dia.

---

### Algoritmos Avaliados

| Algoritmo                                  | Vantagens                                                              | Desvantagens                                              |
| ------------------------------------------ | ---------------------------------------------------------------------- | --------------------------------------------------------- |
| **Logistic Regression**                    | Simples, rápido, bom para baseline                                     | Supõe relação linear entre as variáveis                   |
| **Decision Tree**                          | Fácil de interpretar, lida com variáveis categóricas                   | Pode sofrer de overfitting e ser sensível a ruído         |
| **Random Forest**                          | Reduz overfitting, boa acurácia, robusto                               | Mais lento e menos interpretável que uma árvore única     |
| **K-Nearest Neighbors (KNN)**              | Simples, não-paramétrico, intuitivo                                    | Custo computacional elevado em grandes conjuntos de dados |
| **Support Vector Machine (SVM)**           | Eficaz em espaços de alta dimensão, bom para problemas complexos       | Mais lento e exige ajuste cuidadoso de parâmetros         |
| **Gradient Boosting (LightGBM, CatBoost)** | Alta performance, lida bem com não-linearidades e dados desbalanceados | Complexidade maior e menos interpretável                  |

---

### Metodologia

Todos os algoritmos foram treinados utilizando a biblioteca **Scikit-learn** (com exceção do **LightGBM** e **CatBoost**, implementados com suas respectivas bibliotecas).

O dataset foi dividido em **80% para treino** e **20% para teste** utilizando **stratified split** para manter a proporção das classes.

O pré-processamento incluiu:

* Normalização das variáveis numéricas para algoritmos sensíveis a escala (KNN, SVM).
* Conversão de variáveis categóricas, se houver.
* Tratamento de dados ausentes.

---

### Métricas de Avaliação

Para comparar os modelos, utilizamos as seguintes métricas:

| Métrica                | Justificativa                                                |
| ---------------------- | ------------------------------------------------------------ |
| **Acurácia**           | Percentual de acertos gerais                                 |
| **Precisão**           | Evitar falsos positivos: irrigar desnecessariamente          |
| **Recall**             | Evitar falsos negativos: falhar em irrigar quando necessário |
| **F1-Score**           | Métrica principal para balancear precisão e recall           |
| **Matriz de Confusão** | Análise visual dos erros de cada modelo                      |

**Obs.:** Se o dataset apresentar **desbalanceamento** entre classes, as métricas como **F1-Score** e **Recall** terão maior peso na decisão final.

---

### Processo de Treinamento

Para cada modelo, seguimos o mesmo pipeline:

1. Separação de **features** e **target**.
2. Divisão em **treino** e **teste**.
3. Ajuste de **parâmetros padrão** (sem hiperparâmetros complexos, para avaliação justa).
4. Treinamento do modelo.
5. Avaliação com as métricas definidas.

---

### Exemplo de Código para Avaliação de Todos os Modelos

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

import lightgbm as lgb
from catboost import CatBoostClassifier

# Separação
X = df[['umidade', 'nutrientes', 'temperatura', 'hora_dia']]
y = df['precisa_irrigar']

# Divisão
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# Normalização
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Modelos
models = {
    'Logistic Regression': LogisticRegression(),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
    'KNN': KNeighborsClassifier(),
    'SVM': SVC(probability=True),
    'LightGBM': lgb.LGBMClassifier(),
    'CatBoost': CatBoostClassifier(verbose=0)
}

# Treinamento e avaliação
for name, model in models.items():
    if name in ['KNN', 'SVM', 'Logistic Regression']:
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
    else:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

    print(f"\nModelo: {name}")
    print(classification_report(y_test, y_pred))
    print("Matriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))
```

---

###  Definição do Algoritmo Final

Após realizar a avaliação com todos os modelos e comparar os resultados com base nas métricas definidas, selecionaremos como **algoritmo final** aquele que apresentar o **melhor equilíbrio entre F1-Score, precisão e recall**, priorizando a capacidade do modelo em evitar **erros críticos** para o sistema de irrigação.

---

### Justificativa a ser adicionada após os testes

**Após a execução dos testes, o algoritmo com melhor desempenho foi o:**

 **Random Forest Classifier** com F1-Score: 
 **Precision**: 
 **Recall**: 

O Random Forest foi escolhido como modelo final pois apresentou o melhor equilíbrio entre precisão e recall, além de ser robusto contra overfitting e fornecer uma boa explicabilidade através das importâncias das features.

---

### Considerações Finais

Essa abordagem de testar múltiplos algoritmos garante uma escolha **baseada em dados**, e não apenas em suposições teóricas. Além disso, o pipeline criado é facilmente reutilizável e extensível para novas versões do sistema.


---


5. **Otimização**

   * Aplicação de **Grid Search** e/ou **Random Search** para ajuste de hiperparâmetros.
   * Escolha do modelo com melhor desempenho.

6. **Avaliação**

   * Avaliação final com métricas:

     * Acurácia
     * Precisão
     * Recall
     * F1-score
     * Matriz de confusão
   * Análise de erros e limitações.

7. **Implantação (Deploy)**

   * Desenvolvimento de um **dashboard interativo com Streamlit**.
   * Interface gráfica amigável para utilização do modelo.
   * (Opcional) Integração com banco de dados para armazenar resultados.

---

## 🏗️ **Estrutura do Projeto (Arquitetura de Pastas)**

```
Classificacao-Graos-ML/
├── 📁 dados/
│   ├── seeds_dataset.csv
│   └── dados_tratados.csv
├── 📁 notebooks/
│   ├── 1_analise_exploratoria.ipynb
│   ├── 2_modelagem.ipynb
│   ├── 3_otimizacao.ipynb
│   └── 4_dashboard_streamlit.ipynb
├── 📁 modelos/
│   └── modelo_final.pkl
├── 📁 dashboard_streamlit/
│   ├── app.py
│   ├── model.pkl
│   └── requirements.txt
├── 📁 imagens/
│   ├── boxplot.png
│   ├── heatmap_correlacao.png
│   ├── matriz_confusao.png
│   ├── scatterplot.png
│   └── dashboard.png
├── 📁 banco_de_dados/
│   └── modelo_banco.sql
├── README.md
└── LICENSE
```

---

## 🚦 **Kanban de Organização (Sugestão)**

### 🔧 **Backlog**

* Download e organização do dataset.
* Definir escopo completo e arquitetura de dados.
* Levantamento dos requisitos do dashboard e funcionalidades.

### 🧠 **Design**

* Criar fluxograma da solução.
* Desenhar o layout do dashboard Streamlit.
* Planejar a estrutura de notebooks, modelos e banco de dados.

### 🚀 **A Fazer**

* Realizar análise exploratória dos dados.
* Tratar dados (outliers, normalização).
* Implementar modelos (KNN, SVM, Random Forest).
* Avaliar e comparar modelos.
* Realizar otimização dos hiperparâmetros.
* Exportar modelo final treinado (.pkl).
* Criar dashboard interativo no Streamlit.
* Desenvolver banco de dados (opcional).
* Documentar todo o projeto no README.
* Gravar vídeo de apresentação.

### ✅ **Feito**

* Tarefas concluídas.

---

## 🧠 **Insights Esperados**

1. **Insight Técnico:**
   Avaliar quais características dos grãos são mais relevantes para a classificação. Identificar padrões que poderiam passar despercebidos na análise manual, como correlações entre área, compacidade e comprimento do sulco.

2. **Insight Operacional:**
   Demonstrar que é possível implementar uma solução acessível, barata e eficiente que automatiza um processo tradicionalmente manual, democratizando o acesso à inteligência artificial no setor agrícola, especialmente para pequenas e médias cooperativas.

---

## 🚀 **Impacto Final**

Ao final deste projeto, as cooperativas e produtores terão acesso a uma ferramenta capaz de:

* Reduzir o tempo de classificação dos grãos;
* Aumentar a precisão e consistência dos resultados;
* Melhorar a eficiência dos processos agrícolas;
* Facilitar a integração de inteligência artificial no campo.

## **Referências**

[1] Charytanowicz, M., Niewczas, J., Kulczycki, P., Kowalski, P., & Lukasik, S. (2010). Seeds [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5H30K.
