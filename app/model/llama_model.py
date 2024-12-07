from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft.peft_model import PeftModel
from huggingface_hub import login
import re
import torch


class LLaMAModel:
    def __init__(self, hf_token: str):
        login(hf_token, add_to_git_credential=True)
        BASE_MODEL = "meta-llama/Meta-Llama-3.1-8B"
        FINETUNED_MODEL = "nubufi/PriceProphet"

        self.tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.tokenizer.padding_side = "right"

        quant_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_quant_type="nf4",
        )
        base_model = AutoModelForCausalLM.from_pretrained(
            BASE_MODEL, device_map="auto", quantization_config=quant_config
        )

        self.model = PeftModel.from_pretrained(base_model, FINETUNED_MODEL)

    def predict(self, description):
        QUESTION = "How much does this cost to the nearest dollar?"
        PREFIX = "Price is $"
        prompt = f"{QUESTION}\n{description}\n{PREFIX}"

        inputs = self.tokenizer.encode(prompt, return_tensors="pt").to("cuda")
        attention_mask = torch.ones(inputs.shape, device="cuda")
        outputs = self.model.generate(
            inputs,
            attention_mask=attention_mask
            max_new_tokens=5,
            num_return_sequences=1,
        )
        result = self.tokenizer.decode(outputs[0])

        contents = result.split("Price is $")[1]
        contents = contents.replace(",", "")
        match = re.search(r"[-+]?\d*\.\d+|\d+", contents)

        return float(match.group()) if match else 0
