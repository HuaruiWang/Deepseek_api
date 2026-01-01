import os
from openai import OpenAI

# 初始化客户端
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
    base_url="https://api.deepseek.com"
)

# 读取 .txt 文件内容
def read_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        # 如果utf-8解码失败，尝试其他编码
        try:
            with open(file_path, 'r', encoding='gbk') as file:
                return file.read()
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='gb2312') as file:
                return file.read()

# 文件路径 - 请替换为你的 .txt 文件路径
file_path = r"D:\lili\doc\北大法宝司法案例批量下载2026010119523977\金荣海;李发忠;李发忠故意伤害罪一审刑事判决...(FBM-CLI.C.569791810).txt"  # 替换为你的txt文件路径
file_text = read_txt(file_path)

# 向 DeepSeek 提问，包含文件内容
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful legal assistant."},
        {"role": "user", "content": f"这是一个法律文档的内容:\n{file_text}\n\n请根据文档回答我的问题：法院对被害人陈述是否采信"},
    ],
    stream=False
)

# 输出模型回答
print(response.choices[0].message.content)