from openai import OpenAI

prompt_text = "Your Question or Your Description"
# 设置 Prompt
# 这里我们采用提前预设的方法，后续也可以提供连续的上下文交互接口。
# 以及图形界面、预设提示词等操作。
# 初次尝试，只需要在这里提出你的问题描述即可。

client = OpenAI(
    api_key="",
    base_url="https://models.inference.ai.azure.com"
)
# 初始化请求体 Client
# api_key 是你的专属 API 密钥，一般只能用于个人使用，替换为自己申请的 API Key
# 我比较常用 GitHub 提供的免费 API Key
# 你也可以使用其他来源的 API Key，记得修改 base_url
# base_url 是 API 的基础 URL，用于指定 GPT 模型的 API 服务地址
# 客户端需要通过 api_base_url 找到 GPT 模型的服务端口，从而进行请求和响应
# 上述默认设置的 url 为 GitHub Modules 官方文档示例使用的 url

model_name = "gpt-4o"
# 模型类型。具体调用的模型，需要修改 API Key、URL 和 模型名称
# 相关信息请善于搜索。

temperature_setting = 0.7
# 模型温度，影响模型的回复风格
# 数字越大越任意生成具有创造性的、更自由的内容
# 而越小则会生成更加严谨的内容。0.7的情况下更加自然
# 实测，在短文本下差异不大（

Max_tokens = 300
# 最大字数输出限制
# 如果不想有输出限制，在 response 里面注释掉 max_tokens = Max_tokens 一行即可

support_stream = True
# 是否支持流式输出。
# 流式输出的效果就是即时反馈，在模型生成长文本内容时，可以提前查看并判断部分结果。
# 同时可以让用户实时看到生成过程。

# 创建响应
response = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "system", "content": prompt_text}
    ],
    temperature=temperature_setting,
    max_tokens=Max_tokens,
    stream=support_stream
)

print("Result:")
if support_stream:
    for chunk in response:
        if chunk.choices and (content := chunk.choices[0].delta.content):
            print(content, end="", flush=True)
else:
    print(response.choices[0].message.content)