# OpenAI documentation

-  Generative pre-trained transformers (GPT)
    * **What does this mean? (explain this from back to front)**
    * transformer: an NN architecture
    * pre-trained: weight trained on (vast) corpora of language + code
    * generative: given a context (prompt), output the next most probable word(s) (<- tokens). Decoder portion of a transformer
    * **New programming paradigm: prompt GPT with natural language or code!**
-  GPT models operate on **tokens**
    * [tokenizer tool](https://platform.openai.com/tokenizer).
    * "As a rough rule of thumb, 1 token is approximately 4 characters or 0.75 words for English text."
    * One limitation to keep in mind is that for a GPT model the prompt and the generated output combined must be no more than the model's maximum context length
    * [model index] (https://platform.openai.com/docs/models/overview)
    * 
