Summary:	A file compression and packaging utility compatible with PKZIP
Summary(de):	erstellt mit PKZIP(tm) kompatible .zip-Dateien
Summary(es):	Crea archivos .zip compatibles con PKZIP(tm)
Summary(fr):	CrИe des fichiers .zip compatibles avec PKZIP(tm)
Summary(pl):	Program do kompresji i archiwizacji plikСw, kompatybilny z PKZIP
Summary(pt_BR):	Cria arquivos .zip compatМveis com PKZIP(tm)
Summary(ru):	Утилита для сжатия и упаковки файлов, совместимая с PKZIP
Summary(tr):	PKZIP(tm)-uyumlu .zip dosyalarЩ yaratЩr
Summary(uk):	Утил╕та для компресування та упаковки файл╕в, сум╕сна з PKZIP
Name:		zip
Version:	2.3
Release:	14
License:	distributable
Group:		Applications/Archiving
Source0:	ftp://ftp.uu.net/pub/archiving/zip/src/%{name}23.tar.gz
# Source0-md5: 5206a99541f3b0ab90f1baa167392c4f
Source1:	ftp://ftp.icce.rug.nl/infozip/src/zcrypt29.zip
# Source1-md5:	0c969ba1661183b041a142945ed2710e
Source2:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source2-md5: 72d619b4f70c06c34e5244125b62fdce
Patch0:		%{name}-zmem.patch
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_unzipbin /usr/bin/unzip -o -q

%description
The zip program is a compression and file packaging utility. Zip is
analogous to a combination of the UNIX tar and compress commands and
is compatible with PKZIP (a compression and file packaging utility for
MS-DOS systems).

Install the zip package if you need to compress files using the zip
program.

%description -l de
zip ist ein Komprimierungs- und Dateiarchivierungsprogramm fЭr Unix,
VMS, MSDOS, OS/2, Windows NT, Minix, Atari und Macintosh. Es
entspricht einer Kombination der UNIX-Befehle tar(1) und compress(1)
und ist mit PKZIP kompatibel (ZIP fЭr MSDOS von Phil Katz).

%description -l es
zip es un utilitario de compresiСn y empaquetado de archivo para Unix,
VMS, MSDOS, OS/2, Windows NT, Minix, Atari y Machintosh. Y equivale al
uso de programas UNIX como tar(1) y compress(1) combinados y es
compatible con PKZIP (ZIP de Phil Katz para sistemas MSDOS).

%description -l fr
zip est un utilitaire de compression et d'archivage de fichiers pour
UNIX, MSDOS, OS/2, Windows NT, Minix, Atari et Macintosh. Il est
analogue Ю une combinaison des commandes UNIX tar(1) et compress(1) et
est compatible avec PKZIP (le \"Phil Katz's ZIP\" pour MSDOS).

%description -l pl
Program zip sЁu©y do kompresji oraz archiwizacji plikСw, o
funkcjonalno╤ci analogicznej jak kombinacja unixowych programСw tar i
compress. Jest kompatybilny z programem PKZIP, popularnym
archiwizatorem pod DOSa.

%description -l pt_BR
zip И um utilitАrio de compressЦo e empacotamento de arquivo para
Unix, VMS, MSDOS, OS/2, Windows NT, Minix, Atari e Machintosh. Ele И
equivalente ao uso de programas UNIX como tar(1) e compress(1)
combinados e И compatМvel com o PKZIP (ZIP de Phil Katz para sistemas
MSDOS).

%description -l ru
Программа zip - это утилита для компрессирования и упаковки файлов.
Zip похож на комбинацию из команд Unix tar и compress и совместим с
PKZIP (утилита для компрессирования и упаковки файлов для MS-DOS).

%description -l tr
zip ГeЧitli iЧletim sistemleri iГin geliЧtirilmiЧ bir sЩkЩЧtЩrma
yazЩlЩmЩdЩr. гalЩЧmasЩ aГЩsЩndan tar(1) ve compress(1) komutlarЩnЩn
bir birleЧimi gibidir ve PKZIP uyumludur.

%description -l uk
Програма zip - це утил╕та для компресування та упаковки файл╕в. Zip
схожий на комб╕нац╕ю з команд Unix tar та compress ╕ сум╕сний з PKZIP
(утил╕та для компресування та упаковки файл╕в для MS-DOS).

%prep
%setup -q -a1
%patch0 -p1

%build
%{__make} -f unix/Makefile prefix=%{_prefix} \
	CC="%{__cc}" CFLAGS="%{rpmcflags} -I. -DUNIX" generic_gcc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} -f unix/Makefile install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README WHERE proginfo/algorith.txt proginfo/3rdparty.bug
%doc TODO proginfo/infozip.who CHANGES
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(hu) %{_mandir}/hu/man1/*
