#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : docutils
Version  : 0.15.2
Release  : 59
URL      : https://files.pythonhosted.org/packages/93/22/953e071b589b0b1fee420ab06a0d15e5aa0c7470eb9966d60393ce58ad61/docutils-0.15.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/93/22/953e071b589b0b1fee420ab06a0d15e5aa0c7470eb9966d60393ce58ad61/docutils-0.15.2.tar.gz
Summary  : Docutils -- Python Documentation Utilities
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause GPL-2.0 Public-Domain Python-2.0
Requires: docutils-bin = %{version}-%{release}
Requires: docutils-python = %{version}-%{release}
Requires: docutils-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Docutils is a modular system for processing documentation
into useful formats, such as HTML, XML, and LaTeX.  For
input Docutils supports reStructuredText, an easy-to-read,
what-you-see-is-what-you-get plaintext markup syntax.

%package bin
Summary: bin components for the docutils package.
Group: Binaries

%description bin
bin components for the docutils package.


%package python
Summary: python components for the docutils package.
Group: Default
Requires: docutils-python3 = %{version}-%{release}

%description python
python components for the docutils package.


%package python3
Summary: python3 components for the docutils package.
Group: Default
Requires: python3-core
Provides: pypi(docutils)

%description python3
python3 components for the docutils package.


%prep
%setup -q -n docutils-0.15.2
cd %{_builddir}/docutils-0.15.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583332668
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
cp %{buildroot}/usr/bin/rst2man.py %{buildroot}/usr/bin/rst2man
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rst2html.py
/usr/bin/rst2html4.py
/usr/bin/rst2html5.py
/usr/bin/rst2latex.py
/usr/bin/rst2man
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

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
