Summary:	Isometric WorldForge client
Summary(pl):	Izometryczny klient WorldForge
Name:		uclient
Version:	0.14.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	ftp://victor.worldforge.org/pub/worldforge/clients/uclient/%{name}-%{version}.tar.gz
Patch0:		%{name}-am.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	janus-devel
BuildRequires:	libxml-devel
BuildRequires:	python-devel
Requires:	%{name}-libs = %{version}
Requires:	%{name}-media
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_datadir	/usr/share

%description
UCLIENT is an isometric WorldForge client with items and tiles based
on a 2:1 iso perspective.

%description -l pl
UCLIENT to izometryczny klient WorldForge z przedmiotami i kaflami
bazuj±cymi na perspektywie iso 2:1.

%package libs
Summary:	UCLIENT libraries
Summary(pl):	Biblioteki UCLIENT
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…

%description libs
UCLIENT is an isometric WorldForge client with items and tiles based
on a 2:1 iso perspective.

This package contains the libraries used by UCLIENT program.

%description libs -l pl
UCLIENT to izometryczny klient WorldForge z przedmiotami i kaflami
bazuj±cymi na perspektywie iso 2:1.

Ten pakiet zawiera biblioteki uøywane przez program UCLIENT.

%package devel
Summary:	UCLIENT header files for development
Summary(pl):	Pliki nag≥Ûwkowe UCLIENT
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	janus-devel
Requires:	libxml-devel
Requires:	python-devel

%description devel
UCLIENT is an isometric WorldForge client with items and tiles based
on a 2:1 iso perspective.

This package contains the header files needed to develop programs that
use UCLIENT libraries.

%description devel -l pl
Ten pakiet zawiera pliki nag≥Ûwkowe do tworzenia programÛw z uøyciem
bibliotek UCLIENT.

%prep
%setup -q
%patch0 -p1

%build
aclocal
autoheader
libtoolize --automake --copy --force
automake --add-missing --copy --gnu --force
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -m 755 registry/Registry.la $RPM_BUILD_ROOT%{_libdir}/Registry.la
install -m 755 registry/.libs/Registry.so.0.0.0U \
	       $RPM_BUILD_ROOT%{_libdir}/Registry.so.0.0.0
ln -sf Registry.so.0.0.0 $RPM_BUILD_ROOT%{_libdir}/Registry.so.0
ln -sf Registry.so.0.0.0 $RPM_BUILD_ROOT%{_libdir}/Registry.so

gzip -9 AUTHORS README* userdoc.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/forge
%attr(755,root,root) %{_datadir}/forge/*.sh
%{_datadir}/uclient
# ???!!! it should be moved to /var! In /usr nothing should be modified at runtime.
%dir /usr/X11R6/share/var
%attr(777,root,root) %dir /usr/X11R6/share/var/uclient

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*
%attr(755,root,root) %{_libdir}/Bogo.so
%attr(755,root,root) %{_libdir}/Testmod.so
%{_libdir}/App.so
%{_libdir}/CharStats.so
%{_libdir}/Console.so
%{_libdir}/Dialogs.so
%{_libdir}/Environment.so
%{_libdir}/Gui.so
%{_libdir}/Inventory.so
%{_libdir}/Music.so
%{_libdir}/Observer.so
%{_libdir}/Player.so
%{_libdir}/Registry.so
%{_libdir}/Renderer.so
%{_libdir}/Settings.so
%{_libdir}/Terrain.so
%{_libdir}/Viewport.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/dii
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/*.la
%{_libdir}/lib*.so
