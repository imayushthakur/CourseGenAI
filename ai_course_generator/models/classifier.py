import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
from typing import List, Dict, Any

from ..config import MODEL_NAME

class ZeroShotClassifier:
    """Zero-shot classifier using BART-large-mnli."""
    
    def __init__(self, model_name: str = MODEL_NAME):
        self.model_name = model_name
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        # Initialize the model and tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.model.to(self.device)
        
    def classify(self, text: str, labels: List[str], multi_label: bool = False) -> Dict[str, float]:
        """Classify text into one or more of the given labels."""
        try:
            classifier = pipeline("zero-shot-classification", 
                                  model=self.model_name, 
                                  device=0 if torch.cuda.is_available() else -1)
            
            result = classifier(text, labels, multi_label=multi_label)
            
            # Construct a dictionary mapping labels to scores
            label_scores = {}
            for label, score in zip(result['labels'], result['scores']):
                label_scores[label] = score
            
            return label_scores
            
        except Exception as e:
            # Fallback to manual approach if pipeline fails
            return self._manual_classify(text, labels, multi_label)
    
    def _manual_classify(self, text: str, labels: List[str], multi_label: bool = False) -> Dict[str, float]:
        """Manual implementation of zero-shot classification."""
        label_scores = {}
        
        for label in labels:
            # Create hypothesis for the label
            hypothesis = f"This text is about {label}."
            
            # Tokenize
            encoded = self.tokenizer(text, hypothesis, truncation=True, return_tensors="pt")
            encoded = {k: v.to(self.device) for k, v in encoded.items()}
            
            # Get model prediction
            with torch.no_grad():
                outputs = self.model(**encoded)
                
            # Get entailment and contradiction scores
            entail_contradiction_logits = outputs.logits[0, [0, 2]]
            probs = torch.softmax(entail_contradiction_logits, dim=0)
            
            # Probability of the label being true is the entailment score
            label_scores[label] = probs[1].item()
            
        return label_scores
