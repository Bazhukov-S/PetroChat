from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = f'meta-llama/Llama-2-7b-chat-hf'
access_token = "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"
tokenizer = AutoTokenizer.from_pretrained(model_name, token=access_token, cache_dir='E:\\Work\\Petro_Chat\\PetroChat\\Models')
model = AutoModelForCausalLM.from_pretrained(model_name, token=access_token, cache_dir='E:\\Work\\Petro_Chat\\PetroChat\\Models')