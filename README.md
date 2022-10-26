# P1_Komnum_E6

# Kelompok 6
Nama Kelompok :
- Muhammad Adib Syambudi (5025211017)
- Ilham Insan Wafi (5025211255)
- Yusna Millaturrosyidah (5025211254)

Dengan menggunakan dua library dari phython yaitu numpy dan matplotlib.
Variabel yang digunakan a,b,c,d untuk variabel pada fungsi. Kemudian xl adalah input batas bawah dan xu adalah input batas atas.
Terdapat juga variabel error dan toleransi, dimana kedua variabel ini digunakan sebagai acuan berjalan iterasi.
Kemudian menyimpan titik-titik x pada xlist dan hasil perhitungan fungsi x ke dalam ylist. 

Kemudian langkah-langkah algoritma bolzano sebagai berikut :
1. Mengecek fungsi dengan batas bawah dikali dengan batas atas. Jika hasilnya positif maka hasil terdapat pada rentang yang dimasukkan,
2. Perulangan proses selama memiliki nilai error diatas nilai toleransi.
3. Menggunakan rumus xr = (xl + xu )/2
4. Mencetak nilai dari xr.
5. Mengubah nilai error dengan rumus nilai mutlak dari ((xr - xr_lama)/xr) * 100
6. Jika hasil dimasukkan ke fungsi dikali dengan batas atas bernilai negatif, maka xr menjadi batas bawah. Selain itu, maka xr menjadi batas atas.
7. Proses yang diulang adalah NO 3 sampe 6.
8. Menggambar grafik dengan menggunakan plot dengan memasukkan xlist dan ylist.
9. Menggeser garis sumbu x ke tengah dan memberi judul.
10. Menampilkan grafik fungsi

![test](https://user-images.githubusercontent.com/91377793/198072182-d6491cf2-d054-421b-b1d3-35b28b233006.jpeg)
