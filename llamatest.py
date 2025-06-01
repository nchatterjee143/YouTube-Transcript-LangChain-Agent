from langchain_community.llms import Ollama

# Initialize the LLM
llm = Ollama(model="llama3")

# Run a simple prompt
response = llm.invoke("How do you define GDP?")
print(response)
