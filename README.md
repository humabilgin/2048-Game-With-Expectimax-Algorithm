# 2048-Game-With-Expectimax-Algorithm

KONU : Expectimax Algortiması ile 2048 Botu Yazma

**Expectimax Algoritması Nasıl Çalışır**

Öncelikle Minimax Algoritmasını inceleyelim. Bu algoritma, yapılacak hamle karşısında yapılabilecek bize en zararlı olan hamlenin seçileceği düşünülerek karar verir. Örneğin aşağıdaki örnekte, sağdaki subtreede rakip bizim 100 değil 9 puan kazanmamızı isteyecek ve 9 puan kazanacağımız eli oynayacaktır. Soldaki hamlemizde ise rakip bize 10 puan kazandıracaktır. Bu yüzden soldaki hamlenin yapılması daha mantıklıdır.
![minimaxdrawing](https://user-images.githubusercontent.com/46404802/127633051-8c090bfd-0c4c-4ee6-8d95-519b20c3fb4e.jpg)

Minimax Algoritmasının bir türü olan Expectimax Algoritması, klasik Minimax Algoritmasının aksine hamlelerin optimal geldiğini kabul ederek hesaplama yapmaz. Minimalize edilmesi beklenen hamleler şansa dayalı geldiği durumda direk minimalize etmek her zaman doğru sonuca götürmeyecektir. Bu sebeple minimalize etmek yerine subtreelerin ortalaması alınarak maximumu seçilecek değerler belirlenir. Böylece en çok fayda sağlayabilecek altdala doğru devam edilmiş olur. Expectimax Algoritmasında ortalama alındığı için altdallardaki değerlerin büyüklüğü önemli rol oynar.

![expectimaxdrawing](https://user-images.githubusercontent.com/46404802/127633134-c9c05909-c91c-4f13-8176-1ff2479cbaab.jpg)

Minimax Algoritmasında üç temel fonksiyon kullanılır. Bunlar:

- Değerlendirme Fonksiyonu
- Maximize Fonksiyonu
- Minimize Fonksiyonu

Olmaktadırlar.

Expectimax Algoritmasında ise şu üç temel fonksiyon rol almaktadır:

- Değerlendirme Fonksiyonu
- Maximize Fonksiyonu
- Chance Fonksiyonu

Burada görebileceğimiz gibi minimize eden fonksiyon yerine şansa bağlı seçim yapan fonksiyon gelmiştir.

**2048 Oyunu Nedir?**

2048 oyunu, 2&#39;nin katlarını bir matris üzerinde birleştirip toplayarak 2048&#39;e ulaşmaya çalışılan bir bulmaca oyunudur. 2048&#39;e ulaştıktan sonra da oyuna devam edilebilmektedir. Her elde 2 veya 4 sayıları matrisin boş bir noktasında random olarak oluşmaktadır. 2 oluşma ihtimali 4 oluşma ihtimalinde daha yüksektir. Matrisin tüm kareleri dolduysa ve yapılacak hamle kalmadıysa oyun bitmektedir.

**Expectimax Algoritması İle 2048 Oyunu**

2048 oyununda rastgele gelen 2 veya 4 rakamları tamamen random gelmektedir. Bu randomluk Minimax Algoritmasındansa Expectimax Algoritmasının kullanılmasını daha avantajlı hale getirmektedir.

Yukarıda da belirtildiği gibi Değerlendirme Fonksiyonu, Maximize Fonksiyonu, Chance Fonksiyonu olmak üzere üç temel fonksiyon kullanılmaktadır. Kodları inceleyelim:

![](RackMultipart20210730-4-sfw40p_html_d0129250aee71f7c.png)

NOT:Kodun GUI kısmı - oyunun kendisi [https://github.com/yangshun/2048-python](https://github.com/yangshun/2048-python) tarafından alınmıştır. Bu GUI üzerinde algoritma uygulanmıştır. Bunlar da game\_board.py, main\_cli.py, main\_gui.py dosyaları olmaktadır. Algoritma kodu expectimax.py dosyasında bulunmaktadır.

NOT:PowerShell&#39;e &quot; **python main\_cli.py**&quot; yazılarak output alınabilir.

**Kullanılan Kaynaklar**

[https://www.geeksforgeeks.org/expectimax-algorithm-in-game-theory/](https://www.geeksforgeeks.org/expectimax-algorithm-in-game-theory/)

[https://github.com/yangshun/2048-python](https://github.com/yangshun/2048-python)

https://www.youtube.com/watch?v=EPO9zjbCAz4

**Youtube Video Linki**

https://youtu.be/2bFgYVpkhFY
