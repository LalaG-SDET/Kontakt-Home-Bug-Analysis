# 🛒 Kontakt Home - Price Filter Logic Bug Analysis

### 📋 Project Overview
Bu layihə "Kontakt Home" e-ticarət platformasında tapılmış kritik bir məntiq xətasının (Business Logic Error) analizi və sənədləşdirilməsindən ibarətdir.

### 🕵️‍♂️ Bug Description
**Issue:** Qiymət filtrində minimum məbləğin maksimumdan böyük daxil edilməsi zamanı sistemin heç bir xəbərdarlıq verməməsi.

**Steps to Reproduce:**
1. Kontakt.az saytına daxil ol.
2. Hər hansı bir kateqoriyanı (məs: Telefonlar) seç.
3. Filtr hissəsində "Min" xanasına `50000`, "Max" xanasına `700` yaz.
4. "Göstər" və ya tətbiq et düyməsinə bas.

**Expected Result:**
Sistem daxil edilən rəqəmlərin məntiqsiz olduğunu anlamalı, istifadəçiyə xəta mesajı verməli və düyməni aktiv etməməlidir.

**Actual Result:**
Sistem məlumatı qəbul edir və nəticədə boş bir səhifə (və ya yanlış filtrasiya) göstərilir.

### 🛡️ Suggested Solution (QA & BA Perspective)
- **Front-end:** "Min > Max" halında düymə `disabled` (qeyri-aktiv) olmalıdır.
- **Back-end:** API tərəfində daxil olan datanın validasiyası (sanitizing) təmin edilməlidir.

---
*Status: Reported & Added to Regression Checklist*