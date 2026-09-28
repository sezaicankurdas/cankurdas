# Kişisel CloudStream deposu

Bu proje, [feroxx/Kekik-cloudstream](https://github.com/feroxx/Kekik-cloudstream) projesinin `b050ee8` sürümündeki dört sağlayıcıyı temel alır. Kaynak kod GPL-3.0 lisanslıdır; telif ve yazar bildirimleri korunmuştur.

| Kaynak | Durum | Başlangıç adresi |
| --- | --- | --- |
| DiziPalOriginal | Kaynak kodu var; bu pakette cihaz testi yapılmadı | https://dizipal-orgnl.com |
| HDFilmCehennemi | Kaynak kodu var; bu pakette cihaz testi yapılmadı | https://www.hdfilmcehennemi.nl |
| DiziYou | Kaynak kodu var; bu pakette cihaz testi yapılmadı | https://www.diziyou.one |
| FilmMakinesi | Kaynak kodu var; bu pakette cihaz testi yapılmadı | https://filmmakinesi.to |
| HDFilmIzle | Adres kaydedildi; sağlayıcı henüz yazılmadı | https://www.hdfilmizle.live |

## Kurulum

1. GitHub'daki **herkese açık** ve boş `sezaicankurdas/cankurdas` deposunu aç.
2. Bu klasörün **içindeki** dosya ve klasörleri depoya yükle. `CloudStream_Kisisel_Depo` klasörünü bir üst dizin olarak yükleme. `.github` klasörü de kök dizinde olmalı. Adresler zaten senin depom için ayarlı.
3. Depo ayarlarında **Actions > General > Workflow permissions** altında `Read and write permissions` seç. İlk `Build CloudStream extensions` çalışmasının bitmesini bekle; `builds` dalında `repo.json`, `plugins.json` ve dört `.cs3` dosyası oluşmalı.
4. CloudStream uygulamasında **Ayarlar > Eklentiler > Depo ekle** ekranına `https://raw.githubusercontent.com/sezaicankurdas/cankurdas/builds/repo.json` adresini gir. Ardından dört eklentiyi yükle.

## Adres değiştiğinde

`domains.json` içindeki ilgili alan adını **doğruladığın yeni adresle** değiştir. Ardından `python scripts/sync_domains.py` çalıştır. Bu komut Kotlin'deki başlangıç adresini günceller ve o eklentinin sürümünü bir artırır. Değişen dosyaları GitHub'a gönderince iş akışı derleyip aynı depo adresindeki eklentiyi günceller. CloudStream'de eklenti güncellemesini kontrol et.

Örnek: `dizipal-orgnl.com` güncel adresi değişirse sadece `DiziPalOriginal` girdisini değiştir. Sıradaki sayıdan adres tahmin etme; farklı bir site veya sahte kopya olabilir.

Bu **otomatik alan adı keşfi değildir**. Alan adı değişiminde onaylı adresi senin girmen gerekir. Sitenin HTML, API veya oynatıcı yapısı değişirse ayrıca sağlayıcı kodu düzeltilmelidir. DiziPalOriginal kodunun yeni `dizipal-orgnl.com` ile uyumu henüz doğrulanmamıştır.

`HDFilmIzle` yalnızca takip listesindedir ve derlemeye dahil değildir. Site inceleme aracına yanıt vermediği için çalışan bir sağlayıcıyı doğrulamadan eklemedim.

## Geliştirme

JDK 17, Android SDK ve Gradle gerekir. `./gradlew make makePluginsJson` ile yerel derleme yapılır. Her sağlayıcı kendi klasöründedir. Bir siteye erişim veya oynatma yetkisi olduğundan emin ol.

Bu paket kişisel kullanım için hazırlanan kaynak kodudur. Site erişimi, oynatma ve cihaz üstünde yükleme henüz doğrulanmadı.
