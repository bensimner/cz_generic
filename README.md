# cz_generic

A language agnostic, generic, commitizen style.

## Schema

    ["(" <what> ")"] <kind> ":" <subject>

    <body>

    <footer>

## Kinds
### functional changes
- add: added something new
- remove: took away something old
- update: not new, not old, just different
- fix: oopsy
### refactoring
- move: same old, just somewhere else
- rename: same old, just with a new name
- refactor: same old but in a new box
### inclusion, dependencies and builds
- sync: was old, now new
- revert: was new, now old
### styling
- style: same, but looks different

## Using

### Manually

    pip install git+https://github.com/bensimner/cz_generic.git

Create `.cz.toml`:

    [tool.commitizen]
    name = "cz_generic"

### pre-commit integration

add to `.pre-commit-config.yaml` (updating revision numbers as appropriate):

    -   repo: https://github.com/commitizen-tools/commitizen
        rev: v2.27.1
        hooks:
        -   id: commitizen
            additional_dependencies: [git+https://github.com/bensimner/cz_generic.git]

Create `.cz.toml`:

    [tool.commitizen]
    name = "cz_generic"
