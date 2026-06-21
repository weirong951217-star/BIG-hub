import os
import gradio as gr

# 🌟 確保清理舊的 Port，避免與其他應用衝突
os.system("fuser -k 7860/tcp >/dev/null 2>&1")

# ==========================================
# 🎨 全新現代化毛玻璃 (Glassmorphism) 介面設計
# ==========================================
css = """
    /* 清除預設底色，使用極簡科技灰底 */
    body, html, .gradio-container, .wrap, main {
        background-color: #f4f5f7 !important;
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
        font-family: 'PingFang TC', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif !important;
    }
    
    body.dark { background-color: #f4f5f7 !important; }
    footer { display: none !important; }

    /* 背景動態模糊光暈，增加科技感 */
    .hub-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        padding: 3rem 1.5rem;
        position: relative;
        overflow: hidden;
    }
    .blob {
        position: absolute;
        border-radius: 50%;
        filter: blur(80px);
        z-index: 0;
        opacity: 0.5;
        animation: float 10s infinite ease-in-out;
    }
    .blob-1 { top: -10%; left: -10%; width: 400px; height: 400px; background: #c7d2fe; }
    .blob-2 { bottom: -10%; right: -10%; width: 500px; height: 500px; background: #fbcfe8; animation-delay: -5s; }

    /* 主視覺內容層 */
    .content-layer {
        z-index: 10;
        width: 100%;
        max-width: 1100px;
        text-align: center;
    }

    /* 頂部系統狀態標籤 */
    .meta-tag {
        display: inline-block;
        background: rgba(255, 255, 255, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        padding: 8px 20px;
        border-radius: 30px;
        font-size: 13px;
        font-weight: 700;
        color: #4b5563;
        margin-bottom: 24px;
        letter-spacing: 1px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }

    /* 巨大的漸層主標題 */
    .main-title {
        font-size: clamp(3rem, 6vw, 4.5rem);
        font-weight: 900;
        color: #111827;
        letter-spacing: -2px;
        margin: 0 0 10px 0;
        line-height: 1.1;
    }
    .main-title span {
        background: linear-gradient(135deg, #4f46e5 0%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .sub-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #6b7280;
        margin-bottom: 60px;
        letter-spacing: 2px;
    }

    /* 專案卡片網格佈局 */
    .card-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 30px;
        margin-top: 20px;
    }

    /* 獨立專案卡片設計 */
    .module-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.9);
        border-radius: 24px;
        padding: 40px 30px;
        text-decoration: none !important;
        color: inherit !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 10px 30px rgba(0,0,0,0.04);
        display: flex;
        flex-direction: column;
        align-items: center;
        position: relative;
        overflow: hidden;
    }
    .module-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: linear-gradient(135deg, rgba(255,255,255,0.4) 0%, rgba(255,255,255,0) 100%);
        opacity: 0;
        transition: opacity 0.4s;
    }
    .module-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.08);
        border-color: rgba(255,255,255,1);
    }
    .module-card:hover::before { opacity: 1; }

    /* 卡片內容細節 */
    .card-icon {
        font-size: 3.5rem;
        margin-bottom: 20px;
        display: inline-block;
        transition: transform 0.3s;
    }
    .module-card:hover .card-icon {
        transform: scale(1.1) rotate(5deg);
    }
    .card-title {
        font-size: 1.5rem;
        font-weight: 900;
        color: #1f2937;
        margin: 0 0 12px 0;
    }
    .card-desc {
        font-size: 0.95rem;
        color: #6b7280;
        font-weight: 600;
        line-height: 1.6;
        margin: 0;
    }

    /* 連線中 - 動態狀態燈號 */
    .status-badge {
        position: absolute;
        top: 20px; right: 20px;
        font-size: 11px;
        font-weight: 800;
        padding: 5px 12px;
        border-radius: 20px;
        display: flex;
        align-items: center;
        gap: 6px;
        letter-spacing: 1px;
    }
    .status-badge.online {
        background: #ecfdf5;
        color: #059669;
    }
    .status-dot {
        width: 6px; height: 6px;
        background-color: #10b981;
        border-radius: 50%;
        box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.2);
        animation: pulse 2s infinite;
    }

    /* 動畫設定 */
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
        <div class="meta-tag">✨ 元智工管 AI 系統入口網 ‧ 伺服器已連線</div>
        
        <h1 class="main-title">YZU IEM <span>AI PORTAL</span></h1>
        <div class="sub-title">人工智慧應用與資料分析中心</div>
        
        <div class="card-grid">
            <a href="https://sport-fnqo.onrender.com" target="_blank" class="module-card">
                <div class="status-badge online"><div class="status-dot"></div>連線中</div>
                <span class="card-icon">⚽</span>
                <h2 class="card-title">體育賽事分析</h2>
                <p class="card-desc">運用隨機森林模型與泊松分配，精準預測 NBA 與歐洲足球五大聯賽賽況勝率。</p>
            </a>
            
            <a href="https://education-ly5g.onrender.com" target="_blank" class="module-card">
                <div class="status-badge online"><div class="status-dot"></div>連線中</div>
                <span class="card-icon">📚</span>
                <h2 class="card-title">專題教授推薦</h2>
                <p class="card-desc">透過學術性向測驗與先修門檻評估，為您精準匹配最佳指導教授陣容。</p>
            </a>
            
            <a href="https://music-2-q940.onrender.com" target="_blank" class="module-card">
                <div class="status-badge online"><div class="status-dot"></div>連線中</div>
                <span class="card-icon">🎧</span>
                <h2 class="card-title">情境音樂調音</h2>
                <p class="card-desc">結合環境變數與心理期望狀態，自上萬首曲庫中萃取出專屬您的靈魂歌單。</p>
            </a>
        </div>
    </div>
</div>
"""

with gr.Blocks(css=css, title="YZU IEM AI Portal") as demo:
    gr.HTML(html_content)

# 自動抓取 PORT 並允許對外連線
port = int(os.environ.get("PORT", 7860))
demo.launch(server_name="0.0.0.0", server_port=port)
