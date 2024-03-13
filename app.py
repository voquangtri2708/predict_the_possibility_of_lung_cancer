import streamlit as st
import joblib

models = joblib.load('models.pkl')

st.title("Dự đoán khả năng ung thư phổi")

# Tạo đối tượng nhập độ tuổi
cl2 = st.number_input("Nhập độ tuổi :", min_value=0, max_value=150, value=None, step=1)

# Tạo tùy chọn radio cho giới tính
select_gender = st.radio("Chọn giới tính:", ('Nam', 'Nữ'), index=0)
# Mapping giới tính thành giá trị tương ứng
gender_mapping = {'Nam': 1, 'Nữ': 2}
cl3 = gender_mapping[select_gender]

# Tạo đối tượng nhập mức độ ô nhiễm không khí nơi đang sống (1 - 8)
cl4 = st.number_input("Mức độ ô nhiễm không khí nơi đang sống (1 - 8) :", min_value=1, max_value=8, value=None, step=1)

# Tạo đối tượng nhập mức sử dụng rượu (1 -  8)
cl5 = st.number_input("Mức sử dụng rượu (1 - 8) :", min_value=1, max_value=8, value=None, step=1)

# Tạo đối tượng nhập mức dị ứng bụi (1 -  8)
cl6 = st.number_input("Mức dị ứng bụi (1 - 8) :", min_value=1, max_value=8, value=None, step=1)

# Tạo đối tượng nhập mức nguy hiểm nghề nghiệp (1 -  8)
cl7 = st.number_input("Mức nguy hiểm nghề nghiệp (1 - 8) :", min_value=1, max_value=8, value=None, step=1)

# Tạo đối tượng nhập mức nguy cơ duy truyền (1 -  7)
cl8 = st.number_input("Mức nguy cơ duy truyền (1 - 7) :", min_value=1, max_value=7, value=None, step=1)

# Tạo đối tượng nhập mức bệnh phổi mãn tính (1 -  7)
cl9 = st.number_input("Mức bệnh phổi mãn tính (1 - 7) :", min_value=1, max_value=7, value=None, step=1)

# Tạo đối tượng nhập mức chế độ ăn uống cân bằng (1 -  7)
cl10 = st.number_input("Mức chế độ ăn uống cân bằng (1 - 7) :", min_value=1, max_value=7, value=None, step=1)

# Tạo đối tượng nhập mức độ béo phì (1 -  7)
cl11 = st.number_input("Mức độ béo phì (1 - 7) :", min_value=1, max_value=7, value=None, step=1)

# Tạo đối tượng nhập mức độ hút thuốc (1 -  8)
cl12 = st.number_input("Mức độ hút thuốc (1 - 8) :", min_value=1, max_value=8, value=None, step=1)

# Tạo đối tượng nhập mức hút thuốc thụ động (1 -  8)
cl13 = st.number_input("Mức hút thuốc thụ động (1 - 8) :", min_value=1, max_value=8, value=None, step=1)

# Tạo đối tượng nhập mức độ đau ngực (1 -  9)
cl14 = st.number_input("Mức độ đau ngực (1 - 9) :", min_value=1, max_value=9, value=None, step=1)

# Tạo đối tượng nhập mức ho xuất huyết (1 -  9)
cl15 = st.number_input("Mức ho xuất huyết (1 - 9) :", min_value=1, max_value=9, value=None, step=1)

# Tạo đối tượng nhập mức độ mệt mõi (1 -  9)
cl16 = st.number_input("Mức độ mệt mõi (1 - 9) :", min_value=1, max_value=9, value=None, step=1)

# Tạo đối tượng nhập mức sụt giảm cân nặng (1 -  8)
cl17 = st.number_input("Mức sụt giảm cân nặng (1 - 8) :", min_value=1, max_value=8, value=None, step=1)

# Tạo đối tượng nhập mức độ khó thở (1 -  9)
cl18 = st.number_input("Mức độ khó thở (1 - 9) :", min_value=1, max_value=9, value=None, step=1)

# Tạo đối tượng nhập mức sổ mũi (1 -  8)
cl19 = st.number_input("Mức sổ mũi (1 - 8) :", min_value=1, max_value=8, value=None, step=1)

# Tạo đối tượng nhập mức khó nuốt (1 -  8)
cl20 = st.number_input("Mức khó nuốt (1 - 8) :", min_value=1, max_value=8, value=None, step=1)

# Tạo đối tượng nhập mức độ cắn móng tay (1 -  9)
cl21 = st.number_input("Mức độ cắn móng tay (1 - 9) :", min_value=1, max_value=9, value=None, step=1)

# Tạo đối tượng nhập mức độ cảm lạnh thường xuyên (1 -  7)
cl22 = st.number_input("Mức độ cảm lạnh thường xuyên (1 - 7) :", min_value=1, max_value=7, value=None, step=1)    

# Tạo đối tượng nhập mức độ ho (1 -  7)
cl23 = st.number_input("Mức độ ho (1 - 7) :", min_value=1, max_value=7, value=None, step=1)    

# Tạo đối tượng nhập mức độ ngáy khi ngủ (1 -  7)
cl24 = st.number_input("Mức độ ngáy khi ngủ (1 - 7) :", min_value=1, max_value=7, value=None, step=1)    

if st.button("HỖ TRỢ CHẨN ĐOÁN"):
    new_data = [[cl2, cl3, cl4, cl5, cl6, cl7, cl8, cl9, cl10, cl11, cl12, cl13, cl14, cl15, cl16, cl17, cl18, cl19, cl20, cl21, cl22, cl23, cl24]]
    st.write(models.predict(new_data)[0])
