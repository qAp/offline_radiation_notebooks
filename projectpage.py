import os

import jinja2

import data_model_compare
import rrtmg_continuum_study
import clirad_gpts


dir_template = os.path.join(os.path.dirname(__file__), 'templates')
package_loader = jinja2.PackageLoader('projectpage', dir_template)
jinja_env = jinja2.Environment(loader=package_loader)



def page_index():
    template_index = jinja_env.get_template('index.html')

    with open('index.html', mode='w', encoding='utf-8') as file:
        file.write(template_index.render())


def html_model_compare(spectral_region='lw'):
    '''
    Returns HTML of hyperlink(s) to ipython notebook(s)
    containing results of comparions of different
    radiation models for different combinations of gases
    present in the atmosphere.
    '''
    tmpl_panel = jinja_env.get_template('panel_body_footer.html')
    tmpl_href = jinja_env.get_template('button_href.html')
    
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
        print(d)
        label_link = '+'.join(d['molecules'])
        if 'info' in d:
            label_link += '_{}'.format(d['info'])
        print(label_link)
            
        href_link = os.path.join(data_model_compare.URL_BASE,
                                 whichwave,
                                 d['file_ipynb'])
        lines.append(tmpl_href.render(label=label_link,
                                 href=href_link))

    content_panelbody = '\n</br>\n'.join(lines)
    panel = dict(footer=content_panelbody)
    html_panel = tmpl_panel.render(panel=panel)
    return html_panel




def page_model_compare():
    '''
    Writes HTML file for the comparison of different
    radiation models
    '''
    tmpl_affix = jinja_env.get_template('template_affix.html')

    page_title = 'Offline Radiation Model Comparison'

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
    html_sec_1 = html_model_compare(spectral_region='sw')

    # webpage section 2
    name_sec_2 = 'Longwave'
    html_sec_2 = html_model_compare(spectral_region='lw')

    html = tmpl_affix.render(website_name=('Offline Radiation '
                                           'Results'),
                             page_title=page_title,
                             page_info=page_info,
                             content_1=html_sec_1,
                             name_section_1=name_sec_1,
                             content_2=html_sec_2,
                             name_section_2=name_sec_2)

    with open('model_compare.html', mode='w', encoding='utf-8') as file:
        file.write(html)


def writeHTMLfile_rrtmg_continuum():
    tmpl_affix = jinja_env.get_template('template_affix.html')
    tmpl_panel = jinja_env.get_template('panel_body_footer.html')
    tmpl_link = jinja_env.get_template('button_href.html')
    rrtmg_continuum_study.writeHTMLfile(tmpl_affix=tmpl_affix,
                                        tmpl_panel=tmpl_panel,
                                        tmpl_link=tmpl_link)



def writeHTMLfile_clirad_gpts():
    tmpl_affix = jinja_env.get_template('template_affix.html')
    tmpl_panel = jinja_env.get_template('panel_body_footer.html')
    tmpl_link = jinja_env.get_template('button_href.html')
    html = clirad_gpts.getHTML_affix(tmpl_affix=tmpl_affix,
                                     tmpl_panel=tmpl_panel,
                                     tmpl_link=tmpl_link)

    with open('clirad_gpts.html', mode='w', encoding='utf-8') as f:
        f.write(html)





if __name__ == '__main__':
    page_index()
    page_model_compare()
    writeHTMLfile_rrtmg_continuum()
    writeHTMLfile_clirad_gpts()
    
