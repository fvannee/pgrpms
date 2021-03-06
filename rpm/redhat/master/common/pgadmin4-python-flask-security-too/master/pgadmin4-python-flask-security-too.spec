%global mod_name Flask-Security-Too
%global sname	flask-security-too

%global pgadmin4py3instdir %{python3_sitelib}/pgadmin4-web/

%if 0%{?fedora} > 27 || 0%{?rhel} >= 7
%{!?with_python3:%global with_python3 1}
%global __ospython %{_bindir}/python3
%{expand: %%global pyver %(echo `%{__ospython} -c "import sys; sys.stdout.write(sys.version[:3])"`)}
%global python3_sitelib %(%{__ospython} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
%global python3_sitelib64 %(%{__ospython} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")
%endif

Name:		pgadmin4-python3-%{sname}
Summary:	Quickly add security features to your Flask application
Version:	3.3.3
Release:	1%{?dist}
License:	Python
URL:		https://pypi.python.org/pypi/%{mod_name}
Source0:	https://files.pythonhosted.org/packages/source/F/%{mod_name}/%{mod_name}-%{version}.tar.gz

BuildArch:	noarch

Obsoletes:	pgadmin4-python-flask-security

%if 0%{?fedora} > 27 || 0%{?rhel} >= 7
BuildRequires:	python3-devel python3-setuptools
%endif

%description
This is a independently maintained version of Flask-Security based on
the 3.0.0 version Flask-Security.

%prep
%setup -q -n %{mod_name}-%{version}
# Remove irrelevant files:
find . -name "*DS_Store*" -exec rm -rf {} \;

%build
%{__ospython} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__ospython} setup.py install -O1 --skip-build --root %{buildroot}

# Move everything under pgadmin4 web/ directory.
%{__mkdir} -p %{buildroot}/%{pgadmin4py3instdir}
%{__mv} %{buildroot}%{python3_sitelib}/flask_security %{buildroot}%{python3_sitelib}/Flask_Security_Too-%{version}-py%{pyver}.egg-info %{buildroot}/%{pgadmin4py3instdir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc README.rst
%{pgadmin4py3instdir}/flask_security
%{pgadmin4py3instdir}/Flask_Security_Too-%{version}-py%{pyver}.egg-info

%changelog
* Fri Feb 28 2020 Devrim Gündüz <devrim@gunduz.org> - 3.3.3-1
- Initial version for PostgreSQL RPM repository to satisfy
  pgadmin4 dependency.
