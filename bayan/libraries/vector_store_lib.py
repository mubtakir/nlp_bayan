import logging
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

_stores = {}

class SimpleVectorStore:
    def __init__(self):
        self.documents = []
        self.embeddings = None # numpy array

    def add(self, docs, embeddings):
        """
        Adds documents and their embeddings.
        
        Args:
            docs (list of str): The documents.
            embeddings (list of list of float): The embeddings.
        """
        new_embeddings = np.array(embeddings)
        if self.embeddings is None:
            self.embeddings = new_embeddings
        else:
            self.embeddings = np.vstack([self.embeddings, new_embeddings])
        
        self.documents.extend(docs)

    def search(self, query_embedding, k=3):
        """
        Searches for similar documents.
        
        Args:
            query_embedding (list of float): The query embedding.
            k (int): Number of results to return.
            
        Returns:
            list of dict: [{'doc': str, 'score': float}]
        """
        if self.embeddings is None or len(self.documents) == 0:
            return []

        query_vec = np.array(query_embedding)
        
        # Cosine similarity: (A . B) / (||A|| * ||B||)
        # Assuming embeddings might not be normalized
        norm_docs = np.linalg.norm(self.embeddings, axis=1)
        norm_query = np.linalg.norm(query_vec)
        
        if norm_query == 0:
            return []
            
        scores = np.dot(self.embeddings, query_vec) / (norm_docs * norm_query)
        
        # Get top k indices
        top_k_indices = np.argsort(scores)[::-1][:k]
        
        results = []
        for idx in top_k_indices:
            results.append({
                'doc': self.documents[idx],
                'score': float(scores[idx])
            })
            
        return results

def create_collection(name):
    _stores[name] = SimpleVectorStore()
    return name

def add_documents(name, docs, embeddings):
    if name not in _stores:
        return False
    _stores[name].add(docs, embeddings)
    return True

def search(name, query_embedding, k=3):
    if name not in _stores:
        return []
    return _stores[name].search(query_embedding, k)
