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
|   └── routes.py                   # request api 
│
├── models/
│   └── dictionary.pkl              # Pre-trained model (if available)
│
├── notebook/
│   ├── testing.ipynb               # examplenotebook1
│   └── translator.ipynb            # examplenotebook2
│
├── .gitignore                      # gitignore
├── index.html                      # web-translator
├── README.md                       # Readme.md
├── requirements.txt                # python requirements
├── run.py                          # app run
└── style.css                       # styling to index.html
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project is inspired by various sequence-to-sequence models in natural language processing.
- Thanks to the open-source community for providing valuable resources and tools.

## Contributors

<a href="https://github.com/mehtachandrashekhar/AI-based-Translator-Tool/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=mehtachandrashekhar/AI-based-Translator-Tool" />
</a>
