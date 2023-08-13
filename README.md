# Data Nilai Kelulusan Siswa SMP Maju Jaya Yogyakarta

Aplikasi ini merupakan aplikasi sederhana python yang memuat tentang daftar data nilai kelulusan siswa di SMP Maju Jaya Yogyakarta

## Installation

To clone from github, run :

    mkdir folder
    cd folder
    git clone git@github.com:nornh/capstone_project.git

To install requirement with pip, run:

    pip install -r requirement.txt

## Quickstarts Guide

for Main Menu
1. SubMenu == Menampilkan Daftar Data Nilai Siswa               #Read option
    a. Jalankan fungsi main() di program utama. Hal ini akan menampilkan menu utama program.
    b. Pilih opsi "Menampilkan Daftar Data Nilai Siswa" dengan memasukkan angka menu yang sesuai. Misalnya, jika opsi tersebut adalah opsi pertama, Anda dapat memasukkan angka 1.
    c. Setelah memilih opsi, program akan memanggil fungsi ShowData(dbDataNilai) untuk menampilkan daftar data nilai siswa.
    d. Daftar data nilai siswa akan ditampilkan menggunakan fungsi print() dan tabulate.tabulate(). Anda akan melihat judul "Data Nilai Kelulusan SMP Maju Jaya Yogyakarta" diikuti oleh tabel yang berisi data nilai siswa.
    e. Setelah menampilkan daftar data nilai siswa, program akan kembali ke menu utama.

2. addData == Menambah Daftar Data Nilai Siswa                  #Create Option
    a. Jalankan fungsi main() di program utama. Ini akan menampilkan menu utama program.
    b. Pilih opsi "Menambah Daftar Data Nilai Siswa" dengan memasukkan angka menu yang sesuai. Misalnya, jika opsi tersebut adalah opsi kedua, Anda dapat memasukkan angka 2.
    c. Setelah memilih opsi, program akan memanggil fungsi AddData(dbDataNilai) untuk menambahkan data nilai siswa.
    d. Fungsi AddData(dbDataNilai) akan meminta pengguna memasukkan data nilai siswa yang baru. Ini bisa melibatkan penggunaan fungsi input() untuk mengambil input dari pengguna, atau menggunakan pendekatan lain seperti pyinputplus untuk memvalidasi input.
    e. Setelah menerima data nilai siswa yang baru, program akan menambahkannya ke basis data dbDataNilai.
    f. Setelah data berhasil ditambahkan, program akan memberikan pesan konfirmasi kepada pengguna.
    g. Setelah itu, program akan kembali ke menu utama.

3. ubahData == Mengubah Daftar Data Nilai Siswa                 #Update Option
    a. Jalankan fungsi main().
    b. Pilih opsi menu "Mengubah Daftar Data Nilai Siswa" dari menu utama.
    c. Program akan menampilkan daftar data nilai siswa yang ada.
    d. Pilih siswa yang ingin diubah datanya dengan memasukkan nomor induk siswa yang disediakan oleh program.
    e. Program akan menampilkan data siswa yang dipilih.
    f.Ubah data siswa sesuai dengan kebutuhan Anda, seperti nilai kkm, nilai ujian, dan sebagainya.
    g. Simpan perubahan yang telah Anda lakukan.
    i. Program akan menyimpan perubahan dan menampilkan daftar data nilai siswa yang telah diubah.
    j. Anda dapat kembali ke menu utama atau keluar dari program, tergantung pada pilihan yang disediakan.

4. delete == Menghapus Daftar Data Nilai Siswa                 #Delete Option
    a. Jalankan fungsi main().
    b. Pilih opsi menu "Menghapus Daftar Data Nilai Siswa" dari menu utama.
    c. Program akan menampilkan daftar data nilai siswa yang ada.
    d. Pilih siswa yang ingin dihapus dari daftar dengan memasukkan nomor identitas siswa atau pilihan lain yang disediakan oleh program.
    e. Program akan menampilkan data siswa yang dipilih.
    f. Konfirmasi bahwa Anda ingin menghapus data siswa dengan memasukkan input yang sesuai, seperti "ya" atau "tidak".
    g. Jika Anda mengkonfirmasi untuk menghapus data siswa, program akan menghapus data tersebut dari daftar.
    i. Program akan menampilkan pesan konfirmasi bahwa data siswa telah dihapus.
    h. Anda dapat kembali ke menu utama atau keluar dari program, tergantung pada pilihan yang disediakan.

5. exit
    a. Jalankan fungsi main().
    b. Pilih opsi menu "Exit" dari menu utama.
    c. Program akan menampilkan pesan konfirmasi bahwa Anda akan keluar dari program.
    d. Konfirmasi bahwa Anda ingin keluar dari program dengan memasukkan input yang sesuai, seperti "ya" atau "tidak".
    e.Jika Anda mengkonfirmasi untuk keluar dari program, program akan berakhir dan menutup.
    f. Jika Anda memilih opsi "tidak", program akan kembali ke menu utama, dan Anda dapat memilih opsi menu lainnya atau keluar nanti.

## Contribute

Jika anda ingin berkontribusi ke dalam aplikasi Data Nilai Kelulusan Siswa SMP Maju Jaya, silahkan check: https://github.com/nornh/capstone_project

