import pandas as pd
import random
import matplotlib.pyplot as plt
from collections import Counter

# อ่านข้อมูลจากไฟล์ CSV
data = pd.read_csv('lottery_results.csv')

# แปลงคอลัมน์ winning_numbers เป็น list ของตัวเลข
data['winning_numbers'] = data['winning_numbers'].apply(lambda x: x.split(', '))

# ฟังก์ชันในการนับความถี่ของตัวเลข
def count_frequencies(numbers):
    all_numbers = [number for sublist in numbers for number in sublist]
    return Counter(all_numbers)

# นับความถี่ของตัวเลขที่ออก
number_counts = count_frequencies(data['winning_numbers'])

# แปลงข้อมูลเป็น DataFrame
frequency_df = pd.DataFrame(list(number_counts.items()), columns=['Number', 'Frequency'])

# จัดเรียงข้อมูลตามความถี่
frequency_df = frequency_df.sort_values(by='Frequency', ascending=False)

# แสดงผลลัพธ์ความถี่ของตัวเลขที่ถูกหวย
print(frequency_df)

# แสดงผลกราฟ
plt.figure(figsize=(10, 6))
plt.bar(frequency_df['Number'], frequency_df['Frequency'])
plt.xlabel('หมายเลข')
plt.ylabel('ความถี่')
plt.title('ความถี่ของหมายเลขที่ถูกหวย')
plt.xticks(rotation=90)
plt.show()

# ฟังก์ชันในการทำนายผลลัพธ์ในงวดถัดไป
def predict_next_draw(frequency_df, top_n=10, select_n=6):
    # เลือกตัวเลขจาก top_n ตัวเลขที่มีความถี่สูงสุด
    top_numbers = frequency_df.head(top_n)['Number'].tolist()
    # สุ่มเลือก select_n ตัวเลขจากตัวเลขที่มีความถี่สูงสุด
    return random.sample(top_numbers, select_n)

# ทำนายหมายเลขที่จะออกในงวดถัดไป
predicted_numbers = predict_next_draw(frequency_df)

print(f"หมายเลขที่คาดว่าจะออกในงวดถัดไป: {predicted_numbers}")
