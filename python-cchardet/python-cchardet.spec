%global srcname cchardet

Name:           python-%{srcname}
Version:        2.1.1
Release:        1%{?dist}.ors
Summary:        High speed universal character encoding detector for python

Group:          Development/Languages
License:        MPL
URL:            https://github.com/PyYoshi/cChardet
Source0:        https://pypi.python.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz


%global _description %{expand:
cChardet is high speed universal character encoding detector for python,
binding to charsetdetect.}

%description %_description


%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel, python2-setuptools, python2-Cython 
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build

%install
%py2_install
 

%files -n python2-%{srcname}
%defattr(-,root,root,-)
%doc README.rst CHANGES.rst COPYING
%{_bindir}/cchardetect
%{python2_sitearch}/%{srcname}*


%changelog
* Mon Apr 06 2020 Yoshihiro OKUMURA <orrisroot@gmail.com> - 2.1.1-1
- Rebuild for CentOS 8

* Sat Jul 01 2017 Yasuhito FUTATSUKI <futatuki@poem.co.jp> - 2.1.1
- upgrade to 2.1.1

* Fri Jun 30 2017 Yasuhito FUTATSUKI <futatuki@poem.co.jp> - 2.1.0
- upgrade to 2.1.0

* Fri Sep 11 2015 Yasuhito FUTATSUKI <futatuki@poem.co.jp> - 1.0.0
- upgrade to 1.0.0

* Mon Oct 27 2014 Yasuhito FUTATSUKI <futatuki@poem.co.jp>
- Rebuild for CentOS 7.0

* Wed Apr 30 2014 Yasuhito FUTATSUKI <futatuki@poem.co.jp> - 0.3.5
- Initial build.
