# OpenAI documentation

## Definitional Notes

-  Generative pre-trained transformer (GPT) language model
    * **What does this mean? (explain this from back to front)**
    * language model
    * transformer: an NN architecture
    * pre-trained: weight trained on (vast) corpora of language + code
    * generative: given a context (prompt), output the next most probable word(s) (<- tokens). Decoder portion of a transformer
    * **New programming paradigm: prompt GPT with natural language or code!**
-  GPT models operate on **tokens**
    * [tokenizer tool](https://platform.openai.com/tokenizer).
    * "As a rough rule of thumb, 1 token is approximately 4 characters or 0.75 words for English text."
    * One limitation to keep in mind is that for a GPT model the prompt and the generated output combined must be no more than the model's maximum context length
    * [model index] (https://platform.openai.com/docs/models/overview)

## Setup

- Set up an account (different for ChatGPT and API)
- Explore [costs](https://openai.com/pricing), [data usage policy](https://openai.com/enterprise-privacy)
- Setup python and install openai package
- Create an API key and store in a private location
- [model updates](https://platform.openai.com/docs/models/continuous-model-upgrades)
- Premier model is GPT-4:
  >GPT-4 is a large multimodal model (accepting text inputs and emitting text outputs today, with image inputs coming in the future) that can solve difficult problems with greater accuracy than any of our previous models
- [Data usage](https://platform.openai.com/docs/models/how-we-use-your-data)
- [Terms and policies](https://openai.com/policies)

## [Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)
- Write clear instructions, ask for what you want
- 

# TODO:

- Fixup Introduction and Setup
- Fixup text analysis notebook
- Cleanup code base
- Incorporate code examples into notebook (testing, conda, github)
- Add conclusion notes
-  Record video on setting up and using Copilot
