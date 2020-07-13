from cx_Freeze import setup, Executable

executables = [Executable('runn.py')]

includes = ['_cffi_backend', 'pars_search_v1_0.spiders.spider1', 'scrapy.spiderloader', \
            'scrapy.statscollectors', 'scrapy', 'scrapy.logformatter']
packages = ["scrapy", 'pars_search_v1_0.settings']
options = {
    'build_exe': {
        'includes': includes,
        'packages': packages

    }
}

setup(name='parser',
      version='0.0.1',
      description='My parser!',
      executables=executables,
      options=options
      )