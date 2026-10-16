import streamlit as st

if "history" not in st.session_state:
    st.session_state.history = []
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_done" not in st.session_state:
    st.session_state.quiz_done = False

st.title("🎓 EDUAI")
st.subheader("Trợ lý học tập thông minh — bản mẫu thử nghiệm")
st.info("Đây là bản mẫu ban đầu, chưa kết nối mô hình AI thật. Phần gia sư hiện dùng phản hồi minh họa để kiểm tra giao diện và luồng học tập.")

with st.sidebar:
    st.header("Điều hướng")
    page = st.radio("Chọn chức năng", ["🏠 Tổng quan", "💬 Gia sư học tập", "📝 Kiểm tra kiến thức", "📊 Tiến độ học tập", "👩‍🏫 Trợ lý giáo viên"])
    st.divider()
    st.caption("EDUAI • Phiên bản 0.1")

if page == "🏠 Tổng quan":
    st.markdown("### Chào mừng đến với EDUAI")
    st.write("Mục tiêu: giúp học sinh phát hiện phần kiến thức còn yếu, luyện tập có hướng dẫn và học theo lộ trình phù hợp.")
    a, b, c = st.columns(3)
    a.metric("Chức năng mẫu", "4")
    b.metric("Môn học minh họa", "Hóa học 12")
    c.metric("Phiên bản", "0.1")
    st.markdown("#### Lộ trình phát triển")
    st.markdown("- **Bản 0.1:** giao diện, câu hỏi mẫu và theo dõi kết quả trong phiên hiện tại.\n- **Bản 0.2:** kết nối API mô hình AI.\n- **Bản 0.3:** dùng tài liệu học tập đã kiểm duyệt để hỗ trợ câu trả lời.\n- **Bản 0.4:** lưu tiến độ và thử nghiệm với học sinh.")
    st.warning("Không nhập thông tin cá nhân nhạy cảm vào bản thử nghiệm.")

elif page == "💬 Gia sư học tập":
    st.markdown("### 💬 Gia sư học tập")
    subject = st.selectbox("Môn học", ["Hóa học 12", "Toán học", "Sinh học", "Ngữ văn", "Tiếng Anh"])
    question = st.text_area("Bạn đang chưa hiểu điều gì?", placeholder="Ví dụ: Vì sao glucose phản ứng được với thuốc thử Tollens?", height=120)
    help_style = st.radio("Bạn muốn được hỗ trợ theo cách nào?", ["Gợi ý trước", "Giải thích từng bước", "Ví dụ tương tự"], horizontal=True)
    if st.button("Nhận hỗ trợ", type="primary"):
        if not question.strip():
            st.warning("Hãy nhập câu hỏi trước nhé.")
        else:
            q = question.lower()
            if subject == "Hóa học 12" and ("tollens" in q or "tráng bạc" in q or "glucose" in q):
                answer = (
                    "**Gợi ý kiến thức:** Glucose có dạng mạch hở chứa nhóm aldehyde (–CHO), vì vậy có thể khử ion bạc trong thuốc thử Tollens thành bạc kim loại. "
                    "Trong dung dịch, glucose tồn tại cân bằng giữa dạng mạch vòng và một lượng nhỏ dạng mạch hở.\n\n"
                    "**Cách tự kiểm tra:** Hãy xác định nhóm chức nào chịu trách nhiệm cho phản ứng tráng bạc và viết phương trình theo đúng quy ước trong sách giáo khoa của bạn."
                )
            elif help_style == "Gợi ý trước":
                answer = ("**Gợi ý:** Hãy chia câu hỏi thành ba phần: (1) kiến thức hoặc định nghĩa liên quan, (2) dữ kiện đã biết, (3) điều cần tìm. "
                          "Thử tự trả lời từng phần trước khi xem lời giải.")
            elif help_style == "Ví dụ tương tự":
                answer = ("**Cách luyện tập:** Hãy tạo một ví dụ cùng dạng nhưng thay đổi dữ kiện, tự giải rồi so sánh từng bước với bài ban đầu. "
                          "Bản mẫu này chưa có mô hình AI thật nên chưa thể tạo lời giải chuyên biệt cho mọi câu hỏi.")
            else:
                answer = ("**Hướng dẫn từng bước:**\n\n1. Xác định chủ đề và kiến thức nền.\n2. Ghi lại dữ kiện hoặc yêu cầu.\n3. Chọn quy tắc/phương pháp phù hợp.\n4. Thực hiện từng bước và kiểm tra kết quả.\n\n"
                          "Lưu ý: đây là phản hồi minh họa, không phải câu trả lời do mô hình AI tạo ra.")
            st.session_state.history.append({"subject": subject, "question": question, "answer": answer})
            st.markdown(answer)
    if st.session_state.history:
        st.markdown("#### Câu hỏi trong phiên này")
        for item in reversed(st.session_state.history[-5:]):
            with st.expander(f"{item['subject']}: {item['question'][:70]}"):
                st.markdown(item["answer"])

elif page == "📝 Kiểm tra kiến thức":
    st.markdown("### 📝 Kiểm tra kiến thức — Hóa học 12")
    st.write("Câu hỏi mẫu để kiểm tra luồng làm bài; giáo viên cần rà soát nội dung trước khi sử dụng chính thức.")
    questions = [
        {
            "q": "Nhóm chức nào trong dạng mạch hở của glucose liên quan trực tiếp đến phản ứng tráng bạc?",
            "options": ["Nhóm hydroxyl (–OH)", "Nhóm aldehyde (–CHO)", "Nhóm carboxyl (–COOH)", "Nhóm amino (–NH₂)"],
            "answer": "Nhóm aldehyde (–CHO)",
            "topic": "Nhận biết nhóm chức"
        },
        {
            "q": "Khi học một phản ứng hóa học, điều nào nên làm trước tiên?",
            "options": ["Học thuộc đáp án mà không cần hiểu", "Xác định chất tham gia và điều kiện phản ứng", "Bỏ qua hiện tượng", "Chọn phương trình dài nhất"],
            "answer": "Xác định chất tham gia và điều kiện phản ứng",
            "topic": "Phương pháp học"
        },
        {
            "q": "Nếu trả lời sai một câu hỏi, cách học nào hữu ích nhất?",
            "options": ["Bỏ qua câu hỏi", "Chỉ ghi nhớ chữ cái đáp án", "Xác định nguyên nhân sai rồi làm câu tương tự", "Làm lại y nguyên mà không xem lời giải"],
            "answer": "Xác định nguyên nhân sai rồi làm câu tương tự",
            "topic": "Tự điều chỉnh học tập"
        }
    ]
    with st.form("quiz_form"):
        answers = []
        for i, item in enumerate(questions):
            st.markdown(f"**Câu {i+1}. {item['q']}**")
            answers.append(st.radio("Chọn một đáp án:", item["options"], key=f"q{i}", index=None))
        submitted = st.form_submit_button("Nộp bài", type="primary")
    if submitted:
        unanswered = sum(x is None for x in answers)
        if unanswered:
            st.warning(f"Bạn còn {unanswered} câu chưa trả lời.")
        else:
            score = sum(answers[i] == questions[i]["answer"] for i in range(len(questions)))
            st.session_state.quiz_score = score
            st.session_state.quiz_done = True
            st.session_state.last_answers = answers
            st.session_state.last_questions = questions
    if st.session_state.quiz_done:
        score = st.session_state.quiz_score
        st.success(f"Kết quả: {score}/{len(questions)} câu đúng.")
        for i, item in enumerate(st.session_state.get("last_questions", questions)):
            chosen = st.session_state.last_answers[i]
            ok = chosen == item["answer"]
            st.markdown(f"**Câu {i+1}: {'Đúng' if ok else 'Cần ôn tập'}** — {item['topic']}")
            if not ok:
                st.write(f"Đáp án đúng: {item['answer']}")
        if score < len(questions):
            st.info("Gợi ý lộ trình: ôn lại các câu sai, ghi rõ vì sao chọn nhầm, sau đó làm thêm câu tương tự.")
        else:
            st.info("Bạn có thể thử bộ câu hỏi khó hơn sau khi giáo viên bổ sung ngân hàng câu hỏi.")

elif page == "📊 Tiến độ học tập":
    st.markdown("### 📊 Tiến độ học tập")
    st.write("Bản mẫu chỉ lưu dữ liệu trong phiên trình duyệt hiện tại; chưa có tài khoản hay cơ sở dữ liệu lâu dài.")
    st.metric("Số câu hỏi đã gửi cho gia sư", len(st.session_state.history))
    if st.session_state.quiz_done:
        st.metric("Kết quả bài kiểm tra gần nhất", f"{st.session_state.quiz_score}/3")
    else:
        st.write("Bạn chưa hoàn thành bài kiểm tra mẫu.")
    st.markdown("#### Lộ trình đề xuất")
    st.markdown("1. Làm bài kiểm tra ngắn.\n2. Xem câu sai và giải thích nguyên nhân.\n3. Ôn lại phần kiến thức liên quan.\n4. Làm một bài kiểm tra tương tự để xem tiến bộ.")
    st.caption("Để tránh đưa ra kết luận thiếu căn cứ, bản mẫu chưa tự gán nhãn năng lực học sinh từ một bài kiểm tra ngắn.")

elif page == "👩‍🏫 Trợ lý giáo viên":
    st.markdown("### 👩‍🏫 Trợ lý giáo viên")
    st.write("Tạo khung đề mẫu theo mục tiêu dạy học. Đây là bản tạo khung, chưa phải AI sinh câu hỏi tự động.")
    subject = st.selectbox("Môn học", ["Hóa học 12", "Toán học", "Sinh học", "Ngữ văn", "Tiếng Anh"], key="teacher_subject")
    topic = st.text_input("Chủ đề / bài học", placeholder="Ví dụ: Glucose và fructose")
    count = st.slider("Số câu hỏi cần soạn", min_value=3, max_value=15, value=6)
    if st.button("Tạo khung đề"):
        if not topic.strip():
            st.warning("Hãy nhập chủ đề trước.")
        else:
            st.markdown(f"**Khung đề: {subject} — {topic}**")
            st.markdown(f"- Nhận biết: {max(1, count//3)} câu\n- Thông hiểu: {max(1, count//3)} câu\n- Vận dụng: {max(1, count - 2*(count//3))} câu")
            st.write("Giáo viên cần viết hoặc duyệt từng câu hỏi, đáp án và thang điểm trước khi sử dụng.")
            st.code(f"Chủ đề: {topic}\nMôn: {subject}\nTổng số câu: {count}\nYêu cầu: tạo câu hỏi, đáp án, lời giải và phân loại mức độ.", language="text")
