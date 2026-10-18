import streamlit as st

# =====================================================
# EDUAI | SCI-TECH YOUTH EDITION
# =====================================================
st.set_page_config(
    page_title="EDUAI | Learn Beyond",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------ SESSION STATE --------------------
defaults = {
    "history": [],
    "quiz_score": 0,
    "quiz_done": False,
    "last_answers": [],
    "last_questions": [],
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ------------------ VISUAL DESIGN --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap');

:root {
    --blue: #4F46E5;
    --blue-dark: #3730A3;
    --purple: #8B5CF6;
    --cyan: #06B6D4;
    --ink: #172554;
    --muted: #64748B;
    --line: #E5E7F0;
    --surface: #FFFFFF;
    --page: #F7F8FC;
}

html, body, [class*="css"] {
    font-family: 'Be Vietnam Pro', sans-serif;
}

.stApp {
    background:
        radial-gradient(ellipse at 88% 0%, rgba(167,139,250,.17), transparent 30%),
        radial-gradient(ellipse at 0% 18%, rgba(96,165,250,.13), transparent 28%),
        var(--page);
    color: var(--ink);
}

.block-container {
    max-width: 1280px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3, h4 {
    color: var(--ink);
    letter-spacing: -0.045em;
    font-weight: 800;
}

h1 { line-height: 1.18; }
p, label, .stMarkdown { line-height: 1.72; }

/* Sidebar: soft glass + clear navigation */
[data-testid="stSidebar"] {
    background: linear-gradient(165deg, #EEF2FF 0%, #F7F5FF 52%, #FFFFFF 100%);
    border-right: 1px solid #E0E7FF;
}
[data-testid="stSidebar"] > div { padding-top: 1.35rem; }
[data-testid="stSidebar"] h1 {
    color: #4F46E5;
    letter-spacing: -1.2px;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label {
    border-radius: 12px;
    padding: .35rem .55rem;
    transition: background .18s ease, color .18s ease;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background: rgba(99,102,241,.09);
}

/* Hero banner */
.hero {
    position: relative;
    overflow: hidden;
    padding: clamp(25px, 4vw, 42px);
    border-radius: 28px;
    color: #FFFFFF;
    background: linear-gradient(120deg, #1E40AF 0%, #4F46E5 52%, #9333EA 100%);
    box-shadow: 0 20px 55px rgba(79,70,229,.20);
    margin-bottom: 30px;
    isolation: isolate;
}
.hero:before {
    content: "";
    position: absolute;
    width: 300px;
    height: 300px;
    right: -90px;
    top: -150px;
    border-radius: 50%;
    border: 1px solid rgba(255,255,255,.20);
    box-shadow: 0 0 0 28px rgba(255,255,255,.035), 0 0 0 58px rgba(255,255,255,.025);
    z-index: -1;
}
.hero:after {
    content: "✳";
    position: absolute;
    right: 34px;
    bottom: -65px;
    font-size: 190px;
    color: rgba(255,255,255,.09);
    pointer-events: none;
    z-index: -1;
}
.hero h1 {
    color: #FFFFFF;
    font-size: clamp(2rem, 4.3vw, 3.15rem);
    margin: 14px 0;
    max-width: 820px;
}
.hero p {
    color: #E0E7FF;
    max-width: 700px;
    font-size: 1rem;
}
.eyebrow {
    display: inline-flex;
    align-items: center;
    padding: 7px 12px;
    border-radius: 99px;
    border: 1px solid rgba(255,255,255,.28);
    background: rgba(255,255,255,.12);
    color: #F5F3FF;
    font-size: .72rem;
    font-weight: 800;
    letter-spacing: 1.3px;
    backdrop-filter: blur(8px);
}

/* Feature cards */
.feature {
    background: rgba(255,255,255,.88);
    border: 1px solid rgba(226,232,240,.95);
    border-radius: 22px;
    padding: 23px;
    min-height: 190px;
    box-shadow: 0 8px 28px rgba(30,41,59,.045);
    transition: transform .22s ease, box-shadow .22s ease, border-color .22s ease;
}
.feature:hover {
    transform: translateY(-4px);
    border-color: #C7D2FE;
    box-shadow: 0 16px 34px rgba(79,70,229,.11);
}
.feature-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 48px;
    height: 48px;
    border-radius: 16px;
    background: linear-gradient(135deg, #EEF2FF, #F3E8FF);
    color: #4F46E5;
    font-size: 25px;
    margin-bottom: 14px;
}
.feature h3 { font-size: 1.08rem; margin: 0 0 8px 0; }
.feature p { color: var(--muted); font-size: .9rem; margin: 0; }
.section-kicker {
    color: #6366F1;
    font-size: .72rem;
    font-weight: 800;
    letter-spacing: 1.6px;
    text-transform: uppercase;
}

/* Metrics */
[data-testid="stMetric"] {
    background: rgba(255,255,255,.88);
    border: 1px solid var(--line);
    border-radius: 20px;
    padding: 19px 21px;
    box-shadow: 0 7px 24px rgba(30,41,59,.04);
}
[data-testid="stMetricLabel"] { color: var(--muted); font-weight: 600; }
[data-testid="stMetricValue"] { color: #4338CA; font-weight: 800; }

/* Buttons */
.stButton > button, .stFormSubmitButton > button {
    border-radius: 13px;
    min-height: 45px;
    font-weight: 700;
    border: 1px solid #D8DEFF;
    transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease;
}
.stButton > button[kind="primary"],
.stFormSubmitButton > button[kind="primary"] {
    color: white;
    border: none;
    background: linear-gradient(105deg, #4F46E5, #7C3AED);
    box-shadow: 0 7px 18px rgba(79,70,229,.16);
}
.stButton > button:hover, .stFormSubmitButton > button:hover {
    border-color: #A5B4FC;
    box-shadow: 0 8px 22px rgba(79,70,229,.10);
    transform: translateY(-1px);
}

/* Inputs */
[data-testid="stTextArea"] textarea,
[data-testid="stTextInput"] input,
[data-testid="stChatInput"] textarea {
    border-radius: 13px;
    background: #FFFFFF;
}
[data-testid="stSelectbox"] > div,
[data-baseweb="select"] > div {
    border-radius: 13px;
}
[data-testid="stExpander"] {
    background: rgba(255,255,255,.78);
    border: 1px solid var(--line);
    border-radius: 16px;
}
[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 20px;
    border-color: var(--line);
    background: rgba(255,255,255,.72);
    box-shadow: 0 7px 24px rgba(30,41,59,.035);
}
[data-testid="stChatMessage"] {
    border-radius: 16px;
}
[data-testid="stAlert"] { border-radius: 15px; }
hr { border-color: #E2E8F0; }

/* Footer */
.footer {
    text-align: center;
    color: #94A3B8;
    font-size: .78rem;
    letter-spacing: .2px;
    padding-top: 14px;
}

@media (prefers-reduced-motion: no-preference) {
    [data-testid="stVerticalBlockBorderWrapper"] {
        transition: box-shadow .2s ease, border-color .2s ease;
    }
    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: #D5DDF5;
        box-shadow: 0 12px 30px rgba(30,41,59,.055);
    }
}

@media (max-width: 768px) {
    .block-container { padding-top: 1rem; padding-bottom: 2rem; }
    .hero { padding: 23px; border-radius: 21px; }
    .hero:after { right: 8px; font-size: 105px; }
    .feature { padding: 18px; min-height: auto; }
    [data-testid="stMetric"] { padding: 13px; }
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: .01ms !important;
        transition-duration: .01ms !important;
    }
}
</style>
""", unsafe_allow_html=True)

# ------------------ NAVIGATION -----------------------
PAGES = [
    "⌂  Tổng quan",
    "✳  Gia sư học tập",
    "▤  Kiểm tra kiến thức",
    "◷  Tiến độ học tập",
    "⚗  Trợ lý giáo viên",
]

with st.sidebar:
    st.markdown("# 🧬 EDUAI")
    st.caption("LEARN BEYOND LIMITS")
    st.divider()


page = st.radio(
    "Điều hướng",
    PAGES,
    key="eduai_navigation",
    label_visibility="collapsed",
)

# =====================================================
# PAGE 1: DASHBOARD
# =====================================================
if page == PAGES[0]:
    st.markdown("""
    <div class="hero">
        <div class="eyebrow">✦ YOUR PERSONAL LEARNING SPACE</div>
        <h1>Học thông minh.<br>Khám phá không giới hạn.</h1>
        <p>
            Chào mừng đến với EDUAI — không gian kết hợp
            khoa học, công nghệ và phương pháp học tập chủ động.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-kicker">YOUR WORKSPACE</div>',
                unsafe_allow_html=True)
    st.markdown("## Bạn muốn khám phá điều gì?")

    c1, c2, c3 = st.columns(3, gap="medium")

    with c1:
        st.markdown("""
        <div class="feature">
            <div class="feature-icon">✳</div>
            <h3>Gia sư học tập</h3>
            <p>Phân tích câu hỏi, tìm gợi ý và xây dựng cách hiểu của riêng bạn.</p>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "Khám phá gia sư →",
            key="go_tutor",
            use_container_width=True,
            on_click=lambda: st.session_state.update(
                eduai_navigation=PAGES[1]
            ),
        )

    with c2:
        st.markdown("""
        <div class="feature">
            <div class="feature-icon">▤</div>
            <h3>Kiểm tra kiến thức</h3>
            <p>Thử thách bản thân bằng câu hỏi và xem lại những gì cần ôn.</p>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "Bắt đầu kiểm tra →",
            key="go_quiz",
            use_container_width=True,
            on_click=lambda: st.session_state.update(
                eduai_navigation=PAGES[2]
            ),
        )

    with c3:
        st.markdown("""
        <div class="feature">
            <div class="feature-icon">◷</div>
            <h3>Tiến độ học tập</h3>
            <p>Quan sát hoạt động và kết quả học tập trong phiên hiện tại.</p>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "Xem tiến độ →",
            key="go_progress",
            use_container_width=True,
            on_click=lambda: st.session_state.update(
                eduai_navigation=PAGES[3]
            ),
        )

st.markdown("## 📡 Learning analytics")
m1, m2, m3 = st.columns(3)

m1.metric("Câu hỏi đã gửi", len(st.session_state.history))
m2.metric(
        "Điểm gần nhất",
        f"{st.session_state.quiz_score}/3"
        if st.session_state.quiz_done else "—",
)
m3.metric("Trạng thái AI", "Bản minh họa")

st.info(
        "EDUAI hiện chưa kết nối mô hình AI thật. "
        "Các chỉ số chỉ phản ánh dữ liệu trong phiên hiện tại."
)

st.markdown("## 🧭 Lộ trình phát triển")
with st.container(border=True):
        st.markdown("**01 — Learning interface**")
        st.caption("Giao diện và luồng học tập cơ bản.")

        st.markdown("**02 — AI integration**")
        st.caption("Kết nối mô hình AI sau khi cấu hình API an toàn.")

        st.markdown("**03 — Knowledge system**")
        st.caption("Hỗ trợ tài liệu học tập đã được kiểm duyệt.")

        st.markdown("**04 — Progress tracking**")
        st.caption("Thiết kế cơ chế lưu kết quả lâu dài.")

# =====================================================
# PAGE 2: AI TUTOR - HUGGING FACE
# =====================================================

# =====================================================
# PAGE 2: AI TUTOR - HUGGING FACE
# =====================================================

elif page == PAGES[1]:
    from groq import Groq

    st.markdown("# ✳ Gia sư học tập")
    st.markdown(
        "Hỏi bài, nhận gợi ý và tìm hiểu kiến thức "
        "cùng gia sư AI của EDUAI."
    )

    # Khởi tạo lịch sử trò chuyện
    if "tutor_messages" not in st.session_state:
        st.session_state.tutor_messages = [
            {
                "role": "assistant",
                "content": (
                    "Xin chào! 👋 Mình là gia sư AI của EDUAI. "
                    "Bạn đang muốn học môn nào? Hãy nhập câu hỏi "
                    "vào khung chat bên dưới nhé."
                ),
            }
        ]

    # Tùy chọn học tập
    col1, col2 = st.columns([1, 2])

    with col1:
        subject = st.selectbox(
            "📚 Môn học",
            [
                "Hóa học ",
                "Toán học",
                "Sinh học",
                "Ngữ văn",
                "Tiếng Anh",
            ],
            key="tutor_subject",
        )

    with col2:
        help_style = st.selectbox(
            "🧠 Cách hỗ trợ",
            [
                "Gợi ý trước",
                "Giải thích từng bước",
                "Ví dụ tương tự",
            ],
            key="tutor_help_style",
        )

    # Nút xóa cuộc trò chuyện
    if st.button(
        "🗑️ Xóa cuộc trò chuyện",
        key="clear_tutor",
    ):
        st.session_state.tutor_messages = [
            {
                "role": "assistant",
                "content": (
                    "Cuộc trò chuyện đã được làm mới. "
                    "Bạn có thể bắt đầu hỏi bài!"
                ),
            }
        ]
        st.rerun()

    st.divider()

    # Hiển thị lịch sử chat
    st.markdown("### 💬 Cuộc trò chuyện")

    for message in st.session_state.tutor_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Khung nhập câu hỏi
    question = st.chat_input(
        "Nhập câu hỏi của bạn tại đây...",
        key="tutor_chat_input",
    )

    if question:
        # Lưu và hiển thị câu hỏi
        st.session_state.tutor_messages.append(
            {"role": "user", "content": question}
        )

        with st.chat_message("user"):
            st.markdown(question)

        try:
            # Kết nối Groq API
            token = st.secrets["GROQ_API_KEY"]
            client = Groq(api_key=token)

            instructions = f"""
Bạn là gia sư AI của EDUAI, hỗ trợ học sinh THPT
bằng tiếng Việt rõ ràng, chính xác và dễ hiểu.

Môn học: {subject}
Cách hỗ trợ: {help_style}

Nếu chọn Gợi ý trước, hãy đưa gợi ý trước khi giải.
Nếu chọn Giải thích từng bước, hãy trình bày từng bước
và giải thích lý do.
Nếu chọn Ví dụ tương tự, hãy giải thích kiến thức
rồi đưa một ví dụ phù hợp.

Không tự bịa dữ kiện. Nếu chưa chắc chắn, hãy nói rõ.
"""

            messages = [
                {
                    "role": "system",
                    "content": instructions,
                }
            ]

            # Lấy các tin nhắn gần nhất làm ngữ cảnh
            # Loại bỏ câu hỏi hiện tại khỏi danh sách này
            # để tránh gửi câu hỏi hai lần
            previous_messages = (
                st.session_state.tutor_messages[:-1]
            )

            messages.extend(
                {
                    "role": item["role"],
                    "content": item["content"],
                }
                for item in previous_messages[-10:]
            )

            # Thêm câu hỏi hiện tại đúng một lần
            messages.append(
                {
                    "role": "user",
                    "content": question,
                }
            )

            with st.chat_message("assistant"):
                with st.spinner("Gia sư AI đang suy nghĩ..."):
                    result = client.chat.completions.create(
                        model="openai/gpt-oss-120b",
                        messages=messages,
                        max_completion_tokens=700,
                    )

                    answer = (
                        result.choices[0].message.content
                    )

                    if not answer:
                        answer = (
                            "Mô hình chưa trả về câu trả lời. "
                            "Bạn hãy thử hỏi lại nhé."
                        )

                    st.markdown(answer)

            # Lưu câu trả lời vào lịch sử trò chuyện
            st.session_state.tutor_messages.append(
                {
                    "role": "assistant",
                    "content": answer,
                }
            )

            # Cập nhật lịch sử học tập nếu đã khởi tạo
            if "history" in st.session_state:
                st.session_state.history.append(
                    {
                        "subject": subject,
                        "question": question,
                        "answer": answer,
                    }
                )

        except Exception as e:
            st.error(
                "Không thể kết nối với Groq AI. "
                "Hãy kiểm tra API key, tên mô hình "
                "và hạn mức sử dụng."
            )
            st.write("Loại lỗi:", type(e).__name__)
            st.code(str(e)[:1500])

# =====================================================
# PAGE 3: QUIZ
# =====================================================
elif page == PAGES[2]:
    st.markdown("# ▤ Kiểm tra kiến thức")
    st.write("Mini challenge · Hóa học 12")

    questions = [
        {
            "q": "Nhóm chức nào trong dạng mạch hở của glucose liên quan trực tiếp đến phản ứng tráng bạc?",
            "options": [
                "Nhóm hydroxyl (–OH)",
                "Nhóm aldehyde (–CHO)",
                "Nhóm carboxyl (–COOH)",
                "Nhóm amino (–NH₂)",
            ],
            "answer": "Nhóm aldehyde (–CHO)",
            "topic": "Nhận biết nhóm chức",
        },
        {
            "q": "Khi học một phản ứng hóa học, điều nào nên làm trước tiên?",
            "options": [
                "Học thuộc đáp án mà không cần hiểu",
                "Xác định chất tham gia và điều kiện phản ứng",
                "Bỏ qua hiện tượng",
                "Chọn phương trình dài nhất",
            ],
            "answer": "Xác định chất tham gia và điều kiện phản ứng",
            "topic": "Phương pháp học",
        },
        {
            "q": "Nếu trả lời sai một câu hỏi, cách học nào hữu ích nhất?",
            "options": [
                "Bỏ qua câu hỏi",
                "Chỉ ghi nhớ chữ cái đáp án",
                "Xác định nguyên nhân sai rồi làm câu tương tự",
                "Làm lại y nguyên mà không xem lời giải",
            ],
            "answer": "Xác định nguyên nhân sai rồi làm câu tương tự",
            "topic": "Tự điều chỉnh học tập",
        },
    ]

    with st.container(border=True):
        st.markdown("### 🧪 Knowledge check")
        st.caption("3 câu hỏi · Hãy chọn một đáp án cho mỗi câu.")

        with st.form("eduai_quiz"):
            answers = []

            for i, item in enumerate(questions):
                st.markdown(f"**Câu {i + 1} / 3**")
                st.write(item["q"])
                answers.append(
                    st.radio(
                        "Chọn đáp án",
                        item["options"],
                        key=f"eduai_q{i}",
                        index=None,
                    )
                )
                if i < len(questions) - 1:
                    st.divider()

            submitted = st.form_submit_button(
                "Nộp bài →",
                type="primary",
                use_container_width=True,
            )

    if submitted:
        unanswered = sum(answer is None for answer in answers)

        if unanswered:
            st.warning(f"Còn {unanswered} câu chưa trả lời.")
        else:
            score = sum(
                answers[i] == questions[i]["answer"]
                for i in range(len(questions))
            )
            st.session_state.quiz_score = score
            st.session_state.quiz_done = True
            st.session_state.last_answers = answers
            st.session_state.last_questions = questions

    if st.session_state.quiz_done:
        score = st.session_state.quiz_score
        total = len(st.session_state.last_questions)

        st.markdown("## 📊 Kết quả")
        st.progress(score / total)
        st.metric("Điểm số", f"{score}/{total}")

        for i, item in enumerate(st.session_state.last_questions):
            correct = (
                st.session_state.last_answers[i] == item["answer"]
            )
            with st.expander(
                f"Câu {i + 1} · {'Chính xác' if correct else 'Cần ôn tập'}"
            ):
                st.write(item["topic"])
                st.write(
                    f"Đáp án của bạn: {st.session_state.last_answers[i]}"
                )
                if not correct:
                    st.write(f"Đáp án đúng: {item['answer']}")

        if score == total:
            st.success("Hoàn thành xuất sắc! Hãy thử thách bản thân với bài khó hơn.")
        else:
            st.info("Ôn lại câu sai và thử làm một bộ câu hỏi tương tự.")

# =====================================================
# PAGE 4: PROGRESS
# =====================================================
elif page == PAGES[3]:
    st.markdown("# ◷ Tiến độ học tập")
    st.write("Learning signals · Dữ liệu trong phiên hiện tại")

    col1, col2 = st.columns(2)

    col1.metric("Câu hỏi gia sư", len(st.session_state.history))
    col2.metric(
        "Điểm kiểm tra",
        f"{st.session_state.quiz_score}/3"
        if st.session_state.quiz_done else "Chưa có",
    )

    st.markdown("## 🔬 Chu trình học tập")

    stages = [
        ("01", "Khám phá", "Xác định phần kiến thức cần học."),
        ("02", "Thực hành", "Làm câu hỏi để kiểm tra mức độ hiểu."),
        ("03", "Phân tích", "Xem lại lỗi và nguyên nhân."),
        ("04", "Củng cố", "Luyện tập lại để tự đánh giá tiến bộ."),
    ]

    for number, title, description in stages:
        with st.container(border=True):
            st.markdown(f"### {number} / {title}")
            st.write(description)

    st.caption(
        "Dữ liệu chưa được lưu lâu dài. Một bài kiểm tra ngắn "
        "không đủ để kết luận toàn diện về năng lực học tập."
    )

# =====================================================
# PAGE 5: TEACHER
# =====================================================
elif page == PAGES[4]:
    st.markdown("# ⚗ Trợ lý giáo viên")
    st.write("Thiết kế khung đề theo mục tiêu bài học.")

    with st.container(border=True):
        subject = st.selectbox(
            "Môn học",
            ["Hóa học 12", "Toán học", "Sinh học", "Ngữ văn", "Tiếng Anh"],
            key="teacher_subject",
        )

        topic = st.text_input(
            "Chủ đề",
            placeholder="Ví dụ: Glucose và fructose",
        )

        count = st.slider(
            "Số câu hỏi",
            min_value=3,
            max_value=15,
            value=6,
        )

        if st.button("Tạo khung đề →", type="primary",
                     use_container_width=True):
            if not topic.strip():
                st.warning("Hãy nhập chủ đề trước nhé.")
            else:
                nhận_biết = max(1, count // 3)
                thông_hiểu = max(1, count // 3)
                vận_dụng = count - nhận_biết - thông_hiểu

                st.markdown("## Khung đề tham khảo")
                st.write(f"**Môn:** {subject}")
                st.write(f"**Chủ đề:** {topic}")

                a, b, c = st.columns(3)
                a.metric("Nhận biết", nhận_biết)
                b.metric("Thông hiểu", thông_hiểu)
                c.metric("Vận dụng", vận_dụng)

                st.warning(
                    "Đây là khung phân bổ số câu, chưa tự tạo nội dung "
                    "câu hỏi. Giáo viên cần kiểm duyệt trước khi sử dụng."
                )

                st.code(
                    f"Môn học: {subject}\n"
                    f"Chủ đề: {topic}\n"
                    f"Tổng số câu: {count}\n"
                    "Yêu cầu: soạn câu hỏi, đáp án, lời giải "
                    "và phân loại mức độ.",
                    language="text",
                )

# ------------------ FOOTER ---------------------------
st.divider()
st.markdown(
    '<div class="footer">EDUAI © · LEARN BEYOND LIMITS · '
    'SCI-TECH YOUTH EDITION</div>',
    unsafe_allow_html=True,
)
