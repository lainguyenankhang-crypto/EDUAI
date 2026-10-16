
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
    --blue: #2563EB;
    --purple: #7C3AED;
    --cyan: #06B6D4;
    --ink: #172554;
    --muted: #64748B;
    --line: #E2E8F0;
    --surface: #FFFFFF;
}

html, body, [class*="css"] {
    font-family: 'Be Vietnam Pro', sans-serif;
}

.stApp {
    background:
        radial-gradient(ellipse at 90% 0%, #EDE9FE 0%, transparent 28%),
        radial-gradient(ellipse at 0% 15%, #DBEAFE 0%, transparent 25%),
        #F8FAFF;
    color: var(--ink);
}

.block-container {
    max-width: 1240px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    color: var(--ink);
    letter-spacing: -0.6px;
    font-weight: 800;
}

p, label, .stMarkdown {
    line-height: 1.7;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #EFF6FF, #F5F3FF);
    border-right: 1px solid #DCE5FF;
}

[data-testid="stSidebar"] h1 {
    color: #4338CA;
    letter-spacing: -1px;
}

/* Main hero */
.hero {
    position: relative;
    overflow: hidden;
    padding: 34px;
    border-radius: 26px;
    color: white;
    background: linear-gradient(120deg, #1D4ED8 0%, #4F46E5 55%, #7C3AED 100%);
    box-shadow: 0 18px 45px rgba(79, 70, 229, .18);
    margin-bottom: 26px;
}

.hero:after {
    content: "✳";
    position: absolute;
    right: 34px;
    top: -42px;
    font-size: 180px;
    color: rgba(255,255,255,.10);
    pointer-events: none;
}

.hero h1 {
    color: white;
    font-size: clamp(1.9rem, 4vw, 2.8rem);
    margin: 12px 0;
}

.hero p {
    color: #E0E7FF;
    max-width: 680px;
    font-size: 1rem;
}

.eyebrow {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 99px;
    border: 1px solid rgba(255,255,255,.30);
    background: rgba(255,255,255,.12);
    color: #F5F3FF;
    font-size: .75rem;
    font-weight: 700;
    letter-spacing: 1.1px;
}

/* Feature cards */
.feature {
    background: rgba(255,255,255,.92);
    border: 1px solid #E2E8F0;
    border-radius: 20px;
    padding: 21px;
    min-height: 185px;
    box-shadow: 0 7px 22px rgba(30, 64, 175, .045);
    transition: transform .2s ease, box-shadow .2s ease;
}

.feature:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 28px rgba(79,70,229,.10);
}

.feature-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 46px;
    height: 46px;
    border-radius: 14px;
    background: #EEF2FF;
    font-size: 24px;
    margin-bottom: 12px;
}

.feature h3 {
    font-size: 1.08rem;
    margin: 0 0 6px 0;
}

.feature p {
    color: var(--muted);
    font-size: .9rem;
    margin: 0;
}

.section-kicker {
    color: #6366F1;
    font-size: .76rem;
    font-weight: 800;
    letter-spacing: 1.4px;
    text-transform: uppercase;
}

/* Metrics */
[data-testid="stMetric"] {
    background: white;
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 17px 19px;
    box-shadow: 0 6px 20px rgba(30,64,175,.04);
}

[data-testid="stMetricLabel"] {
    color: #64748B;
    font-weight: 600;
}

[data-testid="stMetricValue"] {
    color: #3730A3;
    font-weight: 800;
}

/* Buttons */
.stButton > button,
.stFormSubmitButton > button {
    border-radius: 12px;
    min-height: 43px;
    font-weight: 700;
    border: 1px solid #D8DEFF;
    transition: all .2s ease;
}

.stButton > button[kind="primary"],
.stFormSubmitButton > button[kind="primary"] {
    color: white;
    border: none;
    background: linear-gradient(100deg, #2563EB, #7C3AED);
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    border-color: #818CF8;
}

/* Inputs */
[data-testid="stTextArea"] textarea,
[data-testid="stTextInput"] input {
    border-radius: 12px;
    background: #FFFFFF;
}

[data-testid="stSelectbox"] > div {
    border-radius: 12px;
}

[data-testid="stExpander"] {
    background: rgba(255,255,255,.75);
    border: 1px solid #E2E8F0;
    border-radius: 14px;
}

/* Footer */
.footer {
    text-align: center;
    color: #94A3B8;
    font-size: .8rem;
    padding-top: 14px;
}

@media (max-width: 768px) {
    .block-container {
        padding-top: 1rem;
    }
    .hero {
        padding: 23px;
        border-radius: 20px;
    }
    .hero:after {
        right: 8px;
        font-size: 100px;
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
        "KHÔNG GIAN HỌC TẬP",
        PAGES,
        label_visibility="visible",
        key="eduai_navigation",
    )

    st.divider()
    st.markdown("**SCI-TECH EDITION**")
    st.caption("Phiên bản giao diện thử nghiệm")
    st.caption("🔵 Learn · 🟣 Explore · 🧬 Evolve")

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
      if st.button(
    "Khám phá gia sư →",
    key="go_tutor",
    use_container_width=True,
    on_click=lambda: st.session_state.update(
        eduai_navigation=PAGES[1]
    ),
):
    pass

    with c2:
        st.markdown("""
        <div class="feature">
            <div class="feature-icon">▤</div>
            <h3>Kiểm tra kiến thức</h3>
            <p>Thử thách bản thân bằng câu hỏi và xem lại những gì cần ôn.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button(
    "Bắt đầu kiểm tra →",
    key="go_quiz",
    use_container_width=True,
    on_click=lambda: st.session_state.update(
        eduai_navigation=PAGES[2]
    ),
):
    pass

    with c3:
        st.markdown("""
        <div class="feature">
            <div class="feature-icon">◷</div>
            <h3>Tiến độ học tập</h3>
            <p>Quan sát hoạt động và kết quả học tập trong phiên hiện tại.</p>
        </div>
        """, unsafe_allow_html=True)
       if st.button(
    "Xem tiến độ →",
    key="go_progress",
    use_container_width=True,
    on_click=lambda: st.session_state.update(
        eduai_navigation=PAGES[3]
    ),
):
    pass

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
# PAGE 2: TUTOR
# =====================================================
elif page == PAGES[1]:
    st.markdown("# ✳ Gia sư học tập")
    st.write("Đặt câu hỏi. Chia nhỏ vấn đề. Tìm cách hiểu rõ hơn.")

    with st.container(border=True):
        subject = st.selectbox(
            "Môn học",
            ["Hóa học 12", "Toán học", "Sinh học", "Ngữ văn", "Tiếng Anh"],
        )

        question = st.text_area(
            "Câu hỏi của bạn",
            placeholder="Ví dụ: Vì sao glucose phản ứng với thuốc thử Tollens?",
            height=125,
        )

        help_style = st.radio(
            "Chế độ hỗ trợ",
            ["Gợi ý trước", "Giải thích từng bước", "Ví dụ tương tự"],
            horizontal=True,
        )

        if st.button("✦ Phân tích câu hỏi", type="primary",
                     use_container_width=True):
            if not question.strip():
                st.warning("Bạn hãy nhập câu hỏi trước nhé.")
            else:
                q = question.lower()

                if subject == "Hóa học 12" and (
                    "tollens" in q or "tráng bạc" in q or "glucose" in q
                ):
                    answer = (
                        "**Gợi ý kiến thức**\n\n"
                        "Glucose ở dạng mạch hở có nhóm aldehyde (–CHO), "
                        "liên quan đến phản ứng tráng bạc. Trong dung dịch, "
                        "glucose tồn tại cân bằng giữa dạng mạch vòng "
                        "và một lượng nhỏ dạng mạch hở.\n\n"
                        "**Thử thách tư duy**\n\n"
                        "Hãy xác định nhóm chức liên quan và viết phương "
                        "trình theo quy ước trong sách giáo khoa."
                    )
                elif help_style == "Gợi ý trước":
                    answer = (
                        "**Bước 1:** Xác định khái niệm liên quan.\n\n"
                        "**Bước 2:** Tách dữ kiện và yêu cầu.\n\n"
                        "**Bước 3:** Thử giải thích bằng kiến thức của bạn.\n\n"
                        "Đây là gợi ý chung từ bản mẫu, chưa phải AI thật."
                    )
                elif help_style == "Ví dụ tương tự":
                    answer = (
                        "Hãy thử tạo một bài cùng dạng với dữ kiện khác. "
                        "Giải từng bước, sau đó so sánh cách làm và kiểm "
                        "tra xem quy tắc nào được áp dụng."
                    )
                else:
                    answer = (
                        "1. Xác định chủ đề.\n\n"
                        "2. Ghi dữ kiện đã biết.\n\n"
                        "3. Chọn quy tắc hoặc phương pháp.\n\n"
                        "4. Thực hiện từng bước.\n\n"
                        "5. Kiểm tra kết quả và đơn vị nếu có.\n\n"
                        "Đây là phản hồi minh họa, chưa phải AI thật."
                    )

                st.session_state.history.append({
                    "subject": subject,
                    "question": question,
                    "answer": answer,
                })

                st.markdown("### 🧠 Kết quả hỗ trợ")
                st.markdown(answer)

    if st.session_state.history:
        st.markdown("## Lịch sử học tập")
        for item in reversed(st.session_state.history[-5:]):
            with st.expander(
                f"{item['subject']} · {item['question'][:65]}"
            ):
                st.markdown(item["answer"])

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

