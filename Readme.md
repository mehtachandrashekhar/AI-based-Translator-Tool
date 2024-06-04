# AI-Based Language Translation

## Overview

This project implements an AI-based language translation system using same core technologies: Encoder-Decoder architecture, Long Short-Term Memory (LSTM) networks,Bidirectional LSTM networks and Embedding layers. The system is designed to translate text from one language to another by learning from a dataset of parallel sentences.

## Features

- **Encoder-Decoder Architecture**: Utilizes a sequence-to-sequence model to handle input and output sequences of different lengths.
- **LSTM Networks**: Employs LSTM cells to manage long-term dependencies and improve translation accuracy.
- **Embedding Layers**: Converts words into dense vectors that capture semantic meanings, enhancing the model's understanding of language.
- **Bidirectional LSTM Networks**: Improves context capture by processing input sequences in both forward and backward directions.

## Usage

### Training the Model

1. **Prepare your dataset**: Ensure you have a dataset of parallel sentences in the source and target languages.
2. **Preprocess the data**: Tokenize the sentences and create the necessary input-output pairs.

### Translating Text

Once the model is trained, you can use it to translate sentences:

**Translate a sentence**:
  ```bash
   python translate.py --sentence "Your sentence here"
   ```

## Directory Structure

```
ai-language-translation/
│
├── app/
│   ├── __init__.py                 # initialization application
|   ├── model.py                    # model from hugging face
|   └── routes.py                   # reqeust api 
│
├── models/
│   └── dictionary.pkl              # Pre-trained model (if available)
│
├── notebook/
│   ├── encoder_decoder.py          # Encoder-Decoder architecture
│   ├── bidirectional_lstm.py       # Bidirectional LSTM implementation
│   ├── embedding.py                # Embedding layer implementation
│   ├── preprocess.py               # Data preprocessing script
│   └── train.py                    # Training script
│   └── translate.py                # Translation script
│   └── evaluate.py                 # Evaluation script
│
├── requirements.txt                # Python dependencies
├── README.md                       # Project overview and instructions
└── LICENSE                         # License information
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project is inspired by various sequence-to-sequence models in natural language processing.
- Thanks to the open-source community for providing valuable resources and tools.
