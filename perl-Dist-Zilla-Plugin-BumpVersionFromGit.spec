%define upstream_name    Dist-Zilla-Plugin-BumpVersionFromGit
%define upstream_version 0.009

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Provide a version number by bumping the last git release tag

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(Dist::Zilla::Role::VersionProvider)
BuildRequires:	perl(Git::Wrapper)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Version::Next)
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(version)
BuildArch:	noarch

%description
This does the the Dist::Zilla::Role::VersionProvider manpage role. It finds
the last version number from tags and increments it as the new version used
by Dist::Zilla.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*


