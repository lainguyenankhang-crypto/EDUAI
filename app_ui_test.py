
import streamlit as st

st.set_page_config(
    page_title="EDUAI",
    page_icon="🎓",
    layout="wide"
)

# Thanh điều hướng bên trái
with st.sidebar:
    st.markdown("## 🎓 EDUAI")
    st.caption("Trợ lý học tập thông minh")
    st.divider()

    trang = st.radio(
        "ĐIỀU HƯỚNG",
        [
            "🏠 Trang chủ",
            "🤖 Gia sư AI",
            "📝 Bài kiểm tra",
            "📈 Tiến độ học tập"
        ],
        key="eduai_navigation"
    )

    st.divider()
    st.caption("Học tập chủ động mỗi ngày ✨")

# Nội dung trang chủ
if trang == "🏠 Trang chủ":
    st.markdown("# Chào mừng đến với EDUAI 👋")
    st.markdown(
        "Không gian học tập của bạn — "
        "hỏi đáp, luyện tập và theo dõi sự tiến bộ."
    )

    st.divider()

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        with st.container(border=True):
            st.markdown("### 🤖 Gia sư AI")
            st.write("Đặt câu hỏi và tìm hiểu kiến thức.")
            if st.button("Mở gia sư", key="home_tutor",
                         use_container_width=True):
                st.session_state["eduai_navigation"] = "🤖 Gia sư AI"
                st.rerun()

    with col2:
        with st.container(border=True):
            st.markdown("### 📝 Bài kiểm tra")
            st.write("Luyện tập và kiểm tra mức độ hiểu bài.")
            if st.button("Làm bài tập", key="home_quiz",
                         use_container_width=True):
                st.session_state["eduai_navigation"] = "📝 Bài kiểm tra"
                st.rerun()

    with col3:
        with st.container(border=True):
            st.markdown("### 📈 Tiến độ học tập")
            st.write("Xem kết quả và quá trình học tập.")
            if st.button("Xem tiến độ", key="home_progress",
                         use_container_width=True):
                st.session_state["eduai_navigation"] = "📈 Tiến độ học tập"
                st.rerun()

# Các trang này cần kết nối với chức năng hiện có
elif trang == "🤖 Gia sư AI":
    st.title("🤖 Gia sư AI")
    st.info("Hãy kết nối phần gia sư AI hiện có tại đây.")

elif trang == "📝 Bài kiểm tra":
    st.title("📝 Bài kiểm tra")
    st.info("Hãy kết nối phần bài kiểm tra hiện có tại đây.")

elif trang == "📈 Tiến độ học tập":
    st.title("📈 Tiến độ học tập")
    st.info("Hãy kết nối phần theo dõi tiến độ hiện có tại đây.")
