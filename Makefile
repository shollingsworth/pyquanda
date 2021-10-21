.DEFAULT_GOAL := pkg

docs := ./docs
srcdir := ./src
pkgname := pyquanda

documentation: clean
	@echo "Running docs"
	mm2github.py ./README.mm -w
	./scripts/gendoc.py
	./scripts/genbadges.py
	./scripts/genpypyreadme.py
	lazydocs --output-path ./docs --overview-file ./documentation.md ./src/pyquanda

pkg_only: clean
	python3 setup.py sdist

# pkg: documentation docker_test
pkg: documentation pkg_only
	@echo "Running PKG"
	twine check dist/*

upload: pkg
	@echo "Running upload"
	twine upload --repository pyquanda dist/*

pre_bump:
	./scripts/version_bump.py
	./scripts/genchangelog.py

bump_version: pre_bump documentation
	# order is important here
	git add ./CHANGELOG.md
	git add ./VERSION
	git add ./.pypyreadme
	git add ./README*
	git diff HEAD
	git commit -S --amend
	bash -c "git tag v$$(cat VERSION)"

push:
	$(eval tag = $(shell cat VERSION))
	git push -u origin HEAD
	git push -u origin v$(tag)

release: pkg upload push
	@echo "Running Release"

clean:
	rm -rfv docs/* dist/* src/*.egg-info
