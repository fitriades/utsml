![image](https://github.com/fitriades/utsml/assets/149255008/bcac5d35-2693-43bf-b692-e475d5c40eb2)# Laporan Proyek Machine Learning
### Nama : Fitria Desiyani
### Nim : 211351057
### Kelas : Pagi B

## Domain Proyek

Pengidap penyakit hepatitis sejatinya beresiko untuk meninggal dunia dan survive. Pada project ini pengidap hepatitis bisa melakukan perhitungan apakah beresiko untuk meninggal dunia atau punya kesempatan untuk survive.

## Business Understanding

Data menunjukan untuk gejala dan penyakit hepatitis berdasarkan beberapa pertanyaan baik itu gender sspesifik dan pengaruh pengobatan lainya dapat menjadikan penyakit itu memiliki resiko kematian. Maka dari itu, dengan algoritma svm linear saya coba klasifikasikan apakah penyakit hepatitis yang di derita si pasien beresiko menyebabkan kematian atau tidak.

Bagian laporan ini mencakup:

### Problem Statements

- Resiko kematian pasien penyakit hepatitis

 
### Goals

- Meningkatkan kewaspadaan terhadap resiko kematian penyakit hepatitis
- Sebagai early warning untuk para pengidap penyakit hepatitis

    ### Solution statements
    - Dilakukanya proses klasifikasi untuk pengidap penyakit hepatitis
    - Menggunakan algoritma svm linear untuk proses klasifikasi

## Data Understanding
Data di dapatkan dari kaggle dengan dataset tentang penyakit hepatitis dan resiko kematian nya.

[Hepatitis Data](https://www.kaggle.com/datasets/codebreaker619/hepatitis-data/).


### Variabel-variabel pada Hepatitis Data Dataset adalah sebagai berikut:
- age = usia dari si pengidap hepatitis, bertipe integer
- sex = jenis kelamin si pengidap hepatitis, bertipe boolean
- steroid = apakah si pasien sedang mengkonsumsi steroid, bertipe boolean
- antivirals = apakah si pasien sedang mengkonsumsi obat yang bersifat antivirus, bertipe boolean
- fatigue = apakah si pasien sering mengalami kelelahan, bertipe boolean
- malaise = apakah si pasien juga mengidap malaise, bertipe boolean
- anorexia = apakah si pasien juga mengidap anorexia, bertipe boolean
- liver_big = apakah si pasien mengalami pembengkakan pada liver, bertipe boolean
- liver_firm = apakash si pasien mengalami pengerasan pada liver, bertipe boolean
- spleen_palpable = apakah si dapat merasakan limpanya secara jelas, bertipe boolean
- spiders = apakah si pasien mengalami spider nevus, bertipe boolean
- ascites = apakah si pasien mengalami ascites, bertipe boolean
- varices = apakah si pasien memiliki varises, bertipe boolean
- bilirubin = jumlah kadar bilirubin si pasien, bertipe float
- alk_phosphate = kandungan alkalin dalah darah si pasien, bertipe float
- sgot = kandungan Serum Glutamic Oxaloacetic Transaminase si pasien, bertipe float
- albumin = tingkat albumin dalam tubuh si pasien, bertipe float
- protime = Jumlah waktu untuk Prothrombin time dalam tubuh si pasien, bertipe float
- histology = histology liver si pasien, bertipe boolean

## Data Preparation
Pertama kita import dulu library yang dibutuhkan
```bash
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
```
selanjutnya kita buka dataset nya
```bash
df =  pd.read_csv('hepatitis-data/hepatitis_csv.csv')
```
kita bisa mengetahui informasi dari dataset kita seperti jumlah entri, kolom, dan tipe data dari dataset kita dengan perintah
```bash
df.info()
```
Karena data yang bisa di terima adalah dalam bentuk integer, maka kita ubah terlebih dahulu semua data yang bukan integer ke integer
```bash
cat_cols = df.select_dtypes(include = ['object', 'bool']).columns.to_list()
cat_cols
```
```bash
from sklearn.preprocessing import LabelEncoder
```
```bash
le = LabelEncoder()

for i in cat_cols:
    le.fit(df[i])
    df[i] = le.transform(df[i])
```
Maka data akan di ubah menjadi integer, selanjutnya kita cek apakah data tersebut memiliki kolom yang kosong
```bash
df.isna().sum()
```
Jika hasil menujukan data yang kosong kita bisa lanjutkan dengan
```bash
df.fillna(df.mode(), inplace = True)
```
atau kita bisa isikan data yang kosong secara otomatis
```bash
df.fillna(df.mean(), inplace = True)
```
Selanjut nya kita bisa visualiasikan data tersebut
```bash
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
```
```bash
plt.figure(figsize=(20, 10))
sns.displot(df.age, bins=40)
```
![visual](https://github.com/fitriades/utsml/assets/149255008/98068017-9237-4b61-89dc-637b65e39185)
maka kita bisa lihat penyebaran pengidap hepatitis berdasarkan usianya

kita juga bisa visualisaikan dengan cara
```bash
plt.figure(figsize=(20, 10))
df['sex'].value_counts().plot(kind="bar", color='blue', title='Gender Distribution')
```
![gender](https://github.com/fitriades/utsml/assets/149255008/3acc7534-8ff5-4e6c-a787-d7f640f5e6f2)
maka kita bisa lihat penyebaran pengidap hepatitis berdarkan gendernya

## Modeling
Kita tentukan dulu untuk nilai x dan y nya
```bash
X = df.drop (columns='class', axis=1)
y = df['class']
```
maka nilai x adalah semua kolom kecuali class dan y hanya kolom class<br>
selanjutnya kita standarisasi datanya terlebih dahulu
```bash
scaler = StandardScaler()
```
```bash
scaler.fit(X)
```
```bash
standarized_data = scaler.transform(X)
```
kita rubah nilai x dengan nilai yang sudah di standarkan
```bash
X = standarized_data
y = df['class']
```
selanjutnya kita bagi data tersebut menjadi data train dan data test dengan porsi data test 30% dan data train 70%
```bash
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, stratify=y, random_state=2)
```
selanjutnya kita bisa lanjutkan ke algoritma svm nya
```bash
classifier = svm.SVC(kernel='linear')
```
```bash
classifier.fit(X_train, y_train)
```
selanjutnya kita bisa cek akurasi data tersebut
```bash
x_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(x_train_prediction, y_train)
```
```bash
print('Tingkat akurasi data training = ', training_data_accuracy)
```
```bash
Tingkat akurasi data training =  0.9074074074074074
```
bisa dilihat untuk model data train nya di dapat akurasi 90% 
```bash
x_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(x_test_prediction, y_test)
```
```bash
print('Tingkat akurasi data test = ', test_data_accuracy)
```
```bash
Tingkat akurasi data test =  0.8936170212765957
```
dan untuk akurasi data test nya 89%<br>
pada tahap ini proses sudah selesai kita bisa cek dengan cara
```bash
input_data_test = (30,1,0,0,0,0,0,0,0,0,0,0,0,1.0,85.000000,18.0,4.0,100.000000,0)

array = np.array(input_data_test)

reshape = array.reshape(1,-1)

std_data = scaler.transform(reshape)
print(std_data)

prediction = classifier.predict(std_data)
print(prediction)

if (prediction[0] == 1):
    print('Rendah Resiko')
else :
    print('Resiko Tinggi')
```
```bash
[[-0.89419175  2.94745653 -1.00710629 -0.42802583 -1.34913081 -0.80623593
  -0.51117706 -1.94145069 -0.84594543 -0.51006137 -0.7147347  -0.41208169
  -0.39184799 -0.36093761 -0.43941439 -0.76983432  0.29724559  2.16692933
  -0.90748521]]
[1]
Rendah Resiko
```
Jika hasil sudah sesuai maka kita bisa import model tersebut
```bash
import pickle
filename = 'resiko-hepatitis.sav'
pickle.dump(classifier,open(filename,'wb'))
```

## Evaluation
Metode pengecekan yang dilakukan adalah metode akurasi dengan membagi 2 dataset nya menjadi data train dan data test
![akurasi](https://github.com/fitriades/utsml/assets/149255008/8be844c7-a32b-4625-8ce8-07efdfd3a619)
dari dua hasil pengecekan akurasi tersebut didapat nilai akurasi yang cukup tinggi maka proses model bisa dilanjutkan.

## Deployment
[link project](https://fitriauts.streamlit.app/)
![Screenshot (48)](https://github.com/fitriades/utsml/assets/149255008/8653e1be-4c6b-48a2-a04f-59b591f9c8ca)


**---Ini adalah bagian akhir laporan---**
