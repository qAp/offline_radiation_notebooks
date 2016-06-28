import os



URL_BASE = os.path.join('http://nbviewer.jupyter.org/github',
                        'qAp/offline_radiation_notebooks',
                        'blob/master')




CASES_SW = [dict(molecules=['H2O'],
                 hitran_year='1996',
                 file_ipynb='shortwave_mls_H2O_solir_gpts.ipynb'),
            dict(molecules=['H2O'],
                 hitran_year='2012',
                 file_ipynb=('shortwave_mls_H2O_'
                             'solir_gpts_newparams.ipynb')
                 )]



CASES_LW = [dict(molecules=['H2O'],
                 hitran_year='1996',
                 file_ipynb='longwave_mls_H2O_gpts.ipynb'),
            dict(molecules=['H2O'],
                 hitran_year='2012',
                 file_ipynb='longwave_mls_H2O_H2012_gpts.ipynb')]
