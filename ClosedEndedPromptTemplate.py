from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

# Local LLM
model = ChatOllama(
    model="llama3.1",
    temperature=0
)

# Prompt Template
closedEndedPromptTemplate = PromptTemplate(
    input_variables=["fact"],
    template="""
Analyze the given fact: {fact}.
Respond with ONLY one word:
Right or Wrong.
"""
)

# Format Prompt
final_prompt = closedEndedPromptTemplate.format(
    fact="Sun Rises In The East"
)

# Invoke Model
response = model.invoke(final_prompt)

print("Model Output:", response.content)

# Check Output
answer = response.content.strip().lower()

if answer == "right" or answer == "wrong":
    print("THE GIVEN PROMPT IS A CLOSED ENDED PROMPT")
else:
    print("THE PROMPT GIVEN IS NOT A CLOSED ENDED PROMPT")

