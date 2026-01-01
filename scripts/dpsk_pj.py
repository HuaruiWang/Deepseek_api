import os
from openai import OpenAI

#
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
    base_url="https://api.deepseek.com"
)

# read .txt 
def read_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        # if utf-8 error:
        try:
            with open(file_path, 'r', encoding='gbk') as file:
                return file.read()
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='gb2312') as file:
                return file.read()

# 
file_path = r"xxxxxxxxxxxx"  # replace
file_text = read_txt(file_path)

# 
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful legal assistant."},
        {"role": "user", "content": f"xxxxxxxx:\n{file_text}\n\nxxxxxxxxxxxxxxxx：xxxxxxxxxxxxxxxx"},
    ],
    stream=False
)

# 
print(response.choices[0].message.content)
