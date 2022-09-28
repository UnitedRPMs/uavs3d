%global commit0 0133ee4b4bbbef7b88802e7ad019b14b9b852c2b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:		uavs3d
Summary:	AVS3 decoder library
Version:	1.1
Release:	2%{dist}
License:	BSD
Source0:	https://github.com/uavs3/uavs3d/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
URL:		https://github.com/uavs3/uavs3d

BuildRequires:	cmake >= 2.8
BuildRequires:  gcc-c++
BuildRequires:  git

%description
uavs3d is an opensource and cross-platform AVS3 decoder, supports
AVS3-P2 baseline profile.

%package devel
Summary:	Header files for uavs3d library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for uavs3d library.


%prep
%autosetup -n %{name}-%{commit0} -p1
sed -i '/libdir/ s/"lib"/"%{_lib}"/' source/CMakeLists.txt

%build
mkdir -p build
%cmake -B build -DCMAKE_INSTALL_PREFIX="/usr" \
	-DCMAKE_INSTALL_LIBDIR=%{_libdir} \
	-DCMAKE_INSTALL_FULL_LIBDIR=%{_lib} 
	
%make_build -C build

%install
%make_install -C build

%files
%doc COPYING README.md 
%{_libdir}/libuavs3d.so

%files devel
%{_includedir}/uavs3d.h
%{_libdir}/pkgconfig/uavs3d.pc

%changelog

* Wed Sep 21 2022 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.1-2
- Updated to current commit

* Fri Feb 04 2022 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.1-1
- Initial build
