#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x89EFD588E975D6DF (rbtcollins@hp.com)
#
Name     : testrepository
Version  : 0.0.20
Release  : 53
URL      : http://pypi.debian.net/testrepository/testrepository-0.0.20.tar.gz
Source0  : http://pypi.debian.net/testrepository/testrepository-0.0.20.tar.gz
Source1  : http://pypi.debian.net/testrepository/testrepository-0.0.20.tar.gz.asc
Summary  : A repository of test results.
Group    : Development/Tools
License  : Apache-2.0
Requires: testrepository-bin = %{version}-%{release}
Requires: testrepository-license = %{version}-%{release}
Requires: testrepository-python = %{version}-%{release}
Requires: testrepository-python3 = %{version}-%{release}
Requires: fixtures
Requires: python-subunit
Requires: testtools
BuildRequires : buildreq-distutils3
BuildRequires : extras
BuildRequires : fixtures
BuildRequires : linecache2
BuildRequires : pytest
BuildRequires : python-mimeparse
BuildRequires : python-subunit
BuildRequires : pytz
BuildRequires : six
BuildRequires : testresources
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : traceback2
BuildRequires : unittest2

%description
+++++++++++++++
        
        Overview
        ~~~~~~~~
        
        This project provides a database of test results which can be used as part of

%package bin
Summary: bin components for the testrepository package.
Group: Binaries
Requires: testrepository-license = %{version}-%{release}

%description bin
bin components for the testrepository package.


%package license
Summary: license components for the testrepository package.
Group: Default

%description license
license components for the testrepository package.


%package python
Summary: python components for the testrepository package.
Group: Default
Requires: testrepository-python3 = %{version}-%{release}

%description python
python components for the testrepository package.


%package python3
Summary: python3 components for the testrepository package.
Group: Default
Requires: python3-core
Provides: pypi(testrepository)
Requires: pypi(fixtures)
Requires: pypi(python_subunit)
Requires: pypi(testtools)

%description python3
python3 components for the testrepository package.


%prep
%setup -q -n testrepository-0.0.20
cd %{_builddir}/testrepository-0.0.20

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603405833
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/testrepository
cp %{_builddir}/testrepository-0.0.20/Apache-2.0 %{buildroot}/usr/share/package-licenses/testrepository/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/testrepository-0.0.20/COPYING %{buildroot}/usr/share/package-licenses/testrepository/92e73d261542eaa865b52c203f3b6dd549f9fda3
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/testr

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/testrepository/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/testrepository/92e73d261542eaa865b52c203f3b6dd549f9fda3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
