Summary:	iRiver driver library
Summary(pl.UTF-8):	Biblioteka sterownika iRiver
Name:		libifp
Version:	1.0.0.2
Release:	4
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/ifp-driver/%{name}-%{version}.tar.gz
# Source0-md5:	d4114794b13bd32b6b767e0870df6fc4
URL:		http://ifp-driver.sourceforge.net/libifp/
BuildRequires:	doxygen
BuildRequires:	libusb-compat-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An interface for iRiver's flash-based portable music players.

%description -l pl.UTF-8
Interfejs do opartych na flashu przenośnych odtwarzaczy muzyki iRiver.

%package devel
Summary:	The files needed for development of applications that use libifp
Summary(pl.UTF-8):	Pliki potrzebne do tworzenia aplikacji używających libifp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libusb-compat-devel

%description devel
Headers needed for development of applications that use libifp.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do tworzenia aplikacji używających libifp.

%package static
Summary:	Static libifp library
Summary(pl.UTF-8):	Statyczna biblioteka libifp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libifp library.

%description static -l pl.UTF-8
Statyczna biblioteka libifp.

%prep
%setup -q

%build
%configure \
	--with-libusb
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man3
install docs/man/man3/* $RPM_BUILD_ROOT%{_mandir}/man3

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
%{_mandir}/man3/ifp.h.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libifp.a
