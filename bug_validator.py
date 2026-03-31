# ==========================================
# KONTAKT HOME - LOGIC VALIDATOR SCRIPT
# ==========================================

def validate_filter(min_price, max_price):
    """
    Qiymət filtrinin məntiqini yoxlayan sadə funksiya.
    """
    print(f"Yoxlanılan dəyərlər: Min={min_price}, Max={max_price}")
    
    if min_price > max_price:
        return "❌ NƏTİCƏ: BUG TAPILDI! Minimum qiymət maksimumdan böyük ola bilməz."
    else:
        return "✅ NƏTİCƏ: Məntiq düzgündür."

# Tapdığımız real xətanın simulyasiyası
test_result = validate_filter(50000, 700)
print(test_result)