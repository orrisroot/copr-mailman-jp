%global pypi_name cchardet

# nose dependency for the unit tests
# https://github.com/PyYoshi/cChardet/issues/63
Name:           python-%{pypi_name}
Version:        2.1.7
Release:        4.1%{?dist}.ors
Summary:        High speed universal character encoding detector

License:        MPLv1.1 or GPLv2 or LGPLv2
URL:            https://github.com/PyYoshi/cChardet
Source0:        %{pypi_source}

BuildRequires:  gcc-c++
# https://github.com/PyYoshi/cChardet/issues/62
#BuildRequires:  uchardet-devel

Provides:       bundle(uchardet)

%description
cChardet is high speed universal character encoding detector.

%package -n     python2-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
cChardet is high speed universal character encoding detector.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# Remove bundled uchardet
#rm -rf src/ext

%build
%py2_build

%install
%py2_install

%files -n python2-%{pypi_name}
%doc README.rst src/ext/uchardet/README.md src/ext/uchardet/doc/README.maintainer
%license COPYING
%{_bindir}/cchardetect
%{python2_sitearch}/%{pypi_name}/
%{python2_sitearch}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Tue Nov 09 2021 Yoshihiro OKUMURA <orrisroot@gmail.com> - 2.1.7-4.1
- Rebuild for EPEL 8

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.7-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.7-1
- Update to latest upstream release 2.1.7 (#1892241)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.6-3
- Rebuilt for Python 3.9

* Sun May 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.6-2
- Add comment about nose
- Update license tag (#1834977)

* Tue May 05 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.6-1
- Initial package for Fedora
