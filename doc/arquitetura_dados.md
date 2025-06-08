

## **1. Como os dados irão fluir no projeto**

### Etapas principais:

1. **Armazenamento inicial**:

   * O dataset será armazenado em arquivos **CSV**.
   * Conversão do arquivo `.txt` para `.csv` utilizando delimitador `,` ou `;`.

2. **Pré-processamento**:

   * Leitura do CSV usando bibliotecas como **pandas**.
   * Tratamento de dados faltantes (há alguns valores ausentes no dataset).
   * Conversão de tipos, normalização ou padronização, se necessário.

3. **Armazenamento intermediário** (opcional):

   * Após o pré-processamento, pode-se salvar um **novo CSV limpo**.

4. **Uso**:

   * Treinamento de modelos de **Machine Learning**.
   * Análises estatísticas ou geração de relatórios.
   * Visualizações gráficas.

5. **Saída**:

   * Resultados salvos em arquivos `.csv` ou `.json`.
   * Modelos salvos como `.pkl` (pickle) ou outros formatos adequados.

---

## **2. Onde os dados serão armazenados, tratados e usados**

| Etapa                       | Local de Armazenamento                | Ferramentas                      |
| --------------------------- | ------------------------------------- | -------------------------------- |
| Original                    | Arquivo `.txt` convertido para `.csv` | Manualmente ou via script Python |
| Tratamento                  | Memória (DataFrame)                   | pandas, NumPy                    |
| Persistência pós-tratamento | Arquivo `.csv` limpo ou SQLite        | pandas (`to_csv`), `sqlite3`     |
| Modelagem                   | Memória (arrays, DataFrame)           | scikit-learn, TensorFlow, etc    |
| Resultados                  | Arquivo `.csv` ou `.json`             | pandas, json                     |

---

## **3. Estrutura do arquivo de dados (.csv)**

### Colunas (baseado no dataset de sementes UCI):

1. Area
1. **Área**

   * **Significado**: Representa a **área** da semente projetada (medida em milímetros quadrados, mm²).
   * **Interpretação**: Quanto maior a área, maior o tamanho físico da semente.

2. Perimeter
2. **Perímetro**

   * **Significado**: É o **perímetro** da semente, ou seja, a soma dos comprimentos das bordas da semente (medido em milímetros).
   * **Interpretação**: Ajuda a descrever a forma geral da semente.

3. Compactness
3. **Compacidade**

   * **Significado**: Mede o **grau de compacidade** da semente, calculado por uma fórmula envolvendo a área e o perímetro.
   * **Interpretação**: Quanto mais próximo de 1, mais **compacta** e **circular** é a semente; valores menores indicam formas mais alongadas.

4. Kernel Length
4. **Comprimento do Grão**

   * **Significado**: Representa o **comprimento** da semente (em mm).
   * **Interpretação**: Mede a maior dimensão da semente.


5. **Largura do Grão** Kernel Width

   * **Significado**: Mede a **largura** da semente (em mm), ou seja, a dimensão perpendicular ao comprimento.
   * **Interpretação**: Ajuda a entender a proporção e o formato da semente.

6. **Coeficiente de Assimetria** Asymmetry Coefficient

   * **Significado**: Avalia o grau de **assimetria** da semente, ou seja, o quanto ela difere de uma forma simétrica ideal.
   * **Interpretação**: Valores mais altos indicam maior assimetria; valores mais baixos indicam sementes mais simétricas.


7. **Comprimento do Sulco do Grão** Kernel Groove Length

   * **Significado**: Mede o comprimento do **sulco** (uma depressão ou marca) presente no grão, em milímetros.
   * **Interpretação**: Esse traço morfológico é importante na distinção entre diferentes tipos de sementes.

8. **Classe** Class Label (1, 2 ou 3)

   * **Significado**: Indica a **classe** ou **tipo de semente**.
   * **Valores possíveis**:

     * **1** → Kama
     * **2** → Rosa
     * **3** → Canadian
   * **Interpretação**: É o **rótulo** usado para classificação, aprendizado supervisionado ou análise.


Exemplo de cabeçalho CSV:

```csv
area,perimeter,compactness,kernel_length,kernel_width,asymmetry,kernel_groove,class
15.26,14.84,0.871,5.763,3.312,2.221,5.22,1
...
```

### Delimitador sugerido: `,` (padrão).

### Formato de codificação: `UTF-8`.


## **4. Decidir sobre banco de dados**

**Decisão:**

**Simples e portátil**: CSV é suficiente para pequenos projetos, análises e protótipos.


**Recomendação:**

* Para Machine Learning ou análise exploratória: **txt**.


