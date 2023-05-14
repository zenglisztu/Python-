from pathlib import Path
import xlwings as xw

Pa = Path(__file__).parent

pa = Pa / '../Excel/2020人口.xlsx'


app = xw.App()

wb = app.books.open(pa.resolve())
