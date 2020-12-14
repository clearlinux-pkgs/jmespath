#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jmespath
Version  : 0.9.5
Release  : 46
URL      : https://files.pythonhosted.org/packages/5c/40/3bed01fc17e2bb1b02633efc29878dfa25da479ad19a69cfb11d2b88ea8e/jmespath-0.9.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/5c/40/3bed01fc17e2bb1b02633efc29878dfa25da479ad19a69cfb11d2b88ea8e/jmespath-0.9.5.tar.gz
Summary  : JSON Matching Expressions
Group    : Development/Tools
License  : MIT
Requires: jmespath-bin = %{version}-%{release}
Requires: jmespath-license = %{version}-%{release}
Requires: jmespath-python = %{version}-%{release}
Requires: jmespath-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
========

%package bin
Summary: bin components for the jmespath package.
Group: Binaries
Requires: jmespath-license = %{version}-%{release}

%description bin
bin components for the jmespath package.


%package license
Summary: license components for the jmespath package.
Group: Default

%description license
license components for the jmespath package.


%package python
Summary: python components for the jmespath package.
Group: Default
Requires: jmespath-python3 = %{version}-%{release}

%description python
python components for the jmespath package.


%package python3
Summary: python3 components for the jmespath package.
Group: Default
Requires: python3-core
Provides: pypi(jmespath)

%description python3
python3 components for the jmespath package.


%prep
%setup -q -n jmespath-0.9.5
cd %{_builddir}/jmespath-0.9.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603394053
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jmespath
cp %{_builddir}/jmespath-0.9.5/LICENSE.txt %{buildroot}/usr/share/package-licenses/jmespath/c012ed6967c9b5f4a93271c9b3132bcbd76320e0
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jp.py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jmespath/c012ed6967c9b5f4a93271c9b3132bcbd76320e0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
