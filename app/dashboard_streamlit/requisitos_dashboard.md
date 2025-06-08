# Requisitos do Dashboard 

Este documento descreve os requisitos para o desenvolvimento do dashboard.

## Requisitos do Dashboard

### Inputs

- Upload de arquivo (TXT ou CSV) contendo o Seeds Dataset
- Filtro por variedade (Kama, Rosa, Canadian)
- Sliders para filtrar intervalos de cada atributo:
  - Área
  - Perímetro
  - Compacidade
  - Comprimento do núcleo
  - Largura do núcleo
  - Assimetria
  - Comprimento do sulco do núcleo

### Outputs

- Estatísticas descritivas (média, mediana, desvio-padrão)
- Exportação de resultados em CSV e PDF

### Gráficos

- Histogramas individuais para cada atributo
- Boxplots para análise de outliers
- Gráficos de dispersão (por exemplo: área vs perímetro)
- Mapa de calor de correlação entre atributos

### Resultados do Modelo

- Métricas de desempenho: acurácia, precisão, recall, F1-score
- Matriz de confusão
- Gráfico de importância das variáveis (para modelos como Random Forest)
- Área de predição: entrada manual de atributos e exibição da classe prevista com probabilidade
