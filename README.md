# Proyek_visdat_Submission_DBS

## Deskripsi 
```
Proyek ini mengembangkan sistem visualisasi data yang terintegrasi dengan database. Sistem ini memungkinkan
pengguna untuk menampilkan data dari sumber database dalam bentuk visual yang lebih mudah dipahami, seperti
grafik dan diagram. Proyek ini dibuat dengan tujuan penyelesaian submission pada kursus "Belajar Analisis
Data dengan Python" oleh DBS_Foundation.
```

## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
```

## Setup Environment - Google Colab
```
from google.colab import drive
drive.mount('/content/drive')
```

## Setup Environment Instalation Dependency - Shell
```
pip install -r requirements.txt
```

## Run Streamlit App
```
streamlit run dashboardVisDat_Proyek.py

or in subfolder:
streamlit run dashboard/dashboardVisDat_Proyek.py
```
