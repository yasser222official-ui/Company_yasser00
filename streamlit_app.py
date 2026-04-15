# دمج خط Rubik وتنسيق Apple عبر CSS
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Rubik:ital,wght@0,300..900;1,300..900&display=swap" rel="stylesheet">
    <style>
    html, body, [class*="css"], .stMarkdown {
        font-family: 'Rubik', sans-serif;
        direction: rtl;
        text-align: right;
    }
    .stButton>button {
        border-radius: 15px;
        height: 3em;
        width: 100%;
        font-weight: bold;
        border: None;
        background-color: #34C759; /* لون أخضر Apple */
        color: white;
    }
    .metric-card-green {
        background-color: #34C759;
        color: white;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(52, 199, 89, 0.2);
    }
    .metric-card-red {
        background-color: #FF3B30;
        color: white;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(255, 59, 48, 0.2);
    }
    </style>
    """, unsafe_allow_html=True) # تم تصحيح الكلمة هنا
