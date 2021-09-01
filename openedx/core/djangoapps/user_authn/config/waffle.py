"""
Waffle flags and switches for user authn.
"""


from edx_toggles.toggles import LegacyWaffleSwitch, LegacyWaffleSwitchNamespace

_WAFFLE_NAMESPACE = 'user_authn'
_WAFFLE_SWITCH_NAMESPACE = LegacyWaffleSwitchNamespace(name=_WAFFLE_NAMESPACE, log_prefix='UserAuthN: ')

# .. toggle_name: user_authn.enable_login_using_thirdparty_auth_only
# .. toggle_implementation: WaffleSwitch
# .. toggle_default: False
# .. toggle_description: When enabled, users must be sign in using their allowed domain SSO account. This includes sign-
#   ins to the Django admin dashboard at "/admin".
# .. toggle_use_cases: temporary
# .. toggle_creation_date: 2019-11-20
# .. toggle_target_removal_date: 2020-01-31
# .. toggle_warnings: Requires THIRD_PARTY_AUTH_ONLY_DOMAIN to also be set.
# .. toggle_tickets: ENT-2461
ENABLE_LOGIN_USING_THIRDPARTY_AUTH_ONLY = LegacyWaffleSwitch(
    _WAFFLE_SWITCH_NAMESPACE,
    'enable_login_using_thirdparty_auth_only',
    __name__
)

# .. toggle_name: user_authn.enable_pwned_password_api
# .. toggle_implementation: WaffleSwitch
# .. toggle_default: False
# .. toggle_description: When enabled, user password's vulnerability would be checked via pwned password database
# .. toggle_use_cases: permanent
# .. toggle_creation_date: 2021-09-22
# .. toggle_tickets: VAN-664
ENABLE_PWNED_PASSWORD_API = LegacyWaffleSwitch(
    _WAFFLE_SWITCH_NAMESPACE,
    'enable_pwned_password_api',
    __name__
)
