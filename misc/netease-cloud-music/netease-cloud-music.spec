%global debug_package %{nil}

Name:           netease-cloud-music
Version:        1.1.3.2
Release:        1%{?dist}
Summary:        Netease Cloud Music client
License:        EULA
URL:            https://music.163.com/
Source0:        https://packages.deepin.com/deepin/pool/main/n/%{name}/%{name}_%{version}_amd64.deb
Source1:        https://music.163.com/html/web2/service.html

ExclusiveArch:  x86_64

BuildRequires:  dpkg
BuildRequires:  desktop-file-utils

Requires:       desktop-file-utils
Requires:       gstreamer1-plugins-ugly

%description
Netease Cloud Music client, converted from official deb package.

%prep
dpkg -X %{S:0} .
find usr -type f -exec mv {} . \;
cp %{S:1} %{_builddir}

%build
# nothing to build

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 %{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.md changelog.gz
%license copyright service.html
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
