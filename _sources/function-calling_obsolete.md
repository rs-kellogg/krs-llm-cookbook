# Function calling
We strongly recommend checking the official page for [Function-calling](https://platform.openai.com/docs/guides/function-calling) for the most up-to-date information.

## Overview
Objective: more reliably get structured data back from the model
- Create assistants that answer questions by calling external APIs (e.g. like ChatGPT Plugins)
    - send_email(to: string, body: string)
    - get_current_weather(location: string, unit: 'celsius' | 'fahrenheit')
- Convert natural language into API calls
    - get_customers(min_revenue: int, created_before: string, limit: int) from internal API
- Extract structured data from text
    - extract_data(name: string, birthday: string)
    - sql_query(query: string)

## Basics
- YOU: describe the function
- YOU: call the model with user query + function parameter
- MODEL: choose to call one or more functions and generate a JSON object with function arguments
- YOU: call your function with the provided arguments 
- YOU: call the model again with the function response in query

## How does it work? 



https://cookbook.openai.com/examples/how_to_call_functions_with_chat_models
https://cookbook.openai.com/examples/function_calling_with_an_openapi_spec