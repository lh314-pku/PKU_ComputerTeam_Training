from openai import OpenAI
from prompt import get_prompt
import json

class Chater:
    def __init__(self, sign: str):
        super().__init__()
        key = self.load_APIkey_from_json()
        self.sign = sign
        self.client = OpenAI(
            api_key=key,
            base_url="https://models.inference.ai.azure.com"
        )
        self.prompt_front = self.load_prompt(self.sign)
        self.prompt_last = None
        self.model_name = "gpt-4o"
        self.messages = []
        self.temperature_set = 0.7
        self.set_max_token = True
        self.max_token_num = 1000
        self.support_stream = True

    @staticmethod
    def load_APIkey_from_json():
        with open('config.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        # print(data)
        return data["api_key"]

    def load_prompt(self, sign: str):
        return get_prompt(sign)

    def chat_start(self, input_str: str):
        self.prompt_last = input_str
        prompt_text = self.prompt_front + self.prompt_last
        self.messages.append(
            {"role": "system", "content": prompt_text}
        )
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=self.messages,
            temperature=self.temperature_set,
            max_tokens=self.max_token_num,
            stream=self.support_stream
        )
        print(self.sign + ":")
        for chunk in response:
            if chunk.choices and (content := chunk.choices[0].delta.content):
                print(content, end="", flush=True)
        print("\n")


