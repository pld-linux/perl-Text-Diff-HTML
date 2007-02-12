#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	Diff-HTML
Summary:	XHTML format for Text::Diff::Unified
Summary(pl.UTF-8):   Format XHTML dla Text::Diff::Unified
Name:		perl-Text-Diff-HTML
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cd8a50dd2f9d90be1f949906441035c1
URL:		http://search.cpan.org/~dwheeler/Text-Diff-HTML-0.04/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Pod >= 1.20
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XHTML format for Text::Diff::Unified.

%description -l pl.UTF-8
Format XHTML dla Text::Diff::Unified.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{perl_vendorlib}/Text/Diff,%{_mandir}/man3}

install lib/Text/Diff/HTML.pm $RPM_BUILD_ROOT%{perl_vendorlib}/Text/Diff
install blib/libdoc/Text::Diff::HTML.3pm $RPM_BUILD_ROOT%{_mandir}/man3 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Text/Diff/HTML.pm
%{_mandir}/man3/*
