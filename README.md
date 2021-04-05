[code_of_conduct]: CODE_OF_CONDUCT.md
[license]: LICENSE.txt

# kema
> :wrench: A tool for helping setting up projects

## :rocket: Getting Started

These instructions will get you a copy of the project up and running on your
local machine for development and testing purposes.

### :inbox_tray: Prerequisites

The following software is required to be installed on your system:

- [go 1.16+](https://golang.org/dl/)

### :package: Installation

You can install the program in your computer for your own use.

```
go get -u github.com/nelsonmestevao/kema
```

### :video_game: Usage

After you have installed the program you can run it from everywhere. Just run
`kema`.

```
kema generate <module_name>
```

Use `--help` for more usage information.

### :hammer: Development

Setup the project and all dependencies for development.

```bash
. bin/setup
```

Run the tests.

```
bin/test
```

Format the code accordingly to common guide lines.

```
bin/format
```

Lint your go code.

```
bin/lint
```

## :handshake: Contributing

When contributing to this repository, please first discuss the change you wish
to make via issue, email, or any other method with the owners of this
repository before making a change.

Please note we have a [Code of Conduct][code_of_conduct], please follow it
in all your interactions with the project.

### :twisted_rightwards_arrows: Pull Request Process

1. It is advised to create a Pull Request if you are stuck (so others can help
   you) or when your feature is complete and tested.
2. To be merged, your Pull Request must have a passing build on the Continuous
   Integration server (not applicable now).
3. To be merged, your Pull Request should add relevant tests (when applicable).
4. You may merge the Pull Request in once you have the sign-off of one other
   developer, or if you do not have permission to do that, you may request the
   reviewer to merge it for you. If you do have merging permissions on the
   repository, you must rebase and squash your Pull Request into a single
   commit.

### :link: References

You can use these resources to learn more about the technologies this project
uses.

- [Getting Started with Go](https://learn.go.dev/)
- [Golang Documentation](https://golang.org/doc/)

## :memo: License

This project is licensed under the MIT License - see the [LICENSE][license]
file for details.
