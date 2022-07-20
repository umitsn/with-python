HEIC formatındaki görüntüleri istenilen kalitede JPEG formatına çevirir.

**python heicToJpeg.py -q 100**\
şeklinde kullanılır. 100 seçilirse kayıpsız, büyük dosya boyutlu JPEG dosyaları oluşur.\
Direkt **python heicToJpeg.py** şeklinde de kullanılabilir. Bu durumda varsayılan kalite değeri 80 olarak kabul edilir.\
Orijinal HEIC uzantılı dosyayı JPEG formatına dönüştürme işlemi bittiğinde HEIC diye oluşturulan klasör içine taşır.\
Oluşturulan JPEG formatlı dosyanın adı orijinal HEIC formatlı dosyanın adına seçilen kalite değeri eklenerek belirlenir.\
**Örnek:**
- giren dosya : img.HEIC
- seçilen kalite : 80
- kaydedilen dosya : img_q80.jpg 
