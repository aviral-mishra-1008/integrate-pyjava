from transformers import GPTNeoXForCausalLM, AutoTokenizer

class Pythia_model:
    def __init__(self):
        self.model_name = "EleutherAI/pythia-70m-deduped"
        self.model = GPTNeoXForCausalLM.from_pretrained(self.model_name, revision="step3000", cache_dir="./pythia-70m-deduped/step3000")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, revision="step3000", cache_dir="./pythia-70m-deduped/step3000")
    
    def generate(self,prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        tokens = self.model.generate(**inputs)
        generated_text = self.tokenizer.decode(tokens[0], skip_special_tokens=True)
        return generated_text
    
    def get_tokenizer(self):
        return self.tokenizer
    
    def get_model(self):
        return self.model
    
    def get_model_name(self):
        return self.model_name