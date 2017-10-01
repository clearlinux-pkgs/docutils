#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : docutils
Version  : 0.14
Release  : 27
URL      : http://pypi.debian.net/docutils/docutils-0.14.tar.gz
Source0  : http://pypi.debian.net/docutils/docutils-0.14.tar.gz
Summary  : Docutils -- Python Documentation Utilities
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause GPL-2.0 Public-Domain Python-2.0
Requires: docutils-bin
Requires: docutils-legacypython
Requires: docutils-python3
Requires: docutils-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
into useful formats, such as HTML, XML, and LaTeX.  For
        input Docutils supports reStructuredText, an easy-to-read,
        what-you-see-is-what-you-get plaintext markup syntax.

%package bin
Summary: bin components for the docutils package.
Group: Binaries

%description bin
bin components for the docutils package.


%package legacypython
Summary: legacypython components for the docutils package.
Group: Default

%description legacypython
legacypython components for the docutils package.


%package python
Summary: python components for the docutils package.
Group: Default
Requires: docutils-legacypython
Requires: docutils-python3

%description python
python components for the docutils package.


%package python3
Summary: python3 components for the docutils package.
Group: Default

%description python3
python3 components for the docutils package.


%prep
%setup -q -n docutils-0.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1506870075
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pushd test ; ./alltests.py ; popd
%install
export SOURCE_DATE_EPOCH=1506870075
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rst2html.py
/usr/bin/rst2html4.py
/usr/bin/rst2html5.py
/usr/bin/rst2latex.py
/usr/bin/rst2man.py
/usr/bin/rst2odt.py
/usr/bin/rst2odt_prepstyles.py
/usr/bin/rst2pseudoxml.py
/usr/bin/rst2s5.py
/usr/bin/rst2xetex.py
/usr/bin/rst2xml.py
/usr/bin/rstpep2html.py

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
