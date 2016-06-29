import os

import data_model_compare





def getHTML_panel(spectral_region='lw',
                  tmpl_panel=None, tmpl_link=None):
    '''
    Returns HTML of hyperlink(s) to ipython notebook(s)
    containing results of comparions of different
    radiation models for different combinations of gases
    present in the atmosphere.
    '''
    
    if spectral_region == 'lw':
        cases = data_model_compare.CASES_LW
        whichwave = 'longwave'
    elif spectral_region == 'sw':
        cases = data_model_compare.CASES_SW
        whichwave = 'shortwave'
    else:
        raise ValueError('spectral_region must be either lw or sw')

    lines = []
    for d in cases:
        label_link = '+'.join(d['molecules'])
        if 'info' in d:
            label_link += '_{}'.format(d['info'])
            
        href_link = os.path.join(data_model_compare.URL_BASE,
                                 whichwave,
                                 d['file_ipynb'])
        lines.append(tmpl_link.render(label=label_link,
                                      href=href_link))

    content_panelbody = '\n</br>\n'.join(lines)
    panel = dict(footer=content_panelbody)
    html_panel = tmpl_panel.render(panel=panel)
    return html_panel




def getHTML_affix(tmpl_affix=None, tmpl_panel=None, tmpl_link=None):
    '''
    Writes HTML file for the comparison of different
    radiation models
    '''
    page_title = 'Model Comparison'
    page_info = ('''The links here redirect to notebooks '''
                 '''that show the comparison of various '''
                 '''offline radiation models '''
                 '''for different gas contents in a '''
                 '''typical mid-latutude summar atmosphere.'''
                 ''' '''
                 '''The radiation models considered include '''
                 '''line-by-line models and parameterized models.''')

    # webpage section 1
    name_sec_1 = 'Shortwave'
    html_sec_1 = getHTML_panel(spectral_region='sw',
                               tmpl_panel=tmpl_panel,
                               tmpl_link=tmpl_link)

    # webpage section 2
    name_sec_2 = 'Longwave'
    html_sec_2 = getHTML_panel(spectral_region='lw',
                               tmpl_panel=tmpl_panel,
                               tmpl_link=tmpl_link)

    html = tmpl_affix.render(website_name=('Offline Radiation '
                                           'Results'),
                             page_title=page_title,
                             page_info=page_info,
                             content_1=html_sec_1,
                             name_section_1=name_sec_1,
                             content_2=html_sec_2,
                             name_section_2=name_sec_2)

    return html
