#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : khangman
Version  : 24.08.0
Release  : 72
URL      : https://download.kde.org/stable/release-service/24.08.0/src/khangman-24.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.08.0/src/khangman-24.08.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.08.0/src/khangman-24.08.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: khangman-bin = %{version}-%{release}
Requires: khangman-data = %{version}-%{release}
Requires: khangman-license = %{version}-%{release}
Requires: khangman-locales = %{version}-%{release}
Requires: khangman-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : knotifications-dev
BuildRequires : libkeduvocdocument-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
24 July 2001
To run the game from cvs:
make -f Makefile.dist
./configure --prefix=/usr
make
su -c "make install"

%package bin
Summary: bin components for the khangman package.
Group: Binaries
Requires: khangman-data = %{version}-%{release}
Requires: khangman-license = %{version}-%{release}

%description bin
bin components for the khangman package.


%package data
Summary: data components for the khangman package.
Group: Data

%description data
data components for the khangman package.


%package doc
Summary: doc components for the khangman package.
Group: Documentation
Requires: khangman-man = %{version}-%{release}

%description doc
doc components for the khangman package.


%package license
Summary: license components for the khangman package.
Group: Default

%description license
license components for the khangman package.


%package locales
Summary: locales components for the khangman package.
Group: Default

%description locales
locales components for the khangman package.


%package man
Summary: man components for the khangman package.
Group: Default

%description man
man components for the khangman package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n khangman-24.08.0
cd %{_builddir}/khangman-24.08.0
pushd ..
cp -a khangman-24.08.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724651310
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1724651310
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/khangman
cp %{_builddir}/khangman-%{version}/COPYING %{buildroot}/usr/share/package-licenses/khangman/d357e60aa8efd63b4475c3363700ba54f9a71343 || :
cp %{_builddir}/khangman-%{version}/COPYING.DOC %{buildroot}/usr/share/package-licenses/khangman/1bd373e4851a93027ba70064bd7dbdc6827147e1 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang khangman
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/khangman
/usr/bin/khangman

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.khangman.desktop
/usr/share/config.kcfg/khangman.kcfg
/usr/share/icons/hicolor/128x128/apps/khangman.png
/usr/share/icons/hicolor/16x16/apps/khangman.png
/usr/share/icons/hicolor/22x22/apps/khangman.png
/usr/share/icons/hicolor/32x32/apps/khangman.png
/usr/share/icons/hicolor/48x48/apps/khangman.png
/usr/share/icons/hicolor/64x64/apps/khangman.png
/usr/share/icons/hicolor/scalable/apps/khangman.svgz
/usr/share/khangman/ca.txt
/usr/share/khangman/cs.txt
/usr/share/khangman/da.txt
/usr/share/khangman/de.txt
/usr/share/khangman/eo.txt
/usr/share/khangman/es.txt
/usr/share/khangman/et.txt
/usr/share/khangman/fi.txt
/usr/share/khangman/fonts/Domestic_Manners.ttf
/usr/share/khangman/fonts/Dustismo_Roman.ttf
/usr/share/khangman/fr.txt
/usr/share/khangman/ga.txt
/usr/share/khangman/gl.txt
/usr/share/khangman/hu.txt
/usr/share/khangman/nb.txt
/usr/share/khangman/nds.txt
/usr/share/khangman/nn.txt
/usr/share/khangman/pl.txt
/usr/share/khangman/pt.txt
/usr/share/khangman/pt_BR.txt
/usr/share/khangman/sk.txt
/usr/share/khangman/sl.txt
/usr/share/khangman/sr@ijekavianlatin.txt
/usr/share/khangman/sr@latin.txt
/usr/share/khangman/sv.txt
/usr/share/khangman/tg.txt
/usr/share/khangman/themes/khangman_bees.svg
/usr/share/khangman/themes/khangman_desert.svg
/usr/share/khangman/themes/khangman_notes.png
/usr/share/khangman/themes/khangman_sea.svg
/usr/share/khangman/themes/khangman_winter.svg
/usr/share/khangman/themes/standardthemes.xml
/usr/share/khangman/tr.txt
/usr/share/knsrcfiles/khangman.knsrc
/usr/share/metainfo/org.kde.khangman.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/khangman/index.cache.bz2
/usr/share/doc/HTML/ca/khangman/index.docbook
/usr/share/doc/HTML/de/khangman/getnewstuff.png
/usr/share/doc/HTML/de/khangman/index.cache.bz2
/usr/share/doc/HTML/de/khangman/index.docbook
/usr/share/doc/HTML/de/khangman/khangman-desert.png
/usr/share/doc/HTML/de/khangman/khangman-main.png
/usr/share/doc/HTML/de/khangman/settings-general.png
/usr/share/doc/HTML/de/khangman/settings-languages.png
/usr/share/doc/HTML/de/khangman/settings-timers.png
/usr/share/doc/HTML/en/khangman/about-kde.png
/usr/share/doc/HTML/en/khangman/application-exit.png
/usr/share/doc/HTML/en/khangman/dialog-information.png
/usr/share/doc/HTML/en/khangman/document-new.png
/usr/share/doc/HTML/en/khangman/games-hint.png
/usr/share/doc/HTML/en/khangman/get-hot-new-stuff.png
/usr/share/doc/HTML/en/khangman/getnewstuff.png
/usr/share/doc/HTML/en/khangman/go-next.png
/usr/share/doc/HTML/en/khangman/handbook.png
/usr/share/doc/HTML/en/khangman/help-hint.png
/usr/share/doc/HTML/en/khangman/index.cache.bz2
/usr/share/doc/HTML/en/khangman/index.docbook
/usr/share/doc/HTML/en/khangman/khangman-desert.png
/usr/share/doc/HTML/en/khangman/khangman-main.png
/usr/share/doc/HTML/en/khangman/pause.png
/usr/share/doc/HTML/en/khangman/play.png
/usr/share/doc/HTML/en/khangman/quit.png
/usr/share/doc/HTML/en/khangman/settings-general.png
/usr/share/doc/HTML/en/khangman/settings-languages.png
/usr/share/doc/HTML/en/khangman/settings-timers.png
/usr/share/doc/HTML/en/khangman/settings.png
/usr/share/doc/HTML/en/khangman/settings_icon.png
/usr/share/doc/HTML/en/khangman/statusbar.png
/usr/share/doc/HTML/en/khangman/toolbar.png
/usr/share/doc/HTML/es/khangman/getnewstuff.png
/usr/share/doc/HTML/es/khangman/index.cache.bz2
/usr/share/doc/HTML/es/khangman/index.docbook
/usr/share/doc/HTML/es/khangman/khangman-desert.png
/usr/share/doc/HTML/es/khangman/khangman-main.png
/usr/share/doc/HTML/es/khangman/settings-general.png
/usr/share/doc/HTML/es/khangman/settings-languages.png
/usr/share/doc/HTML/es/khangman/settings-timers.png
/usr/share/doc/HTML/et/khangman/index.cache.bz2
/usr/share/doc/HTML/et/khangman/index.docbook
/usr/share/doc/HTML/id/khangman/index.cache.bz2
/usr/share/doc/HTML/id/khangman/index.docbook
/usr/share/doc/HTML/it/khangman/getnewstuff.png
/usr/share/doc/HTML/it/khangman/index.cache.bz2
/usr/share/doc/HTML/it/khangman/index.docbook
/usr/share/doc/HTML/it/khangman/khangman-desert.png
/usr/share/doc/HTML/it/khangman/khangman-main.png
/usr/share/doc/HTML/it/khangman/settings.png
/usr/share/doc/HTML/nl/khangman/index.cache.bz2
/usr/share/doc/HTML/nl/khangman/index.docbook
/usr/share/doc/HTML/pt/khangman/index.cache.bz2
/usr/share/doc/HTML/pt/khangman/index.docbook
/usr/share/doc/HTML/pt_BR/khangman/getnewstuff.png
/usr/share/doc/HTML/pt_BR/khangman/index.cache.bz2
/usr/share/doc/HTML/pt_BR/khangman/index.docbook
/usr/share/doc/HTML/pt_BR/khangman/khangman-desert.png
/usr/share/doc/HTML/pt_BR/khangman/khangman-main.png
/usr/share/doc/HTML/pt_BR/khangman/settings-general.png
/usr/share/doc/HTML/pt_BR/khangman/settings-languages.png
/usr/share/doc/HTML/pt_BR/khangman/settings-timers.png
/usr/share/doc/HTML/ru/khangman/getnewstuff.png
/usr/share/doc/HTML/ru/khangman/index.cache.bz2
/usr/share/doc/HTML/ru/khangman/index.docbook
/usr/share/doc/HTML/ru/khangman/khangman-desert.png
/usr/share/doc/HTML/ru/khangman/khangman-main.png
/usr/share/doc/HTML/ru/khangman/settings.png
/usr/share/doc/HTML/sv/khangman/getnewstuff.png
/usr/share/doc/HTML/sv/khangman/index.cache.bz2
/usr/share/doc/HTML/sv/khangman/index.docbook
/usr/share/doc/HTML/uk/khangman/getnewstuff.png
/usr/share/doc/HTML/uk/khangman/index.cache.bz2
/usr/share/doc/HTML/uk/khangman/index.docbook
/usr/share/doc/HTML/uk/khangman/khangman-desert.png
/usr/share/doc/HTML/uk/khangman/khangman-main.png
/usr/share/doc/HTML/uk/khangman/settings-general.png
/usr/share/doc/HTML/uk/khangman/settings-languages.png
/usr/share/doc/HTML/uk/khangman/settings-timers.png
/usr/share/doc/HTML/uk/khangman/settings.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/khangman/1bd373e4851a93027ba70064bd7dbdc6827147e1
/usr/share/package-licenses/khangman/d357e60aa8efd63b4475c3363700ba54f9a71343

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man6/khangman.6
/usr/share/man/de/man6/khangman.6
/usr/share/man/es/man6/khangman.6
/usr/share/man/et/man6/khangman.6
/usr/share/man/fr/man6/khangman.6
/usr/share/man/it/man6/khangman.6
/usr/share/man/man6/khangman.6
/usr/share/man/nl/man6/khangman.6
/usr/share/man/pt/man6/khangman.6
/usr/share/man/pt_BR/man6/khangman.6
/usr/share/man/ru/man6/khangman.6
/usr/share/man/sv/man6/khangman.6
/usr/share/man/uk/man6/khangman.6

%files locales -f khangman.lang
%defattr(-,root,root,-)

