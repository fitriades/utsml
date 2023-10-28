import pickle
import streamlit as st

model = pickle.load(open('resiko-hepatitis.sav', 'rb'))

st.title('RESIKO KEMATIAN PENYAKIT HEPATITIS')

age = st.text_input('Usia Anda')
sex = st.selectbox('Jenis Kelamin', ['Laki Laki', 'Perempuan'])

if sex == 'Laki Laki':
    sex = 1
else:
    sex = 0
steroid = st.selectbox('Apakah anda menggunakan steroid ?', ['Ya', 'Tidak'])

if steroid == 'Ya':
    steroid = 1
else:
    steroid = 0
antivirals = st.selectbox('Apakah anda mengkonsumsi obat anti virus ?', ['Ya', 'Tidak'])

if antivirals == 'Ya':
    antivirals = 1
else:
    antivirals = 0
fatigue = st.selectbox('Apakah anda sering mengalami kelelahan ?', ['Ya', 'Tidak'])

if fatigue == 'Ya':
    fatigue = 1
else:
    fatigue = 0
malaise = st.selectbox('Apakah anda pengidap malaise ?', ['Ya', 'Tidak'])

if malaise == 'Ya':
    malaise = 1
else:
    malaise = 0
anorexia = st.selectbox('Apakah anda pengidap anorexia ?', ['Ya', 'Tidak'])

if anorexia == 'Ya':
    anorexia = 1
else:
    anorexia = 0
liver_big = st.selectbox('Apakah anda mengalami pembengkakan hati ?', ['Ya', 'Tidak'])

if liver_big == 'Ya':
    liver_big = 1
else:
    liver_big = 0
liver_firm = st.selectbox('Apakah anda mengalami pengerasan hati ?', ['Ya', 'Tidak'])

if liver_firm == 'Ya':
    liver_firm = 1
else:
    liver_firm = 0
spleen_palpable = st.selectbox('Apakah anada dapat merasakan limpa anda ?', ['Ya', 'Tidak'])

if spleen_palpable == 'Ya':
    spleen_palpable = 1
else:
    spleen_palpable = 0
spiders = st.selectbox('Apakah anda mengalami spider nevus ?', ['Ya', 'Tidak'])

if spiders == 'Ya':
    spiders = 1
else:
    spiders = 0
ascites = st.selectbox('Apakah anda mengalami memiliki ascites ?', ['Ya', 'Tidak'])

if ascites == 'Ya':
    ascites = 1
else:
    ascites = 0
varices = st.selectbox('Apakah anda memiliki varises ?', ['Ya', 'Tidak'])

if varices == 'Ya':
    varices = 1
else:
    varices = 0
bilirubin = st.number_input('JUmlah kadar bilirubin anda ?')
alk_phosphate = st.number_input('Kandungan alkaline dalam darah ?')
sgot = st.number_input('Jumlah kandungan Serum Glutamic Oxaloacetic Transaminase dalam hati (µ/L) ?')
albumin = st.number_input('Tingkat Albumin dalam tubuh ?')
protime = st.number_input('Jumlah waktu untuk Prothrombin time (detik) ?')
histology = st.selectbox('Apakah Histology liver anda normal ?', ['Ya', 'Tidak'])

if histology == 'Ya':
    histology = 1
else:
    histology = 0

diagnosa = ''

if st.button('Tingkat Resiko'):
    tingkat_resiko = model.predict([[age,sex,steroid,antivirals,fatigue,malaise,anorexia,liver_big,liver_firm,spleen_palpable,spiders,ascites,varices,bilirubin,alk_phosphate,sgot,albumin,protime,histology]])
    
    if(tingkat_resiko[0] == 1):
        diagnosa = 'Tidak beresiko menyebabkan kematian'
    else :
        diagnosa ='Beresiko menyebabkan kematian'

    st.success(diagnosa)