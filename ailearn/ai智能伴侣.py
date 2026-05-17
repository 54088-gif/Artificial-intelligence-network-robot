import os
from openai import OpenAI
import streamlit as st
import base64
from PIL import Image
import io
import datetime
import json


def image_to_base64(image_path):
    try:
        with Image.open(image_path) as img:
            img.thumbnail((100, 100))
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            return base64.b64encode(buffer.getvalue()).decode()
    except Exception as e:
        print(f"图片读取失败: {e}")
        return ""

# 设置页面配置
st.set_page_config(
    page_title="ai智能伴侣",
    page_icon="🔞",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# 加载会话列表
def load_session_list():
    session_list = []
    if os.path.exists("sessions"):
        file_list = os.listdir("sessions")
        for filename in file_list:
            if filename.endswith(".json"):
                # 获取会话ID（去掉.json后缀），用于匹配文件名
                session_id = filename[:-5]
                # 读取会话数据获取昵称，用于显示
                try:
                    with open(f"sessions/{filename}", "r", encoding="utf-8") as f:
                        data = json.load(f)
                        display_name = f"{session_id}_{data.get('nickname', '未知')}"
                except:
                    display_name = session_id
                session_list.append((session_id, display_name))

    session_list.sort( reverse=True)
    return session_list

# 加载指定会话数据 ✅ 修复这里
def load_session_data(session_name):
    try:
        file_path = f"sessions/{session_name}.json"  # 必须加 .json
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.nickname = session_data["nickname"]
                st.session_state.personality = session_data["personality"]
                st.session_state.current_seat = session_data["current_seat"]
                st.session_state.user_avatar_path = session_data["user_avatar_path"]
                st.session_state.ai_avatar_path = session_data["ai_avatar_path"]
                st.session_state.message = session_data["message"]
            st.success(f"✅ 已加载会话：{session_name}")
    except Exception as e:
        st.error(f"加载会话数据失败: {e}")

# 保存会话数据
def save_session():
    if st.session_state.current_seat:
        session_data = {
            "nickname": st.session_state.nickname,
            "personality": st.session_state.personality,
            "message": st.session_state.message,
            "current_seat": st.session_state.current_seat,
            "user_avatar_path": st.session_state.user_avatar_path,
            "ai_avatar_path": st.session_state.ai_avatar_path,
        }
        if not os.path.exists("sessions"):
            os.mkdir("sessions")
        with open(f"sessions/{st.session_state.current_seat}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)

# 初始化会话状态
if "nickname" not in st.session_state:
    st.session_state.nickname = "伴侣"
if "personality" not in st.session_state:
    st.session_state.personality = "温柔体贴，善解人意"
if "current_seat" not in st.session_state:
    st.session_state.current_seat = datetime.datetime.now().strftime("%Y_%m_%d_%H%M%S")
if "user_avatar_path" not in st.session_state:
    st.session_state.user_avatar_path = "./resoures/李珣.png"
if "ai_avatar_path" not in st.session_state:
    st.session_state.ai_avatar_path = "./resoures/师姐.png"
if "message" not in st.session_state:
    st.session_state.message = []

st.logo("./resoures/18.png", size="large")

# 标题
if st.session_state.nickname:
    avatar_base64 = image_to_base64(st.session_state.ai_avatar_path)
    st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 15px;">
            <h1 style="margin: 0;">我的 {st.session_state.nickname}</h1>
            <img src="data:image/png;base64,{avatar_base64}" 
                 style="width: 50px; height: 50px; border-radius: 50%; object-fit: cover;">
        </div>
    """, unsafe_allow_html=True)

# 系统提示词
system_prompt = """
你叫{nickname}，人设性格：{personality}
请严格遵守人物设定，全程保持人设不崩，不暴露自己是AI，自然对话、语气贴合人设，正常和用户聊天互动。
"""
def delete_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            os.remove(f"sessions/{session_name}.json")
            st.success(f"已删除会话：{session_name}")
            st.rerun()
    except:
        st.error("删除失败")
# 侧边栏
with st.sidebar:
    st.subheader("ai智能伴侣设置")

    if st.button("新建会话", width="stretch"):
        if st.session_state.message:
            save_session()
        st.session_state.message = []
        st.session_state.current_seat = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        st.rerun()

    st.text("会话历史")
    sessions_list = load_session_list()
    for session_id, display_name in sessions_list:
        col1, col2 = st.columns([4,1])
        with col1:
            # 使用display_name显示，但session_id用于判断高亮
            is_active = (session_id == st.session_state.current_seat)
            if st.button(display_name, width="stretch", icon="📄", 
                        key=f"select_{session_id}",
                        type="primary" if is_active else "secondary"):
                load_session_data(session_id)  # 传入真实的session_id
                st.rerun()
        with col2:
            if st.button("", width="stretch", icon="❌", key=f"delete_{session_id}"):
                delete_session(session_id)  # 传入真实的session_id
                st.rerun()

    #分割线
    st.divider()
    st.subheader("伴侣信息")
    new_nickname = st.text_input("昵称：", placeholder="请输入伴侣的昵称", value=st.session_state.nickname)
    new_personality = st.text_area("性格设定：", placeholder="请输入伴侣的性格", value=st.session_state.personality)

    if st.button("💾 保存并更新伴侣信息"):
        st.session_state.nickname = new_nickname
        st.session_state.personality = new_personality
        save_session()
        st.success("✅ 伴侣信息已更新！")
        st.rerun()

    st.divider()
    st.subheader("头像设置")

    st.caption("伴侣头像")
    ai_new_path = st.text_input("头像路径", value=st.session_state.ai_avatar_path)
    if ai_new_path != st.session_state.ai_avatar_path:
        st.session_state.ai_avatar_path = ai_new_path
        save_session()
    try:
        st.image(st.session_state.ai_avatar_path, width=140)
    except:
        st.warning("头像路径错误，请检查文件")

    st.divider()
    st.caption("我的头像")
    user_new_path = st.text_input("头像路径", value=st.session_state.user_avatar_path)
    if user_new_path != st.session_state.user_avatar_path:
        st.session_state.user_avatar_path = user_new_path
        save_session()
    try:
        st.image(st.session_state.user_avatar_path, width=140)
    except:
        st.warning("头像路径错误，请检查文件")
st.text(f"当前会话：{st.session_state.current_seat}")
# 渲染对话
for msg in st.session_state.message:
    if msg["role"] == "user":
        st.chat_message("user", avatar=st.session_state.user_avatar_path).write(msg["content"])
    else:
        st.chat_message("assistant", avatar=st.session_state.ai_avatar_path).write(msg["content"])

# AI 客户端
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com"
)

# 聊天输入
prompt = st.chat_input("请输入你的问题：")
if prompt:
    st.chat_message("user", avatar=st.session_state.user_avatar_path).write(prompt)
    st.session_state.message.append({"role": "user", "content": prompt})

    sys_content = system_prompt.format(
        nickname=st.session_state.nickname,
        personality=st.session_state.personality
    )

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "system", "content": sys_content}, *st.session_state.message],
        stream=True,
    )

    full_response = ""
    with st.chat_message("assistant", avatar=st.session_state.ai_avatar_path):
        resp_place = st.empty()
        for chunk in response:
            if chunk.choices[0].delta.content:
                full_response += chunk.choices[0].delta.content
                resp_place.markdown(full_response + "▌")
        resp_place.markdown(full_response)

    st.session_state.message.append({"role": "assistant", "content": full_response})
    save_session()  # 对话后自动保存