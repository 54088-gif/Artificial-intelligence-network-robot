# Artificial-intelligence-network-robot
AI智能伴侣 - 基于 Streamlit 的 AI 聊天伴侣应用，支持自定义人设、头像和多会话管理，使用 DeepSeek API 实现智能对话。
# AI智能伴侣 💕

一个基于 Streamlit 构建的 AI 聊天伴侣应用，支持自定义人设、头像和多会话管理。

## ✨ 功能特性

- **智能对话**：基于 DeepSeek 大语言模型，支持流式响应输出
- **人设定制**：自定义伴侣昵称和性格设定
- **头像设置**：支持自定义用户和AI伴侣头像
- **会话管理**：创建、保存、加载和删除多个会话
- **数据持久化**：自动保存聊天记录到本地 JSON 文件
- **界面美观**：简洁直观的侧边栏布局，支持头像显示

## 🛠️ 技术栈

- **框架**: Streamlit
- **AI服务**: DeepSeek API（兼容 OpenAI API）
- **图像处理**: Pillow (PIL)
- **数据存储**: JSON 文件
- **语言**: Python 3.x

## 🚀 快速开始

### 环境要求

- Python 3.8+
- 安装依赖：
```bash
pip install streamlit openai pillow
```

### 配置 API 密钥

在系统环境变量中设置 DeepSeek API Key：

**Windows**:
```bash
set DEEPSEEK_API_KEY=your_api_key_here
```

**Linux/Mac**:
```bash
export DEEPSEEK_API_KEY=your_api_key_here
```

### 运行应用

```bash
streamlit run ai智能伴侣.py
```

## 📁 项目结构
ai智能伴侣/ ├── ai智能伴侣.py # 主应用文件 ├── resoures/ # 资源目录 │ ├── 18.png # Logo图片 │ ├── 师姐.png # 默认AI头像 │ └── 李珣.png # 默认用户头像 └── sessions/ # 会话存储目录（自动创建） └── {session_id}.json # 会话数据文件
