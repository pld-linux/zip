Summary:	A file compression and packaging utility compatible with PKZIP.
Summary(de): 	erstellt mit PKZIP(tm) kompatible .zip-Dateien
Summary(fr): 	Crée des fichiers .zip compatibles avec PKZIP(tm).
Summary(tr): 	PKZIP(tm)-uyumlu .zip dosyalarý yaratýr
Name:		zip
Version:	2.2
Release:	1
Copyright:	distributable
Group:		Applications/Archiving
Source:		ftp://ftp.uu.net/pub/archiving/zip/src/%{name}22.tar.gz
Patch0:		zip21.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The zip program is a compression and file packaging utility.  Zip is
analogous to a combination of the UNIX tar and compress commands and is
compatible with PKZIP (a compression and file packaging utility for
MS-DOS systems).

Install the zip package if you need to compress files using the zip
program.

%description -l de
zip ist ein Komprimierungs- und Dateiarchivierungsprogramm für Unix,
VMS, MSDOS, OS/2, Windows NT, Minix, Atari und Macintosh. Es
entspricht einer Kombination der UNIX-Befehle tar(1) und compress(1)
und ist mit PKZIP kompatibel (ZIP für MSDOS von Phil Katz).

%description -l fr
zip est un utilitaire de compression et d'archivage de fichiers pour UNIX,
MSDOS, OS/2, Windows NT, Minix, Atari et Macintosh. Il est analogue à une
combinaison des commandes UNIX tar(1) et compress(1) et est compatible
avec PKZIP (le \"Phil Katz's ZIP\" pour  MSDOS).

%description -l tr
zip çeþitli iþletim sistemleri için geliþtirilmiþ bir sýkýþtýrma yazýlýmýdýr.
Çalýþmasý açýsýndan tar(1) ve compress(1) komutlarýnýn bir birleþimi gibidir
ve PKZIP uyumludur.

%prep
%setup  -q 
%patch0 -p1

%build
make -f unix/Makefile prefix=%{_prefix} \
	CFLAGS="$RPM_OPT_FLAGS -I. -DUNIX" generic_gcc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

make -f unix/Makefile install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/* || :

gzip -9nf README WHERE proginfo/algorith.txt proginfo/3rdparty.bug \
	TODO proginfo/infozip.who CHANGES \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,WHERE,proginfo/algorith.txt,proginfo/3rdparty.bug}.gz
%doc {TODO,proginfo/infozip.who,CHANGES}.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
