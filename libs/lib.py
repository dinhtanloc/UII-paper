from translate import Translator
import pandas as pd
from pandas_profiling import ProfileReport



def translate_vietnamese_to_english(text):
    translator = Translator(to_lang="en", from_lang="vi")
    translation = translator.translate(text)
    return translation

def write_data_info(data, path, cols):
    for i in range(0, len(data.columns), cols):
        cols_slice = data.iloc[:, i:i+cols]
        info_string = cols_slice.info()
        print('--------------------------------------------------------\n')
    print('That is all')


# Đọc dữ liệu từ file Excel
def eda_part(df):
    # Số lượng cột trong mỗi phần
    cols_per_section = 40

    # Số lượng phần dữ liệu
    num_sections = df.shape[1] // cols_per_section + 1

    # Chia dữ liệu thành các phần nhỏ và thực hiện EDA
    for i in range(num_sections):
        start_col = i * cols_per_section
        end_col = (i + 1) * cols_per_section
        section_df = df.iloc[:, start_col:end_col]
        
        # Thực hiện EDA cho phần dữ liệu
        profile = ProfileReport(section_df, title=f"EDA Report - Part {i+1}", explorative=True)
        
        # Lưu báo cáo
        profile.to_file(f"html/part_{i+1}_report.html")


import pandas as pd
import statsmodels.api as sm

def stata(data):
    # Tạo DataFrame từ dữ liệu
    data = {
        'X': [1, 2, 3, 4, 5],
        'Y': [2, 3, 5, 4, 6],
    }
    df = pd.DataFrame(data)

    # Thêm cột hằng 1 vào DataFrame để tính intercept trong mô hình
    df['intercept'] = 1

    # Phân tích hồi quy tuyến tính
    model = sm.OLS(df['Y'], df[['X', 'intercept']])
    results = model.fit()

    # Tạo bảng thống kê tuyến tính
    summary = results.summary()
    print(summary)
    return summary
