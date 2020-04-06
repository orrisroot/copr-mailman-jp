%global srcname pykf

Name:           python-%{srcname}
Version:        0.4
Release:        1%{?dist}.ors
Summary:        Japanese character encoding converter for Python

Group:          Development/Languages
License:        MIT
URL:            http://sourceforge.jp/projects/pykf/
Source:         https://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

%global _description %{expand:
pykf is Japanese character encodings(ShiftJIS, JIS, EUC-JP) converter
for Python. See readme.sjis for detail.}

%description %_description

%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel, python2-setuptools
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
%doc README readme.sjis
%{python2_sitearch}/%{srcname}*


%changelog
* Mon Apr 06 2020 Yoshihiro OKUMURA <orrisroot@gmail.com> - 0.4-1
- Rebuild for CentOS 8

* Mon Oct 27 2014 Yasuhito FUTATSUKI <futatuki@poem.co.jp>
- Rebuild for CentOS 7.0

* Tue Apr 22 2014 Yasuhito FUTATSUKI <futatuki@poem.co.jp> - 0.4
- Initial build.
