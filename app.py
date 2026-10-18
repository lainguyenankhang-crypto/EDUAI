
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

st.markdown("""
<style>

/* 1. Bảng màu và nền ứng dụng */
:root {
    --eduai-primary: #6366f1;
    --eduai-primary-dark: #4f46e5;
    --eduai-primary-light: #eef2ff;
    --eduai-accent: #8b5cf6;
    --eduai-text: #172554;
    --eduai-muted: #64748b;
    --eduai-border: #e2e8f0;
    --eduai-surface: #ffffff;
    --eduai-background: #f7f8fc;
}

.stApp {
    background:
        radial-gradient(
            ellipse at 85% 0%,
            rgba(139, 92, 246, 0.10),
            transparent 34%
        ),
        radial-gradient(
            ellipse at 0% 20%,
            rgba(99, 102, 241, 0.07),
            transparent 30%
        ),
        var(--eduai-background);

    color: var(--eduai-text);
}

/* 2. Khu vực nội dung chính */
[data-testid="stMainBlockContainer"] {
    max-width: 1240px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* 3. Thanh điều hướng bên trái */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #eef2ff 0%,
        #f8faff 55%,
        #ffffff 100%
    );

    border-right: 1px solid #e0e7ff;
}

[data-testid="stSidebar"] > div {
    padding-top: 1.5rem;
}

/* 4. Kiểu chữ */
html,
body,
.stApp {
    font-family: "Inter", "Segoe UI", sans-serif;
}

h1,
h2,
h3,
h4 {
    color: var(--eduai-text);
    letter-spacing: -0.035em;
}

h1 {
    font-weight: 800;
    line-height: 1.2;
}

h2 {
    font-weight: 750;
    line-height: 1.3;
}

h3 {
    font-weight: 700;
}

/* 5. Các đoạn văn và chú thích */
[data-testid="stMarkdownContainer"] p {
    line-height: 1.75;
}

.stCaption,
[data-testid="stCaptionContainer"] {
    color: var(--eduai-muted);
}

/* 6. Thanh điều hướng radio */
[data-testid="stRadio"] > div {
    gap: 0.35rem;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label {
    padding: 0.45rem 0.65rem;
    border-radius: 12px;
    transition:
        background 0.18s ease,
        color 0.18s ease;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background: rgba(99, 102, 241, 0.09);
}

/* 7. Nút bấm */
.stButton > button {
    min-height: 44px;
    border: 1px solid #dce3f2;
    border-radius: 12px;

    background: #ffffff;
    color: var(--eduai-text);

    font-weight: 650;

    transition:
        transform 0.18s ease,
        box-shadow 0.18s ease,
        border-color 0.18s ease;
}

.stButton > button:hover {
    border-color: #a5b4fc;
    color: var(--eduai-primary-dark);

    box-shadow:
        0 6px 18px rgba(79, 70, 229, 0.10);

    transform: translateY(-1px);
}

.stButton > button:focus-visible {
    outline: 3px solid rgba(99, 102, 241, 0.35);
    outline-offset: 2px;
}

/* 8. Ô chọn và ô nhập dữ liệu */
[data-baseweb="select"] > div {
    border-radius: 12px;
    border-color: #dce3f2;
    background: #ffffff;
}

[data-baseweb="select"] > div:focus-within {
    border-color: var(--eduai-primary);
    box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.12);
}

[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input,
[data-testid="stTextArea"] textarea {
    border-radius: 12px;
    border-color: #dce3f2;
}

/* 9. Các thẻ nội dung có viền */
[data-testid="stVerticalBlockBorderWrapper"] {
    border: 1px solid var(--eduai-border);
    border-radius: 18px;
    background: rgba(255, 255, 255, 0.86);

    box-shadow:
        0 5px 20px rgba(30, 41, 59, 0.035);
}

/* 10. Chỉ số thống kê */
[data-testid="stMetric"] {
    padding: 18px 20px;

    border: 1px solid #e2e8f0;
    border-radius: 16px;

    background: rgba(255, 255, 255, 0.90);

    box-shadow:
        0 4px 16px rgba(30, 41, 59, 0.035);
}

[data-testid="stMetricLabel"] {
    color: var(--eduai-muted);
    font-weight: 600;
}

[data-testid="stMetricValue"] {
    color: var(--eduai-primary-dark);
    font-weight: 800;
}

/* 11. Khu vực chat */
[data-testid="stChatMessage"] {
    border: 1px solid #e7eaf4;
    border-radius: 16px;
    padding: 1rem;

    background: rgba(255, 255, 255, 0.82);
}

[data-testid="stChatInput"] {
    border-radius: 16px;
}

[data-testid="stChatInput"] textarea {
    border-radius: 16px;
}

/* 12. Hộp thông báo */
[data-testid="stAlert"] {
    border-radius: 14px;
    border-width: 1px;
}

/* 13. Thanh tiến trình */
[data-testid="stProgress"] > div > div {
    border-radius: 999px;
}

/* 14. Đường phân cách */
hr {
    border-color: #e2e8f0;
    opacity: 0.9;
}

/* 15. Bảng dữ liệu */
[data-testid="stDataFrame"],
[data-testid="stTable"] {
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    overflow: hidden;
}

/* 16. Hình ảnh */
[data-testid="stImage"] img {
    border-radius: 14px;
}

/* 17. Hiệu ứng nhẹ, không thay đổi chức năng */
@media (prefers-reduced-motion: no-preference) {
    [data-testid="stVerticalBlockBorderWrapper"] {
        transition:
            box-shadow 0.2s ease,
            border-color 0.2s ease;
    }

    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: #d5dcf0;

        box-shadow:
            0 10px 28px rgba(30, 41, 59, 0.055);
    }
}

/* 18. Tương thích màn hình nhỏ */
@media (max-width: 768px) {
    [data-testid="stMainBlockContainer"] {
        padding: 1.1rem 1rem 2rem;
    }

    h1 {
        font-size: 1.9rem;
    }

    h2 {
        font-size: 1.45rem;
    }

    [data-testid="stMetric"] {
        padding: 12px;
    }
}

/* 19. Hỗ trợ người dùng hạn chế hiệu ứng chuyển động */
@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
    }
}
</style>

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

