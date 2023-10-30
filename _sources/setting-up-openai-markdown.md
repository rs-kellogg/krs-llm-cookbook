# Setting up OpenAI


## Setting up an Account

- ChatGPT
- OpenAI API
- Getting a token
- Selecting a Model
- Cost

## ChatGPT

Everyone knows this interface already, but did you know about some extensions?

## OpenAI Playground

The [OpenAI Playground](https://platform.openai.com/playground?mode=chat) is an excellent place to develop prompts that are tailored to your application. You can also pre-load one of the existing [example prompts](https://platform.openai.com/examples). Once you're satisfied with the results, you can export the example to code

<img src="_images/playground-save-to-code.png" alt="Save to Code" style="border: 2px solid  gray;">

## OpenAI API

The API is the place to go to scale up your jobs.

```python
import openai
# Call the openai ChatCompletion endpoint
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello World!"}],
)
# Extract the response
print(response["choices"][0]["message"]["content"])
```

## OpenAI Plugins

Plugins are for extending functionality.

## OpenAI Cookbook

Loads of example code here.