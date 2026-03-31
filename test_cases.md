# 📋 Kontakt Home - Test Cases Analysis

| ID | Ssenari Adı | Test Addımları | Gözlənilən Nəticə | Status |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Düzgün Qiymət Aralığı | Min: 100, Max: 500 daxil et | Məhsullar 100-500 AZN arası düzgün filtrlənməlidir. | ✅ PASSED |
| **TC-02** | Məntiqsiz Aralıq (Bug) | Min: 50000, Max: 700 daxil et | Sistem xəta verməli və düyməni bloklamalıdır. | ❌ FAILED |
| **TC-03** | Mənfi Qiymət Girişi | Min: -10 daxil et | Sistem mənfi rəqəmi qəbul etməməlidir. | ❌ FAILED |
| **TC-04** | Boş Buraxılan Xanalar | Heç bir rəqəm yazmadan filtrlə | Sistem bütün məhsulları göstərməyə davam etməlidir. | ✅ PASSED |