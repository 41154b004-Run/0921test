def calculate_bmi(height_cm: float, weight_kg: float) -> float:
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)

def get_bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "體重過輕 (Underweight)"
    elif bmi < 24.0:
        return "健康體位 (Normal)"
    elif bmi < 27.0:
        return "體重過重 (Overweight)"
    else:
        return "肥胖 (Obese)"

def main():
    print("=== BMI 計算器 ===")
    try:
        height = float(input("請輸入身高 (公分 cm): "))
        weight = float(input("請輸入體重 (公斤 kg): "))
        if height <= 0 or weight <= 0:
            print("身高與體重必須大於 0！")
            return
        bmi = calculate_bmi(height, weight)
        category = get_bmi_category(bmi)
        print(f"\n您的 BMI 為: {bmi:.2f}")
        print(f"健康評估: {category}")
    except ValueError:
        print("輸入錯誤，請輸入有效的數值！")

if __name__ == "__main__":
    main()
