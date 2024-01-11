%global fontname paratype-pt-sans
%global fontconf 57-%{fontname}

%global archivename PTSans.zip

%global common_desc \
The PT Sans family was developed as part of the “Public Types of Russian \
Federation” project. This project aims at enabling the peoples of Russia to \
read and write their native languages, using free/libre fonts. It is \
dedicated to the 300-year anniversary of the Russian civil type invented by \
Peter the Great from 1708 to 1710, and was realized with financial support \
from the Russian Federal Agency for Press and Mass Communications. \
\
The fonts include support for all 54 title¹ languages of the Russian \
Federation as well as more common Western, Central European and Cyrillic \
blocks making them unique and a very important tool for modern digital \
communications. \
\
PT Sans is a grotesque font based on Russian type designs of the second part \
of the 20th century. However, it also includes very distinctive features of \
modern humanistic design, fulfilling present day aesthetic and functional \
requirements. \
\
It was designed by Alexandra Korolkova, Olga Umpeleva and Vladimir Yefimov \
and released by ParaType. \
\
¹ A “title” language is named after an ethnic group.


Name:           %{fontname}-fonts
Version:        20141121
Release:        6%{?dist}
Summary:        A pan-Cyrillic typeface

License:        OFL
URL:            http://www.paratype.com/public/
# We now got new updated source archive to use
Source0:        http://www.fontstock.com/public/PTSansOFL.zip
# Below is original and old source archive
# Source0:        http://www.fontstock.com/public/PTSans_OFL.zip
Source10:       %{name}-fontconfig.conf
Source11:       %{name}-caption-fontconfig.conf
Source12:       %{fontname}.metainfo.xml
Source13:       %{fontname}-narrow.metainfo.xml
Source14:       %{fontname}-caption.metainfo.xml

BuildArch:      noarch
Requires:       fontpackages-filesystem
BuildRequires:  fontpackages-devel

%description
%common_desc

This package includes the four basic styles and two narrows styles for
economic setting.

%_font_pkg -f %{fontconf}.conf PTS*.ttf PTN*.ttf
%doc *.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml
%{_datadir}/appdata/%{fontname}-narrow.metainfo.xml


%package -n %{fontname}-caption-fonts
Summary:        A pan-Cyrillic typeface (caption forms for small text)
BuildRequires:  fontpackages-devel

%description -n %{fontname}-caption-fonts
%common_desc

This package includes 2 captions styles for small text sizes.

%_font_pkg -n caption -f %{fontconf}-caption.conf PTC*.ttf
%doc *.txt
%{_datadir}/appdata/%{fontname}-caption.metainfo.xml


%prep
%setup -q -c

for txt in *.txt ; do
   if $(echo "$txt" | grep -q "rus\.txt") ; then
     iconv --from=UTF-16       --to=UTF-8 "$txt" > "$txt.1"
   else
     iconv --from=WINDOWS-1251 --to=UTF-8 "$txt" > "$txt.1"
   fi
   sed -i 's/\r//' "$txt.1"
   touch -r "$txt" "$txt.1"
   mv "$txt.1" "$txt"
done


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE10} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE11} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-caption.conf

for fconf in %{fontconf}.conf \
             %{fontconf}-caption.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE12} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE13} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-narrow.metainfo.xml
install -Dm 0644 -p %{SOURCE14} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-caption.metainfo.xml


%changelog
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20141121-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20141121-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 21 2014 Parag Nemade <pnemade AT redhat DOT com> - 20141121-1
- Change the Source0 archive
- Update to current snapshot 20141121

* Sun Nov 09 2014 Parag Nemade <pnemade AT redhat DOT com> - 20101909-5
- Add metainfo file to show this font in gnome-software
- Remove group tag

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101909-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101909-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101909-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 30 2012 Parag <paragn AT fedoraproject DOT org> - 20101909-1
- Resolves:rh#882107 - source files does not match with upstream

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100408-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100408-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100408-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 25 2010 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20100408-1
— Update to latest upstream release
— Switch to the OFL version

* Thu Feb 18 2010 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20100112-3
— Remove vestigial dep in caption subpackage

* Sat Feb 13 2010 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20100112-2
— Update for review

* Sun Jan 17 2010 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 20100112-1
— Initial release

