# GitHub Actions Workflows

This directory contains the CI/CD workflows for cfxdb.

## Workflows

### main.yml

**Trigger:** Push to `master`, tags `v*`, pull requests

Main CI workflow that runs on every push and PR:

| Job | Purpose |
|-----|---------|
| `identifiers` | Extract release type (development/stable) using wamp-cicd |
| `check` | Code quality checks (ruff format, ruff lint, ty type checker) |
| `test` | Test suite across Python 3.11, 3.12, 3.13, 3.14 |
| `docs` | Build Sphinx documentation |
| `build` | Build sdist + wheel, upload verified artifacts |

### release.yml

**Trigger:** After `main` workflow completes successfully

Release workflow for creating GitHub releases and publishing to PyPI:

| Job | Purpose |
|-----|---------|
| `check-main-workflow` | Verify main workflow completed successfully |
| `identifiers` | Determine release type (development/nightly vs stable) |
| `release-development` | Create pre-release on GitHub for nightly builds |
| `release-production` | Create GitHub release AND publish to PyPI for stable tags |

## Release Types

| Type | Trigger | PyPI | GitHub Release |
|------|---------|------|----------------|
| `development` | Push to master | No | Pre-release |
| `nightly` | Push to master | No | Pre-release |
| `stable` | Tag push (`v*`) | Yes | Full release |

## Shared Infrastructure

These workflows use reusable components from [wamp-cicd](https://github.com/wamp-proto/wamp-cicd):

- **Reusable workflow:** `wamp-proto/wamp-cicd/.github/workflows/identifiers.yml@main`
- **Actions:**
  - `wamp-proto/wamp-cicd/actions/upload-artifact-verified@main`
  - `wamp-proto/wamp-cicd/actions/download-artifact-verified@main`
  - `wamp-proto/wamp-cicd/actions/check-release-fileset@main`
  - `wamp-proto/wamp-cicd/actions/validate-audit-file@main`

The `.cicd/` submodule must be present for scripts referenced by these workflows.

## PyPI Publishing

Production releases use OIDC trusted publishing:
- No password/token required
- Automatic attestation generation
- Configured via PyPI project settings

## Audit Requirements

For stable releases, an audit file must exist at `.audit/<branch>.md` documenting:
- AI assistance disclosure
- Policy compliance confirmation
- Related issue reference

## Local Testing

Use `just` recipes to run the same checks locally:

```bash
just check         # Run all code quality checks
just test          # Run test suite
just docs          # Build documentation
just dist          # Build distribution packages
just verify-dist   # Verify built packages
```
