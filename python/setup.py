from glob import glob
from os.path import basename, splitext

import setuptools

print(setuptools.find_packages('src'))
setuptools.setup(name="coolpkg",
                 version="1.0.0",
                 description='Python code for NHL Simulator',
                 long_description='Python code for NHL Simulator',
                 packages=setuptools.find_packages('src'),
                 package_dir={'': 'src'},
                 py_modules=[splitext(basename(path))[0] for path in glob('python/src/*.py')],
                 package_data={'': ['package.yaml', 'clibs/*.so', 'static/*.*', 'csv/*']},
                 include_package_data=True,
                 zip_safe=False,
                 python_requires='>=3.8',
                 )
