# Chapter2
本节课内容比较简单，其实就是API调用。`main.py`是一个（非常非常简易的）API调用模型。这个调用方案甚至只能问一个问题。（如果想要实现问答，还需要记录聊天记录、上下文关联、返回处理等）

后续这个项目可以进一步优化，例如实现一个聊天的图形化界面？（可以考虑 Python 自带的一些图形库或 PyQt6）预设AI提示词来让他用特定风格回复？（调成什么了[恼]）让他自动打开网页、查找系统文件、或者提示你今天的天气？（工作好助手）

考虑到大家没什么Python基础，我就直接写好了代码框架，大家只需要改动相关参数，以及填写自己的 API Key 即可。有相关基础的同学也可以自行探索！

现在还是了解一些简单的事情吧！
## API Key申请
我一般调用的都是 GitHub Modules 提供的免费 tokens，可以调用gpt-4o、gpt-4o-mini等模型回复。申请前需要大家有一个 GitHub 的账号（并且可以稳定访问 GitHub）。

> GitHub 在以后的工作、学习也非常有用，青协例会之后应该也会讲 git 的使用，相信技术部:）

### Step1
打开 GitHub 主页，在左上角头像下的菜单栏中找到 Settings，进入设置界面。

或者直接访问[这里](https://github.com/settings/tokens)，并直接跳转 Step3。

### Step2
点击 "Settings" 左侧栏最下方 "Developer Settings"，进入后再次点击 "Personal access tokens" -> "Tokens(classic)"

### Step3
点击右上角 "Generate new token" 中的 classic 模式。填写内容如下：

- Note：tokens的用途，就当是起个名字。
- Expiration：有效期至--，按需选择即可。（还是建议不要选择无期限"No expiration"，以防安全问题）
- Select scopes：访问权限，选什么影响不大，（至少我觉得没什么影响）实在不行就全选（

最后就可以点击 "Generate token"了！

想要注意的是，生成的 API Key 会且仅会显示一次，记得截图或复制保存，否则只能重新申请。（反正每个人的可申请次数非常多）

最后，你就可以将申请到的 API Key 复制到`main.py`或其他第三方开源AI客户端中完成配置。

如果你想调用其他模型或厂商的 API，也请仔细阅读相关官方文档，并确定其支持 OpenAI 风格 API Key。（例如 DeepSeek 的 API 就是支持的）以及记得在`main.py`修改`model_name`和`base_url`。
## 具体参数的作用
这个详细可见`main.py`的注释。


有能力的同学也欢迎自行探索并修改文件参数。（玩坏了可以从这个仓库重新下一个，而且学会 git 后可以回退版本嘛）
