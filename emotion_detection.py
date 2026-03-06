"""
Emotion Detection Module

This module provides a function to analyze the emotion expressed
in a piece of text using the Watson NLP Emotion Predict API.
"""

import requests
import json


def emotion_detector(text_to_analyse):
    """
    Analyse emotion of a given text using the Watson NLP service.

    Parameters
    ----------
    text_to_analyse : str

    Returns
    -------
    The response text returned by the Watson Emotion Predict API .... str
    """

    # URL for the Watson Emotion Prediction service
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    # Header specifying which pretrained model to use
    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    # JSON payload containing the text to analyze
    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    # Send POST request to Watson NLP service
    response = requests.post(url, json=input_json, headers=headers)

    # Return the raw response text from the API
    return response.text