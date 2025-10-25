import streamlit as st
from PIL import Image

css_file = "./style/main.css"
resume_file = "./assets/resume.pdf"
profile_image = "./assets/avatar_edited.JPG"
@st.dialog("Gửi email hoặc thêm LinkedIn nhé ^^")
def show_contact():
    st.write("📧 ngocanhhy17@gmail.com")
    st.write("🔗 https://www.linkedin.com/in/ng%E1%BB%8Dc-anh-nguy%E1%BB%85n-627b1227a/")

# GLOBAL CONFIG
page_title = "Resume | Nguyễn Ngọc Anh"
page_icon = "👩‍⚖️"
name = "👩‍⚖️ Nguyễn Ngọc Anh"
description = "Chuyên viên pháp chế | Legal Officer"

# BODY
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="wide")

# load CSS
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_image = Image.open(profile_image)

# HEADER
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image(profile_image, width=220)
with col2:
    st.title(name,anchor=False)
    st.write(description)
    st.download_button(
        label="📃 Tải CV của mình ở đây nhé ^_^",
        data=PDFbyte,
        file_name="Resume_Nguyen Ngoc Anh.pdf",
        mime="application/pdf"
    )
    
    if st.button("📫 Bạn có thể liên hệ mình tại đây nha"):
        show_contact()


# SOCIAL MEDIA
# st.write('#')
# cols = st.columns(len(media))
# for i, (platform, link) in enumerate(media.items()):
#     with cols[i]:
#         st.markdown(f"- [{platform}]({link})")

# EXPERIENCE
st.write('#')
st.subheader("Kinh nghiệm làm việc")
st.write("""
         - **Chuyên viên chính kiểm soát chất lượng** tại [VPBank](https://www.vpbank.com.vn/ve-chung-toi/) (12/2023 - Hiện tại)
         - **Cán bộ nghiệp vụ** tại [Công ty ĐGHD Đấu Giá Việt Nam](https://daugiavietnam.vn/) (09/2023 - 12/2023)
         - **Thực tập sinh** tại [Công ty CP chứng khoán Goutai Junan](https://gtjai.com.vn/tong-quan-lich-su/) (02/2023 - 09/2023)
         """)

# SKILLS
st.write('#')
st.subheader("Kỹ năng & chuyên môn")
st.write("""
         - **Tư vấn pháp lý & xây dựng quy trình, văn bản ban hành nội bộ**
         - **Đàm phán, phối hợp với các Khối Phòng ban khác**
         - **Soạn thảo & lập kế hoạch triển khai các văn bản quy phạm pháp luật (nghị định, thông tư, luật TCTD sửa đổi...)**
         - **Xây dựng các lưu đồ, truyền thông nội bộ nhằm đảo bảo vận hành**
         """)

# EDUCATION
st.write('#')   
st.subheader("Học vấn")
st.write("""
         - **Cử nhân Luật Kinh Tế** tại [Đại học Luật Hà Nội](https://hlu.edu.vn/) (2019 - 2023) - Tốt nghiệp loại Giỏi với GPA 3.38/4.0
         - **Hoàn thành Khóa học Luật sư** tại [Học viện Tư pháp](https://hocvientuphap.edu.vn/Pages/gioi-thieu.aspx?ItemID=55) (2024 - 2025)
         """)

# REFERENCES
st.write('#')   
st.subheader("Người tham khảo")
st.write("""
         - **Anh Nguyễn Tiên Phong (phongnt12@vpbank.com.vn)** : Trưởng phòng cao cấp - Ngân hàng VPBank \n
         📞 0916936969
         """)
         
# Author
# st.logo("Link logo")
st.sidebar.text("""Rất vui được làm quen với các bạn 😻. Mình là Ngọc Anh - Alice một người yêu thích luật và ứng dụng. Mục tiêu nghề nghiệp của mình là trở thành một chuyên gia tư vấn luật kinh tế, có thể vận dụng tư duy pháp lý sắc bén và kỹ năng đàm phán chuyên nghiệp để đưa ra giải pháp pháp lý tối ưu cho doanh nghiệp. \n
Mình mong muốn được đồng hành cùng các doanh nghiệp trong việc giảm thiểu rủi ro, đảm bảo tuân thủ pháp luật và thúc đẩy các thỏa thuận kinh doanh hiệu quả, góp phần vào sự phát triển bền vững của nền kinh tế.""")
