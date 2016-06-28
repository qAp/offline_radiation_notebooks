import os



URL_BASE = os.path.join('http://nbviewer.jupyter.org/github',
                        'qAp/offline_radiation_notebooks',
                        'blob/master')

CASES_SW = [
    dict(molecules=['H2O'],
         file_ipynb='shortwave_mls_H2O_cont_vs_nocont.ipynb')]

CASES_LW = [
    dict(molecules=['H2O'],
         file_ipynb='longwave_mls_H2O_cont_vs_nocont.ipynb')]
