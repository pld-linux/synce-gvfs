# TODO:
#	- doesn't work (Mount failed: DBus error org.freedesktop.DBus.Error.InvalidArgs: 
#         Argument 5 is specified to be of type "s", but is actually of type "b")
#	- probably bogus BR: libstdc++-devel
#
Summary:	GVFS module for accessing Windows CE and Pocket PC devices
Summary(pl.UTF-8):	Moduł GVFS służący do dostępu do urządzeń Windows CE i Pocket PC
Name:		synce-gvfs
Version:	0.1
Release:	0.1
License:	LGPL v2
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	0ab01d4c520f7c1f419cfcd6e014f340
URL:		http://www.synce.org/
BuildRequires:	gettext-devel
BuildRequires:	gvfs-devel
BuildRequires:	intltool
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	synce-librapi2-devel
%requires_eq_to	synce-librapi2 synce-librapi2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SynCE-GVFS is a GVFS module for accessing Windows CE and Pocket PC
devices. It is part of the SynCE project: <http://www.synce.org/>.

%description -l pl.UTF-8
SynCE-GVFS to moduł GVFS służący do dostępu do urządzeń Windows CE i
Pocket PC. Jest on częścią projektu SynCE: <http://www.synce.org/>.

%prep
%setup -q

%build
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/gvfsd-synce
%{_iconsdir}/gnome/*/apps/synce-gvfs.png
%{_datadir}/gvfs/mounts/synce.mount
