"""
Neural Engine for Bayan
محرك عصبي للغة بيان
"""

import sys
import logging
from typing import List, Dict, Any, Optional

try:
    import torch
    import torch.nn.functional as F
    from transformers import AutoTokenizer, AutoModel
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False
    logging.warning("Neural Engine: torch/transformers not found. Operating in fallback mode.")

class NeuralEngine:
    """
    Manages Neural Network operations (Embeddings, Similarity, Neural Search).
    Uses lightweight models to keep performance reasonable.
    """
    _instance = None
    
    def __new__(cls, model_name: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"):
        if cls._instance is None:
            cls._instance = super(NeuralEngine, cls).__new__(cls)
            cls._instance.initialized = False
        return cls._instance

    def __init__(self, model_name: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"):
        if self.initialized:
            return
            
        self.model_name = model_name
        self.tokenizer = None
        self.model = None
        self.device = "cpu"
        
        if TRANSFORMERS_AVAILABLE:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
            self._load_model()
        
        self.initialized = True

    def _load_model(self):
        """Load the Transformer model."""
        try:
            logging.info(f"Loading Neural Model: {self.model_name} on {self.device}")
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModel.from_pretrained(self.model_name)
            self.model.to(self.device)
            self.model.eval()
        except Exception as e:
            logging.error(f"Failed to load neural model: {e}")
            self.model = None

    def embed(self, text: str) -> Optional[Any]:
        """Generate embedding vector for text."""
        if not TRANSFORMERS_AVAILABLE or self.model is None:
            return None

        try:
            inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)
            inputs = {k: v.to(self.device) for k, v in inputs.items()}
            
            with torch.no_grad():
                outputs = self.model(**inputs)
                # Mean Pooling - Take attention mask into account for correct averaging
                attention_mask = inputs['attention_mask']
                token_embeddings = outputs.last_hidden_state
                
                input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
                sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
                sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
                embeddings = sum_embeddings / sum_mask
                
                # Normalize embeddings
                embeddings = F.normalize(embeddings, p=2, dim=1)
                
            return embeddings[0].cpu().numpy()
        except Exception as e:
            logging.error(f"Embedding failed: {e}")
            return None

    def compute_similarity(self, text1: str, text2: str) -> float:
        """Compute cosine similarity between two texts."""
        vec1 = self.embed(text1)
        vec2 = self.embed(text2)
        
        if vec1 is None or vec2 is None:
            return 0.0
            
        # Vectors are already normalized, so dot product is cosine similarity
        if TRANSFORMERS_AVAILABLE:
            t1 = torch.tensor(vec1)
            t2 = torch.tensor(vec2)
            return torch.dot(t1, t2).item()
        return 0.0

    def batch_embed(self, texts: List[str]) -> Optional[Any]:
        """Generate embeddings for a batch of texts."""
        if not TRANSFORMERS_AVAILABLE or self.model is None:
            return None
            
        try:
            inputs = self.tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=128)
            inputs = {k: v.to(self.device) for k, v in inputs.items()}
            
            with torch.no_grad():
                outputs = self.model(**inputs)
                attention_mask = inputs['attention_mask']
                token_embeddings = outputs.last_hidden_state
                input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
                sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
                sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
                embeddings = sum_embeddings / sum_mask
                embeddings = F.normalize(embeddings, p=2, dim=1)
                
            return embeddings.cpu().numpy()
        except Exception as e:
            logging.error(f"Batch embedding failed: {e}")
            return None
