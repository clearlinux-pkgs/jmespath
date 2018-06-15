#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jmespath
Version  : 0.9.3
Release  : 24
URL      : http://pypi.debian.net/jmespath/jmespath-0.9.3.tar.gz
Source0  : http://pypi.debian.net/jmespath/jmespath-0.9.3.tar.gz
Summary  : JSON Matching Expressions
Group    : Development/Tools
License  : MIT
Requires: jmespath-bin
Requires: jmespath-python3
Requires: jmespath-python
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
========

%package bin
Summary: bin components for the jmespath package.
Group: Binaries

%description bin
bin components for the jmespath package.


%package legacypython
Summary: legacypython components for the jmespath package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the jmespath package.


%package python
Summary: python components for the jmespath package.
Group: Default
Requires: jmespath-python3

%description python
python components for the jmespath package.


%package python3
Summary: python3 components for the jmespath package.
Group: Default
Requires: python3-core

%description python3
python3 components for the jmespath package.


%prep
%setup -q -n jmespath-0.9.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519344781
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1519344781
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
/usr/bin/jp.py

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
