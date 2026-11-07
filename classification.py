def classify(data):
    """Простейшая классификация: 1 если число положительное, иначе 0"""
    return [1 if x > 0 else 0 for x in data]
