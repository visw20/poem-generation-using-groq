from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

def batch():
    chat = ChatGroq(
        temperature=0,
        model_name="mixtral-8x7b-32768",
        groq_api_key="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"  # Direct API key input
    )

    system = "You are a helpful assistant."
    human = "{text}"
    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

    chain = prompt | chat
    print(chain.invoke({"text": "i need a content about pizza"}))

# Streaming
def streaming():
    chat = ChatGroq(
        temperature=0,
        model_name="gemma2-9b-it",
        groq_api_key="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"  # Direct API key input
    )
    
    prompt = ChatPromptTemplate.from_messages([("human", "Write a very long poem about {topic}")])
    chain = prompt | chat
    for chunk in chain.stream({"topic": "moon"}):
        print(chunk.content, end="", flush=True)

# batch()
streaming()







# import tkinter as tk
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_groq import ChatGroq

# def batch():
#     # Initialize the chat with Groq API
#     chat = ChatGroq(
#         temperature=0,
#         model_name="mixtral-8x7b-32768",
#         groq_api_key="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"  # Direct API key input
#     )

#     system = "You are a helpful assistant."
#     human = "{text}"
#     prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

#     chain = prompt | chat
#     content = chain.invoke({"text": user_input.get()})  # Get the input from the Tkinter entry field
#     output_text.delete(1.0, tk.END)  # Clear previous output
#     output_text.insert(tk.END, content)  # Display the result in the text widget

# def streaming():
#     # Initialize the chat with Groq API for streaming
#     chat = ChatGroq(
#         temperature=0,
#         model_name="gemma2-9b-it",
#         groq_api_key="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"  # Direct API key input
#     )
    
#     prompt = ChatPromptTemplate.from_messages([("human", "Write a very long poem about {topic}")])
#     chain = prompt | chat
#     output_text.delete(1.0, tk.END)  # Clear previous output
    
#     # Streaming output of the poem
#     for chunk in chain.stream({"topic": user_input.get()}):  # Get the input from the Tkinter entry field
#         output_text.insert(tk.END, chunk.content)  # Display the poem content in real-time
#         output_text.yview(tk.END)  # Scroll to the bottom to show the latest content
#         root.update()  # Update the Tkinter window during streaming

# # Initialize the Tkinter window
# root = tk.Tk()
# root.title("Groq API Chat")

# # Input field for the user to type their request
# user_input_label = tk.Label(root, text="Enter Topic or Text:")
# user_input_label.pack()

# user_input = tk.Entry(root, width=50)
# user_input.pack()

# # Button to trigger batch content generation
# batch_button = tk.Button(root, text="Generate Content (Batch)", command=batch)
# batch_button.pack(pady=10)

# # Button to trigger streaming content (poem)
# streaming_button = tk.Button(root, text="Generate Poem (Streaming)", command=streaming)
# streaming_button.pack(pady=10)

# # Output text area to display results
# output_text_label = tk.Label(root, text="Generated Content:")
# output_text_label.pack()

# output_text = tk.Text(root, height=10, width=50)
# output_text.pack()

# # Run the Tkinter application
# root.mainloop()






# from langchain_core.prompts import ChatPromptTemplate
# from langchain_groq import ChatGroq

# def batch(language):
#     chat = ChatGroq(
#         temperature=0,
#         model_name="mixtral-8x7b-32768",
#         groq_api_key="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"  # Direct API key input
#     )

#     system = f"You are a helpful assistant. Please respond in {language}."
#     human = "{text}"
#     prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

#     chain = prompt | chat
#     print(chain.invoke({"text": "what is neurons"}))

# # Streaming
# def streaming(language):
#     chat = ChatGroq(
#         temperature=0,
#         model_name="gemma2-9b-it",
#         groq_api_key="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"  # Direct API key input
#     )
    
#     prompt = ChatPromptTemplate.from_messages([("human", f"Write a very long poem about {{topic}} in {language}")])
#     chain = prompt | chat
#     for chunk in chain.stream({"topic": "Jackie chan"}):
#         print(chunk.content, end="", flush=True)

# # Ask the user for their language choice
# language_choice = input("Enter the language for the content (e.g., English, Tamil, Spanish, etc.): ")

# # Call batch and streaming functions with the chosen language
# batch(language_choice)
# streaming(language_choice)






