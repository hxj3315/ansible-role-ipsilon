from __future__ import absolute_import

from ipsilon.providers.openidc.plugins.common import OpenidCExtensionBase


class OpenidCExtension(OpenidCExtensionBase):
    name = 'circle'
    display_name = 'Circle Tokens'
    scopes = {
        'openid': {
            'display_name': 'openid',
        },
        'profile': {
            'display_name': 'profile',
        },
        'email': {
            'display_name': 'email',
        },
        'address': {
            'display_name': 'address',
        },
        'phone': {
            'display_name': 'phone',
        },
        'https://mbs.cclinux.org/oidc/mbs-submit-build': {
            'display_name': 'mbs',
        },
        'https://id.fedoraproject.org/scope/groups': {
            'display_name': 'groups',
        }
    }
