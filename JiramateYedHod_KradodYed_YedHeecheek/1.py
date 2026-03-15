import numpy as np

# 1. สร้างช่วง x (ใช้ 0 แทน -infinity ตามโจทย์ถือว่ายอมรับได้เพราะค่าเข้าใกล้ 0 มากๆ)
x = np.linspace(0, 45, 100000)

# 2. แก้ไขสมการความน่าจะเป็น (ใส่ np.sqrt ตรง 2*pi)
# mu = 50, sigma = 4
px = (1 / (4 * np.sqrt(2 * np.pi))) * np.exp(-((x - 45)**2) / (2 * (4**2)))

answer = []
# 3. ดึงค่า h มาแค่ค่าเดียว เพราะระยะห่างเท่ากันหมด
h = x[1] - x[0] 

# 4. วนลูปเริ่มที่ index 1 เพื่อไม่ให้ px[i-1] ดึงค่าผิด
for i in range(1, len(px)):
    answer.append(px[i] + px[i-1])

# คำนวณพื้นที่สี่เหลี่ยมคางหมู
print("Probability P(x < 45):", (h/2) * sum(answer))
