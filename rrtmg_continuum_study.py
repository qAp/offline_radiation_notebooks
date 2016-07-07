import os

import data_rrtmg_continuum_study as data






def getList_metadata_sw():
    list_metadata = []
    for d in data.CASES_SW:
        label = '+'.join(d['molecules'])
        href = os.path.join(data.URL_BASE,
                            'shortwave',
                            'study__continuum',
                            d['file_ipynb'])
        list_metadata.append(dict(label=label, href=href))
    return list_metadata



def getList_metadata_lw():
    list_metadata = []
    for d in data.CASES_LW:
        label = '+'.join(d['molecules'])
        href = os.path.join(data.URL_BASE,
                            'longwave',
                            'study__continuum',
                            'rrtmg',
                            d['file_ipynb'])
        list_metadata.append(dict(label=label, href=href))
    return list_metadata



def getHTML_panel_continuum(tmpl_link=None, tmpl_panel=None,
                            region='sw'):
    #tmpl_link = jinja_env.get_template('button_href.html')
    #tmpl_panel = jinja_env.get_template('panel_body_footer.html')

    if region == 'sw':
        nbs = getList_metadata_sw()
    elif region == 'lw':
        nbs = getList_metadata_lw()

    lines = [tmpl_link.render(href=nb['href'], label=nb['label'])
             for nb in nbs]

    panel = {}
    panel['footer'] = '\n</br>/n'.join(lines)

    html = tmpl_panel.render(panel=panel)
    return html
    


def getHTML_affix(tmpl_affix=None, tmpl_panel=None, tmpl_link=None):
    #tmpl_affix = jinja_env.get_template('template_affix.html')

    page_title = 'RRTMG H2O Continuum Study'
    page_info = ("Links here redirect to ipython notebooks "
                 "which compare RRTMG results for when "
                 "there is continuum absorption and when "
                 "is no continuum absorption. "
                 ""
                 "The atmosphere profile considered is "
                 "a mid-latitude summer profile.")
    website_name = 'Offline Radiation Results'

    name_section_1 = 'Shortwave'
    content_1 = getHTML_panel_continuum(tmpl_panel=tmpl_panel,
                                        tmpl_link=tmpl_link,
                                        region='sw')
    
    name_section_2 = 'Longwave'
    content_2 = getHTML_panel_continuum(tmpl_panel=tmpl_panel,
                                        tmpl_link=tmpl_link,
                                        region='lw')

    html = tmpl_affix.render(page_title=page_title,
                             page_info=page_info,
                             website_name=website_name,
                             name_section_1=name_section_1,
                             content_1=content_1,
                             name_section_2=name_section_2,
                             content_2=content_2)
    return html



def writeHTMLfile(tmpl_affix=None, tmpl_panel=None, tmpl_link=None):
    html = getHTML_affix(tmpl_affix=tmpl_affix,
                         tmpl_panel=tmpl_panel,
                         tmpl_link=tmpl_link)
    
    with open('rrtmg_water_continuum.html',
              mode='w', encoding='utf-8') as f:
        f.write(html)





if __name__ == '__main__':
    pass


