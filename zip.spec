Summary:	A file compression and packaging utility compatible with PKZIP
Summary(de):	erstellt mit PKZIP(tm) kompatible .zip-Dateien
Summary(pl):	Program do kompresji i archiwizacji plików, kompatybilny z PKZIP
Summary(fr):	Crée des fichiers .zip compatibles avec PKZIP(tm)
Summary(tr):	PKZIP(tm)-uyumlu .zip dosyalarý yaratýr
Name:		zip
Version:	2.3
Release:	7
Copyright:	distributable
Group:		Utilities/Archiving
Group(pl):	Narzêdzia/Archiwizacja
Source0:	ftp://ftp.uu.net/pub/archiving/zip/src/%{name}23.tar.gz
Source1:	ftp://ftp.icce.rug.nl/infozip/src/zcrypt28.zip
Patch0:		%{name}-zmem.patch
BuildPrereq:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The zip program is a compression and file packaging utility. Zip is
analogous to a combination of the UNIX tar and compress commands and
is compatible with PKZIP (a compression and file packaging utility for
MS-DOS systems).

Install the zip package if you need to compress files using the zip
program.

%description -l de
zip ist ein Komprimierungs- und Dateiarchivierungsprogramm für Unix,
VMS, MSDOS, OS/2, Windows NT, Minix, Atari und Macintosh. Es
entspricht einer Kombination der UNIX-Befehle tar(1) und compress(1)
und ist mit PKZIP kompatibel (ZIP für MSDOS von Phil Katz).

%description -l pl
Program zip s³u¿y do kompresji oraz archiwizacji plików, o
funkcjonalno¶ci analogicznej jak kombinacja unixowych programów tar i
compress. Jest kompatybilny z programem PKZIP, popularnym
archiwizatorem pod DOSa.

%description -l fr
zip est un utilitaire de compression et d'archivage de fichiers pour
UNIX, MSDOS, OS/2, Windows NT, Minix, Atari et Macintosh. Il est
analogue à une combinaison des commandes UNIX tar(1) et compress(1) et
est compatible avec PKZIP (le \"Phil Katz's ZIP\" pour MSDOS).

%description -l tr
zip çeþitli iþletim sistemleri için geliþtirilmiþ bir sýkýþtýrma
yazýlýmýdýr. Çalýþmasý açýsýndan tar(1) ve compress(1) komutlarýnýn
bir birleþimi gibidir ve PKZIP uyumludur.

%prep
%setup  -q 
unzip -o $RPM_SOURCE_DIR/zcrypt28.zip

%patch0 -p1

%build
%{__make} -f unix/Makefile prefix=%{_prefix} \
	CFLAGS="$RPM_OPT_FLAGS -I. -DUNIX" generic_gcc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} -f unix/Makefile install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

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
