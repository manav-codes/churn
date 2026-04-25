import joblib
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Customer Churn Intelligence",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_resource
def load_model():
    return joblib.load("model.pkl")


model = load_model()


st.markdown(
    """
    <style>
        :root {
            --bg: #07111f;
            --panel: rgba(10, 18, 33, 0.82);
            --panel-strong: rgba(13, 23, 42, 0.96);
            --border: rgba(148, 163, 184, 0.18);
            --text: #e5eefb;
            --muted: #96a6c6;
            --accent: #6ee7ff;
            --accent-2: #7c3aed;
            --good: #34d399;
            --warn: #f59e0b;
            --bad: #fb7185;
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(110, 231, 255, 0.18), transparent 28%),
                radial-gradient(circle at top right, rgba(124, 58, 237, 0.2), transparent 26%),
                linear-gradient(180deg, #06101d 0%, #081422 38%, #0b1626 100%);
            color: var(--text);
        }

        .block-container {
            padding-top: 1.25rem;
            padding-bottom: 2rem;
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, rgba(9, 16, 30, 0.98), rgba(10, 19, 35, 0.94));
            border-right: 1px solid rgba(148, 163, 184, 0.12);
        }

        .hero {
            background: linear-gradient(135deg, rgba(14, 24, 42, 0.86), rgba(12, 20, 34, 0.72));
            border: 1px solid var(--border);
            border-radius: 28px;
            padding: 1.6rem 1.8rem;
            box-shadow: 0 24px 80px rgba(0, 0, 0, 0.32);
            position: relative;
            overflow: hidden;
            margin-bottom: 1.2rem;
        }

        .hero:before {
            content: "";
            position: absolute;
            inset: auto -20px -40px auto;
            width: 220px;
            height: 220px;
            background: radial-gradient(circle, rgba(110, 231, 255, 0.24), transparent 68%);
            pointer-events: none;
        }

        .eyebrow {
            text-transform: uppercase;
            letter-spacing: 0.22em;
            font-size: 0.72rem;
            color: var(--accent);
            font-weight: 700;
            margin-bottom: 0.55rem;
        }

        .hero h1 {
            margin: 0;
            font-size: clamp(2.1rem, 4vw, 3.7rem);
            line-height: 1.02;
            color: #f8fbff;
        }

        .hero p {
            margin: 0.9rem 0 0;
            color: var(--muted);
            font-size: 1.02rem;
            max-width: 72ch;
        }

        .pill-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.6rem;
            margin-top: 1rem;
        }

        .pill {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            padding: 0.45rem 0.75rem;
            border-radius: 999px;
            background: rgba(148, 163, 184, 0.1);
            border: 1px solid rgba(148, 163, 184, 0.12);
            color: #d9e6fb;
            font-size: 0.84rem;
            font-weight: 600;
        }

        .panel {
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 1.15rem 1.15rem 1.05rem;
            box-shadow: 0 18px 40px rgba(0, 0, 0, 0.18);
        }

        .panel-title {
            font-size: 0.78rem;
            letter-spacing: 0.16em;
            text-transform: uppercase;
            color: var(--muted);
            margin-bottom: 0.35rem;
        }

        .panel-value {
            font-size: 1.8rem;
            font-weight: 800;
            color: #f7fbff;
            line-height: 1;
        }

        .panel-caption {
            color: var(--muted);
            font-size: 0.9rem;
            margin-top: 0.35rem;
        }

        .glass-card {
            background: var(--panel-strong);
            border: 1px solid var(--border);
            border-radius: 26px;
            padding: 1.2rem;
            box-shadow: 0 22px 60px rgba(0, 0, 0, 0.22);
        }

        .risk-shell {
            position: relative;
            padding: 1.3rem;
            border-radius: 30px;
            background:
                radial-gradient(circle at top right, rgba(110, 231, 255, 0.16), transparent 32%),
                radial-gradient(circle at bottom left, rgba(124, 58, 237, 0.16), transparent 30%),
                linear-gradient(180deg, rgba(8, 15, 29, 0.98), rgba(14, 23, 39, 0.94));
            border: 1px solid rgba(110, 231, 255, 0.22);
            box-shadow:
                0 0 0 1px rgba(110, 231, 255, 0.05),
                0 24px 70px rgba(0, 0, 0, 0.28),
                inset 0 1px 0 rgba(255, 255, 255, 0.04);
            overflow: hidden;
        }

        .risk-shell:before {
            content: "";
            position: absolute;
            inset: -60px auto auto -60px;
            width: 160px;
            height: 160px;
            background: radial-gradient(circle, rgba(110, 231, 255, 0.22), transparent 68%);
            pointer-events: none;
        }

        .risk-shell:after {
            content: "";
            position: absolute;
            inset: auto -20px -20px auto;
            width: 220px;
            height: 220px;
            background: radial-gradient(circle, rgba(124, 58, 237, 0.16), transparent 66%);
            pointer-events: none;
        }

        .risk-kicker {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.45rem 0.75rem;
            border-radius: 999px;
            border: 1px solid rgba(110, 231, 255, 0.2);
            background: rgba(110, 231, 255, 0.08);
            color: #d7f7ff;
            font-size: 0.72rem;
            letter-spacing: 0.18em;
            text-transform: uppercase;
            font-weight: 800;
        }

        .risk-heading {
            margin-top: 0.8rem;
            font-size: 2rem;
            line-height: 1;
            font-weight: 900;
            color: #f8fbff;
            letter-spacing: -0.04em;
        }

        .risk-subheading {
            margin: 0.55rem 0 0;
            color: var(--muted);
            max-width: 50ch;
        }

        .risk-meta {
            display: flex;
            flex-wrap: wrap;
            gap: 0.55rem;
            margin-top: 1rem;
        }

        .risk-chip {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            padding: 0.45rem 0.72rem;
            border-radius: 999px;
            background: rgba(148, 163, 184, 0.08);
            border: 1px solid rgba(148, 163, 184, 0.12);
            color: #d8e7fb;
            font-size: 0.82rem;
            font-weight: 600;
        }

        .risk-score-stack {
            display: grid;
            grid-template-columns: 1.25fr 0.75fr;
            gap: 0.85rem;
            margin-top: 1rem;
            align-items: stretch;
        }

        .risk-score-panel {
            border-radius: 24px;
            padding: 1rem 1rem 0.95rem;
            background: linear-gradient(135deg, rgba(10, 18, 33, 0.95), rgba(17, 27, 46, 0.9));
            border: 1px solid rgba(110, 231, 255, 0.18);
            position: relative;
            z-index: 1;
        }

        .risk-score-label {
            font-size: 0.74rem;
            text-transform: uppercase;
            letter-spacing: 0.18em;
            color: var(--muted);
            margin-bottom: 0.45rem;
        }

        .risk-score-value {
            font-size: clamp(2.35rem, 5vw, 3.6rem);
            font-weight: 900;
            line-height: 0.95;
            color: #f8fbff;
        }

        .risk-score-note {
            margin-top: 0.45rem;
            color: var(--muted);
            font-size: 0.92rem;
        }

        .risk-side-panel {
            border-radius: 24px;
            padding: 1rem;
            background: rgba(148, 163, 184, 0.07);
            border: 1px solid rgba(148, 163, 184, 0.14);
        }

        .risk-side-panel .panel-title {
            margin-bottom: 0.4rem;
        }

        .risk-side-panel .panel-value {
            font-size: 2rem;
        }

        .risk-side-panel .panel-caption {
            margin-top: 0.25rem;
        }

        .result-banner {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            padding: 1rem 1.1rem;
            border-radius: 20px;
            border: 1px solid rgba(148, 163, 184, 0.14);
            background: linear-gradient(135deg, rgba(11, 20, 37, 0.95), rgba(20, 30, 52, 0.88));
            margin-top: 1rem;
        }

        .result-banner strong {
            font-size: 0.78rem;
            letter-spacing: 0.16em;
            text-transform: uppercase;
            color: var(--muted);
        }

        .result-copy h2 {
            margin: 0;
            font-size: 1.4rem;
            color: #f8fbff;
        }

        .result-copy p {
            margin: 0.35rem 0 0;
            color: var(--muted);
        }

        .progress-shell {
            margin-top: 0.85rem;
            height: 14px;
            border-radius: 999px;
            background: rgba(148, 163, 184, 0.12);
            overflow: hidden;
            border: 1px solid rgba(148, 163, 184, 0.1);
        }

        .progress-fill {
            height: 100%;
            border-radius: inherit;
            background: linear-gradient(90deg, var(--good), #5eead4, var(--accent));
        }

        .risk-high {
            background: linear-gradient(135deg, rgba(251, 113, 133, 0.18), rgba(248, 113, 113, 0.08));
            border-color: rgba(251, 113, 133, 0.32);
        }

        .risk-low {
            background: linear-gradient(135deg, rgba(52, 211, 153, 0.18), rgba(16, 185, 129, 0.08));
            border-color: rgba(52, 211, 153, 0.32);
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 0.75rem;
            margin-top: 0.9rem;
        }

        .mini-chip {
            padding: 0.78rem 0.9rem;
            border-radius: 18px;
            background: rgba(148, 163, 184, 0.08);
            border: 1px solid rgba(148, 163, 184, 0.12);
        }

        .mini-chip span {
            display: block;
            font-size: 0.72rem;
            text-transform: uppercase;
            letter-spacing: 0.14em;
            color: var(--muted);
            margin-bottom: 0.3rem;
        }

        .mini-chip strong {
            color: #f8fbff;
            font-size: 0.98rem;
        }

        div[data-testid="stMetric"] {
            background: rgba(10, 18, 33, 0.78);
            border: 1px solid rgba(148, 163, 184, 0.14);
            padding: 0.9rem 1rem;
            border-radius: 18px;
        }

        div[data-testid="stMetricLabel"] {
            color: var(--muted);
        }

        div[data-testid="stMetricValue"] {
            color: #f8fbff;
        }

        .stButton button {
            width: 100%;
            border-radius: 16px;
            padding: 0.85rem 1rem;
            border: none;
            background: linear-gradient(90deg, #4f46e5, #06b6d4);
            color: white;
            font-weight: 800;
            letter-spacing: 0.02em;
            box-shadow: 0 12px 28px rgba(6, 182, 212, 0.22);
        }

        .stButton button:hover {
            filter: brightness(1.08);
        }

        .stTextInput input, .stSelectbox div[data-baseweb="select"], .stNumberInput input {
            border-radius: 14px !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">Travel retention command center</div>
        <h1>Predict churn with a sharper, premium experience.</h1>
        <p>
            Explore a cleaner, more executive-grade interface for customer risk prediction.
            Enter a traveler profile, review the risk signal, and act before the customer slips away.
        </p>
        <div class="pill-row">
            <div class="pill">Live probability scoring</div>
            <div class="pill">Feature-aware guidance</div>
            <div class="pill">Retention-ready insights</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


top_left, top_mid, top_right = st.columns(3)
with top_left:
    st.metric("Model type", "Random Forest")
with top_mid:
    st.metric("Test accuracy", "87.4%")
with top_right:
    st.metric("AUC score", "0.947")


st.sidebar.markdown("## Traveler Profile")
st.sidebar.caption("Use this panel to enter the customer profile. The main view will score the risk instantly.")

with st.sidebar.form("churn_form"):
    st.markdown("### Customer details")
    age = st.slider("Age", 18, 80, 30)
    services_opted = st.slider("Services opted", 1, 7, 3)

    frequent_flyer = st.selectbox("Frequent flyer", ["No", "Yes"])
    annual_income = st.selectbox("Annual income class", ["Low Income", "Middle Income", "High Income"])
    account_synced = st.selectbox("Account synced to social media", ["No", "Yes"])
    booked_hotel = st.selectbox("Booked hotel", ["No", "Yes"])

    submit = st.form_submit_button("Score churn risk")


income_map = {"High Income": 0, "Low Income": 1, "Middle Income": 2}
input_data = pd.DataFrame(
    {
        "Age": [age],
        "FrequentFlyer": [0 if frequent_flyer == "No" else 1],
        "AnnualIncomeClass": [income_map[annual_income]],
        "ServicesOpted": [services_opted],
        "AccountSyncedToSocialMedia": [0 if account_synced == "No" else 1],
        "BookedHotelOrNot": [0 if booked_hotel == "No" else 1],
    }
)


main_left, main_right = st.columns([1.15, 0.85], gap="large")

with main_left:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### Prediction workspace")
    st.caption("The app will render a risk summary only after you score a profile.")

    feature_blocks = [
        ("Age", f"{age} years"),
        ("Services opted", f"{services_opted}"),
        ("Frequent flyer", frequent_flyer),
        ("Income band", annual_income),
        ("Social synced", account_synced),
        ("Hotel booked", booked_hotel),
    ]

    st.markdown(
        "<div class='feature-grid'>"
        + "".join(
            f"<div class='mini-chip'><span>{label}</span><strong>{value}</strong></div>"
            for label, value in feature_blocks
        )
        + "</div>",
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    st.dataframe(input_data, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)

with main_right:
    st.markdown('<div class="glass-card risk-shell">', unsafe_allow_html=True)
    st.markdown('<div class="risk-kicker">Risk intelligence</div>', unsafe_allow_html=True)
    st.markdown('<div class="risk-heading">This is the decision zone.</div>', unsafe_allow_html=True)
    st.markdown(
        '<p class="risk-subheading">The highest-value part of the screen is the churn signal itself: score it, read it, and act on it immediately.</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="risk-meta"><div class="risk-chip">Executive summary</div><div class="risk-chip">Immediate action</div><div class="risk-chip">Probability-led</div></div>',
        unsafe_allow_html=True,
    )

    if submit:
        probability = model.predict_proba(input_data)[0]
        prediction = int(model.predict(input_data)[0])
        churn_prob = float(probability[1])
        retention_prob = float(probability[0])

        risk_class = "risk-high" if prediction == 1 else "risk-low"
        headline = "Churn risk detected" if prediction == 1 else "Customer likely to stay"
        grade = "High risk" if prediction == 1 else "Low risk"
        subcopy = (
            "This profile shows a stronger chance of churn. Prioritize a retention offer or outreach."
            if prediction == 1
            else "This customer profile currently trends toward retention. Maintain the journey and monitor signals."
        )

        st.markdown(
            f"""
            <div class="result-banner {risk_class}">
                <div class="result-copy">
                    <strong>Risk outcome</strong>
                    <h2>{headline}</h2>
                    <p>{subcopy}</p>
                </div>
                <div style="text-align:right; min-width: 150px;">
                    <div class="panel-title">Primary signal</div>
                    <div class="panel-value">{churn_prob*100:.1f}%</div>
                    <div class="panel-caption">{grade} profile</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown('<div class="risk-score-stack">', unsafe_allow_html=True)
        st.markdown(
            f"""
            <div class="risk-score-panel">
                <div class="risk-score-label">Churn probability</div>
                <div class="risk-score-value">{churn_prob*100:.1f}%</div>
                <div class="risk-score-note">This is the dominant signal driving the outcome.</div>
                <div class="progress-shell" style="margin-top: 0.95rem;" aria-label="Churn probability">
                    <div class="progress-fill" style="width: {churn_prob*100:.1f}%;"></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            f"""
            <div class="risk-side-panel">
                <div class="panel-title">Retention probability</div>
                <div class="panel-value">{retention_prob*100:.1f}%</div>
                <div class="panel-caption">What remains if the risk is managed well.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('</div>', unsafe_allow_html=True)

        metric_left, metric_right = st.columns(2)
        with metric_left:
            st.metric("Churn probability", f"{churn_prob*100:.1f}%")
        with metric_right:
            st.metric("Retention probability", f"{retention_prob*100:.1f}%")

        st.markdown("#### Suggested action")
        if prediction == 1:
            st.info("Offer a targeted retention incentive, call the customer, and reduce friction in the next booking step.")
        else:
            st.success("Keep the customer engaged with personalized follow-up and loyalty reinforcement.")
    else:
        st.markdown(
            """
            <div class="result-banner">
                <div class="result-copy">
                    <strong>Spotlight panel</strong>
                    <h2>Waiting for a profile</h2>
                    <p>Score a customer from the sidebar to unlock the churn analysis panel.</p>
                </div>
                <div style="text-align:right; min-width: 140px;">
                    <div class="panel-title">Status</div>
                    <div class="panel-value">Ready</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<div class='panel' style='margin-top: 1rem;'>", unsafe_allow_html=True)
        st.markdown("**What this view does better**")
        st.write(
            "It turns a standard prediction form into a focused decision surface with branded visuals, clearer hierarchy, and result-driven feedback."
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
