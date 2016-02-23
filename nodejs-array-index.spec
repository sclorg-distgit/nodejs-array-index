%{?scl:%scl_package nodejs-array-index}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-array-index

%global npm_name array-index
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-array-index
Version:	0.1.1
Release:	4%{?dist}
Summary:	Invoke getter/setter functions on array-like objects
Url:		https://github.com/TooTallNate/array-index
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source1:    https://raw.githubusercontent.com/TooTallNate/array-index/1.0.0/LICENSE
License:	MIT

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel
BuildRequires:  %{?scl_prefix}runtime

%if 0%{?enable_tests}
%endif

BuildRequires:	%{?scl_prefix}nodejs-debug

Requires:	%{?scl_prefix}nodejs-debug

%description
Invoke getter/setter functions on array-like objects

%prep
%setup -q -n package

cp -p %{SOURCE1} .

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check

%endif

%files
%{nodejs_sitelib}/array-index

%doc README.md LICENSE

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.1-4
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.1-3
- Rebuilt with updated metapackage

* Fri Feb 12 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.1-2
- Add license

* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 0.1.1-1
- Initial build
