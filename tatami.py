import streamlit as st
import datetime

st.set_page_config(page_title="畳屋さんの販促おたすけツール", layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@400;700&display=swap');

    .stApp {
        background-color: #F5F0E8;
    }

    h1, h2, h3 {
        font-family: 'Noto Serif JP', serif !important;
        color: #5B4C3A !important;
    }

    .stButton > button[kind="primary"] {
        background-color: #8B7355 !important;
        border: none !important;
    }

    .stButton > button[kind="primary"]:hover {
        background-color: #6B5740 !important;
    }

    div[data-testid="stForm"] {
        background-color: #EDE8DF;
        border: 1px solid #C9B99A;
        border-radius: 8px;
        padding: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style="text-align: center; margin-bottom: 8px;">
        <span style="font-size: 48px;">🎋</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <h1 style="text-align: center; font-family: 'Noto Serif JP', serif; color: #5B4C3A; margin-bottom: 0;">
        畳屋さんの販促おたすけツール
    </h1>
    <p style="text-align: center; font-family: 'Noto Serif JP', serif; color: #8B7355; font-size: 18px; margin-top: 4px;">
        チラシを選んで、印刷するだけ。
    </p>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<hr style="border: none; border-top: 1px solid #C9B99A; margin: 24px 0;">',
    unsafe_allow_html=True,
)

st.header("📢 最新のお知らせ")

st.markdown(
    """
    <div style="
        background: #FFF9F0;
        border-left: 5px solid #D4A960;
        padding: 16px;
        margin-bottom: 12px;
        border-radius: 4px;
    ">
        <div style="font-size: 12px; color: #8B7355;">2026年4月24日</div>
        <div style="font-size: 16px; font-weight: bold; color: #5B4C3A;">🆕 新商品「ペット向け畳 プレミアム」販売開始</div>
        <div style="font-size: 14px; color: #6B5740; margin-top: 4px;">従来品より耐久性が30%向上。消臭機能もさらにパワーアップしました。</div>
    </div>
    <div style="
        background: #F0F5EE;
        border-left: 5px solid #7B9B6F;
        padding: 16px;
        margin-bottom: 12px;
        border-radius: 4px;
    ">
        <div style="font-size: 12px; color: #8B7355;">2026年4月15日</div>
        <div style="font-size: 16px; font-weight: bold; color: #5B4C3A;">📣 夏のキャンペーンチラシを追加しました</div>
        <div style="font-size: 14px; color: #6B5740; margin-top: 4px;">張替えキャンペーン用の新デザインが選べるようになりました。</div>
    </div>
    <div style="
        background: #F5F0F5;
        border-left: 5px solid #9B7B8E;
        padding: 16px;
        margin-bottom: 12px;
        border-radius: 4px;
    ">
        <div style="font-size: 12px; color: #8B7355;">2026年4月1日</div>
        <div style="font-size: 16px; font-weight: bold; color: #5B4C3A;">🎉 畳屋さんの販促おたすけツールがオープンしました</div>
        <div style="font-size: 14px; color: #6B5740; margin-top: 4px;">チラシ作成・配布がこのプラットフォームから簡単に行えます。</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<hr style="border: none; border-top: 1px solid #C9B99A; margin: 24px 0;">',
    unsafe_allow_html=True,
)

st.header("① チラシデザインを選ぶ")

flyer_data = {
    "🐾 ペット向け畳": {
        "copy": "ペットの爪にも強い！傷つきにくい特殊畳。愛犬・愛猫と快適な暮らしを。",
        "color": "#7B9B6F",
        "icon": "🐾",
        "catch": "ペットと暮らすなら、この畳。",
        "features": "✅ 爪による傷に強い ✅ 撥水加工 ✅ 消臭機能付き",
    },
    "🛁 お風呂場用すべりにくい畳": {
        "copy": "浴室の転倒事故を防ぐ。水に強く、すべりにくい安心の畳。",
        "color": "#6B8E9B",
        "icon": "🛁",
        "catch": "お風呂場の「すべる」を解決。",
        "features": "✅ 防滑加工 ✅ 防カビ・防水 ✅ お手入れ簡単",
    },
    "👶 子育て応援やわらか畳": {
        "copy": "赤ちゃんがハイハイしても安心。クッション性抜群のやさしい畳。",
        "color": "#D4A960",
        "icon": "👶",
        "catch": "赤ちゃんにやさしい、やわらか畳。",
        "features": "✅ 衝撃吸収素材 ✅ 防ダニ加工 ✅ 低ホルムアルデヒド",
    },
    "🏢 オフィス向けモダン畳": {
        "copy": "会議室・休憩スペースに和の空間を。デザイン性と機能性を両立。",
        "color": "#8B7355",
        "icon": "🏢",
        "catch": "オフィスに、和の心地よさを。",
        "features": "✅ モダンデザイン ✅ 防音効果 ✅ サイズオーダー可",
    },
    "✨ 畳の張替えキャンペーン": {
        "copy": "今だけ特別価格！畳の張替えで部屋が生まれ変わります。",
        "color": "#9B5B6B",
        "icon": "✨",
        "catch": "今だけ。畳張替え特別価格。",
        "features": "✅ 期間限定価格 ✅ 最短即日施工 ✅ 見積無料",
    },
}

selected_flyer = st.radio("チラシデザインを選んでください", list(flyer_data.keys()))
flyer = flyer_data[selected_flyer]

st.markdown("### 📄 チラシプレビュー")

st.markdown(
    f"""
    <div style="
        border: 2px solid {flyer['color']};
        border-radius: 12px;
        padding: 40px;
        text-align: center;
        background: linear-gradient(135deg, #FFFEF7 0%, #F5F0E8 100%);
        max-width: 500px;
        margin: 0 auto;
        box-shadow: 2px 2px 8px rgba(91, 76, 58, 0.1);
    ">
        <div style="font-size: 64px; margin-bottom: 16px;">{flyer['icon']}</div>
        <div style="
            font-size: 26px;
            font-weight: bold;
            color: {flyer['color']};
            margin-bottom: 12px;
            font-family: 'Noto Serif JP', serif;
        ">{flyer['catch']}</div>
        <div style="
            font-size: 15px;
            color: #5B4C3A;
            margin-bottom: 20px;
            line-height: 1.8;
        ">{flyer['copy']}</div>
        <div style="
            font-size: 14px;
            color: #6B5740;
            margin-bottom: 24px;
            line-height: 2.0;
        ">{flyer['features']}</div>
        <div style="
            border-top: 2px dashed {flyer['color']};
            padding-top: 20px;
            margin-top: 8px;
        ">
            <div style="font-size: 13px; color: #8B7355;">お問い合わせ・ご相談はこちら</div>
            <div style="font-size: 18px; font-weight: bold; color: #5B4C3A; margin-top: 8px; font-family: 'Noto Serif JP', serif;">
                🏠 あなたの店舗名がここに入ります
            </div>
            <div style="font-size: 13px; color: #8B7355; margin-top: 4px;">
                📍 住所 ｜ 📞 電話番号
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<hr style="border: none; border-top: 1px solid #C9B99A; margin: 24px 0;">',
    unsafe_allow_html=True,
)

st.header("② あなたのお店の情報")

col1, col2 = st.columns(2)

with col1:
    shop_name = st.text_input("店舗名", placeholder="例：山田畳店")
    shop_phone = st.text_input("電話番号", placeholder="例：06-1234-5678")

with col2:
    shop_address = st.text_input("住所", placeholder="例：大阪市中央区〇〇町1-2-3")
    shop_owner = st.text_input("代表者名", placeholder="例：山田太郎")

if shop_name and shop_phone and shop_address:
    st.markdown("### 📄 店舗情報入りチラシプレビュー")

    st.markdown(
        f"""
        <div style="
            border: 2px solid {flyer['color']};
            border-radius: 12px;
            padding: 40px;
            text-align: center;
            background: linear-gradient(135deg, #FFFEF7 0%, #F5F0E8 100%);
            max-width: 500px;
            margin: 0 auto;
            box-shadow: 2px 2px 8px rgba(91, 76, 58, 0.1);
        ">
            <div style="font-size: 64px; margin-bottom: 16px;">{flyer['icon']}</div>
            <div style="
                font-size: 26px;
                font-weight: bold;
                color: {flyer['color']};
                margin-bottom: 12px;
                font-family: 'Noto Serif JP', serif;
            ">{flyer['catch']}</div>
            <div style="
                font-size: 15px;
                color: #5B4C3A;
                margin-bottom: 20px;
                line-height: 1.8;
            ">{flyer['copy']}</div>
            <div style="
                font-size: 14px;
                color: #6B5740;
                margin-bottom: 24px;
                line-height: 2.0;
            ">{flyer['features']}</div>
            <div style="
                border-top: 2px dashed {flyer['color']};
                padding-top: 20px;
                margin-top: 8px;
            ">
                <div style="font-size: 13px; color: #8B7355;">お問い合わせ・ご相談はこちら</div>
                <div style="font-size: 18px; font-weight: bold; color: #5B4C3A; margin-top: 8px; font-family: 'Noto Serif JP', serif;">
                    🏠 {shop_name}
                </div>
                <div style="font-size: 13px; color: #8B7355; margin-top: 4px;">
                    📍 {shop_address} ｜ 📞 {shop_phone}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    '<hr style="border: none; border-top: 1px solid #C9B99A; margin: 24px 0;">',
    unsafe_allow_html=True,
)

st.header("③ 配布方法を選ぶ")

delivery_method = st.radio(
    "どちらの方法で使いますか？",
    ["🖨️ 自分で印刷して手渡し（無料）", "📮 ポスティングで配布（有料）"],
)

posting_cost = 0
posting_area = ""
posting_count = 0

if "ポスティング" in delivery_method:
    st.subheader("ポスティング設定")

    posting_area = st.text_input("配布エリア", placeholder="例：大阪市中央区、北区")
    posting_count = st.number_input(
        "配布枚数", min_value=100, max_value=50000, value=1000, step=100
    )

    cost_per_flyer = 5
    posting_cost = posting_count * cost_per_flyer

    st.warning(
        f"💰 配布費用：**{posting_cost:,}円**（税別）　※{posting_count:,}枚 × @{cost_per_flyer}円"
    )

st.markdown(
    '<hr style="border: none; border-top: 1px solid #C9B99A; margin: 24px 0;">',
    unsafe_allow_html=True,
)

st.header("④ 確定")

if st.button("✅ この内容で確定する", type="primary", use_container_width=True):
    if not (shop_name and shop_phone and shop_address):
        st.error("②の店舗情報を入力してください。")
    else:
        st.balloons()
        if "手渡し" in delivery_method:
            st.success("🖨️ チラシPDFを生成しました！ダウンロードして印刷してください。")
            st.download_button(
                label="📄 チラシPDFをダウンロード",
                data=f"{flyer['catch']}\n{flyer['copy']}\n{flyer['features']}\n---\n{shop_name}\n{shop_address}\nTEL: {shop_phone}\n担当: {shop_owner}\n作成日: {datetime.date.today()}",
                file_name=f"チラシ_{shop_name}_{datetime.date.today()}.txt",
                mime="text/plain",
            )
        else:
            st.success(
                f"📮 ポスティング手配を受け付けました！\n\n{posting_area}エリアに{posting_count:,}枚配布します。\n\n配布費用：{posting_cost:,}円（税別）"
            )

st.markdown(
    '<hr style="border: none; border-top: 1px solid #C9B99A; margin: 24px 0;">',
    unsafe_allow_html=True,
)

st.header("💬 お問い合わせ・ご要望")

st.write("商品に関するご質問や、新しいチラシデザインのご要望など、お気軽にお問い合わせください。")

with st.form("contact_form"):
    contact_shop = st.text_input("店舗名", placeholder="例：山田畳店", key="contact_shop")
    contact_name = st.text_input("お名前", placeholder="例：山田太郎", key="contact_name")
    contact_category = st.selectbox(
        "お問い合わせ種類",
        ["商品について", "チラシデザインの要望", "配布について", "その他"],
    )
    contact_message = st.text_area(
        "お問い合わせ内容",
        placeholder="ご自由にご記入ください",
        height=150,
    )

    submitted = st.form_submit_button("📩 送信する", use_container_width=True)

    if submitted:
        if contact_shop and contact_name and contact_message:
            st.success("お問い合わせを受け付けました。担当者よりご連絡いたします。")
        else:
            st.error("店舗名・お名前・お問い合わせ内容をご入力ください。")

st.markdown(
    """
    <div style="text-align: center; margin-top: 40px; padding: 20px; color: #8B7355; font-size: 12px;">
        © 2026 畳屋さんの販促おたすけツール
    </div>
    """,
    unsafe_allow_html=True,
)
