from pandas.core.frame import DataFrame
import tabula as tb
import pandas as pd

# yapılacak dosya yolunu statik yap.
dosya_yolu = r"C:\Users\velid\Downloads\Documents\tablo201122020.pdf"
df = tb.read_pdf(dosya_yolu,pages="all")
# tb.convert_into(dosya_yolu,"deneme.csv",output_format="csv")

oku = pd.read_csv(r"C:\Users\velid\Exercism\python\two-fer\deneme.csv",encoding="auto")

df.to_excel()
