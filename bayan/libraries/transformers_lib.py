import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    from transformers import pipeline
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False
    logger.warning("Transformers library not found. Please install it using 'pip install transformers torch'.")

_loaded_pipelines = {}

def load_model(task, model_name=None):
    """
    Loads a Hugging Face pipeline.
    
    Args:
        task (str): The task to perform (e.g., 'sentiment-analysis', 'text-generation').
        model_name (str, optional): The name of the model to use.
        
    Returns:
        str: A unique ID for the loaded pipeline, or None if failed.
    """
    if not TRANSFORMERS_AVAILABLE:
        return None
        
    try:
        # Use a default model if none provided, or let pipeline decide
        if model_name:
            pipe = pipeline(task, model=model_name)
        else:
            pipe = pipeline(task)
            
        pipeline_id = f"{task}_{model_name if model_name else 'default'}"
        _loaded_pipelines[pipeline_id] = pipe
        logger.info(f"Loaded pipeline: {pipeline_id}")
        return pipeline_id
    except Exception as e:
        logger.error(f"Error loading pipeline: {e}")
        return None

def predict(pipeline_id, text):
    """
    Runs prediction using a loaded pipeline.
    
    Args:
        pipeline_id (str): The ID of the pipeline to use.
        text (str): The input text.
        
    Returns:
        list/dict: The prediction result.
    """
    if pipeline_id not in _loaded_pipelines:
        logger.error(f"Pipeline not found: {pipeline_id}")
        return None
        
    try:
        pipe = _loaded_pipelines[pipeline_id]
        result = pipe(text)
        return result
    except Exception as e:
        logger.error(f"Error running prediction: {e}")
        return None

def generate(pipeline_id, text, max_length=50):
    """
    Generates text using a loaded pipeline.
    
    Args:
        pipeline_id (str): The ID of the pipeline.
        text (str): The prompt text.
        max_length (int): Maximum length of generated text.
        
    Returns:
        list: The generation result.
    """
    if pipeline_id not in _loaded_pipelines:
        logger.error(f"Pipeline not found: {pipeline_id}")
        return None
        
    try:
        pipe = _loaded_pipelines[pipeline_id]
        result = pipe(text, max_length=max_length)
        return result
    except Exception as e:
        logger.error(f"Error generating text: {e}")
        return None
