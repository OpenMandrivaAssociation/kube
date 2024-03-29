#define stable ([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
# sink doesn't follow KDE's usual versioning scheme yet, it's always unstable
%define stable unstable
%define snapshot 20230809

Name:           kube
Version:        0.9.1
Summary:        The Kube email client

Group:          Applications/Desktop
License:        GPL
URL:            https://www.kube-project.com/
%if 0%{snapshot}
Release:	0.%{snapshot}.1
# https://invent.kde.org/pim/kube
Source0:	https://invent.kde.org/pim/kube/-/archive/master/kube-master.tar.bz2
%else
Release:        1
#Source0:        http://download.kde.org/%{stable}/kube/%{version}/src/%{name}-%{version}.tar.xz
Source0:        https://invent.kde.org/pim/kube/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
%endif

#Patch0:		kube-0.8.1-compile.patch

BuildRequires:  cmake ninja
BuildRequires:  cmake(ECM)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5Mime)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5Sonnet)
BuildRequires:  cmake(KF5SonnetUi)
BuildRequires:	cmake(KAsync)
BuildRequires:	cmake(KPimKDAV2)
BuildRequires:	cmake(KIMAP2)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(Qt5WebEngine)
BuildRequires:	cmake(Qt5WebEngineWidgets)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5QuickTest)
BuildRequires:	cmake(Sink)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libgit2)
BuildRequires:	pkgconfig(readline)
BuildRequires:	pkgconfig(libunwind)
BuildRequires:	lmdb-devel
BuildRequires:	gpgme-devel
BuildRequires:	%mklibname -d binutils

%description
The Kube email client

%prep
%if 0%{snapshot}
%autosetup -p1 -n %{name}-master
%else
%autosetup -p1 -n %{name}-v%{version}
%endif
# The default value for KUBE_DESKTOPFILE_CATEGORIES is
# KUBE_DESKTOPFILE_CATEGORIES:STRING=Qt;KDE;Office;Network;Email;
# We remove Office to avoid a nasty duplicate icon in Plasma Mobile
# until this is fixed properly.
%cmake_kde5 \
	-DKUBE_DESKTOPFILE_CATEGORIES:STRING="Qt;KDE;Network;Email;"

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/kube
%{_libdir}/libkubeframework.so
%{_libdir}/qt5/qml/org/kube
%{_datadir}/appdata/org.kde.kube.appdata.xml
%{_datadir}/applications/org.kde.kube.desktop
%{_datadir}/icons/*/*/apps/kube*.*
%{_datadir}/kube
