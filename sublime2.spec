%define ver 2.0.1
%define rel  1

Name:          sublime-text
Version:       %{ver}
Release:       1%{dist}
Summary:       Sublime Text is a sophisticated text editor for code, html and prose. You'll love the slick user interface and extraordinary features.
Group:         Applications/Editors
License:       Copyright Sublime HQ Pty Ltd
BuildArch:     %{_arch}
URL:           http://www.sublimetext.com
Source0:       %{name}-%{version}-%{_arch}.tar.bz2
Source1:       %{name}.desktop
BuildRoot:     %{_tmppath}/%{name}.%{version}-%{release}
Requires:      python
%description
Sublime Text is a sophisticated text editor for code, html and prose. You'll love the slick user interface and extraordinary features.

%prep
%setup -c -n %{name}-%{version}-%{_arch}

%build

%install
rm -rf %{buildroot}
%{__mkdir_p}  %{buildroot}/usr/local/%{name}
%{__mkdir_p}  %{buildroot}%{_datadir}/applications
%{__mkdir_p}  %{buildroot}/usr/bin
%{__cp} -aR ./Sublime\ Text\ 2/* %{buildroot}/usr/local/%{name}/
%{__chmod} 755 %{buildroot}/usr/local/%{name}/sublime_text
for res in 128x128 16x16 256x256 32x32 48x48; do
    %{__mkdir_p}  %{buildroot}/usr/share/icons/hicolor/$res/apps/
    %{__cp} -aR %{_builddir}/%{name}-%{version}-%{_arch}/Sublime\ Text\ 2/Icon/$res/* %{buildroot}/usr/share/icons/hicolor/$res/apps/
done
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{SOURCE1}
cd %{buildroot}/usr/bin
%{__ln_s} /usr/local/%{name}/sublime_text subl

%clean
%{__rm} -rf %{_builddir}

%files
%defattr(-,root,root,-)
/usr/local/%{name}/
/usr/share/applications/sublime-text.desktop
/usr/share/icons/
/usr/bin/subl

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :

%changelog
* Mon Apr 09 2012 Stefan Kirrmann <stefan.kirrmann@gmail.com> - 2210
- RPM created from release 2.0
