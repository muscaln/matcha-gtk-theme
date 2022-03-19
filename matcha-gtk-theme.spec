%global _version 2021-12-25

Name:           matcha-gtk-theme
Version:        20211225
Release:        1%{?dist}
Summary:        A flat design theme for GTK3, GTK2 and gnome-shell
License:        GPLv3
URL:            https://github.com/vinceliuice/Matcha-gtk-theme
BuildArch:      noarch
Source0:        https://github.com/vinceliuice/Matcha-gtk-theme/archive/%{_version}/%{name}-%{_version}.tar.gz

%description
Matcha is a flat Design theme for GTK 3, GTK 2 and Gnome-Shell which supports GTK 3 and GTK 2 based
desktop environments like Gnome, Unity, Budgie, Pantheon, XFCE, Mate, etc.

%prep
%autosetup -n Matcha-gtk-theme-%{_version}

%build
# nothing to build

%install
mkdir -p %{buildroot}/%{_datadir}/themes
./install.sh -d %{buildroot}/%{_datadir}/themes

%files
%license LICENSE
%{_datadir}/themes/Matcha*

%changelog
* Sat Mar 19 2022 Mustafa Çalışkan <muscaln@protonmail.com> - 20211225-1
- Initial package



