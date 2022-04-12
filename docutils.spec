#
#
# Compat glue package

#
Name     : docutils
Version  : 0.18.1
Release  : 78
URL      : https://files.pythonhosted.org/packages/57/b1/b880503681ea1b64df05106fc7e3c4e3801736cf63deffc6fa7fc5404cf5/docutils-0.18.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/57/b1/b880503681ea1b64df05106fc7e3c4e3801736cf63deffc6fa7fc5404cf5/docutils-0.18.1.tar.gz
Summary  : Docutils -- Python Documentation Utilities
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause GPL-2.0 Public-Domain Python-2.0
Requires: docutils-bin = %{version}-%{release}
Requires: docutils-python = %{version}-%{release}
Requires: docutils-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Requires: pypi-docutils


%description
into useful formats, such as HTML, XML, and LaTeX.  For
        input Docutils supports reStructuredText, an easy-to-read,
        what-you-see-is-what-you-get plaintext markup syntax.


%prep
%setup -q -n docutils-0.18.1
cd %{_builddir}/docutils-0.18.1

%build

%install

%files
%defattr(-,root,root,-)

