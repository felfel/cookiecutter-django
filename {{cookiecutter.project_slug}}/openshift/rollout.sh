#!/bin/sh
# Do an OpenShift Rollout

if [ -z "$1" ]; then
  echo "usage: $0 <DC name>" >&2
  exit 1
fi

set -x
APP="$1"

# start a new deployment
oc rollout latest "dc/$APP-django"
{% if cookiecutter.use_celery == "y" %}
oc rollout latest "dc/$APP-worker"
oc rollout latest "dc/$APP-beat"
{% endif %}

# Wait for the new deployments to finish
{% if cookiecutter.use_celery == "y" %}
oc rollout status "dc/$APP-beat"
oc rollout status "dc/$APP-worker" 
{% endif %}
oc rollout status "dc/$APP-django"
