# Dự án RESTful API Quản lý Danh sách Công việc
# Tổng quan
Dự án này là một ứng dụng quản lý danh sách công việc (To-do List) đơn giản, được xây dựng với API RESTful sử dụng Flask và giao diện người dùng đồ họa (GUI) sử dụng PyQt5. Ứng dụng cho phép người dùng thực hiện các thao tác tạo, đọc, cập nhật và xóa (CRUD) các công việc, được lưu trữ trong cơ sở dữ liệu SQLite. API và GUI chạy đồng thời, với GUI giao tiếp với API thông qua các yêu cầu HTTP.
Tính năng

# API RESTful:
GET /todos: Lấy danh sách tất cả công việc.
POST /todos: Tạo một công việc mới.
GET /todos/<id>: Lấy thông tin chi tiết của một công việc theo ID.
PUT /todos/<id>: Cập nhật một công việc cụ thể.
DELETE /todos/<id>: Xóa một công việc cụ thể.


# Giao diện người dùng (GUI):
Hiển thị danh sách công việc.
Cung cấp biểu mẫu để thêm hoặc chỉnh sửa công việc (tiêu đề và mô tả).
Bao gồm các nút để thêm, cập nhật và xóa công việc.
Tự động làm mới danh sách công việc sau khi có thay đổi.


Cơ sở dữ liệu: Sử dụng SQLite để lưu trữ công việc một cách bền vững.
Chạy đồng thời: Chạy API Flask và GUI PyQt5 cùng lúc bằng cách sử dụng threading.


# Kiến thức cần thiết
Để hiểu và làm việc với dự án này, bạn cần có kiến thức cơ bản về:

Python: Hiểu cú pháp Python, hàm, lớp và module.
Flask: Quen thuộc với việc tạo API RESTful, định tuyến và xử lý yêu cầu HTTP.
PyQt5: Kiến thức về cách tạo ứng dụng GUI, bố cục, widget và xử lý sự kiện.
HTTP/REST: Hiểu các khái niệm API RESTful (GET, POST, PUT, DELETE) và mã trạng thái HTTP.
Threading: Kiến thức cơ bản về chạy nhiều tiến trình đồng thời trong Python.

# Hướng dẫn cài đặt
Cài đặt các thư viện phụ thuộc:
pip install -r requirements.txt

Lệnh này sẽ cài đặt Flask, PyQt5 và requests như được liệt kê trong requirements.txt.

# Chạy ứng dụng:
python main.py


API Flask sẽ khởi động tại http://127.0.0.1:5000.
Giao diện PyQt5 sẽ mở trong một cửa sổ mới.



# Hướng dẫn sử dụng

Giao diện người dùng (GUI):

Bảng bên trái hiển thị danh sách công việc (ID và tiêu đề).
Nhấp vào một công việc để xem chi tiết ở bảng bên phải.
Sử dụng bảng bên phải để:
Nhập tiêu đề và mô tả, sau đó nhấn "Add Todo" để tạo công việc mới.
Chọn một công việc, chỉnh sửa chi tiết và nhấn "Update Todo" để lưu thay đổi.
Chọn một công việc và nhấn "Delete Todo" để xóa.


Thông báo lỗi sẽ xuất hiện nếu thao tác thất bại (ví dụ: không chọn công việc).


API:

Bạn có thể tương tác trực tiếp với API bằng các công cụ như curl hoặc Postman.

Ví dụ các lệnh gọi API:
# Lấy tất cả công việc
curl http://127.0.0.1:5000/todos

# Tạo công việc mới
curl -X POST -H "Content-Type: application/json" -d '{"title":"Công việc mới","description":"Chi tiết"}' http://127.0.0.1:5000/todos

# Lấy thông tin công việc cụ thể
curl http://127.0.0.1:5000/todos/1

# Cập nhật công việc
curl -X PUT -H "Content-Type: application/json" -d '{"title":"Công việc đã cập nhật","description":"Chi tiết mới","completed":false}' http://127.0.0.1:5000/todos/1

# Xóa công việc
curl -X DELETE http://127.0.0.1:5000/todos/1





# Lưu ý

Cơ sở dữ liệu SQLite (todos.db) được tạo tự động trong thư mục dự án khi ứng dụng khởi động.
API chạy trên localhost:5000. Hãy đảm bảo cổng này không bị chiếm dụng trước khi chạy ứng dụng.
GUI sử dụng thư viện requests để giao tiếp với API, vì vậy API phải đang chạy để GUI hoạt động bình thường.
Ứng dụng sử dụng threading để chạy server Flask và GUI PyQt5 đồng thời. Server Flask chạy trong một luồng daemon để đảm bảo nó kết thúc khi GUI đóng.


# Giấy phép
Dự án này được tạo với mục đích học tập và không được cấp phép để sử dụng trong môi trường sản xuất.
