import os
import gradio as gr

# 🌟 如果是在本地端運行，這行可以確保清理舊的 Port
os.system("fuser -k 7860/tcp >/dev/null 2>&1")

css = """
    /* 清除預設內邊距與設定淺白背景 */
    .gradio-container {
        padding: 0 !important;
        max-width: 100% !important;
        background-color: #fbfbfb !important;
    }

    /* 隱藏 Gradio 預設的底部 Footer */
    footer {
        display: none !important;
    }

    .aww-wrapper {
        font-family: 'Helvetica Neue', 'Inter', 'Noto Sans TC', sans-serif;
        min-height: 100vh;
        padding: 30px 4vw;
        color: #000000 !important;
    }

    /* 頂部導覽列：改為 flex-end 讓愛心按鈕靠右 */
    .aww-header {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        border-bottom: 1px solid #eaeaea;
        padding-bottom: 20px;
    }

    /* 右上角黑底白框愛心按鈕 */
    .heart-btn-container {
        background-color: #111;
        width: 48px;
        height: 48px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    .heart-btn-container:hover {
        transform: scale(1.08);
        box-shadow: 0 6px 15px rgba(0,0,0,0.15);
    }
    .heart-icon {
        stroke: #fff;
        fill: transparent;
        transition: fill 0.3s ease;
    }
    .heart-btn-container.active .heart-icon {
        fill: #fff;
    }

    /* 日期與評分小標題 */
    .aww-meta {
        text-align: center;
        font-size: 13px;
        margin-top: 60px;
        color: #888888 !important;
    }
    .aww-meta span {
        background: #eee;
        padding: 4px 10px;
        border-radius: 4px;
        margin: 0 5px;
        color: #333333 !important;
        font-weight: bold;
    }

    /* 巨大的主標題 */
    .aww-title {
        text-align: center;
        font-size: 9vw;
        font-weight: 900;
        letter-spacing: -3px;
        margin: 10px 0 20px 0;
        line-height: 1;
        color: #000000 !important;
    }

    /* YuanZe IEM 強制純黑 */
    .aww-credits {
        display: flex;
        justify-content: center;
        font-weight: 300;
        font-size: 20px;
        margin-bottom: 80px;
        color: #000000 !important;
        letter-spacing: 4px;
    }
    .aww-credits span {
        border: none;
        cursor: default;
        color: #000000 !important;
    }

    /* 按鈕容器 */
    .nav-container {
        display: flex;
        justify-content: center;
        width: 100%;
        margin-top: 20px;
    }

    /* 懸浮導覽列與按鈕 */
    .aww-nav-pill {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 80px;
        padding: 12px;
        display: inline-flex;
        gap: 10px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.06);
    }

    .aww-btn {
        text-decoration: none;
        color: #374151 !important;
        font-weight: 600;
        font-size: 20px;
        padding: 16px 40px;
        border-radius: 60px;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .aww-btn:hover {
        background: #111 !important;
        color: #fff !important;
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
"""

html_content = """
<div class="aww-wrapper">

    <header class="aww-header">
        <div class="heart-btn-container" onclick="this.classList.toggle('active')">
            <svg class="heart-icon" viewBox="0 0 24 24" width="22" height="22" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
            </svg>
        </div>
    </header>

    <div class="aww-meta">Forum of the Day <span>Jun 20, 2026</span> Score 9.8 of 10</div>
    <h1 class="aww-title">COMMUNITY®</h1>

    <div class="aww-credits">
        <span>YuanZe IEM</span>
    </div>

    <div class="nav-container">
        <div class="aww-nav-pill">
            <a href="https://sport-fnqo.onrender.com" target="_blank" class="aww-btn">⚽ 體育版</a>
            <a href="https://education-ly5g.onrender.com" target="_blank" class="aww-btn">📚 教育版</a>
            <a href="https://music-2-q940.onrender.com" target="_blank" class="aww-btn">🎧 音樂版</a>
        </div>
    </div>

</div>
"""

with gr.Blocks(css=css, title="YuanZe IEM Community") as demo:
    gr.HTML(html_content)

# 🌟 為了確保你把這份「首頁」推上 Render 時也能順利運作
# 已經將這裡改為自動抓取 PORT 並允許對外連線的寫法
port = int(os.environ.get("PORT", 7860))
demo.launch(server_name="0.0.0.0", server_port=port)