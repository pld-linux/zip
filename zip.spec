Summary: A file compression and packaging utility compatible with PKZIP.
Name: zip
Version: 2.1
Release: 8
Copyright: distributable
Group: Applications/Archiving
Source: ftp.uu.net:/pub/archiving/zip/zip21.zip
Patch0: zip21.patch
Patch1: zip-2.1-arm.patch
Prefix: /usr
BuildRoot: /var/tmp/zip-root

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
make -f unix/Makefile prefix=/usr "RPM_OPT_FLAGS=$RPM_OPT_FLAGS" generic_gcc

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

make -f unix/Makefile prefix=$RPM_BUILD_ROOT/usr install

pushd $RPM_BUILD_ROOT
for n in zipnote zipsplit zip zipcloak ; do
    strip ./usr/bin/$n
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Where algorith.doc install.doc zip.doc TODO infozip.who
/usr/bin/zipgrep
/usr/bin/zipnote
/usr/bin/zipsplit
/usr/bin/zip
/usr/bin/zipcloak
/usr/man/man1/zip.1
/usr/man/man1/zipgrep.1
