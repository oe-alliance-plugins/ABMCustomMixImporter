from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.ABMCustomMixImporter'
setup(name='enigma2-plugin-systemplugins-abmcustommiximporter',
       version='3.0',
       description='ABM CustomMix Importer',
       package_dir={pkg: 'ABMCustomMixImporter'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'mixes/*.xml', 'setup.xml']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
