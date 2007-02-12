Summary:	Isometric WorldForge client
Summary(pl.UTF-8):	Izometryczny klient WorldForge
Name:		uclient
Version:	0.15.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://victor.worldforge.org/pub/worldforge/clients/uclient/%{name}-%{version}.tar.gz
# Source0-md5:	492d89d9ce5c6df13fc586ddec70f0a0
Patch0:		%{name}-am.patch
Patch1:		%{name}-vardir.patch
Patch2:		%{name}-gcc-3.3.patch
Patch3:		%{name}-overload.patch
BuildRequires:	Atlas-C++-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	janus-devel
BuildRequires:	libxml-devel
BuildRequires:	python-devel
BuildRequires:	skstream-devel
BuildRequires:	varconf-devel
Requires:	%{name}-media
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	/usr/share

%description
UCLIENT is an isometric WorldForge client with items and tiles based
on a 2:1 iso perspective.

%description -l pl.UTF-8
UCLIENT to izometryczny klient WorldForge z przedmiotami i kaflami
bazującymi na perspektywie iso 2:1.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -f missing
%{__aclocal}
%{__autoheader}
%{__libtoolize}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README* userdoc.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/forge
%attr(755,root,root) %{_datadir}/forge/*.sh
%{_datadir}/uclient
%attr(777,root,root) %dir %{_var}/games/uclient
