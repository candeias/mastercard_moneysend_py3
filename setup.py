#
# Copyright 2016 MasterCard International.
#
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this list of
# conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice, this list of
# conditions and the following disclaimer in the documentation and/or other materials
# provided with the distribution.
# Neither the name of the MasterCard International Incorporated nor the names of its
# contributors may be used to endorse or promote products derived from this software
# without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
# SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
# TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#

from setuptools import find_packages, setup

setup(name='mastercard_moneysend_py3',
      version='1.0.4',
      description='MasterCard API Python SDK for Python3',
      long_description='MasterCard API Python SDK for Python3',
      author='Rogerio Candeias',
      author_email='rogerio.candeias@gmail.com',
      url='https://github.com/candeias/mastercard_moneysend_py3',
      license='BSD',
      packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
      classifiers=[
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      tests_require=['mock'],
      install_requires=['mastercard_api_core_py3>=1.4.0,<1.5.0']
      )
