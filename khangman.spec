#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : khangman
Version  : 18.12.2
Release  : 3
URL      : https://download.kde.org/stable/applications/18.12.2/src/khangman-18.12.2.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.2/src/khangman-18.12.2.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.2/src/khangman-18.12.2.tar.xz.sig
Summary  : Hangman Game
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: khangman-bin = %{version}-%{release}
Requires: khangman-data = %{version}-%{release}
Requires: khangman-license = %{version}-%{release}
Requires: khangman-locales = %{version}-%{release}
Requires: khangman-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libkeduvocdocument-dev
BuildRequires : perl
BuildRequires : qtbase-dev mesa-dev

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
Requires: khangman-man = %{version}-%{release}

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
%setup -q -n khangman-18.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549944487
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1549944487
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/khangman
cp COPYING %{buildroot}/usr/share/package-licenses/khangman/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/khangman/COPYING.DOC
cp fonts/licenseDomesticManners.txt %{buildroot}/usr/share/package-licenses/khangman/fonts_licenseDomesticManners.txt
cp fonts/licenseDustimo.txt %{buildroot}/usr/share/package-licenses/khangman/fonts_licenseDustimo.txt
pushd clr-build
%make_install
popd
%find_lang khangman

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/share/khangman/qml/GamePage.qml
/usr/share/khangman/qml/Images/about-kde.png
/usr/share/khangman/qml/Images/action-fail.png
/usr/share/khangman/qml/Images/action-success.png
/usr/share/khangman/qml/Images/dialog-information.png
/usr/share/khangman/qml/Images/get-hot-new-stuff.png
/usr/share/khangman/qml/Images/go-next.png
/usr/share/khangman/qml/Images/handbook.png
/usr/share/khangman/qml/Images/help-hint.png
/usr/share/khangman/qml/Images/pause.png
/usr/share/khangman/qml/Images/play.png
/usr/share/khangman/qml/Images/quit.png
/usr/share/khangman/qml/Images/settings_icon.png
/usr/share/khangman/qml/LetterElement.qml
/usr/share/khangman/qml/MainSettingsDialog.qml
/usr/share/khangman/qml/MySelectionDialog.qml
/usr/share/khangman/qml/gallows/gallows1.png
/usr/share/khangman/qml/gallows/gallows10.png
/usr/share/khangman/qml/gallows/gallows2.png
/usr/share/khangman/qml/gallows/gallows3.png
/usr/share/khangman/qml/gallows/gallows4.png
/usr/share/khangman/qml/gallows/gallows5.png
/usr/share/khangman/qml/gallows/gallows6.png
/usr/share/khangman/qml/gallows/gallows7.png
/usr/share/khangman/qml/gallows/gallows8.png
/usr/share/khangman/qml/gallows/gallows9.png
/usr/share/khangman/qml/main.qml
/usr/share/khangman/qml/sounds/EW_Dialogue_Appear.ogg
/usr/share/khangman/qml/sounds/EW_Dialogue_Appear.wav
/usr/share/khangman/qml/sounds/chalk.ogg
/usr/share/khangman/qml/sounds/chalk.wav
/usr/share/khangman/qml/sounds/khangman-alphabet-button-press.wav
/usr/share/khangman/qml/sounds/new_game.ogg
/usr/share/khangman/qml/sounds/new_game.wav
/usr/share/khangman/qml/sounds/splash.ogg
/usr/share/khangman/qml/sounds/splash.wav
/usr/share/khangman/qml/sounds/wrong.ogg
/usr/share/khangman/qml/sounds/wrong.wav
/usr/share/khangman/sl.txt
/usr/share/khangman/sr@latin.txt
/usr/share/khangman/sv.txt
/usr/share/khangman/themes/khangman_bees.svg
/usr/share/khangman/themes/khangman_desert.svg
/usr/share/khangman/themes/khangman_notes.png
/usr/share/khangman/themes/khangman_sea.svg
/usr/share/khangman/themes/khangman_winter.svg
/usr/share/khangman/themes/standardthemes.xml
/usr/share/khangman/tr.txt
/usr/share/metainfo/org.kde.khangman.appdata.xml
/usr/share/xdg/khangman.knsrc

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
/usr/share/doc/HTML/et/khangman/index.cache.bz2
/usr/share/doc/HTML/et/khangman/index.docbook
/usr/share/doc/HTML/it/khangman/index.cache.bz2
/usr/share/doc/HTML/it/khangman/index.docbook
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
/usr/share/package-licenses/khangman/COPYING
/usr/share/package-licenses/khangman/COPYING.DOC
/usr/share/package-licenses/khangman/fonts_licenseDomesticManners.txt
/usr/share/package-licenses/khangman/fonts_licenseDustimo.txt

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man6/khangman.6
/usr/share/man/de/man6/khangman.6
/usr/share/man/es/man6/khangman.6
/usr/share/man/et/man6/khangman.6
/usr/share/man/it/man6/khangman.6
/usr/share/man/man6/khangman.6
/usr/share/man/nl/man6/khangman.6
/usr/share/man/pt/man6/khangman.6
/usr/share/man/pt_BR/man6/khangman.6
/usr/share/man/sv/man6/khangman.6
/usr/share/man/uk/man6/khangman.6

%files locales -f khangman.lang
%defattr(-,root,root,-)

