#!/bin/bash

rm changed.files
git fetch && git diff --name-only ..origin &> changed.files

