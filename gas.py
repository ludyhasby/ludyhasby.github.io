from codecs import latin_1_decode
from datetime import date
from tkinter import Y
from pytz import country_timezones
from requests import delete
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as py
import matplotlib
import matplotlib.pylab as plt
from PIL import Image
from numerize import numerize
import altair as alt
import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pydeck as pdk
from numerize import numerize



# setting page nya jadi gede
st.set_page_config(layout="wide")
# judul
bag1, bag2 = st.columns([4,1])
with bag1:
    st.markdown("<h1 style='text-align: center; color: black;'>Menilik LPG Bersubsidi: Haruskah Dilanjutkan ?</h1>", unsafe_allow_html=True)
with bag2:
    image = Image.open("gas1.png")
    st.image(image)
# Deklarasi dataset
df = pd.read_csv("bahan_masak.csv", sep=None)
# Data prep
df['tahun'] = pd.to_datetime(df['tahun'])
# End of Data Prep
#Buat index dulu
met1, met2 = st.columns([2,1])
with met1:
    st.markdown("<h3 style='text-align: center; color: red;'>Fraksi Bahan Bakar Memasak RT Indonesia 2001, 2007-2016</h3>", unsafe_allow_html=True)
    sales = df[['tahun', 'lpg', 'listrik', 'minyak_tanah', 'arang', 'kayu', 'lainnya']].set_index('tahun')
    st.area_chart(
        sales
    )
with met2:
    freq = st.selectbox("Pilih Jenis Bahan Bakar Memasak", ['lpg', 'listrik','minyak_tanah', 'arang', 'kayu', 'lainnya'])
    sales2 = df[['tahun', freq]].set_index('tahun')
    st.bar_chart(
        sales2
    )
nat1, nat2 = st.columns([2,1])
with nat1:
    j= st.container()
    j.write("LPG atau Liqufied Petroleum Gas menjadi bahan bakar utama yang signifikan digunakan oleh masyarakat Indonesia utamanya sejak 2011. Sementara itu penggunaan arang, kayu, minyak tanah semakin ditinggalkan oleh masyarakat Indonesia.")
# Pembengkakan Subsidi LPG
subsidi = pd.read_excel("subsidi.xlsx")
#deklarasi date
subsidi['date'] = pd.to_datetime(subsidi['date'])
#bar chart subsidi
subl1, subl2 = st.columns([1,3])
with subl1:
    uang = subsidi.iloc[:, [0, -2,-1]]
    st.dataframe(uang)
    st.write("*data Besaran subsidi dengan asumsi 10.520 Rupiah/metrik (dalam Rupiah)")
with subl2:
    subs1 = subsidi[['date', 'Realisasi', 'Kuota']].set_index('date')
    st.area_chart(subs1)
    st.write("*dalam juta metrik ton")
    su = st.container()
    su.write("Besaran Subsidi LPG terus meningkat dari waktu ke waktu. Setidaknya APBN harus terbebani dengan beban subsidi LPG di tahun 2022 sebesar 84 triliun. Namun besaran subsidi ini hanyalah estimasi mengingat konversi besaran subsidi diasumsikan sama setiap tahun (Rp. 10520/metrik)")
# data kedua tentang harga LPG
st.subheader("Harga komponen utama LPG")
harga = pd.read_csv("spot-prices.csv", sep=',')
# Data prep
harga['date'] = pd.to_datetime(harga['date'])
# End of Data Prep

# Membuat line chart
harga1, harga2 = st.columns([4,1])
with harga1:
    harga_line = harga[['date', ' propane', ' normal butane']].set_index('date').resample('M').mean()
    st.line_chart(  harga_line)
with harga2:
    hu = st.container()
    hu.write("Komponen utama LPG adalah propane (C3H8) dan butana (C4H10). Harga komponen gas itu ditentukan oleh CP Aramco. Bisa dilihat harganya fluktuatif dan mengalami kenaikan signifikan dalam lima tahun terakhir.")

## Data Konsumsi Listrik Domestik
st.markdown("<h3 style='text-align: center; color: red;'>Data Kelistrikan</h3>", unsafe_allow_html=True)
do = st.container()
do.write("Once you got a solar panel on a roof, energy is free. Once we convert our entire electricity grid to green and renewable energy, cost of living goes down. (Elizabeth May)")
do.write("I think electricity will create a new world. I feel like the world will change a lot with electricity, and I wonder how it will change, it's scary, and it's going to be fun. I think there are so many things to think about when it comes to electric cars. (J-Hope)")
lt1 = pd.read_csv("konsumsi_listrik.csv", sep = None)
lt = lt1.iloc[:, 2:]

plis = st.selectbox("Masukkan Tahun Pilihan", ["2020","2019","2018","2017","2016","2015","2014","2013","2012","2011","2010"])

# display 3 kolom
hat33, hat22, hat11 = st.columns(3)
with hat11:
    st.write("Konsumsi listrik", str(plis))
    st.write(alt.Chart(lt).mark_bar().encode(
    y=alt.Y('country', sort =None),
    x= alt.X(str(plis)),
))
with hat22:
    c11= str(int(plis)-10)
    st.write("Konsumsi listrik", c11)
    st.write(alt.Chart(lt).mark_bar().encode(
    y=alt.Y('country', sort =None),
    x= alt.X(c11),
))
with hat33:
    c22= str(int(plis)-20)
    st.write("Konsumsi listrik", c22)
    st.write(alt.Chart(lt).mark_bar().encode(
    y=alt.Y('country', sort =None),
    x= alt.X(c22),
))
hy = st.container()
hy.write("Dapat dilihat pada tahun 2020, China menjadi negara yang mengonsumsi listrik terbesar di dunia. China mengalahkan USA di tahun 2011. Dari tabel konsumsi listrik ini bisa dilihat Indonesia memiliki nilai yang masih rendah dibanding negara dengan populasi besar lainnya.")

trik1, trik2 = st.columns([3,1])
with trik1:
    data1 = lt1.loc[:, ["country", str(plis), str(int(plis)-1),str(int(plis)-2),str(int(plis)-3),str(int(plis)-4),str(int(plis)-5), str(int(plis)-6), str(int(plis)-7), str(int(plis)-8), str(int(plis)-9), str(int(plis)-10)]]
    st.dataframe(data1)
    st.markdown("<h5 style='text-align: right; color: red;'>Berikut adalah Mapping Negara yang dimuat dalam data --></h5>", unsafe_allow_html=True)
with trik2:
    df = lt1.loc[:, ["latitude", "longitude",str(plis)]]
    st.map(df, use_container_width=True)
#aplikasi metrik
st.markdown("<h5 style='text-align: left; color: black;'>Aplikasi Metrik sebagai Shortcut Pencarian</h5>", unsafe_allow_html=True)
mot1, mot2 = st.columns([2,1])
with mot1:
    negara = st.number_input("Masukkan Kode Negara", 0, 41)
    neg = st.write("Anda memilih negara", lt.iloc[int(negara), 0])
    thn = st.selectbox("Tahun Pilihan", ["2020","2019","2018","2017","2016","2015","2014","2013","2012","2011","2010"])
with mot2:
    bahan = lt.loc[negara, thn]
    bahan2 = lt.loc[negara, str(int(thn)-1)]
    per = ((int(bahan)-int(bahan2))/int(bahan2))*100
    st.metric("Besaran Konsumsi", bahan, str(round(per, 2)))
    with st.expander("info Indonesia"):
        st.write("Indonesia mengalami penurunan konsumsi listrik 1.15% di tahun 2020")
## Data Konsumsi litrik nasional Juni 2020
st.markdown("<h3 style='text-align: left; color: red;'>Data Pertumbuhan Konsumsi Listrik Indonesia</h3>", unsafe_allow_html=True)
to_stream = pd.read_excel("listrik_juni.xlsx")
plt.rcParams.update({'font.size': 12, 'font.weight':'bold'})
dfcols = to_stream.columns.tolist()
fig, ax = plt.subplots(figsize=(12,8), )
sns.set_style('whitegrid')
to_stream.plot.barh(x='nama_alias', figsize=(12,8), width = .9, ax= ax)
plt.title("Pertumbuhan Konsumsi Listrik per Wilayah Januari 2020 VS Juni 2019")
plt.legend(loc='lower right')
for patch in ax.patches:
    w, h = patch.get_width(), patch.get_height()
    y = patch.get_y()
    ax.text(w+ -0.1, h/2+y, f'{w:.3f}', va='center')
st.pyplot(fig)
st.write(">Pertumbuhan Konsumsi listrik secara mayoritas turun signifikan dikala PLN mengklaim mengalami surplus pasokan listrik")
st.markdown("<h3 style='text-align: left; color: red;'>Kesimpulan</h3>", unsafe_allow_html=True)
h= st.container()
h.write("Dengan beban subsidi LPG yang terus membengkak dikala pasokan listrik nasional surplus dan perilaku mengonsumsi listrik lebih rendah dibanding negara lain, Penghentian subsidi LPG dapat menjadi opsi dan Kompor Induksi dapat ditelaah lebih lanjut sebagai solusi alternatif.")
# Apps Subsidi
# Sidebar
with st.sidebar:
    st.title("Ingin Tahu Berapa Estimasi Subsidi LPG Yang Anda Terima ?")
    hal1 = st.selectbox("Apakah Anda Menggunakan LPG 3 KG ?", (True, False))
    hal2 = st.number_input("Berapa konsumsi LPG 3kg Anda dalam Satu Minggu ?", 0, 100)
    besar = 10520*48*3*hal2*hal1
    with st.expander("Ketahui lebih lanjut..."):
        st.write("The amount of LPG Subsidy for you is estimated at Rp.", numerize.numerize(besar) + " in a year")
