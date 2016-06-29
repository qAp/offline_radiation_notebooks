import os

import jinja2

import model_compare
import rrtmg_continuum_study
import clirad_gpts


dir_template = os.path.join(os.path.dirname(__file__), 'templates')
package_loader = jinja2.PackageLoader('projectpage', dir_template)
jinja_env = jinja2.Environment(loader=package_loader)



def writeHTMLfile_index():
    template_index = jinja_env.get_template('index.html')

    with open('index.html', mode='w', encoding='utf-8') as file:
        file.write(template_index.render())



def writeHTMLfile_model_compare():
    tmpl_affix = jinja_env.get_template('template_affix.html')
    tmpl_panel = jinja_env.get_template('panel_body_footer.html')
    tmpl_link = jinja_env.get_template('button_href.html')
    html = model_compare.getHTML_affix(tmpl_affix=tmpl_affix,
                                       tmpl_panel=tmpl_panel,
                                       tmpl_link=tmpl_link)

    with open('model_compare.html', mode='w', encoding='utf-8') as f:
        f.write(html)



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
    writeHTMLfile_index()
    writeHTMLfile_model_compare()
    writeHTMLfile_rrtmg_continuum()
    writeHTMLfile_clirad_gpts()
    
