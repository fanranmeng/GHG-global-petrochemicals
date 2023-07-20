"""These functions import data from known published online sources"""
import re
import requests
import numpy as np
import pandas as pd
import rdfpandas as rpd
from rdflib.graph import Graph


def request_excel(url):
  """Fetch Excel file from online source"""
  req = requests.get(url)
  return pd.ExcelFile(req.content)


class ONS(object):
  """UK emissions data for each gas from Office for National Statistics"""
  def __init__(self):
    url = 'https://www.ons.gov.uk/file?uri=%2feconomy%2fenvironmentalaccounts%2fdatasets%2fukenvironmentalaccountsatmosphericemissionsgreenhousegasemissionsbyeconomicsectorandgasunitedkingdom%2fcurrent/atmosphericemissionsghg.xlsx'
    file = request_excel(url)
    for gas in file.sheet_names[1:]:
      sheet = pd.read_excel(file, gas, header=3)
      empty_rows = np.where(np.sum(~pd.isna(sheet).values, axis=1) == 0)[0]
      total, details = sheet.loc[:empty_rows[0]-1].copy(), sheet.loc[empty_rows[2]+2:empty_rows[3]-1].copy()
      setattr(self, re.sub(" ","",gas), total.dropna(how='all', axis=1))
      setattr(self, re.sub(" ","",gas)+'detail', details.dropna(how='all', axis=1))


class NAEI(object):
  """Reported UK emissions by National Atmospheric Emissions Inventory.\n
   Pass unfccc parameter to get figures reported to UNFCCC"""
  def __init__(self, unfccc=False):
    url = 'https://naei.beis.gov.uk/resources/PivotTableViewer_2021_GHG_Final.xlsx'
    file = request_excel(url)
    sheet = file.sheet_names[8] if unfccc else file.sheet_names[2]
    self.data = pd.read_excel(file, sheet_name=sheet)
    self.summary = pd.DataFrame(self.data.groupby('IPCC Code').sum()['Emission'])


class PROBS(object):
  def __init__(self):
    url = 'https://raw.githubusercontent.com/ukfires/material-flow-mapping/master/outputs/flows.csv?token=GHSAT0AAAAAABZHGCL7SWDK4OM2PJRHLMPMYZR2XCQ'
    self.data = pd.read_csv(url)


class RDFStore(object):
  def __init__(self):
    url = 'C:/Users\lukec\.vscode\cthru-data/build\data_store.nt.gz'
    g = Graph()
    g.parse(url, format="nt")
    self.data = rpd.graph.to_dataframe(g)

  def get_equivalents(self, header = 'equivalentto'):
    equivalents = self.data[self.data.columns[[header in i.lower() for i in self.data.columns]]].dropna(how='all')
    for col in equivalents.columns:
        equivalents[col] = [i.split('/')[-1] for i in equivalents[col]]
    return equivalents.drop_duplicates(col)


class Ecoinvent(object):
  def __init__(self):
    url = 'https://drive.google.com/uc?export=download&id=1Wsh1WBk-Dd1tec-j44UkjgMY51Y-HVyQ'
    self.data = pd.read_csv(url)
