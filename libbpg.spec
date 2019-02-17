# upstream only provides static library for now

Name:           libbpg
Version:        0.9.8
Release:        1%{?dist}
Summary:        Tools for the BPG (Better Portable Graphics) image format

# The BPG decoding library uses a modified version of FFmpeg released under the LGPL version 2.1 as HEVC decoder. The BPG decoding library excluding the FFmpeg code is released under the BSD license.
# The BPG encoder as a whole is released under the GPL version 2 license. The BPG encoder sources excluding x265 are released under the BSD license. The x265 library is released under the GPL version 2 license. The optional JCTVC HEVC reference encoder is released under the BSD license.
License:        LGPLv2 and GPLv2 and BSD
URL:            https://bellard.org/bpg/
Source0:        %{url}%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  yasm, cmake
BuildRequires:  sed

# Requires:       

%description
BPG (Better Portable Graphics) is a new image format. Its purpose is to replace 
the JPEG image format when quality or file size is an issue. Its main 
advantages are:
High compression ratio. Files are much smaller than JPEG for similar quality.
Supported by most Web browsers with a small Javascript decoder.
Based on a subset of the HEVC open video compression standard.
Supports the same chroma formats as JPEG (grayscale, YCbCr 4:2:0, 4:2:2, 4:4:4) 
to reduce the losses during the conversion. An alpha channel is supported. The 
RGB, YCgCo and CMYK color spaces are also supported.
Native support of 8 to 14 bits per channel for a higher dynamic range.
Lossless compression is supported.
Various metadata (such as EXIF, ICC profile, XMP) can be included.
Animation support.

%package        devel
Summary:        Development files and static library for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
The %{name}-devel package contains static library and header files for
developing applications that use %{name}.


%prep
%autosetup

%build
# replace hardcoded flags
%{__sed} '\?^CFLAGS:=?s?=.*$?=%{build_cflags}? ; \?^LDFLAGS=?s?=.*$?=%{build_ldflags}?' Makefile

%make_build USE_JCTVC=Y


%install
%{__rm} -rf $RPM_BUILD_ROOT

%{__instal} -D -m 755 -t %{buildroot}/%{_bindir}/ bpgenc bpgdec bpgview
%{__instal} -D -m 644 -t %{buildroot}/%{_includedir}/ libbpg.h bpgenc.h
%{__instal} -D -m 644 -t %{buildroot}/%{_libdir}/ libbpg.a


%files
%doc README ChangeLog
%{_bindir}/*

%files devel
%doc doc/bpg_spec.txt
%{_includedir}/*.h
%{_libdir}/%{name}.a

%changelog
