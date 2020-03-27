%global debug_package %{nil}
%global sname e-maj

Name:		emaj
Version:	3.3.0
Release:	1%{?dist}
Summary:	A table update logger for PostgreSQL
License:	GPLv2
URL:		https://pgxn.org/dist/%{sname}/
Source0:	https://api.pgxn.org/dist/%{sname}/%{version}/%{sname}-%{version}.zip

%description
E-Maj is a set of PL/pgSQL functions allowing PostgreSQL Database
Administrators to record updates applied on a set of tables, with
the capability to "rollback" these updates to a predefined point
in time.

%prep
%setup -q -n %{sname}-%{version}

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_datadir}/%{name}-%{version}/
%{__cp} -r sql %{buildroot}%{_datadir}/%{name}-%{version}/
%{__cp} %{name}.control %{buildroot}%{_datadir}/%{name}-%{version}/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGES.md doc LICENSE README.md
%dir %{_datadir}/%{name}-%{version}
%dir %{_datadir}/%{name}-%{version}/sql
%{_datadir}/%{name}-%{version}/%{name}.control
%{_datadir}/%{name}-%{version}/sql/*.sql

%changelog
* Fri Mar 27 2020 Devrim Gündüz <devrim@gunduz.org> - 3.3.0-1
- Update to 3.3.0

* Mon Nov 4 2019 Devrim Gündüz <devrim@gunduz.org> - 3.2.0-1
- Update to 3.2.0

* Sun Jun 23 2019 Devrim Gündüz <devrim@gunduz.org> - 3.1.0-1
- Update to 3.1.0

* Sun Mar 24 2019 Devrim Gündüz <devrim@gunduz.org> - 3.0.0-1
- Update to 3.0.0

* Mon Oct 15 2018 Devrim Gündüz <devrim@gunduz.org> - 2.3.1-1.1
- Rebuild against PostgreSQL 11.0

* Fri Sep 7 2018 Devrim Gündüz <devrim@gunduz.org> - 2.3.1-1
- Update to 2.3.1

* Wed Mar 14 2018 Devrim Gündüz <devrim@gunduz.org> - 2.2.3-1
- Update to 2.2.3

* Sat Jan 27 2018 Devrim Gündüz <devrim@gunduz.org> - 2.2.2-1
- Update to 2.2.2

* Tue Dec 26 2017 Devrim Gündüz <devrim@gunduz.org> - 2.2.1-1
- Update to 2.2.1

* Wed Dec 20 2017 Devrim Gündüz <devrim@gunduz.org> - 2.2.0-1
- Update to 2.2.0

* Thu Aug 3 2017 Devrim Gündüz <devrim@gunduz.org> - 2.1.0-1
- Update to 2.1.0

* Fri Feb 24 2017 Devrim Gündüz <devrim@gunduz.org> - 2.0.1-1
- Update to 2.0.1

* Wed Nov 16 2016 Devrim Gündüz <devrim@gunduz.org> - 2.0.0-1
- Update to 2.0.0

* Sat Sep 17 2016 Devrim Gündüz <devrim@gunduz.org> - 1.3.1-1
- Update to 1.3.1

* Mon Jan 4 2016 Devrim Gündüz <devrim@gunduz.org> - 1.2.0-1
- Update to 1.2.0

* Mon Nov 9 2015 Devrim Gündüz <devrim@gunduz.org> - 1.1.0-2
- Fixes for Fedora 23 and new doc layout in 9.5.

* Wed Jan 22 2014 Devrim Gündüz <devrim@gunduz.org> - 1.1.0-1
- Update to 1.1.0

* Mon Jan 7 2013 Devrim Gündüz <devrim@gunduz.org> - 1.0.1-1
- Update to 1.0.1

* Tue Dec 11 2012 Devrim Gündüz <devrim@gunduz.org> - 1.0.0-1
- Initial RPM packaging for PostgreSQL RPM repository.
