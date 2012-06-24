Summary:	A file compression and packaging utility compatible with PKZIP
Summary(de.UTF-8):   erstellt mit PKZIP(tm) kompatible .zip-Dateien
Summary(es.UTF-8):   Crea archivos .zip compatibles con PKZIP(tm)
Summary(fr.UTF-8):   Crée des fichiers .zip compatibles avec PKZIP(tm)
Summary(pl.UTF-8):   Program do kompresji i archiwizacji plików, kompatybilny z PKZIP
Summary(pt_BR.UTF-8):   Cria arquivos .zip compatíveis com PKZIP(tm)
Summary(ru.UTF-8):   Утилита для сжатия и упаковки файлов, совместимая с PKZIP
Summary(tr.UTF-8):   PKZIP(tm)-uyumlu .zip dosyaları yaratır
Summary(uk.UTF-8):   Утиліта для компресування та упаковки файлів, сумісна з PKZIP
Name:		zip
Version:	2.31
Release:	2
License:	distributable
Group:		Applications/Archiving
Source0:	ftp://ftp.info-zip.org/pub/infozip/src/%{name}231.tar.gz
# Source0-md5:	6bfc076664416251d7624ab3538d1cb9
Source1:	ftp://ftp.icce.rug.nl/infozip/src/zcrypt29.zip
# Source1-md5:	0c969ba1661183b041a142945ed2710e
Source2:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source2-md5:	72d619b4f70c06c34e5244125b62fdce
Patch0:		%{name}-zmem.patch
Patch1:		%{name}-multilib.patch
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

%description -l de.UTF-8
zip ist ein Komprimierungs- und Dateiarchivierungsprogramm für Unix,
VMS, MSDOS, OS/2, Windows NT, Minix, Atari und Macintosh. Es
entspricht einer Kombination der UNIX-Befehle tar(1) und compress(1)
und ist mit PKZIP kompatibel (ZIP für MSDOS von Phil Katz).

%description -l es.UTF-8
zip es un utilitario de compresión y empaquetado de archivo para Unix,
VMS, MSDOS, OS/2, Windows NT, Minix, Atari y Machintosh. Y equivale al
uso de programas UNIX como tar(1) y compress(1) combinados y es
compatible con PKZIP (ZIP de Phil Katz para sistemas MSDOS).

%description -l fr.UTF-8
zip est un utilitaire de compression et d'archivage de fichiers pour
UNIX, MSDOS, OS/2, Windows NT, Minix, Atari et Macintosh. Il est
analogue à une combinaison des commandes UNIX tar(1) et compress(1) et
est compatible avec PKZIP (le \"Phil Katz's ZIP\" pour MSDOS).

%description -l pl.UTF-8
Program zip służy do kompresji oraz archiwizacji plików, o
funkcjonalności analogicznej jak kombinacja uniksowych programów tar i
compress. Jest kompatybilny z programem PKZIP, popularnym
archiwizatorem pod DOS-a.

%description -l pt_BR.UTF-8
zip é um utilitário de compressão e empacotamento de arquivo para
Unix, VMS, MSDOS, OS/2, Windows NT, Minix, Atari e Machintosh. Ele é
equivalente ao uso de programas UNIX como tar(1) e compress(1)
combinados e é compatível com o PKZIP (ZIP de Phil Katz para sistemas
MSDOS).

%description -l ru.UTF-8
Программа zip - это утилита для компрессирования и упаковки файлов.
Zip похож на комбинацию из команд Unix tar и compress и совместим с
PKZIP (утилита для компрессирования и упаковки файлов для MS-DOS).

%description -l tr.UTF-8
zip çeşitli işletim sistemleri için geliştirilmiş bir sıkıştırma
yazılımıdır. Çalışması açısından tar(1) ve compress(1) komutlarının
bir birleşimi gibidir ve PKZIP uyumludur.

%description -l uk.UTF-8
Програма zip - це утиліта для компресування та упаковки файлів. Zip
схожий на комбінацію з команд Unix tar та compress і сумісний з PKZIP
(утиліта для компресування та упаковки файлів для MS-DOS).

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1

%build
%{__make} -f unix/Makefile generic \
	prefix=%{_prefix} \
	CC="%{__cc}" \
	CPP="%{__cpp}" \
	CFLAGS="%{rpmcflags} -I. -DUNIX -D_FILE_OFFSET_BITS=64"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} -f unix/Makefile install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	INSTALL=install

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README WHERE proginfo/*.txt proginfo/3rdparty.bug
%doc TODO proginfo/infozip.who CHANGES
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(hu) %{_mandir}/hu/man1/*
