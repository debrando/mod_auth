__author__ = 'Alfredo Saglimbeni'
__mail__ = "repirro@gmail.com"

import setuptools

METADATA = dict(
    name='mod-auth',
    version='1.0',
    author='Alfredo Saglimbeni',
    author_email='repirro@gmail.com',
    description='Powerful and useful library to integrate mod_auth_tkt and mod_auth_pubtkt into your projects.',
    long_description=open('./README.txt').read(),
    url='https://github.com/debrando/mod_auth',
    license = "BSD",
    keywords='mod_auth mod_auth_pubtkt mod_auth_tkt authentication single sign on ticket SSO',
    install_requires=['M2Crypto','pycrypto'],
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Environment :: Web Environment',
        'Topic :: Internet',
        'Operating System :: OS Independent',
        ],
    zip_safe=False,
    packages=setuptools.find_packages(),
)

try:
    import distutils.command.bdist_conda
    print("Conda distribution")
    METADATA.update(dict(
        distclass=distutils.command.bdist_conda.CondaDistribution,
        conda_import_tests=True,
        conda_command_tests=True,
        conda_buildnum=1,
        project_urls={
            "Source Code": "https://github.com/debrando/mod_auth"
        }
    ))
except ImportError:
    print("Standard distribution")

if __name__ == '__main__':
    setuptools.setup(**METADATA)
