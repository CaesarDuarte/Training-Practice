import os

structure = [
    "Dados/datasets",
    "Dados/limpeza-e-transformacao",
    "Dados/visualizacao",
    "Estatistica/descritiva",
    "Estatistica/inferencial",
    "Machine-Learning/algoritmos-supervisionados",
    "Machine-Learning/algoritmos-nao-supervisionados",
    "Machine-Learning/validacao-de-modelos",
    "Machine-Learning/engenharia-de-features",
    "Deep-Learning/redes-neurais-convolucionais",
    "Deep-Learning/redes-neurais-recorrentes",
    "Deep-Learning/transfer-learning",
    "NLP/pre-processamento",
    "NLP/modelagem-de-topicos",
    "NLP/word-embeddings",
    "Visao-Computacional/deteccao-de-objetos",
    "Visao-Computacional/classificacao-de-imagens",
    "Visao-Computacional/segmentacao",
]

for folder in structure:
    os.makedirs(folder, exist_ok=True)

# Criar um arquivo README.md em cada pasta principal
main_folders = ["Dados", "Estatistica", "Machine-Learning", "Deep-Learning", "NLP", "Visao-Computacional"]
for folder in main_folders:
    with open(os.path.join(folder, "README.md"), "w") as f:
        f.write(f"# {folder}\n\nEste é um README temporário. Será atualizado no próximo commit que atingir esta pasta.")
