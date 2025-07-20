# Müşteri Segmentasyonu Arayüzü

Bu arayüz, 2024 yılı lisans bitirme projem kapsamında geliştirilen Müşteri Segmentasyonu ve Öneri Sistemi çalışmasının görsel ve etkileşimli bir uzantısıdır.
Python programlama dili ve Streamlit kütüphanesi kullanılarak geliştirilen bu uygulama, kullanıcıya veri ön işleme, modelleme ve sonuç analizlerini kolayca gerçekleştirme imkânı sunar.

## Özellikler ve Dosya Yapısı

CSV formatındaki müşteri verileri indirildikten sonra bu arayüz üzerinden işlenip analiz edilebilir. Bazı analizlerde sistemden doğrudan veri çekilemediği durumlarda, analiz sonuçlarını desteklemek amacıyla ilgili görseller (örneğin .png formatında) manuel olarak yüklenmiştir.

Uygulamanın temel modülleri şunlardır:
- `anasayfa.py`:Ana çalışma ekranı ve yönlendirme arayüzü
- `data_cleaning.py`, `dp_end.py`:: Eksik veri temizleme ve ön işleme adımları
- `feature_engineering.py`: Özellik oluşturma ve dönüştürme işlemleri
- `modelling.py`: Kümeleme algoritmaları ve öneri sistemi
- `performance.py`: Model başarımları ve analizler

## Veri Kullanımı
Kullanıcılar arayüz üzerinden:

Kendi CSV dosyalarını yükleyebilir,
Sistem içinde hazır bulunan görsellerden yararlanabilir,
Tüm analiz adımlarını adım adım takip edebilir.

### 📷 Ekran Görüntüsü: Dosya Yükleme ve Küme Dağılımı

![Küme Dağılımı ve Dosya Yükleme Arayüzü](cluster_distribution.png)

---

## Kümeleme Sonuçları ve Performans

Bu proje kapsamında uygulanan **K-Means kümeleme algoritması**, farklı algoritmalarla yapılan karşılaştırmalar sonucunda en başarılı sonuçları vermiştir. Aşağıda, bu algoritmanın çıktılarına ait görsel ve değerlendirme metrikleri yer almaktadır:

![Kümeleme Sonuç Grafiği ve Performans Metrikleri](performance.png)

**🔍 Görsel Yorum:**  
Yukarıdaki grafik, verilerin **t-SNE** yöntemiyle iki boyuta indirgenerek görselleştirilmiş halini göstermektedir. Genel olarak kümeler birbirinden net şekilde ayrışmaktadır.  
Ancak bazı noktaların birbirine yakınlaştığı, hatta kısmen örtüştüğü görülebilir. Bu durum, **veri doğasında benzer özelliklere sahip müşteri gruplarının bulunmasından** veya **boyut indirgeme sırasında bazı ilişkilerin görselde farklı yansıtılmasından** kaynaklanabilir.  

Bu tür küçük örtüşmeler, gerçek dünyadaki karmaşık verilerin doğasında vardır ve **kümeleme başarısını olumsuz etkilemez**. Özellikle bu projede kullanılan metrikler, segmentasyonun başarılı ve anlamlı olduğunu göstermektedir.

---

### 📈 Değerlendirme Metrikleri

| Metrik                   | Değer       | Açıklama |
|--------------------------|-------------|----------|
| **Silhouette Score**     | `0.6657`     | Küme içi tutarlılık ve kümeler arası ayrım gücünü ölçer. 0.6 üzeri değerler başarılı segmentasyonu gösterir. |
| **Calinski-Harabasz**    | `2188.4509`  | Küme yoğunluğu ve ayrışma ölçütüdür. Yüksek değer daha iyi ayrımı temsil eder. |
| **Davies-Bouldin Score** | `0.4420`     | Küme benzerliğini ölçer. Düşük değer, iyi ayrışmış kümeleri ifade eder. |

Bu sonuçlar, K-Means algoritmasının proje verisi üzerinde yüksek doğrulukla çalıştığını ve kullanıcı segmentlerini etkili şekilde oluşturduğunu ortaya koymaktadır.


---

## Detaylı Açıklama
Bu arayüz, e-ticaret veri setlerinin işlenmesi ve anlamlı segmentlerin oluşturulması için tasarlanmıştır. Aynı zamanda öneri sistemiyle kullanıcıya özel içerikler sunulmasına olanak tanır.

👉 **Bu sürecin nasıl tasarlandığı ve kullanılan yöntemlerin detayları için:**  
[Proje Reposuna Git](https://github.com/elifkaradenizz/bitirme_projesi_ymu_2024)  
