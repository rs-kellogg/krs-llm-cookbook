# Generative Pre-Trained Transfomer Large Language Models (GPTs)

:::{admonition} Breaking this down
:class: note
- Language Models
- Large
- Transformer
- Pre-Trained
- Generative
:::

:::{admonition} **[Language Model](https://en.wikipedia.org/wiki/Language_model)**
:class: tip
A Language Model (LM) is a just model that assigns probabilities to sequences of words. Probabilities are estimated (the models are trained) using collections of naturally ocurring text, called a corpus. You can use a LM to select the most probable next word given a context of a preceding series of words. 
:::

```{figure} ./images/lm-hist.png
---
width: 600px
name: lm-hist
---
[Evolution of language models over time](https://learning.oreilly.com/library/view/developing-apps-with/9781098152475/ch01.html#understanding_the_transformer_architecture_and_its)
```

:::{admonition} **[Large](https://en.wikipedia.org/wiki/Large_language_model#List)**
:class: tip
Large means both model size (number of parameter) and the amount of data the model is trained on 
:::

```{figure} ./images/wikipedia-list.png
---
width: 600px
name: wikipedia-list
---
[LLM List](https://en.wikipedia.org/wiki/Large_language_model#List)
```

:::{admonition} **Transformer**
:class: tip
Transformers were the key innovation that allowed language models to get large. They are a deep learning architecture that allow massive parallelization of training and inference on GPUs
:::

```{figure} ./images/ai-2-transformer.png
---
width: 600px
name: trans-subset
---
```

```{figure} ./images/attention-is-all-you-need.png
---
width: 600px
name: attention
---
[Attention Paper](https://arxiv.org/abs/1706.03762)
[Annotated Version](https://nlp.seas.harvard.edu/2018/04/03/attention.html)
```

```{figure} ./images/animated-transfomer.mp4
---
width: 600px
name: attention
---
[Animated Transfomer](https://prvnsmpth.github.io/animated-transformer/)
```

:::{admonition} **Pre-trained**
:class: tip
Pre-trained language models have been trained via self-supervision on vast quantities of text. These are also called [`foundation`](https://en.wikipedia.org/wiki/Foundation_models) models. They are not typically useful until...
:::

:::{admonition} **Generative**
:class: tip
Generative models are foundation models that have been further trained via supervised fine-tuning and reinforcement learning from human feedback (RLHF) to behave in a useful and safe manner, for example by responding to questions with answers like a chat assistant.
:::

:::{card} [OpenAI](https://en.wikipedia.org/wiki/OpenAI):

> OpenAI is an American artificial intelligence (AI) organization consisting of the non-profit OpenAI, Inc.[4] registered in Delaware and its for-profit subsidiary corporation OpenAI Global, LLC.[5] OpenAI researches artificial intelligence with the declared intention of developing "safe and beneficial" artificial general intelligence, which it defines as "highly autonomous systems that outperform humans at most economically valuable work".[6]

> OpenAI was founded in 2015 by Ilya Sutskever, Greg Brockman, Trevor Blackwell, Vicki Cheung, Andrej Karpathy, Durk Kingma, Jessica Livingston, John Schulman, Pamela Vagata, and Wojciech Zaremba, with Sam Altman and Elon Musk serving as the initial board members.Microsoft provided OpenAI Global LLC with a \$1 billion investment in 2019 and a \$10 billion investment in 2023.
:::

```{figure} ./images/model-zoo.png
---
width: 600px
name: model-zoo
---
[Model Zoo](https://arxiv.org/abs/2303.18223)
```

```{figure} ./images/openai-llm-history.png
---
width: 600px
name: openai-hist
---
[GPT Generations](https://learning.oreilly.com/library/view/developing-apps-with/9781098152475/ch01.html#understanding_the_transformer_architecture_and_its)
```

