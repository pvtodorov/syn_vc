from setuptools import setup

setup(name='synvc',
      version='0.1',
      description='better synapse sync',
      url='http://github.com/pvtodorov/syn_vc',
      author='Petar Todorov, Artem Sokolov',
      author_email='petar.v.todorov@gmail.com',
      license='MIT',
      packages=['synvc'],
      zip_safe=False,
      entry_points={'console_scripts': ['syn-upload=synvc.cli:upload']},
      install_requires=[
          'asciitree', 'morph', 'synapseclient', 'tqdm'
      ]
      )
