# NOTES
# - gvfs interface is still experimental and has no public interface, therefore
#   source it's source is needed to build. see README for details
#
Summary:	GVFS module for accessing Windows CE and Pocket PC devices
Summary(pl.UTF-8):	Moduł GVFS służący do dostępu do urządzeń Windows CE i Pocket PC
Name:		synce-gvfs
Version:	0.7.2
Release:	1
License:	LGPL v2+
Group:		Applications/Communications
Source0:	http://downloads.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	c7967c73debdedb47ea0c0317f9b40ce
%define	gvfs_ver	1.22.3
Source1:	http://ftp.gnome.org/pub/GNOME/sources/gvfs/1.22/gvfs-%{gvfs_ver}.tar.xz
# Source1-md5:	7e6d026addb1658fb24b39e8827d7650
URL:		http://www.synce.org/
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.26
# for private libgvfscommon.so shared library (API taken from gvfs source)
BuildRequires:	gvfs-libs >= %{gvfs_ver}
BuildRequires:	intltool >= 0.35.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.559
BuildRequires:	synce-core-lib-devel >= 0.17
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	shared-mime-info
Requires:	glib2 >= 1:2.26
Requires:	gvfs >= %{gvfs_ver}
Requires:	synce-core-lib >= 0.17
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
GVFS_SOURCE=$(pwd)/gvfs-%{gvfs_ver}
LDFLAGS="%{rpmldflags} -L%{_libdir}/gvfs"
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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/gvfsd-synce
%{_iconsdir}/gnome/*/apps/synce-gvfs.png
%{_datadir}/gvfs/mounts/synce.mount
%{_datadir}/mime/packages/synce-gvfs.xml
