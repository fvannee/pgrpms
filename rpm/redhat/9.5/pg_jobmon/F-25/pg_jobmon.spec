%global pgmajorversion 95
%global pginstdir /usr/pgsql-9.5
%global sname pg_jobmon

Summary:	Job logging and monitoring extension for PostgreSQL
Name:		%{sname}%{pgmajorversion}
Version:	1.3.3
Release:	1%{?dist}
License:	BSD
Group:		Applications/Databases
Source0:	https://github.com/omniti-labs/%{sname}/archive/v%{version}.tar.gz
Patch0:		Makefile-pgxs.patch
URL:		https://github.com/omniti-labs/%{sname}
BuildRequires:	postgresql%{pgmajorversion}-devel
Requires:	postgresql%{pgmajorversion}-server
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
pg_jobmon is a job logging and monitoring extension for PostgreSQL.

%prep
%setup -q -n %{sname}-%{version}
%patch0 -p0

%build
make USE_PGXS=1 %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

make USE_PGXS=1 %{?_smp_mflags} install DESTDIR=%{buildroot}
install -d %{buildroot}%{pginstdir}/share/extension
install -m 755 README.md  %{buildroot}%{pginstdir}/doc/extension/README-%{sname}.md

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{pginstdir}/doc/extension/%{sname}.md
%doc %{pginstdir}/doc/extension/README-%{sname}.md
%{pginstdir}/share/extension/%{sname}*.sql
%{pginstdir}/share/extension/%{sname}.control

%changelog
* Thu Jul 7 2016 - Devrim Gündüz <devrim@gunduz.org> 1.3.3-1
- Update to 1.3.3
- Update URLs

* Tue Jan 26 2016 - Devrim Gündüz <devrim@gunduz.org> 1.3.2-1
- Update to 1.3.2
- Use the new directory for docs.

* Tue Apr 29 2014 - Devrim GUNDUZ <devrim@gunduz.org> 1.2.0-1
- Update to 1.2.0

* Thu Oct 31 2013 - Devrim GUNDUZ <devrim@gunduz.org> 1.1.3-1
- Initial RPM packaging for PostgreSQL RPM Repository
