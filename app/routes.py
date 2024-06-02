from flask import Blueprint, request, jsonify
from .model import translate

bp = Blueprint('translate', __name__)

@bp.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data['text']
    
    # Translate the text
    translated_text = translate(text)
    
    # Return the translated text as JSON response
    return jsonify({'translated_text': translated_text})
