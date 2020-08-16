#!/bin/bash
set -e

pip install Django==3.0.9
pip install -U https://github.com/openwisp/openwisp-utils/tarball/master#egg=openwisp_utils[qa] --upgrade-strategy "only-if-needed"
pip install -U https://github.com/openwisp/openwisp-controller/tarball/master --upgrade-strategy "only-if-needed"
pip install -U https://github.com/openwisp/openwisp-monitoring/tarball/master --upgrade-strategy "only-if-needed"
pip install -U https://github.com/openwisp/openwisp-notifications/tarball/master --upgrade-strategy "only-if-needed"
pip install -U https://github.com/openwisp/openwisp-users/tarball/master --upgrade-strategy "only-if-needed"
pip install django_redis

create_superuser() {
    local username="$1"
    local email="$2"
    local password="$3"
    cat <<EOF | python manage.py shell
from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="$username").exists():
    User.objects.create_superuser("$username", "$email", "$password")
else:
    print('User "{}" exists already, not created'.format("$username"))
EOF
}

set_default_organization_secret(){
    local secret="$1"
    cat <<EOF | python manage.py shell
from django.contrib.auth import get_user_model
from swapper import load_model

Organization = load_model('openwisp_users', 'Organization')
OrganizationConfigSettings = load_model('config', 'OrganizationConfigSettings')

default_organization = Organization.objects.first()
default_config = OrganizationConfigSettings.objects.get(organization_id=default_organization.id)
default_config.shared_secret = "$secret" #openwisp_utils.utils.get_random_key
default_config.save()

print('Secret "{}" has been updated for organization "{}"'.format("$secret",default_organization.name))
EOF
}

python manage.py migrate --no-input
create_superuser admin admin@example.com admin
set_default_organization_secret "------SECRET------"
