## Insertion Sort Algoirtma Ödevi

### Proje 1

[22,27,16,2,18,6] -> Insertion Sort

Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.
Big-O gösterimini yazınız.
Time Complexity: Average case: Aradığımız sayının ortada olması,Worst case: Aradığımız sayının sonda olması, Best case: Aradığımız sayının dizinin en başında olması.
Dizi sıralandıktan sonra 18 sayısı hangi case kapsamına girer? Yazınız.

1. Soru
 (22,27,16,2,18,6) -> (16,22,27,2,18,6) -> (2,16,22,27,18,6) -> (2,16,18,22,27,6) -> (2,6,16,18,22,27)

2. Soru
 O(n^2)'dir.

3. Soru

Worst Case: 1'den N'e kadar tüm verilerin dolaşılması gerekir n(n+1)/2 -> n^2+n olur BigO notasyonunda değer olarak O(n**2) değer alır.

Avarage Case: Veri dizisi kısmen karışık durumdadır. Big O Notation O(n^2) olur.

Best Case: Veri dizisi sıralı haldedir ve dizi sadece n kadar kontrol edilir bu durumda da BigO notasyonunda değer olarak O(n) alır.

4. Soru
 (3,7,5,8,2,9,4,15,6) -> (3,5,7,8,2,9,4,15,6) -> (3,5,7,8,2,9,4,15,6) -> (2,3,5,7,8,9,4,15,6) -> (2,3,5,7,8,9,4,15,6) -> (2,3,4,5,7,8,9,15,6) -> (2,3,4,5,7,8,9,15,6)