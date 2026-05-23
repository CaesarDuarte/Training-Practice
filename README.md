# Práticas de Ciência de Dados / Data Science Practice

Repositório pessoal de estudos em Ciência de Dados.
Cada pasta reúne notebooks de prática organizados por tema, com pipelines comentados e exercícios.

> **Nota:** Idioma principal — **português**. Em desenvolvimento contínuo.

---

## Estrutura

```
Training-Practice/
│
├── Dados/                        # EDA, limpeza, engenharia de features
├── Estatistica/                  # Descritiva, inferencial, testes de hipótese
├── Machine-Learning/             # Supervisionado, não supervisionado, validação
├── Deep-Learning/                # Redes neurais com PyTorch (CPU)
├── NLP/                          # Texto em português, embeddings semânticos
├── Visao-Computacional/          # Transfer learning com PyTorch (CPU)
│
├── data/
│   ├── raw/                      # Dados originais
│   └── processed/                # Dados limpos / transformados
│
├── pixi.toml                     # Ambiente de dependências (Pixi)
└── README.md
```

---

## Como rodar

O projeto usa **[Pixi](https://pixi.sh)** para gerenciar o ambiente.

```bash
# Instalar o ambiente
pixi install

# Baixar recursos de NLP em português (rodar uma vez)
pixi run nltk-data
pixi run spacy-pt

# Abrir Jupyter Lab
pixi run lab
```

---

## Tópicos de Estudo

### Dados
Carregamento, inspeção, EDA, limpeza, transformação e feature engineering. Uso de DuckDB para consultas em arquivos maiores e salvamento em Parquet.

### Estatística
Estatística descritiva e inferencial: distribuições, testes de hipótese (t, Mann-Whitney, qui-quadrado), tamanho de efeito e intervalos de confiança.

### Machine Learning
Algoritmos supervisionados e não supervisionados com scikit-learn. Pipeline, validação cruzada, métricas e explicabilidade com SHAP.

### Deep Learning
Redes neurais com PyTorch: MLP, CNN, RNN. Loop de treino completo com curvas de aprendizado e avaliação.

### NLP
Pré-processamento em português (stopwords, stemming RSLP), TF-IDF e embeddings semânticos com `sentence-transformers`.

### Visão Computacional
Classificação de imagens com transfer learning (EfficientNet-B0). Data augmentation e fine-tuning progressivo.

---

**Principais pacotes:** Python 3.12 · pandas · scikit-learn · PyTorch · transformers · sentence-transformers · spaCy · DuckDB · Polars · SHAP
