%global	sname	safeupdate

Summary:	A simple extension to PostgreSQL that requires criteria for UPDATE and DELETE

Name:		%{sname}_%{pgmajorversion}
Version:	1.2
Release:	1%{?dist}
License:	ISC
URL:		https://github.com/eradman/pg-safeupdate
Source0:	https://github.com/eradman/pg-safeupdate/archive/%{version}.tar.gz
Patch0:		%{sname}-pg%{pgmajorversion}-makefile-pgxs.patch

%description
safeupdate is a simple extension to PostgreSQL that raises an error if UPDATE
and DELETE are executed without specifying conditions. This extension was
initially designed to protect data from accidental obliteration of data that
is writable by PostgREST.

%prep
%setup -q -n pg-%{sname}-%{version}
%patch0 -p0

%build
USE_PGXS=1 %{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
USE_PGXS=1 %{__make} %{?_smp_mflags} DESTDIR=%{buildroot} install


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{pginstdir}/lib/%{sname}.so
%ifarch ppc64 ppc64le
 %else
 %if %{pgmajorversion} >= 11 && %{pgmajorversion} < 90
  %if 0%{?rhel} && 0%{?rhel} <= 6
  %else
   %{pginstdir}/lib/bitcode/%{sname}*.bc
   %{pginstdir}/lib/bitcode/%{sname}/*.bc
  %endif
 %endif
%endif

%changelog
* Fri Aug 30 2019 Devrim Gündüz <devrim@gunduz.org> - 1.2-1
- Initial RPM packaging for PostgreSQL RPM Repository