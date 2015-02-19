Name:       plymouth
Summary:    Plymouth boot splash screen tools
Version:    0.9.0+git361cec
Release:    1
Group:      Base/Boot
License:    GPLv2
URL:        http://www.freedesktop.org/wiki/Software/Plymouth/
Source0:    %{name}-%{version}.tar.bz2

Requires:   libpng >= 1.2.16
BuildRequires: libpng-devel >= 1.2.16

%description
%{summary}

%package devel
Summary:    Plymouth development headers

%description devel
%{summary}

%package initrd-tools
Summary:    Plymouth development headers

%description initrd-tools
%{summary}

#not sure this themes packing is really needed..
%package themes
Summary:    Default plymouth themes

%description themes
%{summary}

%package systemd
Summary:    Plymouth systemd scripts

%description systemd
%{summary}

%prep
%setup -q -n %{name}-%{version}

%build
cd %{name}
%autogen   --enable-tracing \
           --with-logo=%{_datadir}/pixmaps/system-logo-white.png \
           --with-background-start-color-stop=0x0073B3 \
           --with-background-end-color-stop=0x00457E \
           --with-background-color=0x3391cd \
           --enable-gdm-transition \
           --with-system-root-install \
           --disable-gtk \
           --disable-drm \
           --disable-documentation \
           --enable-systemd-integration \
           --disable-pango



make %{?jobs:-j%jobs}
cd ..

%install

cd %{name}
rm -rf %{buildroot}
%make_install
cd ..

%files
%defattr(-,root,root,-)
/bin/*
/sbin/*

%{_sbindir}/*
%{_sysconfdir}/*
%{_includedir}/*

%files devel
%defattr(-,root,root,-)
%{_includedir}
%{_libdir}/*
/lib/libply*

%files initrd-tools
%defattr(-,root,root,-)
%{_libexecdir}/*

%files themes
%defattr(-,root,root,-)
%{_datadir}/*

# Fixme: don't own systemd default *target.wants directories..
%files systemd
%defattr(-,root,root,-)
/lib/systemd/system/*
