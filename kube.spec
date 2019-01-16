#define stable ([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
# sink doesn't follow KDE's usual versioning scheme yet, it's always unstable
%define stable unstable

Name:           kube
Version:        0.7.0
Release:        1
Summary:        The Kube email client

Group:          Applications/Desktop
License:        GPL
URL:            https://www.kube-project.com/
Source0:        http://download.kde.org/%{stable}/kube/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  cmake ninja
BuildRequires:  cmake(ECM)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5Mime)
BuildRequires:	cmake(KF5CalendarCore)
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
BuildRequires:	lmdb-devel
BuildRequires:	gpgme-devel

%description
The Kube email client

%prep
%setup -q
%cmake_kde5

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
