# template-fastapi-react-k8s

Template repo for FastAPI + React with auto-generation of Typescript models from React. Includes actions to lint, test,
build, and deploy to a locally-managed k8s instance and GitHub Pages simultaneously.

This template is python-first, meaning most api/control decisions are populated from the backend first, and then
recreated on the front-end. Namely by creating the model definition first in [api/model](api/model.py) and then running
the model generation scripts to provide the same structure to the front-end.

## Structure and Layout

The managed python environment starts in the root directory, with the `pyproject.toml` and is backed up by several
sub-directories and files:

```
[Development]
- api/          > underlying model/fast api code
- scripts/      > python scripts external to the api
- tests/        > tests for the api or scripts 
- web/          > react-based single-page web app

[Deployment]
- k8s/          > kubernetes deployment scripts (managed by .github/worflows)
- Dockerfile    > api image deployed to docker.io and pulled by k8s 
- VERSION       > release version echo file (updated by deploy workflow)
```

### One-time setup

After this repo is used as a template, there are several one-time changes that should be made to ensure all scripts are
ready for initial use and deployment.

#### Connect to api

Replace urls (`XXXX.template.com`) in api and web with your url for web and k8s respectively.

#### K8s deployment setup

1. rename all instances of `template` in [k8s](k8s) to your app name
2. update the email in `encrypt.yml`
3. update ENV variables in `.github/workflows/deploy.yml`
4. run `login.sh` wherever your k8s is hosted to login to docker.io
5. run `create-service-account.sh` to create a service account and get your secret information to use as a GitHub action
   secret `K8S_SECRET`

## Development

### Installation

- `poetry install`
- (in `web/`) `yarn install`

### Sharing model data

1. Export model from python: `poetry run gen-model`
2. Translate schema to TypeScript (in `web/`): `yarn run gen-model`

### Local development
- run api: `poetry run fastapi dev api.main.py`
- run web (in `web/`): `yarn run start`
  - `REACT_APP_API_URL=http://localhost:8000`
