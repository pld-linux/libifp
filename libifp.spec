Summary:	iRiver driver library
Summary(pl):	Biblioteka sterownika iRiver
Name:		libifp
Version:	1.0.0.1
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/ifp-driver/%{name}-%{version}.tar.gz
# Source0-md5:	3b692cc224391b5714f5a8fbb8abf85b
URL:		http://ifp-driver.sourceforge.net/libifp/
BuildRequires:	libusb-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An interface for iRiver's flash-based portable music players.

%description -l pl
Interfejs do opartych na flashu przeno¶nych odtwarzaczy muzyki iRiver.

%package devel
Summary:	The files needed for development of applications that use libifp
Summary(pl):	Pliki potrzebne do tworzenia aplikacji u¿ywaj±cych libifp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Headers needed for development of applications that use libifp.

%description devel -l pl
Pliki nag³ówkowe potrzebne do tworzenia aplikacji u¿ywaj±cych libifp.

%package static
Summary:	Static libifp library
Summary(pl):	Statyczna biblioteka libifp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libifp library.

%description static -l pl
Statyczna biblioteka libifp.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%attr(755,root,root) %{_bindir}/ifpline
%attr(755,root,root) %{_libdir}/libifp.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libifp.so
%{_libdir}/libifp.la
%{_includedir}/*.h
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libifp.a
