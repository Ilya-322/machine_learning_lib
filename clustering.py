def cluster(data, k=2):
    """Простейшая кластеризация: раскладывает элементы по k группам"""
    return [i % k for i, _ in enumerate(data)]
