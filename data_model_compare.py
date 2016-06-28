import os



URL_BASE = os.path.join('http://nbviewer.jupyter.org/github',
                        'qAp/offline_radiation_notebooks',
                        'blob/master')


# longwave cases
CASES_LW = [
    dict(molecules=['H2O'],
         file_ipynb='longwave_mls_H2O.ipynb'),
    dict(molecules=['CO2'],
         file_ipynb='longwave_mls_CO2.ipynb'),
    dict(molecules=['O3'],
         file_ipynb='longwave_mls_O3.ipynb'),
    dict(molecules=['N2O'],
         file_ipynb='longwave_mls_N2O.ipynb'),
    dict(molecules=['H2O', 'CO2'],
         file_ipynb='longwave_mls_H2O_CO2.ipynb'),
    dict(molecules=['H2O', 'O3'],
         file_ipynb='longwave_mls_H2O_O3.ipynb'),
    dict(molecules=['H2O', 'CO2', 'O3'],
         file_ipynb='longwave_mls_H2O_CO2_O3.ipynb'),
    dict(molecules=['H2O', 'CO2', 'O3'],
         file_ipynb='longwave_mls_H2O_CO2_O3_cont.ipynb',
         info='cont')
    ]


# shortwave cases
CASES_SW = [
    dict(molecules=['H2O'],
         file_ipynb='shortwave_mls_H2O.ipynb'),
    dict(molecules=['CO2'],
         file_ipynb='shortwave_mls_CO2.ipynb'),
    dict(molecules=['O3'],
         file_ipynb='shortwave_mls_O3.ipynb')]

