Summary:	A file compression and packaging utility compatible with PKZIP.
Name:		zip
Version:	2.1
Release:	9
Copyright:	distributable
Group:		Applications/Archiving
Source:		ftp://ftp.uu.net/pub/archiving/zip/%{name}21.zip
Patch0:		zip21.patch
Patch1:		zip-2.1-arm.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The zip program is a compression and file packaging utility.  Zip is
analogous to a combination of the UNIX tar and compress commands and is
compatible with PKZIP (a compression and file packaging utility for
MS-DOS systems).

Install the zip package if you need to compress files using the zip
program.

%prep
%setup -T -c -q 
unzip $RPM_SOURCE_DIR/zip21.zip
%patch0 -p1
%patch1 -p1

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

gzip -9nf README Where algorith.doc zip.doc TODO infozip.who \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,Where,algorith.doc,zip.doc,TODO,infozip.who}.gz
%attr(755,root,root) %{_bindir}/zipgrep
%attr(755,root,root) %{_bindir}/zipnote
%attr(755,root,root) %{_bindir}/zipsplit
%attr(755,root,root) %{_bindir}/zip
%attr(755,root,root) %{_bindir}/zipcloak
%{_mandir}/man1/zip.1*
%{_mandir}/man1/zipgrep.1*
