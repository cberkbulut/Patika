"import numpy as np

#Numpy Array

#tek tip veri içerebilir.
#list lerden farkı budur.

x= np.array([1,2,3,4])

y= np.array([1,2,3,4,5.4]) 

#hepsini float tipine dönüştürür, sebebi daha genel bir ifade olması.

#içinde float, integer ve string varsa hepsini string tipine dönüştürür.



#Array Data tipini manuel vermek;

x = np.array([1,2,3,4.6], dtype= ""int32"")

#şeklinde int şeklinde alabiliriz.

#dtype= ""str"" string için



#Elemanları Sıfırdan oluşan Array oluşturmak;


np.zeros(10) 
#10 tane elemanı olan elemanları 0 olan float tipinde bir array oluşturuyor.

np.zeros(10, dtype = str)
#şeklinde tipini de ayarlayabiliriz.


#3 satır 4 sütunu olan array yaratmak için;

np.zeros((3,4))


np.zeros([3,4])

#ille de tuple formatında olması gerekmiyor list formatıda uygulanabilir.

np.zeros([3,8,8])

#şeklinde 3 boyutlu şekilde de yapılabilir.



#NP FULL;

np.full((4,5),5)

#4 satır 5 sütunluk 5 ile doldur bütün satır ve sütunları



np.arange(0,12)
#0 ile 11 dahil olacak şekilde oluşturur.

np.arange(2,12,2)
#2 den 12 ye 2 şerli git diyor.

np.arange(12,2,-2)
#12 den 2 ye 2 şer azaltarak gidiyor 2 yi dahil etmiyor 4 te bitiyor.



np.linspace(1,2) 

#default olarak 1 ve 2 dahil oalcak şekilde 50 noktaya bölüyor.

np.linspace(1,2, num=3)

#1 ve 2 de dahil toplam 3 e böl diyince 1 1.5,2 şeklinde ayırıyor.




np.random.normal(0,1, (4,,5))

#ortalama 0, st.sapma 1 , 4 satır 5 sütunluk oluşturuyor random normal sayıları.




np.random.randint(1,10,(3,4))

#1 den 9a kadar 9 dahil random şekilde 3 satır 4 sütunluk değerler geliyor.




d={}

for _ in range(20000):






#aşağı yukarı aynı değerler de çıkması gerektiğini düşünüyorduk üstteki randint
#fonksiyonu uniform dağılıma sahip oldugu icin bunu kontrol etmek için yapılmış bir döngü.



np.eye(3,3) 

#3e3 lük bir birim matris oluşturur.



x= np.array([1,2,3])
y= np.array([2,4,8])

#x*y yapıldığında aynı eleman sayısı olması gerekiyor ,

#iki kümenin sırayla 1. elemanlarını, 2.elemanlarını şeklinde son elemana kadar  çarpıyor.

#x+y ve x-y işlemlerindede aynı şekilde işlemi yapıyor ve o sıraya yazıyor.



x= np.zeros((2,3))

#2ye 3 lük boş matris oluşturduk.

y = np.zeros((2,5,4))

#2 tane 5 e 4 lük matris oluşturduk.


x.size 
#kaç elemanlı oldugunu gosteriyor.


x.ndim
#kaç boyutlu oldugunu söylüyor. ( y nin 3 x in 2 )


x.dtype 
#veri tipini veriyor.


#RESHAPE


a = np.arange(1,11)

a.reshape(2,5)

#a yı 2 ye 5 lik şekilde ifade et.

#a.reshape(-1,2) yaparsak hiç bir zaman hata vermeden arkaplanda 5 olması gerektiğini

#10 eleman oldugu için 5 2 şeklinde olması gerektiğini hesaplayıp o şekilde çıktı verir.


a[np.newaxis,:] 

#şeklinde bütün elemanları alacak şekilde satır sütuna çevirir.
#1 satır 10 sütun şekline döndürür.


a[:,np.newaxis] 
# 10 satır 1 sütun şeklinde döndürür.



#CONCATENATION


a = np.array([1,2,3,4])

b = np.array([5,6,7,8])

l = [10,11]

np.concatenate([a,b,l])

#şeklinde birleştirebiliriz. Liste ile arrayleri de birleştirebiliyoruz.




a = np.array([1,2,3,4])

b = np.array([5,6,7,8])

#raw mantıgında birleştirmek istiyoruz.

np.stack([a,b]) 
#axis= 0 olarak default u birleştirme yapar.

np.stack([a,b],axis = 1) 
#şeklinde sütunsal olarak birleştiriyor.




#SPLITTING

l = [10,20,30,40,50,60,70,80]

np.split(l,[2,6])

#2. indeksin başına (30 un) çentik at ve  6. indeksin önüne bir çentik at (70 in önüne)

#dedigimizde [10,20]  [30,40,50,60], [70,80] array olarak döndürür.



#hsplit sütunsal olarak bölüyor.

#vsplit satırsal olarak bölüyor

np.hsiplit(l,[2]) 
#şeklinde yapılabilir.





#SORTING


#a.sort()  ile a = np.sort(a) ile aynı işlemi yapar.

idxs = np.argsort(a) 

#argsort sıralamayı yapar ancak o sıralamadaki sayıların indeks değerlerini döndürür.




a = np.arange(1,21).reshape(4,5)

#4 satır 5 sütunluk 1 20 arası sayıları oluşturduk.


a[0][0]
#1 değerini getirir.

a[1][1] 
#7 yi veriyor.

a[0:3] 
#0 1 ve 2 yi yani ilk 3 satırdaki verileri getiriyor.


a[:,3]
#bütün satırlardaki 3.sütun değerlerini döndür




#FANCY INDEXING

x = np.arange(1,15)

#1 den 14 e kadar sayıları döndürdük.

idxs=[4,5,7,11]

#4 5 7 11 deki elemanları ayırmak istiyoruz.

x[idxs] 
#şeklinde yaparak bu değerleri döndürebiliyoruz.



a = np.arange(12).reshape(3,4)


a[0,[1,3]]

#satırlarda 0. satır sütunlarda ise 1. ve 3. sütundaki değerleri getir.



np.arange(20).reshape(4,5)



idx1= [1,3,2]
idx2= [3,0,2]

a[idx1,idx2]

#1. indeksteki satır ile 3.indeksteki sütun değerini kesiştirip ver
#3. indeksteki satır ile 0.indeksteki sütun değerini kesiştirip ver
#2. indeksteki satır ile 2.indeksteki sütun değerini kesiştirip ver

#8 15 12 çıktısını veriyor.

a [1,2,5] = [100,200,300] 
#şeklinde o indeksteki değerleri değiştirebiliriz.


a=
[1 2 3 4
5 6 7 8
9 10 11 12]

b=a[1,(1,3)] çıktısının boyutu nedir?

#1. indeksi satır bazlı seçer yani 5 6 7 8 i seçti
#buradan da 1. ve 3. sütundaki değerleri alır yani 6 ve 8 i alır
#bunu da sayı obegi olarak kaydettigi için 1 boyutlu olur.



a= np.arange(1,21).reshape(4,5)

b = a[:2,:3]
#en baştan başla 2.indekse kadar al sütun olarak da 3. indekse kadar al dahil etmeden ikisnide.

#iki dimension verdigimiz icin cıktı da 2 boyutlu oldu.

b[0,0] = 100 
#olarak değiştirdik.

#bu şekilde yapınca a da da güncelleme yapıyor.

#bunu engellemek için ;

b = a[:2,:3].copy() 
#şeklinde yazarsak a daki değeri değiştirmemiş oluruz.


#CONDITIONAL INDEXING


a = np.arange(1,10)

a[a<5] 
#a nın içinde bu koşulu sağlayan True değeri verenleri döndürür.


filt= a<3

a[filt] 
#şeklinde değişkene atayarakta yapılabilir.


b = np.array([2,3,3,4,5,61,7,8,11])

a[a==b] 
#eşit olan değerlerini getirir.


#numpy da işlem yaparken or şeklinde yazarak bu kosulu yazamıyoruz
# | işareti ile yapmamız gerekiyor.

a[(a<3) | (a>5)] 
#şeklinde 3 ten kücük ya da 5 ten büyük şeklinde bir koşul sağlayanları getirebiliriz.

#önermenin değilini almak için de ~ işareti ile alınıyor.

#SUM


np.sum(a,axis=0)

#sütun bazında toplama yapıyor.


#NP ALL

#herhangi bir tanesi false ise false döndürür.

np.all(a>8,axis=1) hangi çıktıyı verir?

a=
[1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20]

#array([False,False, True , True]) çıktısını verir.

#çünkü satır bazlı olarak değerlendiriyor. Bir satırda bir tane false varsa false döndürüyor.



#NP ANY

#herhangi bir tanesi true ise true döndürür.


a =
[1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20]

np.any(a>4, axis=0) 
#hangi çıktıyı verir?

#array([True, True,True,True,True]) döndürür. Çünkü sütun bazlı olarak bakıyor ve bir tane true çıkarsa true çıkartıyor.

"
