import numpy as np

# "Baza" filmow z embeddingami (w prawdziwym systemie np. z OpenAI API)
filmy = {
    "Incepcja":          np.array([0.8, 0.3, 0.9]),
    "Matrix":            np.array([0.75, 0.35, 0.85]),
    "Toy Story":         np.array([0.2, 0.9, 0.1]),
    "Shrek":             np.array([0.25, 0.85, 0.15]),
    "Szeregowiec Ryan":  np.array([0.6, 0.1, 0.7]),
}

def semantic_search(query_vec, database, top_k=3):
    results = []
    
    query_norm = np.linalg.norm(query_vec)
    
    for title, doc_vec in database.items():
        dot_product = np.dot(query_vec, doc_vec)
        
        doc_norm = np.linalg.norm(doc_vec)
        
        if query_norm == 0 or doc_norm == 0:
            sim = 0.0 
        else:
            sim = dot_product / (query_norm * doc_norm)
            
        results.append((title, sim))
        
    results.sort(key=lambda x: x[1], reverse=True)
    
    return results[:top_k]

if __name__ == "__main__":
    query = np.array([0.7, 0.3, 0.8])  
    
    print("Szukam filmów najbardziej podobnych do wektora zapytania...\n")
    results = semantic_search(query, filmy, top_k=3)
    
    print("Wyniki:")
    for title, sim in results:
        print(f"  {title}: {sim:.3f}")