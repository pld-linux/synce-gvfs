# TODO:
#	- probably bogus BR: libstdc++-devel
# NOTES
# - gvfs interface is still experimental and has no public interface, therefore
#   source it's source is needed to build. see README for details
#
Summary:	GVFS module for accessing Windows CE and Pocket PC devices
Summary(pl.UTF-8):	Moduł GVFS służący do dostępu do urządzeń Windows CE i Pocket PC
Name:		synce-gvfs
Version:	0.4
Release:	1
License:	LGPL v2
Group:		Applications/Communications
Source0:	http://downloads.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	78c4133f0a43859c0fa45ead9c44f62c
Source1:	http://ftp.gnome.org/pub/GNOME/sources/gvfs/1.6/gvfs-1.6.2.tar.bz2
# Source1-md5:	6ed1d943d1c1b8b15a6b180a6cd51043
URL:		http://www.synce.org/
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.18
BuildRequires:	gvfs-devel
BuildRequires:	intltool
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	synce-librapi2-devel >= 0.12
%requires_eq_to	synce-librapi2 synce-librapi2-devel
Requires(post,postun):  shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SynCE-GVFS is a GVFS module for accessing Windows CE and Pocket PC
devices. It is part of the SynCE project: <http://www.synce.org/>.

%description -l pl.UTF-8
SynCE-GVFS to moduł GVFS służący do dostępu do urządzeń Windows CE i
Pocket PC. Jest on częścią projektu SynCE: <http://www.synce.org/>.

%prep
%setup -q -a1

%build
GVFS_SOURCE=$(echo gvfs-*)
%configure \
	--with-gvfs-source=$GVFS_SOURCE \
	--disable-update-mime-database \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database

%postun
%update_mime_database

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/gvfsd-synce
%{_iconsdir}/gnome/*/apps/synce-gvfs.png
%{_datadir}/gvfs/mounts/synce.mount
%{_datadir}/mime/packages/synce-gvfs.xml
