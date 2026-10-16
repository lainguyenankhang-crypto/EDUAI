# EDUAI Starter (phiên bản 0.1)

Đây là bản mẫu giáo dục để học thử quy trình, KHÔNG phải hệ thống AI hoàn chỉnh.
Phần gia sư hiện sử dụng một số phản hồi minh họa; chưa gọi API AI và chưa lưu dữ liệu lâu dài.

## Cách chạy trên máy tính

1. Cài Python 3.11 hoặc mới hơn từ https://www.python.org/downloads/
   - Trên Windows, đánh dấu chọn "Add Python to PATH" nếu tùy chọn xuất hiện.
2. Tải và giải nén thư mục `EDUAI_starter`.
3. Mở Terminal / Command Prompt tại thư mục đó.
4. Chạy:
   ```bash
   python -m pip install -r requirements.txt
   python -m streamlit run app.py
   ```
5. Trình duyệt sẽ mở địa chỉ thường là `http://localhost:8501`.

Nếu lệnh `python` không chạy trên Windows, thử `py` thay cho `python`.

## Chạy bằng Google Colab

Colab phù hợp để thử Python, nhưng Streamlit cần một cách tạo đường dẫn truy cập công khai/tạm thời để xem giao diện. Để người mới tránh các bước phức tạp, nên chạy bản đầu tiên trên máy tính theo hướng dẫn ở trên. Có thể triển khai lên một dịch vụ hosting sau khi ứng dụng chạy ổn định.

## Cách kiểm tra

- Vào Tổng quan: thấy tên EDUAI và lộ trình.
- Vào Gia sư học tập: nhập câu hỏi “Vì sao glucose phản ứng được với thuốc thử Tollens?” và nhấn Nhận hỗ trợ.
- Vào Kiểm tra kiến thức: trả lời đủ 3 câu và nộp bài.
- Vào Tiến độ học tập: xem số câu hỏi và điểm kiểm tra trong phiên.
- Vào Trợ lý giáo viên: nhập một chủ đề rồi tạo khung đề.

## Giới hạn và an toàn

- Dữ liệu chỉ nằm trong phiên chạy hiện tại; chưa có tài khoản, phân quyền hay cơ sở dữ liệu.
- Không nhập thông tin cá nhân nhạy cảm hoặc dữ liệu thật của học sinh.
- Nội dung câu hỏi mẫu cần được giáo viên chuyên môn kiểm tra.
- Không dùng bản mẫu để chấm điểm chính thức.
- Trước khi kết nối API AI, cần cất khóa API trong biến môi trường hoặc kho bí mật của nền tảng, không ghi khóa trực tiếp vào mã và không đưa khóa lên GitHub.
