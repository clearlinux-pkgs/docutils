#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : docutils
Version  : 0.12
Release  : 22
URL      : https://pypi.python.org/packages/source/d/docutils/docutils-0.12.tar.gz
Source0  : https://pypi.python.org/packages/source/d/docutils/docutils-0.12.tar.gz
Summary  : Docutils -- Python Documentation Utilities
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause GPL-2.0 Public-Domain Python-2.0
Requires: docutils-bin
Requires: docutils-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=======================
=======================
:Author: David Goodger
:Contact: goodger@python.org
:Date: $Date: 2013-07-22 10:28:47 +0200 (Mon, 22. Jul 2013) $
:Web site: http://docutils.sourceforge.net/

%package bin
Summary: bin components for the docutils package.
Group: Binaries

%description bin
bin components for the docutils package.


%package python
Summary: python components for the docutils package.
Group: Default

%description python
python components for the docutils package.


%prep
%setup -q -n docutils-0.12

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484544670
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pushd test ; ./alltests.py ; popd
%install
export SOURCE_DATE_EPOCH=1484544670
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rst2html.py
/usr/bin/rst2latex.py
/usr/bin/rst2man.py
/usr/bin/rst2odt.py
/usr/bin/rst2odt_prepstyles.py
/usr/bin/rst2pseudoxml.py
/usr/bin/rst2s5.py
/usr/bin/rst2xetex.py
/usr/bin/rst2xml.py
/usr/bin/rstpep2html.py

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
