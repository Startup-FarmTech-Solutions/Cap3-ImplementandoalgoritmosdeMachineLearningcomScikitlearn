from sklearn.metrics import classification_report, confusion_matrix

def avaliar_modelo(nome, y_test, y_pred):
    print(f"Modelo: {nome}")
    print("Matriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))
    print("Relatório de Classificação:")
    print(classification_report(y_test, y_pred))
