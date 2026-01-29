import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyze emotions in the given text using Watson NLP Emotion Predict function.
    
    Args:
        text_to_analyze: The text string to analyze for emotions
        
    Returns:
        The text attribute of the response object from the Emotion Detection function
    """
    # Define the URL for the Emotion Predict API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Define the headers with the model ID
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create the input JSON with the text to analyze
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    # Make the POST request to the API
    response = requests.post(url, json=input_json, headers=headers)
    
    # Return the text attribute of the response object
    return response.text
