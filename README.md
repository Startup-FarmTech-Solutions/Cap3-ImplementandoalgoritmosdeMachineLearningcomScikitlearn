FIAP - Faculdade de Informática e Administração Paulista 

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# 🌾  Da Terra ao Código — Automatizando a Classificação de Grãos com Machine Learning

## Nome do grupo

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/antoniobarros99/">Antonio Ancelmo Neto Barros </a>
- <a>Beatriz pilecaarte de Melo 
- <a>Francismar Alves Martins Junior </a> 
- <a href="https://https://www.linkedin.com/in/vitor-eiji/">Vitor Eiji Fernandes Teruia</a> 
- <a href="https://www.linkedin.com/in/matheus-soares04">Matheus Soares Bento da Silva</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/leonardoorabona/">Leo Ruiz</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">André Godoi</a>

--- 

## 📜 Descrição

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
* 
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


## 📁 Estrutura de pastas
```
├── app/
│   ├── app.py
│   └── requisitos_dashboard
├── dados/
│   ├── processados/
│   └── seeds_tratado.csv
├── doc/
│   ├── arquitetura_dados.md
│   └── notebooks/
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```
## 🔧 Como executar o código

### 1. Clonar o repositório

```
git clone https://github.com/seu-usuario/seu-repositorio.git
```
### 2. crie um ambiene virtual (opcional, mas recomendado)
```
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```
### 3. instalar as dependencias
```
pip install -r requirements.txt
```
### 4. executar os notebooks
```
jupyter notebook notebooks/
```
### 5. executar o dashboard
```
streamlit run app/dashboard_streamlit/app.py
```

## 🗃 Histórico de lançamentos
     
* 0.1.0 - 19/06/2025
    *

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
