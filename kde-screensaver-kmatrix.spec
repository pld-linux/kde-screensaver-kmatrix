Summary:	KMatrix3D - OpenGL screensaver for KDE
Summary(de.UTF-8):	KMatrix3D - ein KDE Bildschirmschoner
Summary(pl.UTF-8):	KMatrix3D - wygaszacz ekranu oparty na OpenGL dla KDE
%define		vendor_name	kmatrix3d
Name:		kde-screensaver-%{vendor_name}
Version:	0.1
Release:	2
License:	GPL
Group:		X11/Amusements
Source0:	http://dl.sourceforge.net/kmatrix3d/kmatrix3d-%{version}.tar.bz2
# Source0-md5:	18bfaecbdbb521a8a840e8bd80a70729
Patch0:		kde-am.patch
URL:		http://kmatrix3d.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.229
Requires:	kdebase-screensavers
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMatrix3D is an OpenGL screensaver for KDE.

%description -l de.UTF-8
KMatrix3D ist ein OpenGL KDE Bildschirmschoner.

%description -l pl.UTF-8
KMatrix3D to oparty na OpenGL wygaszacz ekranu dla KDE.

%prep
%setup -q -n %{vendor_name}
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kscreensaver

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	desktopdir=%{_datadir}/apps/kscreensaver

%find_lang kmatrix3d --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kmatrix3d.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{vendor_name}.kss
%{_datadir}/apps/%{vendor_name}
%{_datadir}/apps/kscreensaver/%{vendor_name}.desktop
