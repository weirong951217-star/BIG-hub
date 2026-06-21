import os
import gradio as gr

# 🌟 確保清理舊的 Port，避免與其他應用衝突
os.system("fuser -k 7860/tcp >/dev/null 2>&1")

# ==========================================
# 🎨 現代化毛玻璃 (Glassmorphism) 介面設計 - 最終精簡版
# ==========================================
css = """
    /* 清除預設底色，使用極簡科技灰底 */
    body, html, .gradio-container, .wrap, main {
        background-color: #f8fafc !important;
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
        font-family: 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif !important;
    }
    
    body.dark { background-color: #f8fafc !important; }
    footer { display: none !important; }

    /* 背景動態模糊光暈 */
    .hub-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        padding: 4rem 1.5rem;
        position: relative;
        overflow: hidden;
    }
    .blob {
        position: absolute;
        border-radius: 50%;
        filter: blur(90px);
        z-index: 0;
        opacity: 0.6;
        animation: float 12s infinite ease-in-out;
    }
    .blob-1 { top: -5%; left: -5%; width: 450px; height: 450px; background: #c7d2fe; }
    .blob-2 { bottom: -5%; right: -5%; width: 550px; height: 550px; background: #fbcfe8; animation-delay: -6s; }

    /* 主視覺內容層 */
    .content-layer {
        z-index: 10;
        width: 100%;
        max-width: 1100px;
        text-align: center;
    }

    /* 頂部系統狀態標籤 */
    .meta-tag {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(255, 255, 255, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(12px);
        padding: 8px 24px;
        border-radius: 30px;
        font-size: 14px;
        font-weight: 700;
        color: #475569;
        margin-bottom: 40px; /* 增加與標題的距離 */
        letter-spacing: 1px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }

    /* 漸層主標題 (已移除左側籃球) */
    .main-title {
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 900;
        color: #1e293b;
        letter-spacing: -1px;
        margin: 0 0 80px 0; /* 標題下方直接接卡片 */
        line-height: 1.2;
    }
    .main-title span {
        background: linear-gradient(135deg, #4f46e5 0%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* 專案卡片網格 */
    .card-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 32px;
    }

    /* 獨立專案卡片 */
    .module-card {
        background: rgba(255, 255, 255, 0.65);
        backdrop-filter: blur(24px);
        border: 1px solid rgba(255, 255, 255, 1);
        border-radius: 28px;
        padding: 40px 30px;
        text-decoration: none !important;
        color: inherit !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 10px 40px rgba(0,0,0,0.03);
        display: flex;
        flex-direction: column;
        align-items: center;
        position: relative;
        overflow: hidden;
    }
    .module-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.06);
    }

    /* 卡片內容細節 (體育卡片會呈現雙球圖案) */
    .card-icon {
        font-size: 3.5rem;
        margin-bottom: 20px;
        display: inline-block;
        transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    .module-card:hover .card-icon {
        transform: scale(1.15) rotate(5deg);
    }
    .card-title {
        font-size: 1.4rem;
        font-weight: 900;
        color: #0f172a;
        margin: 0 0 12px 0;
    }
    .card-desc {
        font-size: 0.95rem;
        color: #475569;
        font-weight: 500;
        line-height: 1.6;
        margin: 0;
    }

    /* 狀態燈號 */
    .status-badge {
        position: absolute;
        top: 24px; right: 24px;
        font-size: 12px;
        font-weight: 700;
        padding: 6px 14px;
        border-radius: 20px;
        display: flex;
        align-items: center;
        gap: 8px;
        background: rgba(236, 253, 245, 0.8);
        color: #059669;
        border: 1px solid rgba(16, 185, 129, 0.2);
    }
    .status-dot {
        width: 6px; height: 6px;
        background-color: #10b981;
        border-radius: 50%;
        animation: pulse 2s infinite;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0) scale(1); }
        50% { transform: translateY(-20px) scale(1.05); }
    }
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.4); }
        70% { box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }
        100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
    }
"""

html_content = """
<div class="hub-wrapper">
    <div class="blob blob-1"></div>
    <div class="blob blob-2"></div>
    
    <div class="content-layer">
        <div class="meta-tag">✨ 系統入口網 ‧ 伺服器已連線</div>
        
        <h1 class="main-title"><span>多功能智慧分析與推薦平台</span></h1>
        
        <div class="card-grid">
            <a href="https://sport-fnqo.onrender.com" target="_blank" class="module-card">
                <div class="status-badge"><div class="status-dot"></div>連線中</div>
                <span class="card-icon">🏀⚽</span>
                <h2 class="card-title">體育賽事分析</h2>
                <p class="card-desc">運用隨機森林模型與卜瓦松分配，精準預測 NBA 與歐洲足球五大聯賽賽況勝率。</p>
            </a>
            
            <a href="https://education-ly5g.onrender.com" target="_blank" class="module-card">
                <div class="status-badge"><div class="status-dot"></div>連線中</div>
                <span class="card-icon">📚</span>
                <h2 class="card-title">專題教授推薦</h2>
                <p class="card-desc">透過學術性向測驗與先修門檻評估，為您精準匹配最佳指導教授陣容。</p>
            </a>
            
            <a href="https://music-2-q940.onrender.com" target="_blank" class="module-card">
                <div class="status-badge"><div class="status-dot"></div>連線中</div>
                <span class="card-icon">🎧</span>
                <h2 class="card-title">情境音樂調音</h2>
                <p class="card-desc">結合環境變數與心理期望狀態，自上萬首曲庫中萃取出專屬您的靈魂歌單。</p>
            </a>
        </div>
    </div>
</div>
"""

with gr.Blocks(css=css, title="多功能智慧分析與推薦平台") as demo:
    gr.HTML(html_content)

# 自動抓取 PORT
port = int(os.environ.get("PORT", 7860))
demo.launch(server_name="0.0.0.0", server_port=port)
