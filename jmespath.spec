#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jmespath
Version  : 0.9.0
Release  : 8
URL      : https://pypi.python.org/packages/source/j/jmespath/jmespath-0.9.0.tar.gz
Source0  : https://pypi.python.org/packages/source/j/jmespath/jmespath-0.9.0.tar.gz
Summary  : JSON Matching Expressions
Group    : Development/Tools
License  : MIT
Requires: jmespath-bin
Requires: jmespath-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
JMESPath
========
.. image:: https://badges.gitter.im/Join Chat.svg
:target: https://gitter.im/jmespath/chat

%package bin
Summary: bin components for the jmespath package.
Group: Binaries

%description bin
bin components for the jmespath package.


%package python
Summary: python components for the jmespath package.
Group: Default

%description python
python components for the jmespath package.


%prep
%setup -q -n jmespath-0.9.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jp.py

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
