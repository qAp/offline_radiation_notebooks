import os

import data_clirad_gpts as data



def getList_notebooks_sw():
    nbs = []
    for d in data.CASES_SW:
        label = '+'.join(d['molecules']) + '_' + d['hitran_year']
        href = os.path.join(data.URL_BASE, 'shortwave', d['file_ipynb'])
        nbs.append(dict(label=label, href=href))
    return nbs


def getList_notebooks_lw():
    nbs = []
    for d in data.CASES_LW:
        label = '+'.join(d['molecules']) + '_' + d['hitran_year']
        href = os.path.join(data.URL_BASE, 'longwave', d['file_ipynb'])
        nbs.append(dict(label=label, href=href))
    return nbs



def getHTML_panel_sw(tmpl_panel=None, tmpl_link=None):
    panel = {}
    panel['body'] = ('''<p style="color:#000;">'''
                     "Radiation results for individual g-points "
                     "in the solar infra-red spectral bands "
                     "of CLIRAD-SW. "
                     ""
                     "Only the tables `xk` and `hk` in the subroutine "
                     "solir() are changed between 1996 and 2012 results."
                     '''</p>''')

    nbs = getList_notebooks_sw()
    links = [tmpl_link.render(href=nb['href'], label=nb['label'])
             for nb in nbs]
    panel['footer'] = ' '.join(links)

    html = tmpl_panel.render(panel=panel)
    return html



def getHTML_panel_lw(tmpl_panel=None, tmpl_link=None):
    panel = {}
    panel['body'] = ('''<p style="color:#000;">'''
                     "Radiation results for individual g-points "
                     "in CLIRAD-LW. "
                     "All data tables are changed between 1996 and 2012."
                     '''</p>''')

    nbs = getList_notebooks_lw()
    links = [tmpl_link.render(href=nb['href'], label=nb['label'])
             for nb in nbs]
    panel['footer'] = ' '.join(links)

    html = tmpl_panel.render(panel=panel)
    return html



def getHTML_affix(tmpl_affix=None, tmpl_panel=None, tmpl_link=None):
    page_title = 'CLIRAD: results for individual g-points'
    page_info = ("Results pointed to by the links here show "
                 "CLIRAD results for individual g-points.")
    website_name = 'Offline Radiation Results'

    name_section_1 = 'Shortwave'
    content_1 = getHTML_panel_sw(tmpl_panel=tmpl_panel,
                                 tmpl_link=tmpl_link)
                                 
    name_section_2 = 'Longwave'
    content_2 = getHTML_panel_lw(tmpl_panel=tmpl_panel,
                                 tmpl_link=tmpl_link)

    html = tmpl_affix.render(page_title=page_title,
                             page_info=page_info,
                             website_name=website_name,
                             name_section_1=name_section_1,
                             content_1=content_1,
                             name_section_2=name_section_2,
                             content_2=content_2)
    return html

    


