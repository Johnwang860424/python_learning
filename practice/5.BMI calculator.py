# BMI計算機
# 取得使用者的身高(cm:float)跟體重(kg:float)
cm = float(input("請輸入您的身高:"))
kg = float(input("請輸入您的體重:"))

m = cm /100
# bmi = kg / m**2
bmi = kg / m**2
bmi = round(bmi, 1)

# 肥胖,過重,正常,過輕
level = ""
if bmi >= 30:
    level = "肥胖"
elif bmi >= 25:
    level = "過重"
elif bmi >= 18.5:
    level = "正常"
else:
    # else 上述條件都不符合時
    level = "過輕"

# 回傳使用者一份報告
report = f"身高: {cm} cm 體重: {kg} kg BMI:{bmi} {level}"
print(report)