from datetime import date
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
from numerize import numerize
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from scipy import stats

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
    st.area_chart(sales)
    st.write("Sumber : BPS")
with met2:
    freq = st.selectbox("Pilih Jenis Bahan Bakar Memasak", ['lpg', 'listrik','minyak_tanah', 'arang', 'kayu', 'lainnya'])
    sales2 = df[['tahun', freq]].set_index('tahun')
    st.bar_chart(
        sales2
    )
    st.write("*dalam persentase")
nat1, nat2 = st.columns([2,1])
with nat1:
    j= st.container()
    j.write("LPG atau Liqufied Petroleum Gas menjadi bahan bakar utama yang signifikan digunakan oleh masyarakat Indonesia utamanya sejak 2011. Sementara itu penggunaan arang, kayu, minyak tanah semakin ditinggalkan oleh masyarakat Indonesia.")
    j.write("Penggunaan bahan bakar memasak listrik terlihat mengalami tren yang menurun. Hal ini di hipetesiskan mungkin saja 'magic jar' dan alat lainnya baru ditemukan dan menjadi viral. Kemudian hal ini didesak dengan program konversi LPG yang digalakkan mulai tahun 2008")
st.markdown("<h3 style='text-align: center; color: red;'>Besaran Subsidi LPG</h3>", unsafe_allow_html=True)
# Pembengkakan Subsidi LPG
subsidi = pd.read_excel("subsidi.xlsx")
#deklarasi date
subsidi['date'] = pd.to_datetime(subsidi['date'])
#bar chart subsidi
subl1, subl2 = st.columns([1,3])
with subl1:
    uang = subsidi.iloc[:, [0, -2,-1]]
    st.dataframe(uang)
    st.write("*data Besaran subsidi dengan asumsi 10,520 Rupiah/metrik (dalam Rupiah)")
with subl2:
    subs1 = subsidi[['date', 'Realisasi', 'Kuota']].set_index('date')
    st.area_chart(subs1)
    st.write("*dalam juta metrik ton")
    st.write(" Sumber: BPS")
    su = st.container()
    su.write("Besaran Subsidi LPG terus meningkat dari waktu ke waktu. Setidaknya APBN harus terbebani dengan beban subsidi LPG di tahun 2022 sebesar 84 triliun. Namun besaran subsidi ini hanyalah estimasi mengingat konversi besaran subsidi diasumsikan sama setiap tahun (Rp. 10,520/metrik)")
# data kedua tentang harga LPG
harga = pd.read_csv("spot-prices.csv", sep=',')
# Data prep
harga['date'] = pd.to_datetime(harga['date'])
# End of Data Prep

# Membuat line chart
harga1, harga2 = st.columns([4,1])
with harga1:
    st.markdown("<h3 style='text-align: center; color: red;'>Harga komponen utama LPG</h3>", unsafe_allow_html=True)
    harga_line = harga[['date', ' propane', ' normal butane']].set_index('date').resample('M').mean()
    st.line_chart(  harga_line)
with harga2:
    hu = st.container()
    hu.write(" ")
    hu.write(" ")
    hu.write(" ")
    hu.write("Komponen utama LPG adalah propane (C3H8) dan butana (C4H10). Harga komponen gas itu ditentukan oleh CP Aramco. Bisa dilihat harganya fluktuatif dan mengalami kenaikan signifikan dalam lima tahun terakhir.")
    hu.write(" ")
    hu.write("Sumber : Energydata")
## 
st.markdown("<h2 style='text-align: left; color: red;'> Adakah Alternatif LPG sebagai Bahan Bakar Memasak ?</h2>", unsafe_allow_html=True)
## Data Konsumsi Listrik Domestik
st.markdown("<h3 style='text-align: center; color: blue;'>Data Kelistrikan</h3>", unsafe_allow_html=True)
do = st.container()
do.write("Once you got a solar panel on a roof, energy is free. Once we convert our entire electricity grid to green and renewable energy, cost of living goes down. (Elizabeth May)")
do.write("I think electricity will create a new world. I feel like the world will change a lot with electricity, and I wonder how it will change, it's scary, and it's going to be fun. I think there are so many things to think about when it comes to electric cars. (J-Hope)")
lt1 = pd.read_csv("konsumsi_listrik.csv", sep = None)
lt = lt1.iloc[:, 2:]

plis = st.selectbox("Masukkan Tahun Pilihan", ["2020","2019","2018","2017","2016","2015","2014","2013","2012","2011","2010", "2019","2008","2007","2006","2005","2004","2003", "2002", "2001", "2000"])

# display 3 kolom
hat33, hat22, hat11 = st.columns([3,3,2])
with hat33:
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
with hat11:
    df = lt1.loc[:, ["latitude", "longitude",str(plis)]]
    st.map(df, use_container_width=True)
    st.markdown("<h5 style='text-align: center; color: blue;'>Berikut adalah Mapping Negara yang dimuat dalam data</h5>", unsafe_allow_html=True)
    hy = st.container()
    hy.write("Dapat dilihat pada tahun 2020, China menjadi negara yang mengonsumsi listrik terbesar di dunia. China mengalahkan USA di tahun 2011. Dari tabel konsumsi listrik ini bisa dilihat Indonesia memiliki nilai yang masih rendah dibanding negara dengan populasi besar lainnya.")
    st.write("Sumber : US Energy Information and Administration")
    st.markdown("<h5 style='text-align: right; color: black;'>*dalam TWh</h5>", unsafe_allow_html=True)

#aplikasi metrik
st.markdown("<h5 style='text-align: left; color: black;'>Aplikasi Metrik sebagai Shortcut Pencarian</h5>", unsafe_allow_html=True)
with st.expander("Daftar Negara"):
    st.dataframe(lt.iloc[:, 0])
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
## 
st.subheader("Seberapa Kecil kah Konsumsi Listrik Indonesia")
st.markdown("<h4 style='text-align: left; color:blue; '>Analisis Hubungan Konsumsi Listrik dan Populasi</h4>", unsafe_allow_html=True)
kop_lis = pd.read_csv("kor_pop_lis.csv")
x = kop_lis.iloc[:, 1]
y = kop_lis.iloc[:, 2]
tab1, tab2, tab3 = st.tabs(["Univariate Analysis", "Bivariate Analysis", "Model Regresi"])
with tab1:
    #### scatterplot, Korelasi
    st.markdown("Univariate Analysis")
    uni = st.selectbox("Silahkah pilih Data", ("populasi", "konsumsi_listrik"))
    st.write("ini adalah gambar distribusi data", uni)
    f= plt.figure(figsize=(12,4))
    f.add_subplot(1,2,1)
    kop_lis[uni].plot(kind='kde', c='g')
    f.add_subplot(1,2,2)
    plt.boxplot(kop_lis[uni])
    st.pyplot(f)

    des, scat = st.columns(2)
    with des:
        st.dataframe(kop_lis.describe())
    with scat:
        st.write( alt.Chart(kop_lis).mark_circle(size=60).encode(
            x='populasi',
            y='konsumsi_listrik',
            color='country',
            tooltip=['country', 'populasi', 'konsumsi_listrik']
            ).interactive()
    )
with tab2:
    # Bivariate Analysis
    st.write("Analisis Bivariate")
    bi1, bi2 = st.columns([3,2])
    with bi1:
        fi= plt.figure(figsize=(6,4))
        plt.scatter(kop_lis['populasi'], kop_lis['konsumsi_listrik'])
        plt.xlabel('Populasi dalam milliar')
        plt.ylabel('Konsumsi Listrik dalam TWh')
        plt.title("Scatter Plot Konsumsi Listrik VS Populasi")
        #calculate equation for trendline
        z = np.polyfit(kop_lis['populasi'], kop_lis['konsumsi_listrik'], 1)
        p= np.poly1d(z)
        #add trendline to plot
        plt.plot(kop_lis['populasi'], p(kop_lis['populasi']))
        st.pyplot(fi)
    with bi2:
        st.write("Pearson Correlation")
        pearson = kop_lis.corr()
        st.dataframe(pearson)
        st.write("Berarti terdapat hubungan kuat dua arah antara Konsumsi Listrik dengan Besaran Populasi. Semakin tinggi Populasi maka semakin besar konsumsi listriknya")
with tab3:
    ## Regresi
    st.write("Analisis Regresi")
    reg1, reg2 = st.columns(2)
    with reg1:
        kk = st.container()
        kk.write("Hipotesis Null : Besaran Populasi Tidak Mempengaruhi Besaran Konsumsi Listrik")
        kk.write("Hipotesis Alternatif: Besaran Populasi Mempengaruhi Besaran Konsumsi Listrik")
        st.latex(r''' \alpha = 0.05 ''')
    with reg2:
        ## Modelling
        x = kop_lis['populasi'].values.reshape(-1,1)
        y = kop_lis['konsumsi_listrik'].values.reshape(-1,1)
        # split ke trainin dan test dengan perbandinan 80:20
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
        # Object Linear Regresi
        lin_reg = LinearRegression()
        np.random.seed(5)
        lin_reg.fit(x_train, y_train)
        #nilai slope dan intercept
        print(lin_reg.coef_)
        print(lin_reg.intercept_)
        st.write("Hasil Modelling regresi :")
        st.write("konsumsi listrik hat = 3.07844483e-06 + 116.142(populasi)")
        st.write("dengan p-value = 0.000")

    prediks = st.number_input("Masukkan Nomor Negara untuk prediksi Konsumsi Listrik (sudah dalam juta)", 0, 42)
    with st.expander("Daftar Nomor Negara"):
        st.dataframe(kop_lis.iloc[:, 0])

    with st.expander("Nilai Prediksi"):
        pil_pred= kop_lis.iloc[prediks, 1]
        st.write("Nilai prediksi 2020", kop_lis.iloc[prediks, 0], "adalah", lin_reg.predict([[pil_pred]]))

    bel = kop_lis.iloc[prediks, 2]
    with st.expander("Nilai Aktual"):
        st.write("Nilai Aktual konsumsi listrik 2020", kop_lis.iloc[prediks, 0], "adalah", bel)
    with st.expander("Indonesia"):
        st.write("Dari hasil prediksi, nilai Indonesia sangat jauh dengan nilai aktual (nilai prediksi hampir 4 kali nilai aktual). Artinya penggunaan listrik di Indonesia relatif kecil dibandingkan dengan besarnya populasi yang dimiliki.")
    #### 
    # ini menampilkan p-value
    x = sm.add_constant(x)
    model = sm.OLS(y, x)
    res= model.fit()
    print(res.summary())

## Data Konsumsi litrik nasional Juni 2020
st.markdown("<h3 style='text-align: left; color: blue;'>Data Pertumbuhan Konsumsi Listrik Indonesia</h3>", unsafe_allow_html=True)
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
st.write("Sumber: ESDM, Katadata")
st.write(">Pertumbuhan Konsumsi listrik secara mayoritas turun signifikan dikala PLN mengklaim mengalami surplus pasokan listrik")
st.markdown("<h3 style='text-align: left; color: blue;'>Kompor Listrik diklaim lebih hemat dan beberapa keunggulan lain</h3>", unsafe_allow_html=True)
kl1, kl2 = st.columns([1,3])
with kl1:
    foto = Image.open("kl.jpg")
    st.image(foto)
    st.markdown("<h6 style='text-align: center; color: black;'>sumber gambar: BPGuide</h6>", unsafe_allow_html=True)
with kl2:
    kl = st.container()
    kl.write("- Dengan asumsi 23,6 kWh setara dengan 3 metrik gas dan listrik dengan subsidi berbiaya 495/kWh, 1 tabung lpg = 11.682 Rupiah sedangkan harga LPG bersubsidi rata-rata berkisar 21.000 Rupiah. (Kompor Listrik lebih hemat dibanding LPG sekalipun bersubsidi, cateris paribus)")
    kl.write("- Lebih aman-> Tidak ada api, asap, dll (Kompas, 2021)")
    kl.write("- Lebih praktis -> Mudah digunakan, lebih cepat karena terkonduktor langsung, (Kompas, 2021)")
    kl.write("- Lebih bersih (Kompas, 2021)")
    kl.write("- Pengaturan suhu yang lebih akurat (Kompas, 2021)")
st.markdown("<h3 style='text-align: left; color: red;'>Kesimpulan</h3>", unsafe_allow_html=True)
h= st.container()
h.write("Distribusi LPG subsidi yang buruk  memungkinkan menjadi penyebab tingginya prmintaan subsidi sehingga beban subsidi terus membengkak. Selain itu, harga komoditasnya fluktuatif cenderung naik sedangkan komoditasnya didominasi impor memperparah beban subsidi. Dilain sisi, perilaku konsumsi listrik Indonesia relatif rendah dibandingkan negara lain. Sedangkan Populasi Indonesia relatif sangat besar. Analisis membuktikan populasi memperuhi besaran konsumsi listrik. Oleh karena itu, penghentian subsidi LPG dapat menjadi opsi dan pengalihannya ke subsidi listrik dalam program Kompor Induksi dapat ditelaah lebih lanjut sebagai solusi alternatif.")

# Apps Subsidi
# Sidebar
with st.sidebar:
    st.title("Ingin Tahu Berapa Estimasi Subsidi LPG Yang Anda Terima ?")
    hal1 = st.selectbox("Apakah Anda Menggunakan LPG 3 KG ?", (True, False))
    hal2 = st.number_input("Berapa konsumsi LPG 3kg Anda dalam Satu Minggu ?", 0, 100)
    besar = 10520*48*3*hal2*hal1
    with st.expander("Ketahui lebih lanjut..."):
        st.write("The amount of LPG Subsidy for you is estimated at Rp.", numerize.numerize(besar) + " in a year")
