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

## 📖 使用说明

1. **新建会话**：点击侧边栏"新建会话"按钮
2. **修改人设**：在侧边栏输入昵称和性格设定，点击保存
3. **更换头像**：输入头像文件路径，系统自动更新
4. **历史会话**：点击会话列表中的会话名称加载历史记录
5. **删除会话**：点击会话右侧的 ❌ 按钮删除

## 🔧 自定义设置

### 默认配置

- 默认昵称：伴侣
- 默认性格：温柔体贴，善解人意
- 默认头像路径：`./resoures/` 目录下的图片

### 会话文件格式

每个会话以 JSON 格式存储，包含以下字段：
```json
{
"nickname": "伴侣",
"personality": "温柔体贴，善解人意",
"message": [...],
"current_seat": "20240101120000",
"user_avatar_path": "./resoures/李珣.png",
"ai_avatar_path": "./resoures/师姐.png"
}
```

## 📝 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 📱 界面预览

应用包含以下主要区域：
- **顶部**: 伴侣名称和头像展示
- **主区域**: 聊天消息列表和输入框
- **侧边栏**: 会话管理、人设设置、头像配置

---


