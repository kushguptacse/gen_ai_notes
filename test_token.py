import tiktoken

# convert text to tokens
encoding = tiktoken.encoding_for_model("gpt-4.1-mini")   
tokens = encoding.encode("hi my name is kush and i like lotus biscoff ice cream.")
print(tokens)

# decode the token id to text
for token_id in tokens:
    token_text = encoding.decode([token_id])
    print(f"{token_id}:{token_text}")
