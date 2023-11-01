# What are Language Models?

:::{card} **Language Model**
A Language Model (LM) is a just model that assigns probabilities to sequences of words. Probabilities are estimated (the models are trained) using collections of naturally ocurring text, called a corpus. You can use a LM to select the most probable next word given a context of a preceding series of words. 
:::



:::{admonition} LM Origin
```{figure} ./images/shannon-english-entropy.png
---
width: 600px
name: entropy
---
The idea of a language model was first proposed by Claude Shannon circa 1950
```
:::

:::{card} Generative Pre-Trained Transformers
The technology to create language models has evolved over the years, from simple **n-gram** models up until the current generation of **neural network** approaches. The current state of the art is called **Generative Pre-Trained Transfomers** (GPT)
:::

:::{admonition} LM Evolution
```{figure} ./images/lm-hist.png
---
width: 600px
name: lm-hist
---
Evolution of language models over time
```
:::

:::{admonition} Transformers
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
```
:::

:::{card} OpenAI
[History](https://en.wikipedia.org/wiki/OpenAI):

> OpenAI is an American artificial intelligence (AI) organization consisting of the non-profit OpenAI, Inc.[4] registered in Delaware and its for-profit subsidiary corporation OpenAI Global, LLC.[5] OpenAI researches artificial intelligence with the declared intention of developing "safe and beneficial" artificial general intelligence, which it defines as "highly autonomous systems that outperform humans at most economically valuable work".[6]

> OpenAI was founded in 2015 by Ilya Sutskever, Greg Brockman, Trevor Blackwell, Vicki Cheung, Andrej Karpathy, Durk Kingma, Jessica Livingston, John Schulman, Pamela Vagata, and Wojciech Zaremba, with Sam Altman and Elon Musk serving as the initial board members.Microsoft provided OpenAI Global LLC with a \$1 billion investment in 2019 and a \$10 billion investment in 2023.
:::

:::{admonition} Model Zoo
```{figure} ./images/model-zoo.png
---
width: 600px
name: model-zoo
---
[Source](https://arxiv.org/abs/2303.18223)
```

```{figure} ./images/openai-llm-history.png
---
width: 600px
name: openai-hist
---
[Source](https://learning.oreilly.com/library/view/developing-apps-with/9781098152475/ch01.html#understanding_the_transformer_architecture_and_its)
```
:::
