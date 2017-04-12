#!/bin/bash

set -e

if ! [ -z ${DOCKER_IMAGE+x} ]; then
    docker run -e PYPI_PASSWORD=${PYPI_PASSWORD} --rm -v `pwd`:/io $DOCKER_IMAGE /bin/bash
    ls
    ls wheelhouse/
    pip install twine
    twine upload ${TRAVIS_BUILD_DIR}/wheelhouse/numpy_sugar*.whl \
        -u dhorta -p ${PYPI_PASSWORD}
fi
