from transformers import MarianMTModel, MarianTokenizer

# Load pre-trained model and tokenizer for English to Hindi translation
model_name = 'Helsinki-NLP/opus-mt-en-hi'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate(text):
    # Tokenize the input text
    batch = tokenizer.prepare_seq2seq_batch(src_texts=[text], return_tensors="pt")
    
    # Perform the translation
    translated = model.generate(**batch)
    
    # Decode the translated text
    translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)[0]
    return translated_text
    