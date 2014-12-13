"""
SQLAlchemy FullText Search
"""

from setuptools import setup


setup(
        name='ioloop',
        version='0.1a',
        url='https://github.com/mengzhuo/ioloop',
        license='MIT',
        author='Meng Zhuo',
        author_email='mengzhuo1203@gmail.com',
        description=('Simple IOloop by epoll or kqueue'),
        long_description = __doc__,
        packages=['ioloop'],
        zip_safe=True,
        include_package_data=True,
        platforms='any',
        install_requires=[],
            classifiers=[
                        'Environment :: Web Environment',
                        'Intended Audience :: Developers',
                        'License :: OSI Approved :: BSD License',
                        'Operating System :: OS Independent',
                        'Programming Language :: Python :: 2.7',
                        'Programming Language :: Python :: 3.3',
                        'Programming Language :: Python :: 3.4',
                        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                        'Topic :: Software Development :: Libraries :: Python Modules'            ]
)
