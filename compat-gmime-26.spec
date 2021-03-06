#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-gmime-26
Version  : 2.6.23
Release  : 6
URL      : https://download.gnome.org/sources/gmime/2.6/gmime-2.6.23.tar.xz
Source0  : https://download.gnome.org/sources/gmime/2.6/gmime-2.6.23.tar.xz
Summary  : MIME library
Group    : Development/Tools
License  : LGPL-2.1
Requires: compat-gmime-26-data = %{version}-%{release}
Requires: compat-gmime-26-lib = %{version}-%{release}
Requires: compat-gmime-26-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : docbook-utils
BuildRequires : docbook-xml
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libgpg-error-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(zlib)
# Suppress generation of debuginfo
%global debug_package %{nil}

%description
GMime is a set of utilities for parsing and creating messages using
the Multipurpose Internet Mail Extension (MIME)

%package data
Summary: data components for the compat-gmime-26 package.
Group: Data

%description data
data components for the compat-gmime-26 package.


%package dev
Summary: dev components for the compat-gmime-26 package.
Group: Development
Requires: compat-gmime-26-lib = %{version}-%{release}
Requires: compat-gmime-26-data = %{version}-%{release}
Provides: compat-gmime-26-devel = %{version}-%{release}
Requires: compat-gmime-26 = %{version}-%{release}

%description dev
dev components for the compat-gmime-26 package.


%package doc
Summary: doc components for the compat-gmime-26 package.
Group: Documentation

%description doc
doc components for the compat-gmime-26 package.


%package lib
Summary: lib components for the compat-gmime-26 package.
Group: Libraries
Requires: compat-gmime-26-data = %{version}-%{release}
Requires: compat-gmime-26-license = %{version}-%{release}

%description lib
lib components for the compat-gmime-26 package.


%package license
Summary: license components for the compat-gmime-26 package.
Group: Default

%description license
license components for the compat-gmime-26 package.


%prep
%setup -q -n gmime-2.6.23
cd %{_builddir}/gmime-2.6.23

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586223413
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1586223413
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-gmime-26
cp %{_builddir}/gmime-2.6.23/COPYING %{buildroot}/usr/share/package-licenses/compat-gmime-26/caeb68c46fa36651acf592771d09de7937926bb3
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GMime-2.6.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/gmime-2.6.deps
/usr/share/vala/vapi/gmime-2.6.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/gmime-2.6/gmime/gmime-certificate.h
/usr/include/gmime-2.6/gmime/gmime-charset.h
/usr/include/gmime-2.6/gmime/gmime-content-type.h
/usr/include/gmime-2.6/gmime/gmime-crypto-context.h
/usr/include/gmime-2.6/gmime/gmime-data-wrapper.h
/usr/include/gmime-2.6/gmime/gmime-disposition.h
/usr/include/gmime-2.6/gmime/gmime-encodings.h
/usr/include/gmime-2.6/gmime/gmime-error.h
/usr/include/gmime-2.6/gmime/gmime-filter-basic.h
/usr/include/gmime-2.6/gmime/gmime-filter-best.h
/usr/include/gmime-2.6/gmime/gmime-filter-charset.h
/usr/include/gmime-2.6/gmime/gmime-filter-crlf.h
/usr/include/gmime-2.6/gmime/gmime-filter-enriched.h
/usr/include/gmime-2.6/gmime/gmime-filter-from.h
/usr/include/gmime-2.6/gmime/gmime-filter-gzip.h
/usr/include/gmime-2.6/gmime/gmime-filter-html.h
/usr/include/gmime-2.6/gmime/gmime-filter-md5.h
/usr/include/gmime-2.6/gmime/gmime-filter-strip.h
/usr/include/gmime-2.6/gmime/gmime-filter-windows.h
/usr/include/gmime-2.6/gmime/gmime-filter-yenc.h
/usr/include/gmime-2.6/gmime/gmime-filter.h
/usr/include/gmime-2.6/gmime/gmime-gpg-context.h
/usr/include/gmime-2.6/gmime/gmime-header.h
/usr/include/gmime-2.6/gmime/gmime-iconv-utils.h
/usr/include/gmime-2.6/gmime/gmime-iconv.h
/usr/include/gmime-2.6/gmime/gmime-message-part.h
/usr/include/gmime-2.6/gmime/gmime-message-partial.h
/usr/include/gmime-2.6/gmime/gmime-message.h
/usr/include/gmime-2.6/gmime/gmime-multipart-encrypted.h
/usr/include/gmime-2.6/gmime/gmime-multipart-signed.h
/usr/include/gmime-2.6/gmime/gmime-multipart.h
/usr/include/gmime-2.6/gmime/gmime-object.h
/usr/include/gmime-2.6/gmime/gmime-param.h
/usr/include/gmime-2.6/gmime/gmime-parser.h
/usr/include/gmime-2.6/gmime/gmime-part-iter.h
/usr/include/gmime-2.6/gmime/gmime-part.h
/usr/include/gmime-2.6/gmime/gmime-pkcs7-context.h
/usr/include/gmime-2.6/gmime/gmime-signature.h
/usr/include/gmime-2.6/gmime/gmime-stream-buffer.h
/usr/include/gmime-2.6/gmime/gmime-stream-cat.h
/usr/include/gmime-2.6/gmime/gmime-stream-file.h
/usr/include/gmime-2.6/gmime/gmime-stream-filter.h
/usr/include/gmime-2.6/gmime/gmime-stream-fs.h
/usr/include/gmime-2.6/gmime/gmime-stream-gio.h
/usr/include/gmime-2.6/gmime/gmime-stream-mem.h
/usr/include/gmime-2.6/gmime/gmime-stream-mmap.h
/usr/include/gmime-2.6/gmime/gmime-stream-null.h
/usr/include/gmime-2.6/gmime/gmime-stream-pipe.h
/usr/include/gmime-2.6/gmime/gmime-stream.h
/usr/include/gmime-2.6/gmime/gmime-utils.h
/usr/include/gmime-2.6/gmime/gmime-version.h
/usr/include/gmime-2.6/gmime/gmime.h
/usr/include/gmime-2.6/gmime/internet-address.h
/usr/lib64/libgmime-2.6.so
/usr/lib64/pkgconfig/gmime-2.6.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/gmime-2.6/CryptoContexts.html
/usr/share/gtk-doc/html/gmime-2.6/DataWrappers.html
/usr/share/gtk-doc/html/gmime-2.6/Filters.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeCertificate.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeContentDisposition.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeContentType.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeCryptoContext.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeDataWrapper.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeFilter.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeFilterBasic.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeFilterBest.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeFilterCRLF.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeFilterCharset.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeFilterEnriched.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeFilterFrom.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeFilterGZip.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeFilterHTML.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeFilterMd5.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeFilterStrip.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeFilterWindows.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeFilterYenc.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeGpgContext.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeMessage.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeMessagePart.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeMessagePartial.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeMultipart.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeMultipartEncrypted.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeMultipartSigned.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeObject.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeParser.html
/usr/share/gtk-doc/html/gmime-2.6/GMimePart.html
/usr/share/gtk-doc/html/gmime-2.6/GMimePkcs7Context.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeSignature.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeStream.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeStreamBuffer.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeStreamCat.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeStreamFile.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeStreamFilter.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeStreamFs.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeStreamMem.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeStreamMmap.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeStreamNull.html
/usr/share/gtk-doc/html/gmime-2.6/GMimeStreamPipe.html
/usr/share/gtk-doc/html/gmime-2.6/Headers.html
/usr/share/gtk-doc/html/gmime-2.6/InternetAddress.html
/usr/share/gtk-doc/html/gmime-2.6/InternetAddressGroup.html
/usr/share/gtk-doc/html/gmime-2.6/InternetAddressList.html
/usr/share/gtk-doc/html/gmime-2.6/InternetAddressMailbox.html
/usr/share/gtk-doc/html/gmime-2.6/InternetAddresses.html
/usr/share/gtk-doc/html/gmime-2.6/MimeParts.html
/usr/share/gtk-doc/html/gmime-2.6/Parsers.html
/usr/share/gtk-doc/html/gmime-2.6/Streams.html
/usr/share/gtk-doc/html/gmime-2.6/ch01.html
/usr/share/gtk-doc/html/gmime-2.6/classes.html
/usr/share/gtk-doc/html/gmime-2.6/core.html
/usr/share/gtk-doc/html/gmime-2.6/fundamentals.html
/usr/share/gtk-doc/html/gmime-2.6/gmime-2.6.devhelp2
/usr/share/gtk-doc/html/gmime-2.6/gmime-GMimeHeader.html
/usr/share/gtk-doc/html/gmime-2.6/gmime-GMimeParam.html
/usr/share/gtk-doc/html/gmime-2.6/gmime-GMimePartIter.html
/usr/share/gtk-doc/html/gmime-2.6/gmime-building.html
/usr/share/gtk-doc/html/gmime-2.6/gmime-changes-2-0.html
/usr/share/gtk-doc/html/gmime-2.6/gmime-changes-2-2.html
/usr/share/gtk-doc/html/gmime-2.6/gmime-changes-2-4.html
/usr/share/gtk-doc/html/gmime-2.6/gmime-changes-2-6.html
/usr/share/gtk-doc/html/gmime-2.6/gmime-compiling.html
/usr/share/gtk-doc/html/gmime-2.6/gmime-data-wrappers.html
/usr/share/gtk-doc/html/gmime-2.6/gmime-filters.html
/usr/share/gtk-doc/html/gmime-2.6/gmime-gmime-charset.html
/usr/share/gtk-doc/html/gmime-2.6/gmime-gmime-encodings.html
/usr/share/gtk-doc/html/gmime-2.6/gmime-gmime-iconv-utils.html
/usr/share/gtk-doc/html/gmime-2.6/gmime-gmime-iconv.html
/usr/share/gtk-doc/html/gmime-2.6/gmime-gmime-utils.html
/usr/share/gtk-doc/html/gmime-2.6/gmime-gmime.html
/usr/share/gtk-doc/html/gmime-2.6/gmime-question-index.html
/usr/share/gtk-doc/html/gmime-2.6/gmime-resources.html
/usr/share/gtk-doc/html/gmime-2.6/gmime-streams.html
/usr/share/gtk-doc/html/gmime-2.6/gmime.html
/usr/share/gtk-doc/html/gmime-2.6/home.png
/usr/share/gtk-doc/html/gmime-2.6/index.html
/usr/share/gtk-doc/html/gmime-2.6/left-insensitive.png
/usr/share/gtk-doc/html/gmime-2.6/left.png
/usr/share/gtk-doc/html/gmime-2.6/right-insensitive.png
/usr/share/gtk-doc/html/gmime-2.6/right.png
/usr/share/gtk-doc/html/gmime-2.6/style.css
/usr/share/gtk-doc/html/gmime-2.6/up-insensitive.png
/usr/share/gtk-doc/html/gmime-2.6/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgmime-2.6.so.0
/usr/lib64/libgmime-2.6.so.0.623.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-gmime-26/caeb68c46fa36651acf592771d09de7937926bb3
